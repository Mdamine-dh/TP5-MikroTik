
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

    # DELETE: Supprimer l'adresse IP
    response = requests.delete(
        f"{BASE_URL}/ip/address/{address_id}",
        auth=AUTH,
        timeout=5
    )

    response.raise_for_status()

    print("Adresse IP supprimée avec succès !")
