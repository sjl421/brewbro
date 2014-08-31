import logging as log
import os
import sqlite3

from brewbro import settings

bootstrap = False

if not os.path.exists(settings.DB_FILE):
	bootstrap = True

class IntegrityError(Exception):
	pass
	
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class DB:
	
	def __init__(self, conn):
		self.conn = conn
		self.conn.row_factory = dict_factory
	
	def bootstrap(self):
		print "Bootstrap: Creating tables... "
		c = self.conn.cursor()
		
		c.execute('''
			CREATE TABLE malts
			(
				id						integer primary key autoincrement,
				name 					varchar(255) unique
			)
			''')
		c.execute('''
			CREATE TABLE hops
			(
				id						integer primary key autoincrement,
				name 					varchar(255) unique
			)
			''')
		c.execute('''
			CREATE TABLE recipes
			(
				id						integer primary key autoincrement,
				name 					varchar(255) unique, 
				fermentation_volume 	int, 
				description 			text
			)
			''')

		self.conn.commit()
	
	def _get_rows(self, table):
		c = self.conn.cursor()
		
		c.execute('''
			SELECT * FROM %s
			''' % table);
		
		results = c.fetchall()
		self.conn.commit()
		
		return results
	
	def _add_row(self, table, values):
		c = self.conn.cursor()
		
		c.execute('''
			INSERT INTO %s(%s)
			VALUES (%s)''' %
				(
					table, 
					", ".join(values.keys()), 
					", ".join([":%s" % key for key in values.keys()]),
				),
			values)
	
		self.conn.commit();
	
	# Hops
	def get_hops(self):
		return self._get_rows("hops");
	def add_hops(self, **kwargs):
		values = {
			"name": kwargs["name"],
		}
		
		self._add_row("hops", values)
	
	# Malts
	def get_malts(self):
		return self._get_rows("malts");
	def add_malt(self, **kwargs):
		values = {
			"name": kwargs["name"],
		}
		self._add_row("malts", values)

def connect():
	conn = sqlite3.connect(settings.DB_FILE)
	db = DB(conn)
	if bootstrap:
		db.bootstrap()
	return db