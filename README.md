### vison

#### 1. 项目结构
```
```

#### 2. 安装路径及配置
```
nginx安装路径：/usr/local/nginx
nginx配置文件夹： /usr/local/nginx/conf.d/
supervisor配置文件夹：/etc/supervisor.d/
logging配置文件夹：/{{project_dir}}/{{project_name}}/etc/
项目配置文件（config.yaml）：/{{project_dir}}/{{project_name}}/etc/
```

#### 3. 项目部署
```
Usage:
    sh install-ctl.sh <command> [option]
Commend:
    init
Option:
    --all
```

#### 4. 启动服务
```
启动supervisord
    /usr/bin/supervisord -c /etc/supervisor.conf
启动nginx
    /usr/local/nginx/sbin/nginx -c /usr/local/nginx/conf/nginx.conf
```

#### 5. 启动程序
```
测试环境
    python server.py --env=local
开发环境
    python server.py --env=dev
正式环境
    python server.py --env=prod
```

#### 6. 项目说明
```
```