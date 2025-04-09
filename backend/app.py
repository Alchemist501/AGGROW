from flask_cors import CORS
from flask import Flask, send_from_directory

from routes.fertilizer import fertilizer_bp
from routes.diseaseDetection import diseaseDetection_bp
from routes.cropRecommendation import cropRecommendation_bp


app = Flask(__name__, static_folder="static", static_url_path="/")
CORS(app)
app.register_blueprint(fertilizer_bp, url_prefix="/fertilizer")
app.register_blueprint(cropRecommendation_bp, url_prefix="/cropRecommendation")
app.register_blueprint(diseaseDetection_bp, url_prefix="/diseaseDetection")


# --- React routes ---
@app.route("/")
@app.route("/dashboard")
@app.route("/crop-recommendation")
@app.route("/fertilizer-recommendation")
@app.route("/disease-detection")
def serve_react():
    return send_from_directory(app.static_folder, "index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
