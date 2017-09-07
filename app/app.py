#libraries 
from flask import Flask, render_template, flash, url_for, session, logging, redirect, request
from flask_mysqldb import MySQL
from passlib.hash import sha256_crypt

#files
from forms import RegisterForm, LoginForm, ArticleForm
from decorators import login_required, is_loggedin

app = Flask(__name__)
app.secret_key = '$5$rounds=535000$O/od5B7GUkTCkcG.$7U6jJ6QnLvyJo8NkAch7KWfwMrPKolfzwtYJOq/7JQ5'
app.debug = True

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'flaskApp'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# init MYSQL
mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/about')
def about():
	return render_template('about.html')


@app.route('/register', methods=['GET','POST'])
# @is_loggedin
def register():
	form = RegisterForm(request.form)

	if request.method == 'POST' and form.validate():
		name = form.name.data
		email = form.email.data
		username = form.username.data
		password = sha256_crypt.encrypt(str(form.password.data))
		
		# mysql connection

		cur = mysql.connection.cursor()

		cur.execute("INSERT INTO users(name, email, username, password) values(%s, %s, %s, %s)",(name, email, username, password))
		mysql.connection.commit()
		cur.close()

		flash('You are now registered', 'success')
		return redirect(url_for('login'))
	return render_template('register.html', form = form)


@app.route('/login', methods=['GET', 'POST'])
# @is_loggedin
def login():
	form = LoginForm(request.form)

	if request.method == 'POST' and form.validate():
		username = form.username.data
		password = form.password.data
		cur = mysql.connection.cursor()
		result = cur.execute("SELECT * FROM users WHERE username = %s", [username])
		if result > 0:
			data = cur.fetchone()
			db_password = data['password']
			if sha256_crypt.verify(password, db_password):
				session['logged_in'] = True
				session['username'] = username

				flash('You are now loggedin', 'success')
				return redirect(url_for('dashboard'))
			else:
				flash('Your password is incorrect', 'danger')
		else:
			flash('No user found with these details', 'danger')		
	return render_template('login.html', form = form)
	

@app.route('/logout')
def logout():
	session.clear()
	flash('You are now logged out', 'success')
	return redirect(url_for('login'))


@app.route('/dashboard')
@login_required
def dashboard():
	cur = mysql.connection.cursor()
	# Get articles
	result = cur.execute("SELECT * FROM articles")
	articles = cur.fetchall()
	if result > 0:
		return render_template('dashboard.html', articles=articles)
	else:
		flash('No Articles Found', 'danger')
		return render_template('dashboard.html')
	# Close connection
	cur.close()

	
@app.route('/addarticle', methods=['GET', 'POST'])
@login_required
def add_article():
	form = ArticleForm(request.form)
	if request.method == 'POST' and form.validate():
		title = form.title.data
		body = form.body.data
		# mysql connection
		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO articles(title, body, author) values(%s, %s, %s)",(title, body, session['username']))
		mysql.connection.commit()
		cur.close()
		flash('Article succesfully added', 'success')
		return redirect(url_for('dashboard'))
	return render_template('addarticle.html', form = form)

@app.route('/articles')
def articles():
	cur = mysql.connection.cursor()
	# Get articles
	result = cur.execute("SELECT * FROM articles")
	articles = cur.fetchall()
	if result > 0:
		return render_template('articles.html', articles=articles)
	else:
		flash('No Articles Found', 'danger')
		return render_template('articles.html')
	# Close connection
	cur.close()
	

@app.route('/article/<string:id>')
def article(id):
	return render_template('article.html', id = id)


if __name__ == '__main__':
    app.run()