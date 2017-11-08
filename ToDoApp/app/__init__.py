from flask import Flask

app = Flask(__name__)

from app.todo.views import module


app.register_blueprint(todo.views.module)
