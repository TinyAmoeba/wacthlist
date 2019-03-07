#-*- coding:utf8 -*-
from flask import Flask
from flask import url_for
app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1> Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

@app.route('/home')
def home():
    return 'Welcome to my Home'

@app.route('/user/<name>')
def user_page(name):
    return 'user:{}'.format(name)

@app.route('/test')
def test_url_for():
    print(url_for('user_page',name='greyli'))
    print(url_for('test_url_for'))
    return 'Test page'
