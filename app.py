from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask import send_from_directory
from flask_moment import Moment
from datetime import datetime
from views import NameForm, LoginForm
import os
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(10)  # CSRF
Bootstrap(app)
moment = Moment(app)  # 本地时间
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'MYSQL://root:Zhangjiayu0.0@QAQ/database'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])  # 首页
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        oldName = session.get('name')
        if oldName is not None and oldName != form.name.data:
            flash('Looks like you have change a name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', current_time=datetime.utcnow(),
                           form=form, name=session.get('name'))


@app.route('/user/<name>')  # 个人页面
def user(name):
        return render_template('user.html', name=name)


@app.errorhandler(404)  # 请求错误页面
def page_not_found(e):
    return render_template('404.html')


@app.errorhandler(500)  # 服务器错误页面
def internal_server_error(e):
    return render_template('500.html')


@app.route('/favicon.ico')  # 页面小图标
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico')


@app.route('/login', methods=['GET', 'POST'])   # 登陆页面
def login():
    form = LoginForm()
    return render_template('login.html',
                           title='Sign In',
                           form=form)


if __name__ == '__main__':
    app.run(debug=True)


