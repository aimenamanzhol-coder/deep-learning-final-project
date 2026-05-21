# Scene Image Classification using Deep Learning

## Project Overview

This project focuses on classifying natural and urban scene images using deep learning techniques. The goal is to build a model that can automatically recognize different types of environments such as buildings, forests, mountains, sea, glacier, and streets.

We use both a custom Convolutional Neural Network (CNN) and a transfer learning approach with MobileNetV2 to improve performance. The project demonstrates the full pipeline of a deep learning workflow: dataset preparation, preprocessing, model training, evaluation, and error analysis.

---

##  Problem Statement

The objective of this project is to solve a multi-class image classification problem.

- **Input:** RGB images of natural and urban scenes (150×150 pixels)
- **Output:** One of 6 classes:
  - buildings
  - forest
  - glacier
  - mountain
  - sea
  - street

The model learns to automatically classify images into these categories.

This problem is useful for applications such as:
- environmental monitoring
- autonomous systems
- image organization
- geographic scene recognition

---

##  Dataset Description

- **Dataset name:** Intel Image Classification Dataset (Scene Recognition)
- **Source:** Kaggle
- **Link:** https://www.kaggle.com/datasets/puneet6060/intel-image-classification
- **Total images:** ~17,000
- **Classes:** 6 categories
- **Format:** JPEG images organized in folders
- **Split:**
  - Training set: ~14,000 images
  - Test set: ~3,000 images

Each class contains balanced image distribution.

---

## Project Structure
project-repo/
│
├── data/ # Dataset (not uploaded to GitHub)
├── notebooks/ # Google collab notebooks (experiments)
├── src/ # Training and model scripts
├── results/ # Plots, confusion matrices, metrics
│
├── reports/
│ ├── week-01.md
│ ├── week-02.md
│ ├── week-03.md
│ └── week-04.md
│
├── README.md
├── requirements.txt
└── final-report.md


---

## ⚙️ Setup Instructions

### 1. Clone repository
```bash
git clone <your-repo-link>
cd project-repo

2. Install dependencies
pip install -r requirements.txt
3. Dataset setup

Download dataset from Kaggle and extract it into:

/data/seg_train
/data/seg_test

Or mount Google Drive if using Colab.


🧠 Models Used
1. Baseline Model (Custom CNN)
3 Convolutional layers
MaxPooling layers
Dense fully connected layer
Softmax output layer
Optimizer: Adam
Loss: Sparse Categorical Crossentropy

2. Deep Learning Model (Transfer Learning)
Base model: MobileNetV2 (pretrained on ImageNet)
Frozen convolutional base
Added layers:
GlobalAveragePooling2D
Dropout (0.3)
Dense (128, ReLU)
Output layer (Softmax)
Data augmentation:
RandomFlip
RandomRotation
RandomZoom


📏 Evaluation Metrics

The following metrics were used:

Accuracy
Precision
Recall
F1-score
Confusion Matrix

Loss function:

Sparse Categorical Crossentropy

| Model                           | Train Accuracy | Validation Accuracy | Test Accuracy              |
| ------------------------------- | -------------- | ------------------- | -------------------------- |
| CNN (Baseline)                  | ~92%           | ~78%                | ~17% (poor generalization) |
| MobileNetV2 (Transfer Learning) | ~85%           | ~88%                | **~89%**                   |


📉 Error Analysis

From confusion matrix and classification reports:

The baseline CNN model overfitted the training data and performed poorly on test data.
Transfer learning significantly improved generalization.
Some confusion exists between:
mountain vs glacier
street vs buildings
sea vs glacier

Possible reasons:

Similar visual features in certain classes
Limited fine-tuning of pretrained model
Small image resolution (150×150)


⚠️ Limitations
Limited training epochs (5 epochs only)
No full fine-tuning of MobileNetV2
Image resolution is relatively low (150×150)
No hyperparameter optimization (learning rate tuning, etc.)
Class overlap in visual features
📌 Important Notes
Dataset is not included in the repository (too large)
All results are reproducible using provided code
Model training was done in Google Colab
Weekly progress was tracked using GitHub commits
Transfer learning model significantly outperformed baseline CNN

🚀 Future Improvements
Fine-tune MobileNetV2 layers
Increase image resolution (224×224)
Try EfficientNet or ResNet
Add hyperparameter tuning
Train for more epochs
Use data balancing techniques
