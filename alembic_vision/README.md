### alembic

#### 数据库版本花
我们通常会将代码放在某个版本管理系统中，进行可追溯的版本管理。例如GIT，SVN等等。
在一个项目中，除了必要的代码代理，数据库也会随着项目的演变而不断版本迭代。
Alembic是Sqlalchemy的作者实现的一个数据库版本化管理工具，可以基于Sqlalchemy的Model与数据库之间的关系进行版本化维护。

#### 文档
[alembic文档说明](http://alembic.zzzcomputing.com/en/latest/)

#### 安装
```
pip install alembic
```

#### 初始化
在项目的根目录下进行初始化
```
alembic init alembic_vision
```
初始化的名字可自定义命名，随后，项目的根目录下会生成alembic配置文件alembic.ini。
初始化的alembic目录结构大致如下：
```
.
├── env.py
├── README
├── README.md
├── script.py.mako
└── versions
    └── 91008d822299_create_test_table.py

```
* alembic.ini 提供基本的配置
* env.py 每次执行Alembic都会加载这个模块，主要提供项目Sqlalchemy Model的连接
* script.py.mako 迁移脚本生成模版
* versions 存放生成的迁移脚本目录

#### 配置
修改alembic.ini配置来连接数据库,新增一条数据库配置即可
```
sqlalchemy.url = postgresql+psycopg2://vision:vision@localhost/vision
```

#### 版本控制
创建一个基础数据库版本，也可从已有的数据库版本出发
```
alembic revision -m "create test_account table"
```
生成的版本文件大致如下：
```
"""create test table

Revision ID: 91008d822299
Revises: 
Create Date: 2016-12-17 10:40:26.345335

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91008d822299'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    pass

def downgrade():
    pass

```
其中revision = '91008d822299'和down_revision = None指定了这个reversion的当前版本号，以及父版本号，可以通过版本号进行追溯。

#### 数据库升级和降级
通过修改upgrade和downgrade进行实际上的数据库升降级操作，只需要操作op和sa对象即可
```
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91008d822299'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'test_account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(20), nullable=False),
        sa.Column('description', sa.String(255))
    )


def downgrade():
    op.drop_table('test_account')
```
一般来说，需要指定特定的版本号进行升级或者降级，但对于最新和最初版本的数据库有两个别名，head指的是最新版本，base指的是最初版本
升级：
```
alembic upgrade head
```
降级：
```
alembic downgrade base
```

#### 自动生成迁移脚本
* alembic不仅能够维护数据库的历史版本，还可以自动生成迁移脚本
* 通常在确定需求后，难免会对数据模型进行修改
* 如下，在User表中新增了token字段
```
class User(BaseModel):
    __tablename__ = 'user'
    user_id = Column(Integer, Sequence('tb_user_id_seq', metadata=BaseModel.metadata, start=1000), primary_key=True)
    name = Column(String(64), nullable=False)
    email = Column(String(64), nullable=False)
    password = Column(String(255), nullable=False)
    token = Column(String(128), nullable=False)
    create_at = Column(DateTime, nullable=False, server_default=text("now()"))
    update_at = Column(DateTime, nullable=False, server_default=text("now()"))

    __table_args__ = (
        Index('user_email_uindex', email, unique=True),
        Index('user_index', user_id, unique=True),
    )
  
```
* 这个时候运行项目肯定是失败的，数据库的映射关系已经打乱了，需要重建映射
步骤如下：
1.  配置alembic_vision/env.py文件，修改target_metadata = None为项目的元信息对象
```
import os
import sys
sys.path.insert(0, os.path.realpath("./vision"))
from model.vision import user
target_metadata = user.BaseModel.metadata
```
这里的引入存在目录问题，因此加入了目录拼接。

2. 执行以下命令生成自动迁移脚本：
```
alembic revision --autogenerate -m "add token field for user"
```
生成信息大致如下：
```
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.ddl.postgresql] Detected sequence named 'test_account_id_seq' as owned by integer column 'test_account(id)', assuming SERIAL and omitting
INFO  [alembic.autogenerate.compare] Detected removed table u'test_account'
INFO  [alembic.autogenerate.compare] Detected added column 'user.token'
```
剩下的步骤就是正常的升降级操作了
3. 数据库升级
```
alembic upgrade 2c24ef5e4a4d
```
生成信息大致如下：
```
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade 91008d822299 -> 2c24ef5e4a4d, add token field for user
```
