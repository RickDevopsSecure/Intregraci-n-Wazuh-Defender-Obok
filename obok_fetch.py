import requests
import json
import os

# Configuración de la API de Obok
OBOk_API_URL = "https://api.getobok.com/v1/recommendations"
API_KEY = "TU_API_KEY"

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
