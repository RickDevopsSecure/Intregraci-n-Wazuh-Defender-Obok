import requests
import json
import logging
import time

# Configuración del logging
logging.basicConfig(
    filename='/var/ossec/logs/obok_logs.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Configuración de la API
API_URL = "https://api.gethypercube.com/recommendations"
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwczovL2F1dGguZ2V0b2Jvay5jb20vdXNlcl9pZCI6ImF1dGgwfDY2Yzc5Yjk5ZDc3YmUwMmU2YTVmMGE4ZiIsInVzZXJJZCI6IjY2Yzc5YjlhZWM1NzM2NDJkMDQ3OWY2NyIsImFjY2Vzc0tleUlkIjoiNjdiOGI0NDhmM2EyYTUzNDZlMGVlYmZlIiwiaWF0IjoxNzQwMTU4MDI0fQ.TZgsxqgLRkzSF89f_vRq8Vofy1hjXtGAZQ6hrju7gHE"
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

# ID de la organización
ORGANIZATION_ID = "62bb3427e72c89805bb1d1dd"

# Función para obtener recomendaciones
def get_recommendations(limit=10, page=1):
    params = {
        "sortBy": "createdAt:desc",
        "limit": limit,
        "pageNumber": page,
        "organizationId": ORGANIZATION_ID
    }
    try:
        response = requests.get(API_URL, headers=HEADERS, params=params)
        response.raise_for_status()  # Lanza un error si la respuesta es 4xx o 5xx
        data = response.json()
        
        # Guardar los logs
        with open("/var/ossec/logs/obok_recommendations.json", "w") as file:
            json.dump(data, file, indent=4)
        
        logging.info("Datos obtenidos y almacenados correctamente.")
        return data
    except requests.exceptions.RequestException as e:
        logging.error(f"Error en la solicitud: {e}")
        return None

# Función para visualizar los logs
def show_logs():
    try:
        with open("/var/ossec/logs/obok_recommendations.json", "r") as file:
            data = json.load(file)
            print(json.dumps(data, indent=4))
    except FileNotFoundError:
        logging.warning("El archivo de logs no existe.")
        print("No hay logs disponibles.")

# Ejecución automática cada cierto tiempo
def run_monitor(interval=600):  # Cada 10 minutos
    while True:
        logging.info("Ejecutando consulta a la API de Obok...")
        get_recommendations()
        time.sleep(interval)

if __name__ == "__main__":
    run_monitor()
