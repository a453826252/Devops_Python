from flask import request, Blueprint

login_api = Blueprint('login_api', __name__)


@login_api.route('/login/', methods=["POST"])
def login():
    username = request.form.get("username")
    pwd = request.form.get("pwd")
    if username == "123456" and pwd == "123456":
        return "login success"
    return "login failed"
