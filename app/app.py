#libraries 
from flask import Flask, render_template, flash, url_for, session, logging, redirect, request
from flask_mysqldb import MySQL
# from wtforms import *
from passlib.hash import sha256_crypt

#files
from data import Articles
from forms import RegisterForm, LoginForm

app = Flask(__name__)

app.debug = True

#app initiation
Articles = Articles()


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/register', methods=['GET','POST'])
def register():
	form = RegisterForm(request.form)
	if request.method == 'POST' and form.validate():
		return render_template('register.html')

	return render_template('register.html', form = form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm(request.form)
	if request.method == 'POST' and form.validate():
		return render_template('login.html')
		
	return render_template('login.html', form = form)
	

@app.route('/articles')
def articles():
	return render_template('articles.html', articles = Articles)

@app.route('/article/<string:id>')
def article(id):
	return render_template('article.html', id = id)


if __name__ == '__main__':
    app.run()