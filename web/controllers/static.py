from flask import  Blueprint,send_from_directory
from app import app

route_static = Blueprint('static_page', __name__)

@route_static.route("/<path:filename>")
def index(filename):
    #app.logger.info(filename)
    return send_from_directory(app.root_path+"/web/static/",filename)