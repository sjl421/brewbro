from flask import Flask

from brewbro import database, settings

app = Flask(__name__)

db = database.connect()

def run():
    app.run(host=settings.HOST,
    		port=settings.PORT,
    		debug=settings.DEBUG)

if __name__ == "__main__":
	run()