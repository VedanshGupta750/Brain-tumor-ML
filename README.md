# Brain Tumor Detection using YOLO

This project is an **AI-based Brain Tumor Detection System** using **YOLO (You Only Look Once) segmentation**. It detects and segments brain tumors from MRI images. The project is implemented using **Flask** for the backend and a web interface for user interaction.

## 📌 Features
- **Brain Tumor Detection** using YOLO segmentation.
- **Web Interface** for image upload and result display.
- **Deep Learning Model** trained on a **Roboflow dataset**.
- **Automated Image Processing** for accurate segmentation.
- **Flask Backend** to handle image uploads and predictions.

---
## 🛠 Installation & Setup

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/Brain-Tumor-Detection.git
cd Brain-Tumor-Detection
```

### **2️⃣ Set Up a Virtual Environment (Recommended)**
```bash
python -m venv env
source env/bin/activate  # For Mac/Linux
env\Scripts\activate    # For Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Run the Flask App**
```bash
python app.py
```
The application will be available at **http://127.0.0.1:5000/**.

---
## 🚀 Usage
1. **Upload an MRI Image**: Open the web app and select an MRI image.
2. **Model Prediction**: The YOLO model segments the tumor region.
3. **View Results**: If a tumor is detected, the segmented image is displayed with confidence scores.
4. **Download Segmented Image**: The processed image can be saved.

---
## 📂 Project Structure
```
Brain-Tumour-Backend/
│── static/css/        # Stylesheets for the frontend
│── templates/         # HTML files (index.html, result.html)
│── uploads/           # Uploaded images
│── results/           # Segmented output images
│── app.py             # Flask backend
│── best.pt            # Trained YOLO model weights
│── requirements.txt   # Required dependencies
```

---
## 🏆 Model Details
- **YOLOv11** segmentation model trained on a **Roboflow dataset**.
- **Image Size**: 640x640
- **Training**: 100 epochs with augmentations.
- **Frameworks Used**: PyTorch & OpenCV.

---
## 🔗 API Endpoints
- `POST /` - Upload an image and get the segmentation result.
- `GET /results/<filename>` - Fetch segmented images.

---
## 🛠 Troubleshooting
- **`ModuleNotFoundError: No module named 'flask'`** → Run `pip install flask`
- **Model not loading?** → Ensure `best.pt` is in the project folder.
- **Permission issues on Windows?** → Run the command prompt as administrator.

---
## 📜 License
This project is open-source and available under the **MIT License**.

---
## 💡 Future Enhancements
✅ Improve model accuracy with more diverse datasets.
✅ Deploy the model as a cloud-based API.
✅ Add real-time inference using video streams.

---
## 🙌 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to improve.

---

🔗 **GitHub Repository**: [Your Repo Link Here]

