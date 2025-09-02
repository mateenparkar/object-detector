# YOLOv8 Object Detector (Webcam Demo)

**Real-time object detection using YOLOv8**, trained on a COCO subset, with bounding boxes and labels displayed on your webcam feed.

![YOLOv8 Demo](https://img.shields.io/badge/YOLOv8-Object%20Detection-blue) ![Python](https://img.shields.io/badge/Python-3.9--3.11-green) ![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-red)

---

## 🔍 Project Overview

This project demonstrates a complete object detection pipeline:

1. **Dataset download & preparation** – COCO subset (80 classes)
2. **Model training** – fine-tuning a pretrained YOLOv8 model (`yolov8n.pt`) in Google Colab
3. **Real-time inference** – webcam detection using the trained model (`best.pt`)

The YOLOv8 model was trained for 5 epochs and the Python script captures webcam frames, detects objects, and draws bounding boxes with class labels in real-time.

---

> **Note**: `datasets/` and large model files are ignored via `.gitignore` to keep the repo size manageable. Best.pt was included to allow quick use of the detector.

---

## ⚡ Quickstart (Local Setup)

### Prerequisites

- Python 3.9–3.11
- pip package manager
- Webcam/camera access
- (Optional but recommended) Virtual environment

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/object-detector.git
cd object-detector
```

### 2. Install Dependencies
```
pip install -r requirements.txt
```

### Run the webcam demo
```
python predict_webcam.py
```

# 🎯 Features
- Real-time detection: Live webcam feed processing
- Multiple object classes: Trained on COCO dataset subset
- Bounding box visualization: Clear object localization
- Class labels: Object classification display
