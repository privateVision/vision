# -*- coding: utf-8 -*-
# @Time    : 2017-03-04 13:09:10
# @Author  : xiezhigang
# @Site    : vision
# @File    : handler.py
# @Software: PyCharm
from tornado import gen
from tornado.web import authenticated, HTTPError, asynchronous

from handlers.baseHandlers import BaseHandler


__all__ = ["VisionHandler"]

class VisionHandler(BaseHandler):
    def prepare(self):
        pass

    def get(self):
        self.render("vision/template/vision.html")