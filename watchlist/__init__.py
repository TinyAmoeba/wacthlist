import os
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

win=sys.platform.startswith('win')
if win:
    prefix='sqlite:///'
else:
    prefix='sqlite:////'

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'dev'
#优先读取环境变量
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev') 
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(os.path.dirname(app.root_path), os.getenv('DATABASE_FILE', 'data.db'))
# 注意更新这里的路径，把 app.root_path 添加到 os.path.dirname() 中
# 以便把文件定位到项目根目录
# app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(os.path.dirname(app.root_path), 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控

db = SQLAlchemy(app) #连接数据库
login_manager = LoginManager(app) #实例化Flask-Login

#通过user_id 获取user对象
@login_manager.user_loader
def load_user(user_id):
    from watchlist.models import User
    user = User.query.get(int(user_id))
    return user

login_manager.login_view = 'login' #对于未登录用户，跳转到login界面。

#注册上下文变量，返回值以后可直接调佣
@app.context_processor
def inject_user():
    from watchlist.models import User
    user = User.query.first()
    return dict(user=user)

from watchlist import views, errors, commands #暂时不能理解，先放下。