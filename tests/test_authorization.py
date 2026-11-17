
def test_create_listing_without_login(client):
    response = client.post(
        "/listings",
        data={},
        allow_redirects=False
    )
    assert response.status_code == 302
def test_access_nonexistent_listing(client):
    response = client.get(
        "/listings/000000000000000000000000",
        allow_redirects=False
    )
    assert response.status_code == 302
    assert response.headers["Location"] == "/listings"