
import os
import requests
from dotenv import load_dotenv

load_dotenv()

DEVICE_HOST = os.getenv("DEVICE_HOST")
DEVICE_USER = os.getenv("DEVICE_USER")
DEVICE_PASSWORD = os.getenv("DEVICE_PASSWORD")

BASE_URL = f"http://{DEVICE_HOST}/rest"
AUTH = (DEVICE_USER, DEVICE_PASSWORD)

# POST: Ajouter une adresse IP
payload = {
    "address": "192.168.20.1/24",
    "interface": "ether2"
}


response = requests.put(
    f"{BASE_URL}/ip/address",
    json=payload,
    auth=AUTH,
    timeout=5
)

print("Status:", response.status_code)
print("Response:", response.text)

response.raise_for_status()

print("Adresse IP ajoutée avec succès !")

print(response.json())





