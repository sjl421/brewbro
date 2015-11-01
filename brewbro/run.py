import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)8s] - %(filename)12s: %(message)s")

from brewbro import app, config

import tornado.ioloop

if __name__ == "__main__":
	config.init()

	try:
		tornado.ioloop.IOLoop.current().start()
	except KeyboardInterrupt:
		pass