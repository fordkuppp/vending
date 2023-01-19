from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from vending.api import *


db = SQLAlchemy()
from vending import models              # models have to be imported after db object is defined

# create and configure the app
app = Flask(__name__, instance_relative_config=True)
api = Api(app, prefix='/api')
app.config.from_mapping(
    SECRET_KEY=';)',
    SQLALCHEMY_DATABASE_URI="mysql://root:15346@localhost:3306/vending-db",
)

db.init_app(app)
api.add_resource(Hello, '/')
api.add_resource(Machine, '/machine')

if __name__ == "__main__":
    app.run()
