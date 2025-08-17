# tests/test_users.py
from uuid import uuid4

def test_create_user(client):
    unique_email = f"test_{uuid4().hex[:8]}@example.com"

    resp = client.post("/users/", json={
        "email": unique_email,
        "password": "password123"
    })

    assert resp.status_code in (200, 201)  # your API may return 200 or 201
    data = resp.json()
    assert data["email"] == unique_email
    assert "id" in data
