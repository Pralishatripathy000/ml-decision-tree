
<img width="1402" height="1122" alt="cd3e44c6-604d-4bd8-8761-21868babb134" src="https://github.com/user-attachments/assets/bf2e56fd-b5f4-45ce-a0d5-c309ad770947" />


# 🌳 ML Decision Tree

> **An end-to-end implementation of Decision Tree Classification using the Breast Cancer Wisconsin dataset, covering exploratory data analysis, model training, tree visualization, feature importance, and model evaluation.**

---

## 📖 Overview

Decision Trees are one of the most intuitive supervised machine learning algorithms for classification and regression tasks. They recursively split the feature space into decision regions by selecting the most informative features, making them highly interpretable and easy to visualize.

This project demonstrates the complete machine learning workflow, including data exploration, preprocessing, model training, prediction, evaluation, visualization of the learned tree, and interpretation of feature importance.

This repository is part of my **ML Fundamentals** series, where each project focuses on understanding a core machine learning algorithm through theory, implementation, and practical experimentation.

---

## 🚀 Project Status

> 🚧 Currently under development.

The repository will include:

* Dataset exploration and preprocessing
* Exploratory Data Analysis (EDA)
* Decision Tree model training
* Tree visualization
* Feature importance analysis
* Prediction on unseen data
* Confusion Matrix
* Accuracy, Precision, Recall and F1-Score
* ROC Curve and AUC
* Model serialization using Joblib

---

## 📊 Dataset

This project uses the **Breast Cancer Wisconsin Diagnostic Dataset**, available through the **Scikit-learn** library.

The dataset contains measurements computed from digitized images of breast cell nuclei. The objective is to classify tumors as **Malignant** or **Benign** based on thirty numerical features describing cell characteristics.

### Dataset Summary

| Property       |                 Value |
| -------------- | --------------------: |
| Samples        |                   569 |
| Features       |                    30 |
| Target Classes |                     2 |
| Missing Values |                  None |
| Problem Type   | Binary Classification |

### Target Variable

| Class | Description |
| ----- | ----------- |
| **0** | Malignant   |
| **1** | Benign      |

### Feature Categories

The dataset contains numerical measurements describing:

* Radius
* Texture
* Perimeter
* Area
* Smoothness
* Compactness
* Concavity
* Concave Points
* Symmetry
* Fractal Dimension

Each characteristic includes:

* Mean
* Standard Error (SE)
* Worst value

---

## 📂 Repository Structure

```text
ml-decision-tree
│
├── data/
├── models/
├── outputs/
│   ├── figures/
│   └── tables/
│
├── src/
│   ├── train.py
│   └── predict.py
│
├── notebook.ipynb
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib
* Jupyter Notebook

---

## 📈 Results

The Decision Tree Classifier demonstrated strong predictive performance on the Breast Cancer Wisconsin dataset, accurately distinguishing between malignant and benign tumors while maintaining high precision and recall.

### Model Performance

| Metric | Score |
|--------|------:|
| Accuracy | **93.86%** |
| Precision | **95.77%** |
| Recall | **94.44%** |
| F1-Score | **95.10%** |
| ROC-AUC | **93.42%** |

### Key Outcomes

- Achieved **93.86% classification accuracy** on the test dataset.
- Correctly identified malignant and benign tumors with high precision and recall.
- Generated an interpretable Decision Tree for transparent decision-making.
- Ranked feature importance to identify the most influential predictors.
- Saved evaluation metrics, classification reports, predictions, and visualizations to the `outputs/` directory.
- Exported the trained model using **Joblib** for future inference without retraining.

### Generated Outputs

**Figures**
- Decision Tree Visualization
- Feature Importance
- Confusion Matrix
- ROC Curve
- Target Distribution
- Feature Distributions
- Correlation Heatmap

**Tables**
- Dataset Preview
- Dataset Summary
- Missing Values
- Target Distribution
- Correlation Matrix
- Training Features & Labels
- Sample Predictions
- Evaluation Metrics
- Classification Report
- Feature Importance
- Confusion Matrix


---


## 📚 ML Fundamentals Series

This repository is part of my **ML Fundamentals** series, where each project explores a fundamental machine learning algorithm through practical implementation, visualization, evaluation, and interpretation.
