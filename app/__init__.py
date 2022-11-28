from flask import Flask
from config import Config
from flask_migrate import Migrate
from .models import db

from .auth.routes import auth

app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(auth)



from . import routes
from . import models