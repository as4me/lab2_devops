

import tornado.ioloop
import tornado.web
import json


class Fib(tornado.web.RequestHandler):

    def fib_f(self,n):
        if n<3:
            return 1
        return self.fib_f(n-1) + self.fib_f(n-2)


    def get(self):
        n = int(self.get_argument('n'))
        fib_n = self.fib_f(int(n))
        self.write({"result":fib_n })

application = tornado.web.Application([
    (r"/", Fib),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
