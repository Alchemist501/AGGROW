from flask import Blueprint, request, jsonify
from utils.recommend import recommend_fertilizer
from utils.range import range
from utils.locationFetch import (
    get_state_from_coords,
    get_state_id,
    get_district_soil_details,
)
import json

fertilizer_bp = Blueprint("fertilizer", __name__)

# Load predefined NPK & pH ranges from Fertilizer.csv
nitrogen_range = range()[0]
phosphorous_range = range()[1]
potassium_range = range()[2]
ph_values = range()[3]


@fertilizer_bp.route("/autofill", methods=["GET"])
def autofill_data():
    lat, lon = request.args.get("lat"), request.args.get("lon")
    if not lat or not lon:
        return jsonify({"error": "Latitude and longitude are required"}), 400
    location = get_state_from_coords(lat, lon)
    if not location:
        return jsonify({"error": "Failed to determine state"}), 500

    state, district = location["state"], location["district"]
    state_id = get_state_id(state)
    if not state_id:
        return jsonify({"error": "State not found in soil database"}), 404

    soil_data = get_district_soil_details(state_id, district)
    if not soil_data:
        return jsonify({"error": "Soil data not available"}), 404

    # Determine dominant NPK & pH levels
    n_dominant = max(soil_data["n"], key=soil_data["n"].get)
    p_dominant = max(soil_data["p"], key=soil_data["p"].get)
    k_dominant = max(soil_data["k"], key=soil_data["k"].get)
    pH_dominant = max(soil_data["pH"], key=soil_data["pH"].get)

    autofill_data = {
        "nitrogen": float(nitrogen_range[n_dominant.lower()]),
        "phosphorous": float(phosphorous_range[p_dominant.lower()]),
        "potassium": float(potassium_range[k_dominant.lower()]),
        "ph": float(ph_values[pH_dominant.lower()]),
    }
    return json.loads(json.dumps(autofill_data, default=int))


@fertilizer_bp.route("/recommend", methods=["POST"])
def predict_fertilizer():
    try:
        data = request.get_json()
        crop_name = data["crop_type"]
        fertilizer = recommend_fertilizer(
            data["nitrogen"],
            data["phosphorous"],
            data["potassium"],
            data.get("ph"),
            crop_name,
        )
        return jsonify({"fertilizer": fertilizer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
