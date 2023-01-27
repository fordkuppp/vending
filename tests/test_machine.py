from vending import app


def test_all_machines():
    response = app.test_client().get('/api/machines')
    assert response.status_code == 500

def test_post_machines():
    response = app.test_client().post('/api/machine/<int:machine_id>', json={
        "building_num": "99",
        "floor": "88"
    })
    assert response.status_code == 200
