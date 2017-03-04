# -*- coding:utf-8 -*-
import traceback
from tornado.web import RequestHandler
from tornado import escape
from tornado.escape import utf8
from tornado.util import unicode_type
from public import log
from utils import session

class UTILMixin(object):
    pass

# Handlers 共享的 Handler 方法。API 使用不正确错误处理
class BaseHandler(RequestHandler, UTILMixin):
    def __init__(self, *args, **kwargs):
        super(BaseHandler, self).__init__(*args, **kwargs)
        self.session = session.Session(self.application.session_manager, self)
        self.db = self.application.db

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