# 💰 SafeLoan AI — Loan Risk Analyzer

> 🚀 Understand Loan Risks in Seconds using AI

---

## 📌 Overview

**SafeLoan AI** is an AI-powered system that helps users analyze loan agreements and detect hidden financial risks.
It uses **OCR (Optical Character Recognition)** and **NLP (Natural Language Processing)** to extract text from documents and highlight risky clauses.

This tool is especially useful for:

- Students
- First-time borrowers
- Rural users with limited financial awareness

---

## 🎯 Problem Statement

Many people sign loan agreements without fully understanding:

- Hidden penalties
- High interest rates
- Complex financial terms

⚠️ Studies show that **over 60% of borrowers do not fully understand loan documents**.

---

## 💡 Our Solution

SafeLoan AI solves this by:

- Extracting text from images/PDFs
- Identifying risky terms
- Providing a **risk score (0–100)**
- Giving **clear explanations**

👉 Works **offline**, ensuring **privacy and accessibility**

---

## ✨ Key Features

- 📄 OCR-based text extraction (images + PDFs)
- 🧠 AI + Rule-based risk detection
- 📊 Risk score calculation (0–100)
- 🚨 Highlighted risky clauses
- 🌐 Multilingual support (English + Hindi)
- 🔒 Fully offline (no external APIs used)

---

## 🧠 How It Works (Pipeline)

```text
User Upload → OCR (Tesseract) → OpenCV Processing → NLP Analysis → Risk Score → UI Output
```

---

## 🛠️ Tech Stack

### 🔹 Frontend

- React.js
- Axios
- CSS

### 🔹 Backend

- Flask (Python)
- OpenCV
- Pytesseract (OCR)
- pdf2image
- NumPy
- Regex (text processing)

---

Example Output:

- Extracted loan text
- Risk score
- Highlighted risky keywords
- Explanation of risks

---

## 🚀 How to Run Locally

### 🔹 1. Clone Repository

```bash
git clone https://github.com/your-username/Safe-Loan-Ai.git
cd Safe-Loan-Ai
```

---

### 🔹 2. Backend Setup

```bash
cd backend
pip install -r requirements.txt
python app.py
```

👉 Runs on: `http://127.0.0.1:5001`

---

### 🔹 3. Frontend Setup

```bash
cd frontend
npm install
npm start
```

👉 Runs on: `http://localhost:3000`

---

## 🌍 Multilingual Support

Supports:

- English 🇺🇸
- Hindi 🇮🇳

👉 Detects keywords like:

- penalty / जुर्माना
- interest / ब्याज
- default / डिफ़ॉल्ट

---

## 🔮 Future Scope

- 🤖 Advanced AI models (BERT / LLM)
- 📊 Financial risk prediction
- 🎤 Voice-based input (for rural users)
- 📱 Mobile app development
- 🏦 Integration with banking systems

---

## 🏆 What Makes Us Unique

- 🔒 Works completely offline
- 🌐 Multilingual analysis
- ⚡ Real-time processing
- 🧩 End-to-end system (not API-based)

---

## 👨‍💻 Team

**Team Name:** Young Monks
**Member:** Arpit Patni

---

## 📢 Conclusion

SafeLoan AI empowers users to:

> **Make smarter and safer financial decisions**

---

## ⭐ Show Your Support

If you like this project:

- ⭐ Star this repo
- 🍴 Fork it
- 🚀 Share it

---
