"""
evaluation.py
--------------
Evaluation metrics and confusion matrix.
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import (
    classification_report,
    confusion_matrix
)


def evaluate_model(model, dataset, class_names):

    # True labels
    y_true = np.concatenate(
        [y for x, y in dataset],
        axis=0
    )

    # Predictions
    y_pred = np.argmax(
        model.predict(dataset),
        axis=1
    )

    # Classification report
    print("\nClassification Report:\n")

    print(classification_report(
        y_true,
        y_pred,
        target_names=class_names
    ))

    # Confusion matrix
    cm = confusion_matrix(y_true, y_pred)

    # Plot confusion matrix
    plt.figure(figsize=(8, 6))

    sns.heatmap(
        cm,
        annot=True,
        fmt='d',
        cmap='Blues',
        xticklabels=class_names,
        yticklabels=class_names
    )

    plt.xlabel("Predicted")
    plt.ylabel("True")
    plt.title("Confusion Matrix")

    plt.show()

    return cm
