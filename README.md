### vison

#### 1. 项目结构
```
.
├── bin
│   └── install-ctl.sh                                                      # 部署脚本
├── etc                                                                     # 配置文件
│   └── config.yaml
├── README.md
├── site-packages                                                           # 依赖模块说明
│   └── requerments.txt
└── vision                                                                  # 项目根目录
    ├── application.py                                                      # 应用程序入口
    ├── backend                                                             # 后台执行程序
    │   └── __init__.py
    ├── handlers                                                            # 句柄
    │   └── __init__.py
    ├── __init__.py
    ├── public                                                              # 公共函数
    │   └── __init__.py
    ├── server.py                                                           # 服务启动
    ├── settings.py
    ├── static                                                              # 静态文件
    │   └── __init__.py
    ├── temp
    │   └── __init__.py
    ├── template                                                            # 模板文件
    │   └── __init__.py
    ├── test                                                                # 单元测试脚本
    │   └── __init__.py
    └── utils                                                               # 第三方扩展
        ├── __init__.py
        └── session.py

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