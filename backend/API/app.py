from flask import Flask
from flask_cors import CORS
from user_api.users_api import userApi
#from mails_api.mail_api import mailApi

app = Flask(__name__)
CORS(app, origins="http://localhost:3000", supports_credentials=True)
app.register_blueprint(userApi)
#app.register_blueprint(mailApi)

    