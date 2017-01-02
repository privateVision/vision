# -*- coding: utf-8 -*-
# @Time    : 2017-01-03 00:38:27
# @Author  : xiezhigang
# @Site    : vision
# @File    : prod.py
# @Software: PyCharm

from public.config import Config

# config
pgConfig = Config.get('config', 'postgresql')
redisConfig = Config.get('config', 'redis')

# prod port host
portDFLT = 8888
server_port = str(portDFLT)
server = '127.0.0.1'
server_port = str(int(server_port) + 6)
BaseUrl = "http://" + server + ":" + server_port + "/"

# debug
server_debug = True
# redis配置
redis_db = redisConfig.get('prod').get('db')
redis_host = redisConfig.get('prod').get('host')
redis_port = redisConfig.get('prod').get('port')

# pg配置
pg_db = pgConfig.get('prod').get('db')
pg_host = pgConfig.get('prod').get('host')
pg_passwd = pgConfig.get('prod').get('password')
pg_port = pgConfig.get('prod').get('port')
pg_user = pgConfig.get('prod').get('user')
pg_charset = 'utf8'

sqlalchemy_db = "postgresql+psycopg2://{0}:{1}@{2}/{3}" .format(pg_user, pg_passwd, pg_host, pg_db)