# -*- coding: utf-8 -*-
from handlers.app.vision.url import urlpattern as vision_url

from baseHandlers import BaseHandler

urlpattern = ()

urlpattern += vision_url

urlpattern += (
    (r'.*', BaseHandler),
)