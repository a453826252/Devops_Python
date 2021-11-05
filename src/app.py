from flask import Flask, render_template
from src.Login import login_api

app = Flask(__name__)
app.register_blueprint(login_api)


@app.route('/', methods=["GET"])
def index():
    return render_template('Index.html')
