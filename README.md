# Image Steganography using LSB (Python)

## 📌 Project Description
This project implements image steganography using the Least Significant Bit (LSB) technique in Python.  
It allows hiding a secret text message inside a BMP image and later extracting it without visible changes to the image.

---

## ⚙️ Features
- Embed secret text into a BMP image
- Extract hidden text from stego-image
- Uses LSB (Least Significant Bit) technique
- Random pixel selection using a secret key
- Supports RGB images

---

## 📁 Project Structure

```text
SteganographyLab/
│
├── embed.py          # Script to hide secret message
├── extract.py        # Script to retrieve secret message
├── secret.txt        # Secret message input
├── stego-image.bmp   # Output image with hidden data
└── img/
    └── flowers.bmp   # Cover image
```

---

## 📦 Requirements

Install the required library:

```bash
pip install pillow
```
