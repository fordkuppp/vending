from vending import app
from vending.models import db


with app.app_context():
    db.create_all()
