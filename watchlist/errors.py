from watchlist.models import User
from watchlist import app
from flask import render_template


# 注册异常函数
@app.errorhandler(404)
def page_not_found(e):
    # user=User.query.first()
    return render_template('404.html'),404