import os
import json
import numpy as np
from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Load model and class labels
model = load_model('Crop Disease Detection/model/crop_disease_model.keras')

with open('Crop Disease Detection/model/class_indices.json') as f:
    class_indices = json.load(f)

# Reverse the class indices
class_labels = {v: k for k, v in class_indices.items()}

# Flask app setup
app = Flask(__name__, template_folder='Crop Disease Detection/templates')
UPLOAD_FOLDER = 'Crop Disease Detection/static/upload'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return render_template('index.html', error='No file part')
    
    file = request.files['file']
    if file.filename == '':
        return render_template('index.html', error='No selected file')

    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Preprocess the image
        img = image.load_img(file_path, target_size=(128, 128))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array / 255.0

        # Prediction
        prediction = model.predict(img_array)[0][0]
        predicted_class = "Unhealthy" if prediction >= 0.5 else "Healthy"
        confidence = prediction if predicted_class == "Unhealthy" else 1 - prediction

        # Static info
        info = {
            "Healthy": {
                "description": "The crop appears healthy with no visible disease symptoms.",
                "precautions": "Continue regular monitoring and proper care."
            },
            "Unhealthy": {
                "description": "The crop might be infected by a disease. Further diagnosis recommended.",
                "precautions": "Isolate affected crops, consult an expert, and apply proper treatment."
            }
        }

        return render_template('index.html',
                               prediction=predicted_class,
                               description=info[predicted_class]["description"],
                               precautions=info[predicted_class]["precautions"],
                               confidence=f"{confidence*100:.2f}%",
                               image_path=file_path)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
