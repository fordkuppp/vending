# Vending Machine Tracking APIs
![build](https://github.com/fordkuppp/vending/actions/workflows/build.yml/badge.svg)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=fordkuppp_vending&metric=coverage)](https://sonarcloud.io/summary/new_code?id=fordkuppp_vending)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=fordkuppp_vending&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=fordkuppp_vending)

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
