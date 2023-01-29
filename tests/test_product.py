import pytest
from sqlalchemy.exc import NoResultFound


def test_all_products(app):
    response = app.test_client().get("/api/products")
    assert response.status_code == 200


def test_product_api(app, models):
    post_response = app.test_client().post(
        "/api/product",
        json={"machine_id": "1", "name": "A", "quantity": "99", "price": "88"},
    )
    assert post_response.status_code == 200
    with app.app_context():
        new_product_id = post_response.get_json()["id"]
        product = (
            models.db.session.query(models.Product)
            .filter(models.Product.id == new_product_id)
            .one()
        )
        assert models.Product == type(product)

    get_response = app.test_client().get(f"/api/product/{product.id}")
    assert get_response.status_code == 200
    assert get_response.get_json() != {}

    put_response = app.test_client().put(f"/api/product/{product.id}")
    assert put_response.status_code == 200
    assert put_response.get_json() != {}

    delete_response = app.test_client().delete(f"/api/product/{product.id}")
    assert delete_response.status_code == 204
    with app.app_context():
        with pytest.raises(NoResultFound):
            models.db.session.query(models.Product).filter(
                models.Product.id == product.id
            ).one()
