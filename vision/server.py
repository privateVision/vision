# -*- coding:utf-8 -*-
import os
import tornado.ioloop
import tornado.web
import tornado.httpserver
from application import Application
from settings import server_port, server
import traceback


def main():
    application = Application()
    application.listen(port=server_port)
    print 'Production server is running at http://%s:%s/' % (server, server_port)
    print 'Quit the server with Control-C'
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    try:
        main()
    except Exception, e:
        traceback.print_exc(e)
        print "     >>>>> App terminating.....\n"
        os._exit(0)
    except KeyboardInterrupt:
        print "\n"
        print "KI"
        print "     >>>>> App terminating.....\n"
        os._exit(0)
