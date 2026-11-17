
import os
import requests
from dotenv import load_dotenv

load_dotenv()

DEVICE_HOST = os.getenv("DEVICE_HOST")
DEVICE_USER = os.getenv("DEVICE_USER")
DEVICE_PASSWORD = os.getenv("DEVICE_PASSWORD")

BASE_URL = f"http://{DEVICE_HOST}/rest"
AUTH = (DEVICE_USER, DEVICE_PASSWORD)

# GET: Rechercher l'adresse IP
response = requests.get(
    f"{BASE_URL}/ip/address",
    auth=AUTH,
    timeout=5
)
response.raise_for_status()

addresses = response.json()

ip = next(
    (item for item in addresses
     if item["address"] == "192.168.20.1/24"),
    None
)

if ip is None:
    print("Adresse IP introuvable")
else:
    address_id = ip[".id"]
    print("ID trouvé:", address_id)

    # PATCH: Modifier le commentaire
    payload = {
        "comment": "IP added by Python"
    }

    response = requests.patch(
        f"{BASE_URL}/ip/address/{address_id}",
        json=payload,
        auth=AUTH,
        timeout=5
    )

    response.raise_for_status()

    print("Commentaire modifié avec succès !")
    print(response.json())
