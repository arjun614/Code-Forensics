import joblib
from scipy.sparse import hstack
from forensic_analysis import analyze_code

label_names = {
    0: "Machine-generated",
    1: "Human-written",
    2: "Hybrid",
    3: "Adversarial"
}

# Load model
model = joblib.load("models/code_detector_model.pkl")

# Load vectorizers
word_vectorizer = joblib.load("models/word_vectorizer.pkl")
char_vectorizer = joblib.load("models/char_vectorizer.pkl")


def predict_code(code):

    # Convert code into word features
    word_features = word_vectorizer.transform([code])

    # Convert code into character features
    char_features = char_vectorizer.transform([code])

    # Combine features
    features = hstack([
        word_features,
        char_features
    ])

    # Predict
    prediction = model.predict(features)[0]
    probabilities = model.predict_proba(features)[0]
    all_confidences = {
    label_names[i]: round(probabilities[i] * 100, 2)
    for i in range(len(probabilities))
    }
    confidence = probabilities[prediction] * 100

    forensic_results = analyze_code(code)

    return (
    label_names[prediction],
    confidence,
    all_confidences,
    forensic_results
)


# Test code
sample_code = """
def add(a, b):
    return a + b
"""

result, confidence, all_confidences, forensic_results = predict_code(sample_code)

print("Prediction:", result)
print("Confidence:", round(confidence, 2), "%")
print("\nAll class probabilities:")

for label, probability in all_confidences.items():
    print(f"{label}: {probability}%")

print("\nForensic Analysis:")

for indicator, value in forensic_results.items():
    print(f"{indicator}: {value}")