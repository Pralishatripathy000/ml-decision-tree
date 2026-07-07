import os
import joblib
import pandas as pd

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    classification_report,
)

os.makedirs("models", exist_ok=True)
os.makedirs("outputs/tables", exist_ok=True)


def main():
    cancer = load_breast_cancer(as_frame=True)
    df = cancer.frame

    X = df.drop("target", axis=1)
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    model = DecisionTreeClassifier(
        criterion="gini",
        max_depth=4,
        random_state=42
    )

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    metrics = pd.DataFrame({
        "Metric": [
            "Accuracy",
            "Precision",
            "Recall",
            "F1 Score",
            "ROC-AUC"
        ],
        "Value": [
            accuracy_score(y_test, y_pred),
            precision_score(y_test, y_pred),
            recall_score(y_test, y_pred),
            f1_score(y_test, y_pred),
            roc_auc_score(y_test, y_prob)
        ]
    })

    metrics.to_csv(
        "outputs/tables/evaluation_metrics.csv",
        index=False
    )

    report = pd.DataFrame(
        classification_report(
            y_test,
            y_pred,
            output_dict=True
        )
    ).transpose()

    report.to_csv(
        "outputs/tables/classification_report.csv"
    )

    importance = pd.DataFrame({
        "Feature": X.columns,
        "Importance": model.feature_importances_
    }).sort_values(
        by="Importance",
        ascending=False
    )

    importance.to_csv(
        "outputs/tables/feature_importance.csv",
        index=False
    )

    joblib.dump(
        model,
        "models/decision_tree.pkl"
    )

    print(metrics)


if __name__ == "__main__":
    main()