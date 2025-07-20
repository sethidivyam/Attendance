🧠 Automated Attendance System using Python & OCR


📌 Project Summary
This project was developed during the COVID-19 pandemic (2021) when classes were conducted online via Zoom. I was assigned the task of marking daily attendance based on Zoom screenshots — a repetitive and time-consuming job. To automate this, I built a Python-based application using Tkinter for GUI and Tesseract OCR for extracting names from screenshots.

💡 Problem Statement
Manually marking attendance from Zoom screenshots became inefficient and error-prone. I needed a way to automate this process by extracting names from images and comparing them with a list of enrolled students.

🔧 Features
📸 Upload Zoom screenshots as input

🔍 Extract participant names using Tesseract OCR

✅ Compare against predefined student list

📅 Generate daily attendance

📊 Export attendance summary to a CSV file for the month

🖥️ User-friendly GUI built with Tkinter

📂 Batch processing support

🧰 Tech Stack
Python 3.x

Tkinter – GUI Framework

pytesseract – Python wrapper for Tesseract OCR

PIL (Pillow) – Image processing

CSV Module – Data handling & export

🚀 How It Works
Run the app using Python.

Upload screenshot(s) of the Zoom participant window.

The app uses OCR to extract names from the screenshot.

Matches names with the students_list.csv file.

Saves the attendance for each day in a CSV format.

At the end of the month, a compiled attendance report is generated.
