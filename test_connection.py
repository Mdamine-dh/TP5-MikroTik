
import os
import requests
from dotenv import load_dotenv

load_dotenv()

DEVICE_HOST = os.getenv("DEVICE_HOST")
DEVICE_USER = os.getenv("DEVICE_USER")
DEVICE_PASSWORD = os.getenv("DEVICE_PASSWORD")

BASE_URL = f"http://{DEVICE_HOST}/rest"
AUTH = (DEVICE_USER, DEVICE_PASSWORD)

try:
    resp = requests.get(
        f"{BASE_URL}/ip/address",
        auth=AUTH,
        timeout=5
    )

    resp.raise_for_status()

    print("Connexion MikroTik réussie !")
    print(resp.json())

except requests.exceptions.RequestException as e:
    print("Erreur de connexion :", e)
