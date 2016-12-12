# -*- coding:utf-8 -*-
import tornado.web
import functools
import traceback
from tornado import escape
from tornado.escape import utf8
from tornado.util import unicode_type
from public import log
from utils import session

# Handlers 共享的 Handler 方法。API 使用不正确错误处理
class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, *args, **kwargs):
        super(BaseHandler, self).__init__(*args, **kwargs)
        self.session = session.Session(self.application.session_manager, self)

    def initialize(self):
        self.add_header("Access-Control-Allow-Origin", "*")

    def write(self, chunk):
        if self._finished:
            raise RuntimeError("Cannot write() after finish()")
        if not isinstance(chunk, (bytes, unicode_type, dict)):
            message = "write() only accepts bytes, unicode, and dict objects"
            if isinstance(chunk, list):
                message += ". Lists not accepted for security reasons; see http://www.tornadoweb.org/en/stable/web.html#tornado.web.RequestHandler.write"
            raise TypeError(message)
        if isinstance(chunk, dict):
            chunk = escape.json_encode(chunk)
            self.set_header("Content-Type", "application/json; charset=UTF-8")
            try:
                log.request.info(">>>>>>>>>> " + str(chunk))
            except Exception as err:
                log.request.info(">>>>>>>>>> " + str(err))
        chunk = utf8(chunk)
        self._write_buffer.append(chunk)

    def write_error(self, status_code, **kwargs):
        if "exc_info" in kwargs:
            for line in traceback.format_exception(*kwargs["exc_info"]):
                log.exception.info(line)
        if status_code == 500:
            self.render('common/500.html')
        elif status_code == 404:
            self.render('common/404.html')
        else:
            self.write(str(status_code))
            self.finish()

    def get_client_ip(self):
        try:
            real_ip = self.request.META['HTTP_X_FORWARDED_FOR']
            regip = real_ip.split(",")[0]
        except:
            try:
                regip = self.request.META['REMOTE_ADDR']
            except:
                regip = ""
        return regip

    def get_navigate_html(self, counts=0, pagesize=10):
        # 分页处理
        pageindex = int(self.get_argument("p", 1))
        page_number = 0
        if counts > 0:
            if counts % pagesize == 0:
                page_number = counts / pagesize
            else:
                page_number = counts / pagesize + 1
        is_pre = False
        is_next = False
        if page_number > 1 and pageindex > 1:
            is_pre = True
        if page_number > 1 and pageindex < page_number:
            is_next = True
        return self.render_string("common/navigate.html", pageindex=pageindex, page_number=page_number, is_pre=is_pre,
                                  is_next=is_next, counts=counts)


# 图片 - 静态文件读取加查找文件路径错误处理
class ImageHandler(tornado.web.StaticFileHandler):
    """docstring for ImageHandler"""

    def write_error(self, status_code, **kwargs):
        if status_code == 500:
            self.render('common/500.html')
        elif status_code == 404:
            self.render('common/404.html')
        else:
            self.write(str(status_code))
            self.finish()


# 文件 - 静态文件读取加查找文件路径错误处理
class StaticHandler(tornado.web.StaticFileHandler):
    def get(self, path, include_body=True):
        self.set_header("Access-Control-Allow-Origin", "*")
        super(StaticHandler, self).get(path, include_body)

    def write_error(self, status_code, **kwargs):
        self.finish({str(status_code): "a nicer message!"})


# 错误 API 链接处理
class ErrorLinkHandler(BaseHandler):
    """docstring for ErrorLinkHandler"""

    def get(self):
        self.render('common/404.html')