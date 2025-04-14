import pickle
from flask import Blueprint, request, jsonify

cropRecommendation_bp = Blueprint("cropRecommendation", __name__)

# Load models
with open("models/cropRecommendationModel/CropRecommendation.pkl", "rb") as file:
    crop_recommendation_model = pickle.load(file)


@cropRecommendation_bp.route("/recommendation", methods=["POST"])
def predict_crop():
    try:
        data = request.get_json()
        features = [
            float(data["nitrogen"]),
            float(data["phosphorous"]),
            float(data["pottasium"]),
            float(data["temperature"]),
            float(data["humidity"]),
            float(data["ph"]),
            float(data["rainfall"]),
        ]
        prediction = crop_recommendation_model.predict([features])
        return jsonify({"success": True, "recommendedCrop": prediction[0]})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
