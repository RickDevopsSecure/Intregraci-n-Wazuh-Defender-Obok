import requests
import json
import os
from msal import ConfidentialClientApplication

# Configurar credenciales de Azure
TENANT_ID = "261bc682-cd4a-4ee7-8ae4-9e82e1342e72"
CLIENT_ID = "81ca360c-5261-4226-abb5-99469b84ee04"
CLIENT_SECRET = "d22fa040-2099-41c0-ac2d-1e63a9e18b53"
AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPE = ["https://graph.microsoft.com/.default"]

# URL de la API de Defender
GRAPH_URL = "https://graph.microsoft.com/v1.0/security/alerts"

def get_access_token():
    app = ConfidentialClientApplication(CLIENT_ID, CLIENT_SECRET, AUTHORITY)
    result = app.acquire_token_for_client(SCOPES=SCOPE)
    return result.get("access_token", None)

def fetch_defender_logs():
    token = get_access_token()
    if not token:
        print("Error obteniendo el token de acceso.")
        return
    
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    response = requests.get(GRAPH_URL, headers=headers)
    
    if response.status_code == 200:
        alerts = response.json().get("value", [])
        for alert in alerts:
            print(json.dumps(alert))
            send_to_wazuh(json.dumps(alert))
    else:
        print(f"Error obteniendo logs: {response.status_code} - {response.text}")

def send_to_wazuh(log):
    with open("/var/ossec/logs/alerts/defender.log", "a") as f:
        f.write(log + "\n")

if __name__ == "__main__":
    fetch_defender_logs()
