# -*- coding:utf-8 -*-
import os

import redis
import tornado.web

from handlers import baseHandlers as base
from handlers.urls import urlpattern
from settings import redis_db, redis_host, redis_port, server_debug
from utils import session
from utils.database import init_db, session_scope


class Application(tornado.web.Application):
    def __init__(self):
        self.base_dir = os.path.dirname(__file__)
        settings = dict(
            debug=server_debug,
            # default_handler_class=base.ErrorLinkHandler,
            template_path=os.path.join(self.base_dir, "handlers/app" if server_debug else "templates"),
            static_path=os.path.join(self.base_dir, "static"),
            cookie_secret='1ks1tuCW3x0lU14H3m0CV39Q288rVkc9113ieivhYi610E0i4fRhB6u5VhiZRu72',
            session_secret="3cdcb1f00803b6e78ab50b466a40b9977db396840c28307f428b25e2277f1bcc",
            session_timeout=60 * 60,
            xsrf_cookies=server_debug,
            store_options={
                'redis_host': redis_host,
                'redis_port': redis_port,
                'redis_pass': None
            },
        )
        tornado.web.Application.__init__(self, handlers=urlpattern, **settings)
        self.client = redis.Redis(host=redis_host, port=redis_port, db=redis_db)
        self.session_manager = session.SessionManager(settings["session_secret"],
                                                      settings["store_options"], settings["session_timeout"])
        init_db()
        self.db = session_scope()
