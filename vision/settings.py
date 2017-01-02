# -*- coding: utf-8 -*-
# @Time    : 2017-01-03 00:50:19
# @Author  : xiezhigang
# @Site    : vision
# @File    : settings.py
# @Software: PyCharm

import os
import re
from os.path import expanduser

bash_rc = ''
if os.path.exists(expanduser("~/.bashrc")):
    with open(expanduser("~/.bashrc")) as f:
        bash_rc += f.read()

if os.path.exists(expanduser("~/.bash_profile")):
    with open(expanduser("~/.bash_profile")) as f:
        bash_rc += f.read()

match = re.search(r'vision_CMS_ENV=(.+)', bash_rc)
env = match.group(1) if match else 'default'

if env == 'DEV':
    from conf.dev import *
elif env == 'PROD':
    from conf.prod import *
else:
    from conf.base import *

print("=========== start ===========")
print("env == " + env)
print("postgresql_vision == " + pg_host)
print("postgresql_vision_db == " + pg_db)
print("redis == " + redis_host)
print("redis_db == " + str(redis_db))
print("server port == " + str(server_port))