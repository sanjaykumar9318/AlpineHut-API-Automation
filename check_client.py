from config.config import BASE_URL
from clients.api_client import APIClient

client = APIClient(BASE_URL)
response = client.get("/listings")

print("Status:", response.status_code)
print("Final URL:", response.url)
print("Content Type:", response.headers.get("Content-Type"))