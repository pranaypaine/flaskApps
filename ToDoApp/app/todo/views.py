from flask import Blueprint, render_template

module = Blueprint('todo', __name__, template_folder='templates')


@module.route('/')
def home():
	return render_template('index.html')

@module.route('/about')
def about():
	return render_template('about.html')
	pass

@module.route('/add', methods=['GET', 'POST'])
def add():
	return 'Add a ToDo'


@module.route('/remove/<string:id>', methods=['POST'])
def remove(id):
	return id
