from flask import Flask

app_flask = Flask(__name__)

from app import routes

from flask_mail import Mail, Message

