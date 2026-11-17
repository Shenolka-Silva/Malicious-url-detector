import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

df = pd.read_csv("data/features.csv")
X = df.drop(columns=["label", "type"])
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=25,
    min_samples_leaf=5,
    n_jobs=2,
    class_weight="balanced",
    random_state=42,
)
model.fit(X_train, y_train)

pred = model.predict(X_test)
print(classification_report(y_test, pred, target_names=["benign", "malicious"]))
print(confusion_matrix(y_test, pred))

joblib.dump({"model": model, "columns": list(X.columns)}, "model.joblib", compress=3)
print("Saved model.joblib")
