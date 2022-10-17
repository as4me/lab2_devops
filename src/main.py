

import tornado.ioloop
import tornado.web
import json
from functional import fib_f

class Fib(tornado.web.RequestHandler):



    def get(self):
        n = int(self.get_argument('n'))
        fib_n = fib_f(int(n))
        self.write({"result":fib_n })

application = tornado.web.Application([
    (r"/", Fib),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
