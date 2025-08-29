# 👁️ OpenCV Mini Projects  

Welcome to my collection of **OpenCV-based projects**   
These were built while exploring computer vision concepts in Python. Each project is simple, practical, and demonstrates the power of OpenCV in real-world applications.  

---

## 📂 Projects  

### 🎨 1. Virtual Paint  
Draw on the screen by moving your finger in the air.  
- Tracks hand movement  
- Detects fingertip  
- Paints in real-time  



🔑 **Concepts:** Hand tracking, contours, masking  

---

### 🚗 2. Number Plate Scanner  
Automatically detects and extracts license plate numbers.  
- Identifies number plate region  
- Preprocesses image  
- Uses **OCR (pytesseract)** to read text  

 

🔑 **Concepts:** ROI extraction, thresholding, OCR  

---

### ✋ 3. Virtual Zoom Gesture  
Zoom into an image using only your hands.  
- Detects both hands  
- Measures distance between fingers  
- Dynamically resizes the image for zoom effect  



🔑 **Concepts:** Hand landmarks, distance calculation, scaling  

---

### 📦 4. QR/Barcode Authentication  
Verify QR/Barcodes in real-time using webcam.  
- Scans QR/Barcode  
- Decodes data  
- Matches against stored database (`myData.text`)  
- Displays **Authorized ✅ / Un-authorized ❌**  



🔑 **Concepts:** Barcode decoding, database matching, overlays  

---

## 🛠️ Tech Stack  

- **OpenCV (`cv2`)** – Core computer vision  
- **cvzone** – Easy hand tracking  
- **Pytesseract** – OCR for text recognition  
- **Pyzbar** – QR/Barcode decoding  
- **NumPy** – Array operations  

---

## 📸 Project Overview  

| Project                  | Libraries Used                           | Key Concepts                                | Output                         |
|---------------------------|------------------------------------------|---------------------------------------------|--------------------------------|
| 🎨 Virtual Paint          | `cv2`                                    | Hand tracking, contours                     | Draw on screen with finger     |
| 🚗 Number Plate Scanner   | `cv2`, `pytesseract`                     | ROI extraction, OCR                         | Extract & display plate text   |
| ✋ Virtual Zoom Gesture   | `cv2`, `cvzone.HandTrackingModule`       | Landmarks, distance → scaling               | Zoom via hand gestures         |
| 📦 QR/Barcode Auth        | `cv2`, `pyzbar`, `numpy`                 | Decoding, database validation               | Authorized / Un-authorized     |

---

## ⚙️ Setup & Usage  

1. Clone the repo  
   ```bash
 git clone https://github.com/hasini-0307/OpenCV_Projects.git
cd OpenCV_Projects

