
from pathlib import Path
import re
import uuid


def test_get_listings(client):
    response = client.get("/listings")

    assert response.status_code == 200
    assert "text/html" in response.headers.get("Content-Type", "")


def test_get_listing_page(client):
    response = client.get("/listings")

    assert response.status_code == 200
    assert "listings" in response.text.lower()


def test_listing_crud(authenticated_client):

    client = authenticated_client

    # Unique title prevents conflicts with previous test runs
    title = f"Automation Hotel {uuid.uuid4().hex[:8]}"
    updated_title = f"Updated {title}"

    # Test image path
    image_path = (
        Path(__file__).parent.parent
        / "test_data"
        / "test_image.jpg"
    )

    assert image_path.exists(), "Test image not found"

    listing_id = None
    deleted = False

    try:
        # --------------------------------
        # POST - Create listing
        # --------------------------------

        with open(image_path, "rb") as image:
            response = client.post(
                "/listings",
                data={
                    "listing[title]": title,
                    "listing[description]": "Created by Pytest",
                    "listing[price]": 2500,
                    "listing[location]": "Manali",
                    "listing[country]": "India"
                },
                files={
                    "listing[image]": (
                        "test_image.jpg",
                        image,
                        "image/jpeg"
                    )
                },
                allow_redirects=False
            )
        print("POST status:", response.status_code)
        print("POST response:", response.text[-5000:])


        assert response.status_code == 302
        assert response.headers["Location"] == "/listings"

        # --------------------------------
        # GET - Find created listing ID
        # --------------------------------

        
        # --------------------------------
        # GET - Find created listing ID
        # --------------------------------

        response = client.get("/listings")

        assert response.status_code == 200
        assert title in response.text

        listing_id = None

        anchors = re.findall(
            r'<a href="/listings/([a-f0-9]{24})"[^>]*>(.*?)</a>',
            response.text,
            re.DOTALL
        )

        for candidate_id, anchor_html in anchors:
            if title in anchor_html:
                listing_id = candidate_id
                break

        assert listing_id, "Could not find ID for newly created listing"

        print("Created listing ID:", listing_id)

        # --------------------------------
        # GET - Verify listing details
        # --------------------------------

        # --------------------------------
        # GET - Verify listing details
        # --------------------------------

        response = client.get(f"/listings/{listing_id}")

        print("Listing ID:", listing_id)
        print("Detail page status:", response.status_code)
        print("Title expected:", title)
        print("Title found:", title in response.text)
        print(response.text[:5000])

        assert response.status_code == 200
        assert title in response.text
        print("Expected title:", title)
        print("Extracted listing ID:", listing_id)
        print("Detail page status:", response.status_code)
        print("Title found:", title in response.text)
        print(response.text[:4000])

        # --------------------------------
        # PUT - Update listing
        # --------------------------------

        response = client.put(
            f"/listings/{listing_id}",
            data={
                "listing[title]": updated_title,
                "listing[description]": "Updated by Pytest",
                "listing[price]": 3000,
                "listing[location]": "Manali",
                "listing[country]": "India"
            },
            allow_redirects=False
        )

        assert response.status_code == 302
        assert response.headers["Location"] == "/listings"

        # --------------------------------
        # GET - Verify updated listing
        # --------------------------------

        response = client.get(f"/listings/{listing_id}")

        assert response.status_code == 200
        assert updated_title in response.text
        assert "Updated by Pytest" in response.text

        # --------------------------------
        # DELETE - Delete listing
        # --------------------------------

        response = client.delete(
            f"/listings/{listing_id}",
            allow_redirects=False
        )

        assert response.status_code == 302
        assert response.headers["Location"] == "/listings"

        deleted = True

        # --------------------------------
        # GET - Verify deletion
        # --------------------------------
        response = client.get(
    f"/listings/{listing_id}",
    allow_redirects=False
)

        assert response.status_code == 302
        assert response.headers["Location"] == "/listings"  
    finally:

        # Cleanup if an earlier assertion fails
        if listing_id and not deleted:
            client.delete(
                f"/listings/{listing_id}",
                allow_redirects=False
            )
