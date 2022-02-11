from flask import make_response
from redis import Redis
import os
# flask文件配置
# 数据库账户
# User = ''
User = ''
# mysql数据库的密码
Password = ''
# 用户数据库名
# Database_User = 'personalInformation'
Database_User = ''
# mysql 数据库的端口号
MysqlPort = 3306
# redis 数据库的端口号
RedisPort = 6379
# 远程服务器的公网ip
# Ip = ''
Ip = '127.0.0.1'
# 开发方式运行
ENV = 'development'
DEBUG = True
# 配置flask + session + redis
SESSION_TYPE = 'redis'  # session类型为redis
# SESSION_REDIS = Redis(host=Ip, port=RedisPort, password=Password)   # 连接redis的配置
SESSION_REDIS = Redis(host=Ip, port=RedisPort, password='')
SESSION_USE_SIGNER = True   # 是否强制加盐混淆session
# SECRET_KEY = os.urandom(24)     # 设置加密密钥
SECRET_KEY = 'yujunxiong'
SESSION_KEY_PREFIX = 'session:'     # 保存到session中值的前缀
PERMANENT_SESSION_LIFETIME = 24*60*60   # 设置session的生命周期，整数秒
SESSION_PERMANENT = True    # 设置session是否永久有效,设置为True则关闭浏览器就失效

