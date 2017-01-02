# -*- coding: utf-8 -*-
# @Time    : 2017-01-03 00:36:47
# @Author  : xiezhigang
# @Site    : vision
# @File    : dev.py
# @Software: PyCharm

from public.config import Config

# config
pgConfig = Config.get('config', 'postgresql')
redisConfig = Config.get('config', 'redis')

# dev port host
portDFLT = 8888
server_port = str(portDFLT)
server = '127.0.0.1'
server_port = str(int(server_port) + 5)
BaseUrl = "http://" + server + ":" + server_port + "/"

# debug
server_debug = True
# redis配置
redis_db = redisConfig.get('dev').get('db')
redis_host = redisConfig.get('dev').get('host')
redis_port = redisConfig.get('dev').get('port')

# pg配置
pg_db = pgConfig.get('dev').get('db')
pg_host = pgConfig.get('dev').get('host')
pg_passwd = pgConfig.get('dev').get('password')
pg_port = pgConfig.get('dev').get('port')
pg_user = pgConfig.get('dev').get('user')
pg_charset = 'utf8'

sqlalchemy_db = "postgresql+psycopg2://{0}:{1}@{2}/{3}" .format(pg_user, pg_passwd, pg_host, pg_db)