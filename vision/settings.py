# -*- coding:utf-8 -*-
from public.config import Config
from tornado.options import define, options

pgConfig = Config.get('config', 'postgresql_uline')
pgTradeConfig = Config.get('config', 'postgresql_uline_trade')
redisConfig = Config.get('config', 'redis')

define("src", default='app', help="run on the given src", type=str)
define("env", default='local', help="run on the given env", type=str)
options.parse_command_line()
src = options.src
# 生产 port -> page/api: app-*/8888, pub-100/8100， admin-90/8090,  index-80/8080
if src == 'pub':
    portDFLT = 8100
elif src == 'adm':
    portDFLT = 8090
elif src == 'idx':
    portDFLT = 8080
else:
    portDFLT = 8888
server_port = str(portDFLT)
env = options.env


def enum(**enums):
    return type('Enum', (), enums)

server_debug = True
# redis配置
redis_db = redisConfig.get('default').get('db')
redis_host = redisConfig.get('default').get('host')
redis_port = redisConfig.get('default').get('port')

# pg_uline配置
pg_db = pgConfig.get('default').get('db')
pg_host = pgConfig.get('default').get('host')
pg_passwd = pgConfig.get('default').get('password')
pg_port = pgConfig.get('default').get('port')
pg_user = pgConfig.get('default').get('user')
pg_charset = 'utf8'

# pg_uline_trade配置
pg_trade_db = pgTradeConfig.get('default').get('db')
pg_trade_host = pgTradeConfig.get('default').get('host')
pg_trade_password = pgTradeConfig.get('default').get('password')
pg_trade_port = pgTradeConfig.get('default').get('port')
pg_trade_user = pgTradeConfig.get('default').get('user')
pg_trade_charset = 'utf8'

# server
server = '127.0.0.1'
BaseUrl = "http://"+server+":"+server_port+"/"

### 测试商户号
WX_MCH_ID = '1900008951'
WXPAY_KEY = '3AC991426F056322E053645AA8C0CC12'
APPID = 'wxdace645e0bc2c424'

# 环境配置
if env == 'prod':
    server_debug = False
    pg_db = pgConfig.get('prod').get('db')
    pg_host = pgConfig.get('prod').get('host')
    pg_passwd = pgConfig.get('prod').get('password')
    pg_port = pgConfig.get('prod').get('port')
    pg_user = pgConfig.get('prod').get('user')

    pg_trade_db = pgTradeConfig.get('prod').get('db')
    pg_trade_host = pgTradeConfig.get('prod').get('host')
    pg_trade_password = pgTradeConfig.get('prod').get('password')
    pg_trade_port = pgTradeConfig.get('prod').get('port')
    pg_trade_user = pgTradeConfig.get('prod').get('user')

    redis_db = redisConfig.get('prod').get('db')
    redis_host = redisConfig.get('prod').get('host')
    redis_port = redisConfig.get('prod').get('port')

    BaseUrl = "http://"+server+":"+server_port+"/"
    server_port = str(int(server_port) + 6)

    ### 正式商户号
    WX_MCH_ID = '1404851802'
    WXPAY_KEY = '161fc571f37e534c04c8436e1f1c0bbd'
    APPID = 'wxb68005e5db5d29ce'
    AppSecret = 'c05d27c5230aeb1816fd3f912f629b08'

elif env == 'dev':
    pg_db = pgConfig.get('dev').get('db')
    pg_host = pgConfig.get('dev').get('host')
    pg_passwd = pgConfig.get('dev').get('password')
    pg_port = pgConfig.get('dev').get('port')
    pg_user = pgConfig.get('dev').get('user')

    pg_trade_db = pgTradeConfig.get('dev').get('db')
    pg_trade_host = pgTradeConfig.get('dev').get('host')
    pg_trade_password = pgTradeConfig.get('dev').get('password')
    pg_trade_port = pgTradeConfig.get('dev').get('port')
    pg_trade_user = pgTradeConfig.get('dev').get('user')

    redis_db = redisConfig.get('dev').get('db')
    redis_host = redisConfig.get('dev').get('host')
    redis_port = redisConfig.get('dev').get('port')

    server_port = str(int(server_port) + 5)
    BaseUrl = "http://"+server+":"+server_port+"/"

print("=========== start ===========")
print("src == "+src)
print("env == "+env)
print("postgresql_uline == "+pg_host)
print("postgresql_uline_db == "+pg_db)
print("postgresql_uline_trade == "+pg_trade_host)
print("postgresql_uline_trade_db == "+pg_trade_db)
print("redis == "+redis_host)
print("redis_db == "+str(redis_db))
print("server port == "+str(server_port))
print("wx_mch_id == " + str(WX_MCH_ID))
