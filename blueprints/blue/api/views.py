from flask import Blueprint, jsonify

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/users')
def users():
	list = [
		{
			"first_name"	:	"John",
			"last_name"		:	"Doe",
			"user_since"	:	"12 days"

		},
		{
			"first_name"	:	"Dojo",
			"last_name"		:	"Dodo",
			"user_since"	:	"30 days"
		}
	]
	return jsonify(results = list)
