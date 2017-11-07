from flask import Blueprint, render_template

web_blueprint = Blueprint('web', __name__, template_folder='templates')

@web_blueprint.route('/')
def home():
	return render_template('web/index.html')