# -*- coding: utf-8 -*-
# @Time    : 2017-03-04 13:09:26
# @Author  : xiezhigang
# @Site    : vision
# @File    : url.py
# @Software: PyCharm
from handlers.app.vision.handler import VisionHandler


urlpattern = (
    ("/?", VisionHandler),
    ("/vision/?", VisionHandler),
)