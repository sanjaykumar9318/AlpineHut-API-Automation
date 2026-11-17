from pathlib import Path
import uuid
import re
def test_get_listing_for_review(client):
    listing_id = "6afc57eea29ef2dd7a5e0e19"
    response = client.get(f"/listings/{listing_id}")
    assert response.status_code == 200

def test_add_review(authenticated_client):
      # 1. Create a unique test listing
    title = f"Review Test Hotel {uuid.uuid4().hex[:8]}"
    image_path = Path(__file__).parent.parent / "test_data" / "test_image.jpg"
    with open(image_path, "rb") as image:
        create_response = authenticated_client.post(
            "/listings",
            data={
                "listing[title]": title,
                "listing[description]": "Created for review automation",
                "listing[price]": 2500,
                "listing[location]": "Manali",
                "listing[country]": "India"
            },
            files={
                "listing[image]": ("test_image.jpg", image, "image/jpeg")
            },
            allow_redirects=False
        )
    assert create_response.status_code == 302
    # 2. Find the newly created listing ID
    import re
    listings_response = authenticated_client.get("/listings")
    match = re.search(
        rf'href="/listings/([a-f0-9]{{24}})"[^>]*>.*?'
        rf'<b>{re.escape(title)}</b>',
        listings_response.text,
        re.DOTALL
    )
    assert match, "Created test listing was not found"
    listing_id = match.group(1)
    # 3. Add a review
    review_response = authenticated_client.post(
        f"/listings/{listing_id}/reviews",
        data={
            "review[rating]": 5,
            "review[comment]": "Excellent stay"
        },
        allow_redirects=False
    )
    assert review_response.status_code == 302
    assert review_response.headers["Location"] == f"/listings/{listing_id}"
    # 4. Verify review appears on listing page
    detail_response = authenticated_client.get(f"/listings/{listing_id}")
    assert detail_response.status_code == 200
    assert "Excellent stay" in detail_response.text
    # 5. Cleanup: delete the test listing
    delete_response = authenticated_client.delete(
        f"/listings/{listing_id}",
        allow_redirects=False
    )
    assert delete_response.status_code == 302