# -*- coding: utf-8 -*-
from __future__ import absolute_import
from backend.celery import app
from celery import platforms
platforms.C_FORCE_ROOT = True
## https://github.com/pika/pika/issues/663
## https://www.zhihu.com/question/37625671
### pika 0.9.14 to 0.10.0 有bug，不能正常回调返回response,降级pika
from public import log

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

## 10位报文长度+报文正文
## 报文的编码为GBK
@app.task(name='ProcessingTask.add')
def add(x, y):
    return x + y
## 任务计划