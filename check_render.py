from config.config import BASE_URL
from clients.api_client import APIClient

client = APIClient(BASE_URL)

response = client.get("/listings", timeout=30)

print("Status:", response.status_code)
print("URL:", response.url)
print("Content-Type:", response.headers.get("Content-Type"))
print("Response:", response.text[:500])

client.session.close()