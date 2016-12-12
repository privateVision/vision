# -*- coding: utf-8 -*-
from __future__ import absolute_import
from celery import Celery
## 启动worker: celery -A backend worker -l info
## 启动schedule: celery beat -A backend

app = Celery('backend', include=['backend.tasks'])
app.config_from_object('backend.config')

if __name__ == '__main__':
    app.start()