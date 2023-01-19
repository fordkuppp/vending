from flask_restful import Resource, Api, reqparse
from vending.models import Machine, Product, Category, ProductCategory

parser = reqparse.RequestParser()
parser.add_argument('id', type=int)

machine_parser = parser.copy()
machine_parser.add_argument('building', type=int)
machine_parser.add_argument('floor', type=int)

product_parser = parser.copy()
product_parser.add_argument('name', type=str)
product_parser.add_argument('quantity', type=int)
product_parser.add_argument('price', type=float)


class Hello(Resource):
    def get(self):
        return {'task': 'Say "Hello, World!"'}


class MachineApi(Resource):
    def get(self):
        return Machine.id
