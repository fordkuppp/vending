from flask_restful import Resource, reqparse
# TODO: from flask_restful_swagger import swagger

from vending.models import *
from flask import jsonify

parser = reqparse.RequestParser()
parser.add_argument('id', type=int, location='form')

machine_parser = parser.copy()
machine_parser.add_argument('building', type=int, location='form')
machine_parser.add_argument('floor', type=int, location='form')

product_parser = parser.copy()
product_parser.add_argument('name', type=str, location='form')
product_parser.add_argument('quantity', type=int, location='form')
product_parser.add_argument('price', type=float, location='form')

category_parser = parser.copy()
category_parser.add_argument('name', type=str, location='form')


class MachineApi(Resource):
    def get(self, machine_id: int):
        machine = db.session.query(Machine).filter(Machine.id == machine_id).one()
        return jsonify(machine)

    def delete(self, machine_id: int):
        Machine.query.filter(Machine.id == machine_id).delete()
        db.session.commit()
        return {'status': '204'}, 204

    def put(self, machine_id: int):
        machine = db.session.query(Machine).filter(Machine.id == machine_id).one()
        args = machine_parser.parse_args()
        machine.floor = args['floor']
        machine.building_num = args['building']
        db.session.commit()
        return {'status': '204'}, 204

    def post(self):
        args = machine_parser.parse_args()
        new_machine = Machine(building_num=args['building'],
                              floor=args['floor'])
        db.session.add(new_machine)
        db.session.commit()
        return {'status': '201'}, 201


class ProductApi(Resource):
    def get(self, product_id: int):
        product = db.session.query(Product).filter(Product.id == product_id).one()
        return jsonify(product)

    def delete(self, product_id: int):
        Product.query.filter(Product.id == product_id).delete()
        db.session.commit()
        return {'status': '204'}, 204

    def put(self, product_id: int):
        product = db.session.query(Product).filter(Product.id == product_id).one()
        args = product_parser.parse_args()
        product.name = args['name']
        product.quantity = args['quantity']
        product.price = args['price']
        db.session.commit()
        return {'status': '204'}, 204

    def post(self):
        args = product_parser.parse_args()
        new_product = Product(name=args['name'])
        db.session.add(new_product)
        db.session.commit()
        return {'status': '201'}, 201


class CategoryApi(Resource):
    def get(self, category_id: int):
        category = db.session.query(Category).filter(Category.id == category_id).one()
        return jsonify(category)

    def delete(self, category_id: int):
        Category.query.filter(Category.id == category_id).delete()
        db.session.commit()
        return {'status': '204'}, 204

    def put(self, category_id: int):
        category = db.session.query(Category).filter(Category.id == category_id).one()
        args = category_parser.parse_args()
        category.name = args['name']
        db.session.commit()
        return {'status': '204'}, 204

    def post(self):
        args = category_parser.parse_args()
        new_category = Category(name=args['name'])
        db.session.add(new_category)
        db.session.commit()
        return {'status': '201'}, 201


class AllMachineApi(Resource):
    def get(self):
        machines = Machine.query.all()
        return jsonify(machines)


class AllProductApi(Resource):
    def get(self):
        products = Product.query.all()
        return jsonify(products)


class AllCategoryApi(Resource):
    def get(self):
        categories = Category.query.all()
        return jsonify(categories)