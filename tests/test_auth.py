import pytest
def test_login(authenticated_client):
    response = authenticated_client.get("/listings")
    assert response.status_code == 200
def test_login(authenticated_client):
    response = authenticated_client.get("/listings")
    assert response.status_code == 200
def test_invalid_login(client):
    response = client.post(
        "/login",
        data={
            "username": "invalid_test_user",
            "password": "wrong_password"
        },
        allow_redirects=False
    )
    assert response.status_code == 302
    assert response.headers.get("Location")
def test_login_with_wrong_password(client):
    response = client.post(
        "/login",
        data={
            "username": "YOUR_TEST_USERNAME",
            "password": "wrong_password"
        },
        allow_redirects=False
    )
    assert response.status_code == 302
    assert response.headers.get("Location")
    import pytest

@pytest.mark.parametrize(
    "username,password",
    [
        ("wrong_user", "wrong_pass"),
        ("invalid_user", "123456"),
        ("", "password"),
        ("test_user", "")
    ]
)
def test_invalid_login_multiple_inputs(client, username, password):
    response = client.post(
        "/login",
        data={
            "username": username,
            "password": password
        },
        allow_redirects=False
    )
    assert response.status_code == 302
