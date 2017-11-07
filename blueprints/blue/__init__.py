from flask import Flask

app = Flask(__name__)

from blue.web.views import web_blueprint
from blue.api.views import api_blueprint
from blue.admin.views import admin_blueprint


app.register_blueprint(web.views.web_blueprint)
app.register_blueprint(admin.views.admin_blueprint, url_prefix='/admin')
app.register_blueprint(api.views.api_blueprint, url_prefix='/api')