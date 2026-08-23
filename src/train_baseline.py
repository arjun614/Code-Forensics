import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, f1_score, confusion_matrix


# 1. Load dataset
df = pd.read_parquet("data/task_c/task_c_trial.parquet")

# Input = code
X = df["code"]

# Output = label
y = df["label"]


# 2. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# 3. Convert code into numerical features using TF-IDF
vectorizer = TfidfVectorizer(
    analyzer="char",
    ngram_range=(3, 5),
    max_features=30000
)

X_train_tfidf = vectorizer.fit_transform(X_train)

X_test_tfidf = vectorizer.transform(X_test)


# 4. Create and train the model
model = LogisticRegression(
    max_iter=1000,
    class_weight="balanced"
)

model.fit(X_train_tfidf, y_train)


# 5. Make predictions
predictions = model.predict(X_test_tfidf)


# 6. Evaluate the model
macro_f1 = f1_score(
    y_test,
    predictions,
    average="macro"
)

print("Macro F1 Score:", macro_f1)

print("\nClassification Report:\n")

print(
    classification_report(
        y_test,
        predictions
    )
)

cm = confusion_matrix(y_test, predictions)

print("\nConfusion Matrix:\n")
print(cm)