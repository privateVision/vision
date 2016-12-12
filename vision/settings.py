# -*- coding:utf-8 -*-
from public.config import Config
from tornado.options import define, options

define("src", default='app', help="run on the given src", type=str)
define("env", default='local', help="run on the given env", type=str)
options.parse_command_line()
src = options.src
env = options.env

server_port = str(8080)
server = '127.0.0.1'

# 环境配置
if env == 'prod':
    dbConfig = Config.get('config-prod', 'mysql')
    rdbConfig = Config.get('config-prod', 'redis')
    server_debug = False
    BaseUrl = "http://"+server+":"+server_port+"/"
    server_port = str(int(server_port) + 6)

elif env == 'dev':
    dbConfig = Config.get('config-dev', 'mysql')
    rdbConfig = Config.get('config-dev', 'redis')
    server_debug = True
    server_port = str(int(server_port) + 5)
    BaseUrl = "http://"+server+":"+server_port+"/"

else:
    dbConfig = Config.get('config', 'mysql')
    rdbConfig = Config.get('config', 'redis')
    server_debug = True
    BaseUrl = "http://" + server + ":" + server_port + "/"

db = dbConfig.get('db')
host = dbConfig.get('host')
passwd = dbConfig.get('password')
port = dbConfig.get('port')
user = dbConfig.get('user')
charset = 'utf8'

redis_db = rdbConfig.get('db')
redis_host = rdbConfig.get('host')
redis_port = rdbConfig.get('port')

print("=========== start ===========")
print("src == " + src)
print("env == " + env)
print("db_host == " + host)
print("db == " + db)
print("redis_host == " + redis_host)
print("redis_db == " + str(redis_db))
print("server port == " + str(server_port))