import joblib
import pandas as pd

from sklearn.datasets import load_breast_cancer


def main():
    model = joblib.load("models/decision_tree.pkl")

    cancer = load_breast_cancer(as_frame=True)
    df = cancer.frame

    X = df.drop("target", axis=1)

    sample = X.iloc[[0]]

    prediction = model.predict(sample)[0]
    probability = model.predict_proba(sample)[0]

    class_name = "Benign" if prediction == 1 else "Malignant"

    print("Sample Features:")
    print(sample)

    print("\nPredicted Class:")
    print(class_name)

    print("\nPrediction Probabilities:")
    print(pd.DataFrame({
        "Class": ["Malignant", "Benign"],
        "Probability": probability
    }))


if __name__ == "__main__":
    main()