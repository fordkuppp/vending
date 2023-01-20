from dataclasses import dataclass

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


@dataclass
class Machine(db.Model):
    id: int
    building_num: int
    floor: int

    id = db.Column(db.Integer, primary_key=True)
    building_num = db.Column(db.Integer)
    floor = db.Column(db.Integer)


@dataclass
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    machine_id = db.Column(db.Integer, db.ForeignKey(Machine.id))
    name = db.Column(db.String(255))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)


@dataclass
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


@dataclass
class ProductCategory(db.Model):
    product_id = db.Column(db.Integer, db.ForeignKey(Product.id), primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey(Category.id))
