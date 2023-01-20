from flask import Flask, Blueprint
from vending.api import *
from vending import models

# create and configure the app
app = Flask(__name__, instance_relative_config=True)
api = Api(app, prefix='/api')
app.config.from_mapping(
    SECRET_KEY=';)',
    SQLALCHEMY_DATABASE_URI="mysql://root:15346@localhost:3306/vending-db",
)

models.db.init_app(app)

api.add_resource(Hello, '/')
api.add_resource(MachineApi, '/machine')

if __name__ == "__main__":
    app.run()
