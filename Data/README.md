# Data Directory

Do not commit raw dataset files to this repository.

The Intel Image Classification dataset contains thousands of image files and zip archives that are too large for GitHub. Please download the dataset separately using the instructions below.

---

# Dataset Information

| Field | Detail |
|---|---|
| Name | Intel Image Classification |
| Source | Kaggle |
| Total images | ~25,000 |
| Training images | ~14,000 |
| Test images | ~3,000 |
| Prediction images | ~7,000 |
| Image size | 150x150 |
| Classes | buildings, forest, glacier, mountain, sea, street |
| Task type | Multi-class image classification |
| Format | JPG images organized into folders |
| License | Data files © Original Authors |

---

# Dataset Source

Kaggle Dataset Link:

https://www.kaggle.com/datasets/puneet6060/intel-image-classification

---

# Class Labels

```python
{
    'buildings': 0,
    'forest': 1,
    'glacier': 2,
    'mountain': 3,
    'sea': 4,
    'street': 5
}
```

---

# Download Instructions

## Option A — Manual Download

1. Open the Kaggle dataset page
2. Download:
   - seg_train.zip
   - seg_test.zip
3. Extract files into the `data/` directory

Expected structure:

```text
data/
├── seg_train/
├── seg_test/
```

---

## Option B — Google Colab

Run the following code in Google Colab:

```python
from google.colab import drive
drive.mount('/content/drive')

import zipfile

with zipfile.ZipFile('/content/drive/MyDrive/seg_train.zip', 'r') as zip_ref:
    zip_ref.extractall('/content/data')

with zipfile.ZipFile('/content/drive/MyDrive/seg_test.zip', 'r') as zip_ref:
    zip_ref.extractall('/content/data')
```

---

# Directory Structure

After setup, the dataset should look like this:

```text
data/
├── README.md
├── seg_train/
│   ├── buildings/
│   ├── forest/
│   ├── glacier/
│   ├── mountain/
│   ├── sea/
│   └── street/
│
├── seg_test/
│   ├── buildings/
│   ├── forest/
│   ├── glacier/
│   ├── mountain/
│   ├── sea/
│   └── street/
```

---

# Notes

- Dataset files are not included in this repository
- The project was trained using Google Colab
- Images are automatically resized to 150×150 during preprocessing
- Dataset is relatively balanced across all classes
