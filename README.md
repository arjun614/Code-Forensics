# 🔍 Code Forensics

A code analysis system that classifies source code as **Machine-generated, Human-written, Hybrid, or Adversarial** using Machine Learning. The application combines **TF-IDF-based feature extraction** with a **Logistic Regression model** and provides confidence scores, class probabilities, and structural forensic analysis.

---

## 📌 Features

- 🧠 Classifies code into four categories:
  - Machine-generated
  - Human-written
  - Hybrid
  - Adversarial
- 📊 Confidence score for predictions
- 📈 Class probability distribution
- 🔤 Word-level TF-IDF feature extraction
- 🔡 Character-level TF-IDF feature extraction
- 🔍 Structural forensic code analysis
- 📋 Function, loop, conditional, and import detection
- 📊 Code statistics and token analysis
- ⚡ REST API built with FastAPI
- 💻 Interactive React-based dashboard

---

## 🛠 Tech Stack

### Machine Learning

- Python
- Scikit-learn
- TF-IDF
- Logistic Regression

### Backend

- FastAPI
- Pydantic
- Uvicorn
- REST API

### Frontend

- React.js
- Axios
- CSS3

---

## 📂 Project Structure

```text
AI-Forensics/
│
├── data/
│   └── task_c/
│       └── task_c_trial.parquet
│
├── models/
│   ├── code_detector_model.pkl
│   ├── word_vectorizer.pkl
│   └── char_vectorizer.pkl
│
├── src/
│   ├── train_baseline.py
│   ├── predict.py
│   ├── forensic_analysis.py
│   └── app.py
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   └── App.css
│   └── package.json
│
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

```text
User Code
    │
    ▼
React Frontend
    │
    ▼
FastAPI Backend
    │
    ├───────────────┐
    ▼               ▼
ML Prediction    Forensic Analysis
    │               │
    ▼               ▼
TF-IDF Features   Code Statistics
    │
    ▼
Logistic Regression
    │
    ▼
Prediction + Probabilities
    │
    ▼
Structured JSON Response
    │
    ▼
React Dashboard
```

---

## 🧠 Machine Learning Approach

The project uses a supervised machine learning approach to classify source code.

### Dataset

The dataset contains code samples labeled into four categories:

- `0` → Machine-generated
- `1` → Human-written
- `2` → Hybrid
- `3` → Adversarial

The dataset is split into:

- **80% Training Data**
- **20% Testing Data**

Stratified sampling is used to maintain class distribution.

---

### Feature Extraction

Raw source code cannot be directly processed by a machine learning model. Therefore, the code is converted into numerical features using two TF-IDF vectorizers.

#### Word-Level TF-IDF

- Analyzer: `word`
- N-gram range: `1–2`
- Maximum features: `20,000`

#### Character-Level TF-IDF

- Analyzer: `char`
- N-gram range: `3–5`
- Maximum features: `30,000`

Both feature sets are combined before training the model.

---

### Model

The classification model uses:

- **Logistic Regression**
- `class_weight="balanced"`
- `max_iter=1000`

Class balancing is used to reduce the impact of dataset imbalance.

---

## 📊 Model Performance

Current model performance:

- **Accuracy:** ~68%
- **Macro F1 Score:** ~0.54

The model performs relatively well on:

- Machine-generated code
- Human-written code

Hybrid and Adversarial code remain more challenging to classify.

---

## 🔍 Forensic Analysis

Along with ML classification, the application performs structural analysis of the submitted code.

The analysis includes:

- Total characters
- Total lines
- Non-empty lines
- Blank lines
- Comment lines
- Comment ratio
- Average line length
- Function count
- Loop count
- Conditional count
- Import count
- Class count
- Exception count
- Token count
- Unique token count

These metrics provide additional information about the structure of the analyzed code.

---

## 🔌 API

### Analyze Code

**POST** `/analyze`

### Request

```json
{
  "code": "def add(a, b):\n    return a + b"
}
```

### Response

```json
{
  "prediction": "Machine-generated",
  "confidence": 48.05,
  "probabilities": {
    "Machine-generated": 48.05,
    "Human-written": 29.09,
    "Hybrid": 12.14,
    "Adversarial": 10.72
  },
  "forensic_analysis": {
    "total_characters": 31,
    "total_lines": 2,
    "non_empty_lines": 2,
    "function_count": 1,
    "loop_count": 0,
    "conditional_count": 0
  }
}
```

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/<your-username>/AI-Forensics.git
cd AI-Forensics
```

---

## 🐍 Backend Setup

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the FastAPI server:

```bash
uvicorn src.app:app --reload
```

The backend will run at:

```text
http://127.0.0.1:8000
```

---

## 💻 Frontend Setup

Open a new terminal and navigate to the frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Run the frontend:

```bash
npm run dev
```

The application will usually run at:

```text
http://localhost:5173
```

---

## 🧠 Workflow

1. The user enters source code into the application.
2. The React frontend sends the code to the FastAPI backend.
3. The backend receives the request through the `/analyze` endpoint.
4. The code is transformed using the saved TF-IDF vectorizers.
5. Word-level and character-level features are combined.
6. The Logistic Regression model predicts the code category.
7. Class probabilities and confidence scores are generated.
8. Structural forensic analysis is performed on the code.
9. The backend returns a structured JSON response.
10. The frontend displays the analysis results.

---

## 📷 Screenshots

You can add screenshots of the application here.

```text
Code Input Page

Analysis Results

Class Probabilities

Forensic Analysis Dashboard
```

---

## 🔮 Future Enhancements

- Improve classification performance for Hybrid and Adversarial code
- Experiment with advanced Machine Learning models
- Explore transformer-based models for code classification
- Support additional programming languages
- Improve forensic feature extraction
- Add user authentication
- Store analysis history
- Add downloadable analysis reports
- Deploy the application online

---

## 👨‍💻 Author

**Arjun Maheshwari**

GitHub: github.com/arjun614

LinkedIn: linkedin.com/in/arjunmaheshwari04/

---

## 📄 License

This project is intended for educational and research purposes.
