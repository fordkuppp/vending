import pytest
from sqlalchemy.exc import NoResultFound


def test_all_categories(app):
    response = app.test_client().get("/api/categories")
    assert response.status_code == 200


def test_category_api(app, models):
    post_response = app.test_client().post("/api/category", json={"name": "A"})
    assert post_response.status_code == 200
    with app.app_context():
        new_category_id = post_response.get_json()["id"]
        category = (
            models.db.session.query(models.Category)
            .filter(models.Category.id == new_category_id)
            .one()
        )
        assert models.Category == type(category)

    get_response = app.test_client().get(f"/api/category/{category.id}")
    assert get_response.status_code == 200
    assert get_response.get_json() != {}

    put_response = app.test_client().put(f"/api/category/{category.id}")
    assert put_response.status_code == 200
    assert put_response.get_json() != {}

    delete_response = app.test_client().delete(f"/api/category/{category.id}")
    assert delete_response.status_code == 204
    with app.app_context():
        with pytest.raises(NoResultFound):
            models.db.session.query(models.Category).filter(
                models.Category.id == category.id
            ).one()
