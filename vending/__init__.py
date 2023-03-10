from flask import Flask
from flask_restful import Api

from vending import models
from vending.api.crud import (
    AllCategoryApi,
    AllMachineApi,
    AllProductApi,
    CategoryApi,
    MachineApi,
    ProductApi,
)

# create and configure the app
app = Flask(__name__, instance_relative_config=True)
api = Api(app, prefix="/api")
app.config.from_mapping(
    SECRET_KEY=";)",
    SQLALCHEMY_DATABASE_URI="mysql://root:root@localhost:3306/vending-db",
)

models.db.init_app(app)

api.add_resource(AllMachineApi, "/machines")
api.add_resource(MachineApi, "/machine/<int:machine_id>", "/machine")

api.add_resource(AllProductApi, "/products")
api.add_resource(ProductApi, "/product/<int:product_id>", "/product")

api.add_resource(AllCategoryApi, "/categories")
api.add_resource(CategoryApi, "/category/<int:category_id>", "/category")

if __name__ == "__main__":
    app.run()
