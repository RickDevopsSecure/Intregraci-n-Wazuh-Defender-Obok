import requests
import json
import os
import time

API_KEY = ""
API_RECOMMENDATIONS = "https://api.gethypercube.com/recommendations"
LOG_FILE = "/var/ossec/logs/hypercube_logs.json"

def get_recommendations():
    headers = {"Authorization": f"Bearer {API_KEY}", "Accept": "application/json"}
    params = {"limit": 100, "sortBy": "updatedAt:desc", "status": "Pending"}

    try:
        response = requests.get(API_RECOMMENDATIONS, headers=headers, params=params, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")
        return None

def save_to_log(data):
    with open(LOG_FILE, "a") as log_file:
        for rec in data.get("result", []):
            log_entry = {
                "integration": rec.get("integration", ""),
                "title": rec.get("title", ""),
                "description": rec.get("description", ""),
                "status": rec.get("status", ""),
                "created_at": rec.get("createdAt", ""),
                "updated_at": rec.get("updatedAt", ""),
                "documentation": f"https://knowledge.getobok.com/?s={rec.get('_id', '')}"
            }
            log_file.write(json.dumps(log_entry) + "\n")

def main():
    start_time = time.time()
    recommendations = get_recommendations()
    if recommendations:
        save_to_log(recommendations)
    print(f"Proceso completado en {time.time() - start_time:.2f} segundos")

if __name__ == "__main__":
    main()
