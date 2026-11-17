import os
import pytest
from config.config import BASE_URL
from clients.api_client import APIClient
@pytest.fixture
def client():
    api_client = APIClient(BASE_URL)
    yield api_client
    api_client.session.close()

@pytest.fixture
# def authenticated_client(client):

#     username = os.getenv("TEST_USERNAME")
#     password = os.getenv("TEST_PASSWORD")

#     if not username or not password:
#         pytest.fail("Test credentials missing from .env")

#     response = client.post(
#         "/login",
#         data={
#             "username": username,
#             "password": password
#         },
#         allow_redirects=False
#     )
#     print("Login status:", response.status_code)
#     print("Login redirect:", response.headers.get("Location"))
#     print("Session cookies:", client.session.cookies.get_dict())

#     assert response.status_code == 302
#     assert response.headers.get("Location") != "/login", (
#     f"Login was unsuccessful. Redirected to: "
#     f"{response.headers.get('Location')}"
# )

#     assert client.session.cookies

#     return client
def authenticated_client(client):
    username = os.getenv("TEST_USERNAME")
    password = os.getenv("TEST_PASSWORD")
    if not username or not password:
        pytest.fail("Test credentials missing from .env")
    response = client.post(
        "/login",
        data={
            "username": username,
            "password": password
        },
        allow_redirects=False
    )
    print("Login status:", response.status_code)
    print("Login redirect:", response.headers.get("Location"))
    print("Cookies:", client.session.cookies.get_dict())
    assert response.status_code == 302
    assert response.headers.get("Location") != "/login", "Login unsuccessful"
    protected_response = client.get(
        "/listings/new",
        allow_redirects=False
    )
    print("Protected route status:", protected_response.status_code)
    print("Protected route redirect:", protected_response.headers.get("Location"))
    assert protected_response.status_code == 200, "Session authentication not maintained"
    return client
