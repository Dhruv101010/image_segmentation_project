# 🧠 Image Captioning & Segmentation Web App

This is a simple and complete project that performs **Image Captioning** and **Image Segmentation** using deep learning. It features a **Streamlit web interface** where users can upload an image and get both a descriptive caption and segmented visual results.

---

## 📌 Features
- ✨ Generate descriptive **captions** using a pretrained **BLIP** model
- 🟩 Perform **object detection and segmentation** using **Mask R-CNN**
- 🎯 Web-based interface with **Streamlit**
- ⚡ Easy to run, even on CPU — no model training needed

---

## 🖼️ Example Output
**Input:** ![](example_input.jpg)

**Caption:** *"A dog catching a frisbee in the park."*

**Segmented Output:** ![](example_segmented.jpg)

---

## 🛠️ Tech Stack
- Python
- Streamlit
- HuggingFace Transformers (`BLIP`)
- PyTorch (`Mask R-CNN` from torchvision)
- OpenCV & PIL

---

## 📂 Project Structure
```bash
image_captioning_segmentation/
├── app/
│   └── app.py
├── captioning/
│   └── caption_model.py
├── segmentation/
│   └── mask_rcnn.py
├── requirements.txt
├── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/image-captioning-segmentation.git
cd image-captioning-segmentation
```

### 2. Create Virtual Environment (optional but recommended)
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the App
```bash
streamlit run app/app.py
```

---

## 📦 Dependencies
```txt
streamlit
torch
torchvision
transformers
Pillow
opencv-python

## CREDITS
Pranav Shahapure 
