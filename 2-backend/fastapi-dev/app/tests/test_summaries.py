import json

import pytest


def test_create_summary(test_app_with_db):
    response = test_app_with_db.post(
        "/summaries/1/", content=json.dumps({"url": "https://foo.bar"})
    )

    assert response.status_code == 201
    assert response.json()["url"] == "https://foo.bar"


@pytest.mark.parametrize("summary_id, payload, status_code, detail", [
    [999, {"url": "https://foo.bar", "summary": "updated!"}, 201, {"url": "https://foo.bar", "id": 999}],
    [1, {"url": "https://foo2.bar", "summary": "updated!"}, 201,  {"url": "https://foo2.bar", "id": 1}]
])
def test_update_summary_invalid(test_app_with_db, summary_id, payload, status_code, detail):
    response = test_app_with_db.post(
        f"/summaries/{summary_id}",
        content=json.dumps(payload)
    )

    assert response.status_code == status_code
    assert response.json()["id"] == detail["id"]
    assert response.json()["url"] == detail["url"]