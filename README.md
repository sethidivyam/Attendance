# 🧠 MarkMe – Automated Attendance System using Python & OCR

**MarkMe** is a desktop application that automates attendance marking from Zoom screenshots using **Tesseract OCR**, developed in **Python** with a simple GUI built using **Tkinter**. It extracts participant names from screenshots and compares them with a predefined student list, then generates daily and monthly attendance reports in CSV format.

---

## 📌 Project Summary

This project was developed during the COVID-19 pandemic (2021), when online classes were conducted via Zoom. Manually marking attendance from Zoom screenshots became repetitive, time-consuming, and error-prone. **MarkMe** solves this by using image processing and optical character recognition (OCR) to extract names and automate the process.

---

## 💡 Problem Statement

Marking attendance manually from Zoom participant screenshots was inefficient and prone to human error. The need was to automate the workflow by reading names from screenshots and matching them against a list of enrolled students.

---

## 🔧 Features

- 📸 Upload up to 5 Zoom participant screenshots per session  
- 🔍 Extract participant names using **Tesseract OCR**  
- ✅ Match names with the official class list (CSV format)  
- 📅 Save attendance entries with date and period info  
- 📊 Generate a consolidated monthly attendance CSV file  
- 🖥️ GUI built with **Tkinter** for easy input and processing  
- 📂 Batch processing of multiple screenshots  

---

## 🧰 Tech Stack

- **Python 3.x**
- **Tkinter** – for GUI
- **Pytesseract** – OCR (Python wrapper for Tesseract)
- **Pillow (PIL)** – image loading and processing
- **CSV module** – attendance data management

---

## 🚀 How It Works

1. Launch the GUI by running the Python script.
2. Upload up to 5 Zoom screenshot image paths.
3. Enter the period number.
4. Optionally, input manually typed names or roll numbers (if any).
5. Click **Submit**.
6. The app will:
   - Use OCR to extract names from screenshots
   - Match them against entries in `CLASS DATA.csv`
   - Log present students as `'P'` in the attendance sheet
   - Save/update the monthly CSV file in the `CHEMISTRY ATTENDANCE` folder

---

## 🗂️ Project Structure

```
MarkMe/
├── CHEMISTRY ATTENDANCE/
│   ├── CLASS DATA.csv                      # Master student list (keywords + full names)
│   ├── chemistry attendance MM - YYYY.csv  # Monthly attendance sheet (auto-generated)
├── Tesseract-OCR/
│   └── tesseract.exe                       # Path to Tesseract executable
├── markme.py                               # Main application script
```

> ⚠️ Ensure the path to `tesseract.exe` is set correctly in the code and Tesseract is installed on your system.

---

## 📋 CLASS DATA.csv Format

```
keyword1,Full Name 1
keyword2,Full Name 2
...
```

- `keyword`: A unique identifier (first or last name) expected to appear in OCR results.
- `Full Name`: The name to appear as a header in the attendance sheet.

---

## 📥 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/MarkMe.git
   cd MarkMe
   ```

2. Install required dependencies:
   ```bash
   pip install pytesseract pillow
   ```

3. [Install Tesseract OCR](https://github.com/tesseract-ocr/tesseract) and update its path in the script:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r'path_to_your_tesseract.exe'
   ```

---

## 📊 Output

- Attendance saved to:
  ```
  CHEMISTRY ATTENDANCE/chemistry attendance MM - YYYY.csv
  ```
- Each entry marked with date and period:
  ```
  25 # 1, P,  , P,  , P
  ```

---

## 💬 Sample GUI

The GUI accepts:

- 📂 Image paths (Entry fields for up to 5 screenshots)
- ⏱️ Period number
- 📝 Optional manual input (e.g., typed names/roll numbers)
- ✅ Submit button to generate attendance

---

## ✅ To-Do / Future Improvements

- Add file picker dialogs for image selection
- Enhance OCR with image preprocessing (grayscale, thresholding)
- Enable multi-class/multi-section support
- Export monthly reports in Excel format
- Add logging and error handling

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## 👨‍💻 Author

**Divyam Sethi**  
🔗 [LinkedIn](https://www.linkedin.com/in/divyam-sethi-3a5141232)  
📧 [Email](mailto:divyamsethi1804@gmail.com)

---

## ⭐️ Support

If you found this project helpful, feel free to ⭐ the repository and share it with your peers!
