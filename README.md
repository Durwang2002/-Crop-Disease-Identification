# 🌾 Crop Disease Identification System (Binary Classification)

This project is a real-time web application that allows users—especially farmers and agronomists—to identify whether a crop leaf is **Healthy** or **Unhealthy** by simply uploading an image. It leverages a Convolutional Neural Network (CNN) trained on plant leaf images and offers not only the prediction but also related **description**, **precautions**, and **confidence score**.

---

## 🔍 Project Overview

The main goal is to simplify disease detection using AI and provide accessible tools for agricultural communities. This helps with early identification and prevention of crop diseases, thus improving yield and reducing losses.

---

## 🚀 Features

- Upload crop leaf image for real-time disease detection
- Predicts either **Healthy** or **Unhealthy**
- Displays:
  - Disease **description**
  - **Precautionary** measures
  - **Confidence** percentage
- Web-based user interface using **Flask**
- Image preprocessing, resizing, and normalization handled automatically

---

## 🛠️ Technologies Used

| Component      | Technology/Tool       |
|----------------|------------------------|
| Programming Language | Python 3.11+          |
| Deep Learning Framework | TensorFlow 2.12.0 + Keras 2.12.0 |
| Web Framework | Flask                   |
| Image Processing | OpenCV, Pillow (PIL) |
| Data Handling | NumPy, Pandas           |
| Visualization | Matplotlib (for training) |
| Dataset | [PlantVillage](https://www.kaggle.com/emmarex/plantdisease) (Manually organized for binary classification) |
| Model Format | `.keras` (Keras SavedModel) |
| Frontend | HTML5, CSS3 |

---

## 📁 Folder Structure

project_root/ │ ├── app.py # Flask web app ├── train_model.py # CNN model training script ├── requirements.txt # Python dependencies ├── model/ │ ├── crop_disease_model.keras │ └── class_indices.json ├── static/ │ └── upload/ # Saved uploaded images ├── templates/ │ └── index.html # Frontend UI ├── dataset/ # Structured dataset (Healthy/Unhealthy) └── README.md, LICENSE

---

## 🧪 How to Run the Project

### Step 1: Clone the Repository

```bash
git clone  https://github.com/Durwang2002/-Crop-Disease-Identification

Step 2: Install Python Dependencies
Ensure you're using Python 3.11+. Then install dependencies:

bash
pip install -r requirements.txt

Step 3: Prepare the Dataset
Ensure your dataset folder (dataset/) has two subfolders:
dataset/
├── Healthy/
└── Unhealthy/

tep 4: Train the CNN Model (Optional)
bash
python train_model.py

Step 5: Run the Flask App
bash
python app.py
Then visit: http://127.0.0.1:5000/ in your browser.
