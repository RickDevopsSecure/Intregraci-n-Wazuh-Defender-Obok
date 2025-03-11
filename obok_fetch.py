import requests
import json
import os

# Configuración de la API de Obok
OBOk_API_URL = "https://api.getobok.com/v1/recommendations"
API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwczovL2F1dGguZ2V0b2Jvay5jb20vdXNlcl9pZCI6ImF1dGgwfDY2Yzc5Yjk5ZDc3YmUwMmU2YTVmMGE4ZiIsInVzZXJJZCI6IjY2Yzc5YjlhZWM1NzM2NDJkMDQ3OWY2NyIsImFjY2Vzc0tleUlkIjoiNjdkMDk3NzEzMzJhOTdjZTVmZjRmZTQ2IiwiaWF0IjoxNzQxNzIzNTA1fQ.jYI-CYbBxG3KY0tfHYSDxO9wvD-4zz6fnA1Z0JJ_zp0"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Archivo donde se almacenarán los eventos
WAZUH_LOG_PATH = "/var/ossec/logs/alerts/obok_recommendations.log"

def obtener_recomendaciones():
    response = requests.get(OBOk_API_URL, headers=HEADERS)

    if response.status_code == 200:
        recomendaciones = response.json()

        # Guardar cada recomendación en el archivo de logs de Wazuh
        with open(WAZUH_LOG_PATH, "a") as log_file:
            for rec in recomendaciones:
                log_file.write(json.dumps(rec) + "\n")
        
        print("Recomendaciones guardadas correctamente en Wazuh.")
    else:
        print(f"Error al obtener recomendaciones: {response.status_code} - {response.text}")

if __name__ == "__main__":
    obtener_recomendaciones()
