from flask import Flask, request, render_template, send_from_directory
import cv2
import os
import numpy as np
from ultralytics import YOLO
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load YOLO segmentation model
model = YOLO("best.pt")  # Ensure "best.pt" is in the same directory or provide full path

# Define folders
UPLOAD_FOLDER = os.path.abspath("uploads")
RESULT_FOLDER = os.path.abspath("results")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        # Get the uploaded image
        file = request.files["file"]
        if file:
            img_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(img_path)

            # Run YOLO segmentation
            results = model(img_path)
            output_img = results[0].plot()  # Get segmented image (BGR format)

            # Convert BGR to RGB before saving
            output_img_rgb = cv2.cvtColor(output_img, cv2.COLOR_BGR2RGB)

            # Save the output image
            output_path = os.path.join(RESULT_FOLDER, file.filename)
            cv2.imwrite(output_path, output_img_rgb)

            # Extract class names and confidence levels
            detections = []
            for box in results[0].boxes:
                class_id = int(box.cls[0].item())  # Get class ID
                class_name = results[0].names[class_id]  # Get class name
                confidence = round(box.conf[0].item() * 100, 2)  # Confidence %
                detections.append({"class": class_name, "confidence": confidence})

            # If no detections, return "No brain tumor detected"
            if not detections:
                detections.append({"class": "No brain tumor detected", "confidence": 0.0})

            return render_template("result.html", image_file=file.filename, detections=detections)

    return render_template("index.html")

@app.route("/results/<filename>")
def get_result_image(filename):
    return send_from_directory(RESULT_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)
#