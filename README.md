# Vending Machine Tracking APIs

## Instruction

### Create database schema
Edit the `SQLALCHEMY_DATABASE_URI` in `__init__.py`:
```python
"mysql://user:password@localhost:3306/vending-db"
```
to your database uri.

### Create tables
Run `create_tables.py` to create tables with empty content..

### Run
Use this command at the root directory of this repo:
```sh
flask --app vending
```
