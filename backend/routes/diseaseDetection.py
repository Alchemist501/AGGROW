import io
import torch
from PIL import Image
from utils.model import ResNet9
from torchvision import transforms
import google.generativeai as genai
from flask import Blueprint, request, jsonify
from Data.disease_classes import disease_classes

diseaseDetection_bp = Blueprint("diseaseDetection", __name__)

disease_model = ResNet9(3, len(disease_classes))
disease_model.load_state_dict(
    torch.load(
        "models/diseaseDetection/plant_disease_model.pth",
        map_location=torch.device("cpu"),
    )
)
disease_model.eval()


@diseaseDetection_bp.route("/api/disease-detection", methods=["POST"])
def detect_disease():
    try:
        if "file" not in request.files:
            return jsonify({"success": False, "error": "No file uploaded"}), 400

        file = request.files["file"]
        if file.filename == "":
            return jsonify({"success": False, "error": "No selected file"}), 400

        image = Image.open(io.BytesIO(file.read())).convert("RGB")
        transform = transforms.Compose(
            [
                transforms.Resize(256),
                transforms.ToTensor(),
            ]
        )
        img_tensor = transform(image).unsqueeze(0)

        with torch.no_grad():
            output = disease_model(img_tensor)
            _, predicted = torch.max(output, 1)
            prediction = disease_classes[predicted.item()]
            confidence = float(
                torch.max(torch.nn.functional.softmax(output, dim=1)) * 100
            )

        # Gemini content generation with error handling
        try:
            prompt = f"Suggest both organic and chemical treatments for the following plant disease in a short and concise manner: {prediction.replace('_', ' ')}."
            model = genai.GenerativeModel("gemini-2.0-flash")
            gemini_response = model.generate_content(prompt)
            cures = gemini_response.text.strip()
        except Exception as gemini_error:
            cures = f"Unable to generate treatment suggestions: {str(gemini_error)}"

        return jsonify(
            {
                "success": True,
                "prediction": prediction,
                "confidence": round(confidence, 2),
                "cures": cures,
            }
        )
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
