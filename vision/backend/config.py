# -*- coding: utf-8 -*-
from __future__ import absolute_import
from celery.schedules import timedelta
# 某个程序中出现的队列，在broker中不存在，则立刻创建它
CELERY_CREATE_MISSING_QUEUES = True

# 使用rabbit-mq 作为任务队列
## https://github.com/mher/tornado-celery/blob/master/tcelery/__init__.py#L46
## 似乎只能使用rabbit-mq作为broker
## 使用redis做broker会报错，raise TypeError(repr(o) + " is not JSON serializable")
# BROKER_URL = "redis://localhost:6379/2"
BROKER_URL = "amqp://guest@localhost:5672/"
# CELERY_RESULT_BACKEND = "amqp://"
## 使用amqp做backend会报错，assert self._connection is not None，取不到broker
CELERY_RESULT_BACKEND = "redis://localhost:6379/3"

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json', 'msgpack']

# 并发worker数
CELERYD_CONCURRENCY = 10

CELERY_TIMEZONE = 'Asia/Shanghai'

# 非常重要,有些情况下可以防止死锁
CELERYD_FORCE_EXECV = True

CELERYD_PREFETCH_MULTIPLIER = 1

# 每个worker最多执行完100个任务就会被销毁，可防止内存泄露
CELERYD_MAX_TASKS_PER_CHILD = 100

# CELERYD_TASK_TIME_LIMIT = 60    # 单个任务的运行时间不超过此值，否则会被SIGKILL 信号杀死
# BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 90}

# 任务发出后，经过一段时间还未收到acknowledge , 就将任务重新交给其他worker执行
CELERY_DISABLE_RATE_LIMITS = True

# 定时任务
# CELERYBEAT_SCHEDULE = {
#     'resend_activated_email': {
#         'task': 'backend.tasks.resend_activated_email',
#         'schedule': timedelta(minutes=30),
#         'args': ()
#     },
# }