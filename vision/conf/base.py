# -*- coding: utf-8 -*-
# @Time    : 2017-01-03 00:36:29
# @Author  : xiezhigang
# @Site    : vision
# @File    : base.py
# @Software: PyCharm

from public.config import Config

# config
pgConfig = Config.get('config', 'postgresql')
redisConfig = Config.get('config', 'redis')

# default port host
portDFLT = 8888
server_port = str(portDFLT)
server = '127.0.0.1'
BaseUrl = "http://" + server + ":" + server_port + "/"

# debug
server_debug = True
# redis配置
redis_db = redisConfig.get('default').get('db')
redis_host = redisConfig.get('default').get('host')
redis_port = redisConfig.get('default').get('port')

# pg配置
pg_db = pgConfig.get('default').get('db')
pg_host = pgConfig.get('default').get('host')
pg_passwd = pgConfig.get('default').get('password')
pg_port = pgConfig.get('default').get('port')
pg_user = pgConfig.get('default').get('user')
pg_charset = 'utf8'

sqlalchemy_db = "postgresql+psycopg2://{0}:{1}@{2}/{3}" .format(pg_user, pg_passwd, pg_host, pg_db)


