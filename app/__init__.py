from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'random key'
from app import views