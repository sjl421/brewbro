import os

import tornado.ioloop
import tornado.httpserver
import tornado.template
import tornado.web

loader = tornado.template.Loader(os.path.join(os.path.dirname(__file__), "templates"))

class MainHandler(tornado.web.RequestHandler):

	def get(self):
		self.write(loader.load("index.html").generate())
		self.finish()

app = tornado.web.Application(
	[
		("/", MainHandler),
	],
	static_path=os.path.join(os.path.dirname(__file__), "static"),
	debug=True,
	compiled_template_cache=False
)

server = tornado.httpserver.HTTPServer(app)
server.listen(5000)