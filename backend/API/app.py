from flask import Flask
from user_api.users_api import userApi

app = Flask(__name__)
app.register_blueprint(userApi)

    