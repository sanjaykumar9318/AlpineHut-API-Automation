import json
from pathlib import Path
from jsonschema import validate
def test_listing_schema():
    schema_path = (
        Path(__file__).parent.parent
        / "schemas"
        / "listing_schema.json"
    )
    with open(schema_path) as file:
        schema = json.load(file)
    listing = {
        "title": "Mountain Hotel",
        "description": "Beautiful hotel",
        "price": 2500,
        "location": "Manali",
        "country": "India"
    }
    validate(instance=listing, schema=schema)