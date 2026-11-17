
import os
import requests
from dotenv import load_dotenv

# Charger les variables depuis .env
load_dotenv()

DEVICE_HOST = os.getenv("DEVICE_HOST")
DEVICE_USER = os.getenv("DEVICE_USER")
DEVICE_PASSWORD = os.getenv("DEVICE_PASSWORD")

BASE_URL = f"http://{DEVICE_HOST}/rest"
AUTH = (DEVICE_USER, DEVICE_PASSWORD)

# Liste des routes à configurer
routes = [
    {
        "destination": "10.10.10.0/24",
        "gateway": "192.168.44.2"
    },
    {
        "destination": "172.16.10.0/24",
        "gateway": "192.168.44.2"
    }
]

try:
    # GET: Recuperer les routes existantes
    response = requests.get(
        f"{BASE_URL}/ip/route",
        auth=AUTH,
        timeout=5
    )

    response.raise_for_status()
    existing_routes = response.json()

    print("Verification des routes...")

    # Verifier chaque route
    for route in routes:

        exists = any(
            item.get("dst-address") == route["destination"]
            and item.get("gateway") == route["gateway"]
            for item in existing_routes
        )

        if exists:
            print(
                f"Route deja existante : "
                f"{route['destination']}"
            )

        else:
            # PUT: Ajouter la route manquante
            payload = {
                "dst-address": route["destination"],
                "gateway": route["gateway"]
            }

            response = requests.put(
                f"{BASE_URL}/ip/route",
                json=payload,
                auth=AUTH,
                timeout=5
            )

            response.raise_for_status()

            print(
                f"Route ajoutee : "
                f"{route['destination']}"
            )

    print("\nConfiguration terminee !")

except requests.exceptions.RequestException as e:
    print("Erreur :", e)

