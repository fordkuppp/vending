import pytest
from sqlalchemy.exc import NoResultFound


def test_all_machines(app):
    response = app.test_client().get("/api/machines")
    assert response.status_code == 200


def test_machine_api(app, models):
    post_response = app.test_client().post(
        "/api/machine", json={"building_num": "99", "floor": "88"}
    )
    assert post_response.status_code == 200
    with app.app_context():
        new_machine_id = post_response.get_json()["id"]
        machine = (
            models.db.session.query(models.Machine)
            .filter(models.Machine.id == new_machine_id)
            .one()
        )
        assert models.Machine == type(machine)

    get_response = app.test_client().get(f"/api/machine/{machine.id}")
    assert get_response.status_code == 200
    assert get_response.get_json() != {}

    put_response = app.test_client().put(f"/api/machine/{machine.id}")
    assert put_response.status_code == 200
    assert put_response.get_json() != {}

    delete_response = app.test_client().delete(f"/api/machine/{machine.id}")
    assert delete_response.status_code == 204
    with app.app_context():
        with pytest.raises(NoResultFound):
            models.db.session.query(models.Machine).filter(
                models.Machine.id == machine.id
            ).one()
