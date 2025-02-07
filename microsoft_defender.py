import requests
import json
import os

# 📌 Credenciales de Azure AD (Reemplazadas con tus valores de ejemplo)
TENANT_ID = ""  # Directory ID
CLIENT_ID = ""  # Application (Client) ID
CLIENT_SECRET = ""  # Valor del secreto de cliente

# 📌 URL de autenticación en Azure AD
AUTH_URL = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"

# 📌 URL de la API de Microsoft Defender para obtener incidentes
DEFENDER_API_URL = "https://api.security.microsoft.com/api/incidents"

# 🔐 Obtener Token de acceso desde Azure AD
def get_access_token():
    data = {
        "client_id": CLIENT_ID,
        "scope": "https://api.security.microsoft.com/.default",
        "client_secret": CLIENT_SECRET,
        "grant_type": "client_credentials"
    }
    response = requests.post(AUTH_URL, data=data)
    response.raise_for_status()
    return response.json()["access_token"]

# 🔍 Obtener incidentes de Microsoft Defender
def get_defender_incidents():
    headers = {
        "Authorization": f"Bearer {get_access_token()}",
        "Content-Type": "application/json"
    }
    response = requests.get(DEFENDER_API_URL, headers=headers)
    response.raise_for_status()
    return response.json()["value"]

# 💾 Guardar logs en un archivo para que Wazuh los procese
def save_logs_to_file(logs):
    log_file = "/var/log/microsoft_defender.log"
    with open(log_file, "a") as file:
        for log in logs:
            file.write(json.dumps(log) + "\n")

# 🚀 Ejecutar el proceso
if __name__ == "__main__":
    try:
        incidents = get_defender_incidents()
        if incidents:
            save_logs_to_file(incidents)
            print("✅ Logs guardados en /var/log/microsoft_defender.log")
        else:
            print("⚠️ No se encontraron nuevos incidentes.")
    except Exception as e:
        print(f"❌ Error: {e}")

