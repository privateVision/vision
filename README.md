### vison

#### 1. 项目结构
```
.
├── README.md
├── bin                                                                     # 部署脚本
│   └── install-ctl.sh
├── etc                                                                     # 配置文件
│   ├── config-dev.yaml
│   ├── config-prod.yaml
│   ├── config.yaml
│   ├── logging.conf
│   ├── nginx.conf
│   ├── pyvision.conf
│   ├── supervisord.conf
│   └── vision.conf
├── site-packages                                                           # 依赖模块说明
│   └── requerments.txt
└── vision                                                                  # 主程序
    ├── __init__.py
    ├── application.py                                                      # 应用程序入口
    ├── backend                                                             # 任务计划
    │   ├── __init__.py
    │   ├── celery.py
    │   ├── config.py
    │   └── tasks.py
    ├── handlers                                                            # 句柄
    │   ├── __init__.py
    │   ├── api                                                             # 接口
    │   │   └── __init__.py
    │   ├── app                                                             # web
    │   │   └── __init__.py
    │   ├── baseHandlers.py
    │   └── urls.py
    ├── log                                                                 # 日志
    │   ├── detail.lock
    │   ├── detail.log
    │   ├── exception.lock
    │   ├── exception.log
    │   ├── request.lock
    │   └── request.log
    ├── public                                                              # 公共模块
    │   ├── __init__.py
    │   ├── baseException.py
    │   ├── config.py
    │   └── log.py
    ├── server.py                                                           # 服务启动
    ├── settings.py
    ├── static                                                              # 静态文件
    │   └── __init__.py
    ├── temp                                                                # 临时文件
    │   └── __init__.py
    ├── template                                                            # 模板文件
    │   └── __init__.py
    ├── test                                                                # 测试脚本
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
    python server.py
开发环境
    python server.py --env=dev
正式环境
    python server.py --env=prod
```

#### 6. 项目说明
```
tornado项目
1. 整合学过的知识点
2. 练手新的知识
3. 个人社区
4. 朋友社区
5. 看事情的不同视角
```

#### 7. git提交规范说明
```
1. 添加[add] (需求)
2. 修复[fix] (bug)
3. 更正[modify] (需求已完成，更正某个功能点)
4. 更新[update] (需求已完成，更新第三方模块或常量设置)
5. 移除[remove] (移除功能或文件)
6. 重构[refactor] (重构代码或架构)
```