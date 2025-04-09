import requests

# API URL & Headers
SOIL_API_URL = "https://soilhealth4.dac.gov.in/"
HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/json",
    "Accept": "application/json",
}


def get_state_from_coords(lat, lon):
    """Fetch state and district from coordinates using OpenStreetMap API."""
    try:
        url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}"
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        if response.status_code != 200:
            return None
        data = response.json()
        return {
            "state": data.get("address", {}).get("state", "Unknown State"),
            "district": data.get("address", {}).get(
                "state_district", "Unknown District"
            ),
        }
    except Exception:
        return None


def get_state_id(state_name):
    """Fetch state ID from soil API."""
    payload = {"query": "query { getNutrientDashboardForPortal }"}
    try:
        response = requests.post(SOIL_API_URL, json=payload, headers=HEADERS)
        data = response.json()
        for state in data["data"]["getNutrientDashboardForPortal"]:
            if state["state"]["name"].lower() == state_name.lower():
                return state["state"]["_id"]
    except Exception:
        return None


def get_district_soil_details(state_id, district_name):
    """Fetch soil details for a specific district."""
    payload = {
        "query": f'query {{ getNutrientDashboardForPortal(state:"{state_id}") }}'
    }
    try:
        response = requests.post(SOIL_API_URL, json=payload, headers=HEADERS)
        data = response.json().get("data", {}).get("getNutrientDashboardForPortal", [])
        for entry in data:
            if (
                entry["district"]["name"].strip().lower()
                == district_name.strip().lower()
            ):
                return entry["results"]
    except Exception:
        return None
    return None
