from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_marshmallow import Marshmallow
import time
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

import models.user

db.create_all()

api = Api(app)
ma = Marshmallow(app)


@app.route('/time')
def get_current_time():
    return {'time': time.time()}

import resources.UserResource