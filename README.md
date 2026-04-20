
# 💰 SafeLoan AI – Loan Risk Analyzer

SafeLoan AI is an AI-powered system that analyzes loan documents and detects potential financial risks such as penalties, high interest rates, and default clauses.

It helps users understand complex loan agreements quickly and make informed financial decisions.

---

## 🚀 Features

* 📄 Upload **loan documents (Images & PDFs)**
* 🔍 Extract text using **OCR (Tesseract)**
* 🧠 Analyze content using **NLP pipeline**
* ⚠️ Detect risky clauses (penalty, interest, default, etc.)
* 📊 Generate **risk score (0–100)**
* 🎯 Provide **final decision (Low / Medium / High Risk)**
* 🌍 Supports **multilingual input (English + Hindi)**
* 🔒 Works **offline (no external API dependency)**

---

## 🧠 How It Works

The system follows a pipeline architecture:

```
User Input → OCR → Image Processing → NLP Analysis → Risk Score → Output UI
```

### Step-by-step:

1. User uploads document (image or PDF)
2. OpenCV preprocesses image for better clarity
3. Tesseract OCR extracts text
4. NLP logic detects risk keywords
5. System calculates risk score and displays results

---

## 🛠️ Tech Stack

### 🔹 Frontend

* React.js
* Axios
* React Icons

### 🔹 Backend

* Flask (Python API)
* Flask-CORS

### 🔹 Core Technologies

* Tesseract OCR → Text extraction
* OpenCV → Image preprocessing
* NumPy → Image handling
* pdf2image → PDF to image conversion
* Regex → Text processing
* Custom NLP → Risk detection

---

## 📂 Project Structure

```
loan-detector/
│
├── backend/
│   ├── app.py
│   ├── uploads/
│
├── frontend/
│   ├── src/
│   ├── package.json
│
└── README.md
```

---

## ⚙️ Installation & Setup

### 🔹 Backend Setup

```bash
cd backend
pip install flask flask-cors pytesseract opencv-python numpy pdf2image
brew install tesseract
brew install poppler
python app.py
```

---

### 🔹 Frontend Setup

```bash
cd frontend
npm install
npm start
```

---

## 🌍 Supported Inputs

* PNG / JPG / JPEG images
* PDF documents (multi-page supported)

---

## 🎯 Use Cases

* Loan agreement analysis
* Financial risk awareness
* Banking & fintech applications
* Legal document understanding

---

## 🔮 Future Scope

* 🤖 AI-based semantic analysis (BERT / LLMs)
* 🌐 Support for more regional languages
* 📊 Financial impact prediction
* ☁️ Cloud deployment for scalability
* 📱 Mobile app integration

---

## 🏆 Key Highlights

* Fully **offline system (no API cost)**
* Ensures **data privacy**
* Built as a **complete end-to-end pipeline**
* Beginner-friendly yet scalable architecture

---

## 👨‍💻 Team

**Team Name:** Young Monks
**Member:** Arpit Patni 

---

## 📌 Conclusion

SafeLoan AI simplifies complex loan documents by converting them into understandable insights. It empowers users to make safer financial decisions using AI-driven analysis.

---

⭐ If you like this project, consider giving it a star!
