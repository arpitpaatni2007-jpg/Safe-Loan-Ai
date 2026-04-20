from flask import Flask, request, jsonify
from flask_cors import CORS
import pytesseract
import cv2
import numpy as np
import os
from pdf2image import convert_from_path
import re

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# 🔥 Keywords (English + Hindi)
KEYWORDS = {
    # English
    "penalty": ("HIGH", "Heavy penalty charges may apply."),
    "interest": ("MEDIUM", "High interest rate can increase total repayment."),
    "late fee": ("HIGH", "Late payment will add extra cost."),
    "compound": ("HIGH", "Compound interest grows rapidly."),
    "default": ("HIGH", "Defaulting may cause legal issues."),

    # Hindi
    "जुर्माना": ("HIGH", "अतिरिक्त शुल्क लागू हो सकता है।"),
    "ब्याज": ("MEDIUM", "ब्याज दर कुल भुगतान बढ़ा सकती है।"),
    "देरी शुल्क": ("HIGH", "देरी से भुगतान पर अतिरिक्त शुल्क लगेगा।"),
    "चक्रवृद्धि": ("HIGH", "चक्रवृद्धि ब्याज तेजी से बढ़ता है।"),
    "डिफ़ॉल्ट": ("HIGH", "भुगतान न करने पर कानूनी कार्रवाई हो सकती है।")
}

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "pdf"}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# 🧠 Detect Hindi
def is_hindi(text):
    return re.search(r'[\u0900-\u097F]', text) is not None


# 🧠 Image preprocessing
def preprocess_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        return None

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return thresh


def preprocess_image_array(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return thresh


# 🔥 SAFE OCR (NO CRASH)
def extract_text(file_path):
    text = ""

    try:
        if file_path.lower().endswith(".pdf"):
            pages = convert_from_path(file_path)
            for page in pages:
                img = np.array(page)
                processed = preprocess_image_array(img)
                text += pytesseract.image_to_string(processed, lang='eng+hin')
        else:
            processed = preprocess_image(file_path)
            if processed is not None:
                text = pytesseract.image_to_string(processed, lang='eng+hin')

    except Exception as e:
        print("❌ OCR ERROR:", e)
        return ""

    return text


# 🔥 NLP
def analyze_text(text):
    sentences = re.split(r'[.|।]', text)
    results = []
    risk_score = 0

    hindi_mode = is_hindi(text)

    for sentence in sentences:
        sentence = sentence.strip().replace("\n", " ")
        if not sentence:
            continue

        detected = []

        for word, (level, explanation) in KEYWORDS.items():
            if word.lower() in sentence.lower():
                detected.append((word, level, explanation))

        if detected:
            final_level = "LOW"
            final_explanation = ""
            keywords_found = []

            for word, level, explanation in detected:
                keywords_found.append(word)

                if level == "HIGH":
                    final_level = "HIGH"
                    final_explanation = explanation
                    break
                elif level == "MEDIUM":
                    final_level = "MEDIUM"
                    final_explanation = explanation

            # 🔥 Hindi / English label
            if hindi_mode:
                level_map = {
                    "HIGH": "उच्च जोखिम",
                    "MEDIUM": "मध्यम जोखिम",
                    "LOW": "कम जोखिम"
                }
                display_level = level_map[final_level]
            else:
                display_level = final_level

            results.append({
                "sentence": sentence,
                "risk": display_level,
                "explanation": final_explanation,
                "keywords": keywords_found
            })

            if final_level == "HIGH":
                risk_score += 30
            elif final_level == "MEDIUM":
                risk_score += 15

    return results, min(risk_score, 100), hindi_mode


@app.route('/')
def home():
    return "Backend is running 🚀"


@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        print("📩 Request received")

        if 'file' not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({"error": "Empty filename"}), 400

        if not allowed_file(file.filename):
            return jsonify({"error": "Invalid file type"}), 400

        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        print("📂 File saved:", filepath)

        text = extract_text(filepath)

        if not text.strip():
            return jsonify({"error": "Could not extract text"}), 400

        results, score, hindi_mode = analyze_text(text)

        # 🔥 Overall Risk
        if score > 70:
            overall = "HIGH RISK"
        elif score > 40:
            overall = "MEDIUM RISK"
        else:
            overall = "LOW RISK"

        # Hindi version
        if hindi_mode:
            overall_map = {
                "HIGH RISK": "उच्च जोखिम",
                "MEDIUM RISK": "मध्यम जोखिम",
                "LOW RISK": "कम जोखिम"
            }
            overall = overall_map[overall]

        return jsonify({
            "text": text,
            "risks": results,
            "score": score,
            "overall_risk": overall
        })

    except Exception as e:
        print("❌ ERROR:", str(e))
        return jsonify({
            "error": "Internal server error",
            "details": str(e)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)