# -*- coding: utf-8 -*-
import datetime
import os
from tkinter import *
import tkinter as tk
import pytesseract
from PIL import Image
import csv
from csv import reader

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ATTENDANCE_FOLDER = os.path.join(BASE_DIR, "CHEMISTRY ATTENDANCE")
CLASS_DATA_PATH = os.path.join(ATTENDANCE_FOLDER, "CLASS DATA.csv")
TESSERACT_PATH = os.path.join(BASE_DIR, "Tesseract-OCR", "tesseract.exe")
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

x = datetime.datetime.now()
year = x.year
month = x.month
date = x.day

student_keyword = []
students_name = ['date']

with open(CLASS_DATA_PATH, 'r', encoding='utf-8') as read_bill_data:
    csv_reader = reader(read_bill_data)
    for row in csv_reader:
        student_keyword.append(row[0])
        students_name.append(row[1])

def submit():
    attendance_screenshot = []
    
    image_1_ = image_1.get()
    image_2_ = image_2.get()
    image_3_ = image_3.get()
    image_4_ = image_4.get()
    image_5_ = image_5.get()
    period_1_ = period_1.get()
    text = text_1.get("1.0", END)
    roll_no = text_2.get("1.0", END)

    attendance_time = str(date) + ' # ' + str(period_1_)
    student_found = []
    student_attendace = [attendance_time]

    if image_1_ != '':
        attendance_screenshot.append(image_1_)
    if image_2_ != '':
        attendance_screenshot.append(image_2_)
    if image_3_ != '':
        attendance_screenshot.append(image_3_)
    if image_4_ != '':
        attendance_screenshot.append(image_4_)
    if image_5_ != '':
        attendance_screenshot.append(image_5_)

    for screen_find in attendance_screenshot:
        img = Image.open(screen_find)
        result = pytesseract.image_to_string(img)
        for i in range(len(student_keyword)):
            if (student_keyword[i]).lower() in result.lower() and i not in student_found:
                student_found.append(i)

    for i in range(len(student_keyword)):
        if (student_keyword[i]).lower() in text.lower() and i not in student_found:
            student_found.append(i)

    for i in range(len(student_keyword)):
        if i in student_found:
            student_attendace.append('P')
        else:
            student_attendace.append(' ')

    attendance_csv_path = os.path.join(ATTENDANCE_FOLDER, f'chemistry attendance {month} - {year}.csv')
    if not os.path.isfile(attendance_csv_path):
        csvfile = open(attendance_csv_path, 'w', newline='', encoding='utf-8')
        c = csv.writer(csvfile)
        c.writerow(students_name)
        c.writerow(student_attendace)
        csvfile.close()
    else:
        found_attendance_already = False
        student_previous = []
        with open(attendance_csv_path, 'r', encoding='utf-8') as data:
            csv_reader = reader(data)
            for row in csv_reader:
                student_previous.append(row)
            for i in range(len(student_previous)):
                if student_previous[i][0] == attendance_time:
                    student_previous[i] = student_attendace
                    found_attendance_already = True
                    break
        if not found_attendance_already:
            student_previous.append(student_attendace)
        csvfile = open(attendance_csv_path, 'w', newline='', encoding='utf-8')
        c = csv.writer(csvfile)
        for bill_1234 in student_previous:
            c.writerow(bill_1234)
        csvfile.close()

        inform_window = Toplevel(window)
        inform_window.minsize(height=50, width=50)
        inform_window.resizable(False, False)
        inform_window.title("DONE")

        canvasna = Canvas(inform_window, highlightthickness=0)
        canvasna.pack(fill=BOTH)

        canvasna1 = Canvas(canvasna)
        canvasna1.pack(fill=X)

        Label(canvasna1, text=" SUCESSFULLY DONE ", relief=GROOVE, font=("areial", 20, "bold")).pack(fill=X)

        canvasna2 = Canvas(canvasna)
        canvasna2.pack(fill=X)

        def return_window():
            inform_window.destroy()
            image_1.delete(0, END)
            image_2.delete(0, END)
            image_3.delete(0, END)
            image_4.delete(0, END)
            image_5.delete(0, END)
            period_1.delete(0, END)
            text_1.delete("1.0", "end")

        Button(canvasna2, text=" RETURN ", relief=GROOVE, font=("areial", 13, "bold"), command=return_window).pack(fill=X)

window = Tk()
window.minsize(height=250, width=1000)
window.title("attendace marker")
window.resizable(False, False)

Label(window, text='ATTENDANCE MARKER ', font=('calibre', 10, 'bold')).grid(row=0, column=1)

Label(window, text='IMAGE 1', font=('calibre', 10, 'bold'), width=20).grid(row=1, column=0)
image_1 = Entry(window, font=('calibre', 10, 'normal'), width=100)

Label(window, text='IMAGE 2', font=('calibre', 10, 'bold'), width=20).grid(row=2, column=0)
image_2 = Entry(window, font=('calibre', 10, 'normal'), width=100)

Label(window, text='IMAGE 3', font=('calibre', 10, 'bold'), width=20).grid(row=3, column=0)
image_3 = Entry(window, font=('calibre', 10, 'normal'), width=100)

Label(window, text='IMAGE 4', font=('calibre', 10, 'bold'), width=20).grid(row=4, column=0)
image_4 = Entry(window, font=('calibre', 10, 'normal'), width=100)

Label(window, text='IMAGE 5', font=('calibre', 10, 'bold'), width=20).grid(row=5, column=0)
image_5 = Entry(window, font=('calibre', 10, 'normal'), width=100)

Label(window, text='PERIOD NO', font=('calibre', 10, 'bold'), width=20).grid(row=6, column=0)
period_1 = Entry(window, font=('calibre', 10, 'normal'), width=100)

text_1 = Text(window, font=('calibre', 10, 'normal'), width=100)
text_2 = Text(window, font=('calibre', 10, 'normal'), width=20)

Label(window, text='', font=('calibre', 10, 'bold'), width=20).grid(row=8, column=0)
sub_btn = Button(window, text='Submit', width=50, command=submit)
Label(window, text='', font=('calibre', 10, 'bold'), width=20).grid(row=10, column=0)

def submit_bind(event):
    submit()

window.bind('<Return>', submit_bind)

image_1.grid(row=1, column=1)
image_2.grid(row=2, column=1)
image_3.grid(row=3, column=1)
image_4.grid(row=4, column=1)
image_5.grid(row=5, column=1)
period_1.grid(row=6, column=1)
text_1.grid(row=7, column=1)
text_2.grid(row=7, column=0)
sub_btn.grid(row=9, column=1)
period_1.focus()

def image_1_down(event):
    image_2.focus_set()

image_1.bind('<Down>', image_1_down)

def image_2_up(event):
    image_1.focus_set()
def image_2_down(event):
    image_3.focus_set()

image_2.bind('<Up>', image_2_up)
image_2.bind('<Down>', image_2_down)

def image_3_up(event):
    image_2.focus_set()
def image_3_down(event):
    image_4.focus_set()

image_3.bind('<Up>', image_3_up)
image_3.bind('<Down>', image_3_down)

def image_4_up(event):
    image_3.focus_set()
def image_4_down(event):
    image_5.focus_set()

image_4.bind('<Up>', image_4_up)
image_4.bind('<Down>', image_4_down)

def image_5_up(event):
    image_4.focus_set()
def image_5_down(event):
    period_1.focus_set()

image_5.bind('<Up>', image_5_up)
image_5.bind('<Down>', image_5_down)

def period_1_up(event):
    image_5.focus_set()
def period_1_down(event):
    text_1.focus_set()

period_1.bind('<Up>', period_1_up)
period_1.bind('<Down>', period_1_down)

window.mainloop()


'''
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 16:32:02 2021
@author: divyam
"""
#===========TIME============#
import datetime

x=datetime.datetime.now()
year = x.year
month = x.month
date = x.day

import os

from tkinter import *
import tkinter as tk

import pytesseract	
from PIL import Image

import csv 
from csv import reader

student_keyword = []
students_name   = [ 'date' ]
with open(f"c:/Users/divya/Desktop/attendance/CHEMISTRY ATTENDANCE/CLASS DATA.csv", 'r') as read_bill_data:
    csv_reader = reader(read_bill_data)
    for row in csv_reader:
        student_keyword.append(row[0])
        students_name  .append(row[1])
        

def submit() :
    attendance_screenshot = []
    
    image_1_	= image_1.get()
    image_2_	= image_2.get()
    image_3_	= image_3.get()
    image_4_	= image_4.get()
    image_5_	= image_5.get()
    period_1_   = period_1.get()
    text = text_1.get("1.0" , END )
    
    attendance_time = str(date) +' # '+ str(period_1_)
    student_found = []
    student_attendace = [attendance_time]

    if image_1_ != '' :
        attendance_screenshot.append(image_1_)
 
    if image_2_ != '' :
        attendance_screenshot.append(image_2_)
        
    if image_3_ != '' :
        attendance_screenshot.append(image_3_)
        
    if image_4_ != '' :
        attendance_screenshot.append(image_4_)
    
    if image_5_ != '' :
        attendance_screenshot.append(image_5_)

    for screen_find in attendance_screenshot :
        img = Image.open(screen_find)	
        pytesseract.pytesseract.tesseract_cmd ='C:/Users/divya/Desktop/attendance/Tesseract-OCR/tesseract.exe'
        result = pytesseract.image_to_string(img)
    
        for i in range(len(student_keyword)) :
            if (student_keyword[i]).lower() in result.lower() and i not in student_found :
                student_found.append(i)
    
    for i in range(len(student_keyword)) :
        if (student_keyword[i]).lower() in text.lower() and i not in student_found :
            student_found.append(i)
            
    for i in range(len(student_keyword)) :
        if i in student_found :
            student_attendace.append('P')                
        else :
            student_attendace.append(' ')
           

    if os.path.isfile(f'c:/Users/divya/Desktop/attendance/CHEMISTRY ATTENDANCE/chemistry attendance {month} - {year}.csv') == False : 
        csvfile = open(f'c:/Users/divya/Desktop/attendance/CHEMISTRY ATTENDANCE/chemistry attendance {month} - {year}.csv' , 'w', newline='', encoding='utf-8')
        c = csv.writer(csvfile)
        c.writerow(students_name)
        c.writerow(student_attendace)
        csvfile.close()

    else :
        found_attendance_already = False
        student_previous = []
        with open(f'c:/Users/divya/Desktop/attendance/CHEMISTRY ATTENDANCE/chemistry attendance {month} - {year}.csv' , 'r') as data :
            csv_reader = reader(data)
            for row in csv_reader:
                student_previous.append(row)
                
            for i in range(len(student_previous)) :
                if student_previous[i][0] == attendance_time :
                    student_previous[i] = student_attendace
                    found_attendance_already = True 
                    break

        if found_attendance_already == False :
            student_previous.append( student_attendace )
                    
        csvfile = open(f'c:/Users/divya/Desktop/attendance/CHEMISTRY ATTENDANCE/chemistry attendance {month} - {year}.csv' , 'w', newline='', encoding='utf-8')
        c = csv.writer(csvfile)
        for bill_1234 in student_previous :
            c.writerow(bill_1234)
        csvfile.close()

        inform_window = Toplevel(window)
        inform_window.minsize(height=50, width=50)
        inform_window.resizable(False , False)
        inform_window.title("DONE")

        canvasna = Canvas(inform_window , highlightthickness=0 )
        canvasna.pack(fill= BOTH  )
        
        canvasna1 = Canvas(canvasna )
        canvasna1.pack(fill= X )
               
        label=Label(canvasna1 ,text=" SUCESSFULLY DONE " , relief=GROOVE ,font=("areial",20,"bold")).pack(fill=X)

        canvasna2 = Canvas(canvasna )
        canvasna2.pack(fill=X )
        
        def return_window() :
            inform_window.destroy()

            image_1	.delete(0, END)
            image_2	.delete(0, END)
            image_3	.delete(0, END)
            image_4	.delete(0, END)
            image_5	.delete(0, END)
            period_1    .delete(0, END)
            text_1      .delete("1.0","end")
        button=Button(canvasna2 ,text=" RETURN "  , relief=GROOVE ,font=("areial",13,"bold") , command = return_window ).pack(fill = X)
       
        

window = Tk()
window .minsize( height = 250 , width = 1000 )
window.title("attendace marker")
window.resizable(False , False)


	
label = Label(window, text = 'ATTENDANCE MARKER ', font=('calibre',10, 'bold')  ).grid(row=0,column=1)


label = Label(window, text = 'IMAGE 1', font=('calibre',10, 'bold') , width = 20 ).grid(row=1,column=0)
image_1 = Entry(window , font=('calibre',10,'normal') , width = 100 )

label = Label(window, text = 'IMAGE 2', font=('calibre',10, 'bold') , width = 20 ).grid(row=2,column=0)
image_2 = Entry(window , font=('calibre',10,'normal') , width = 100 )

label = Label(window, text = 'IMAGE 3', font=('calibre',10, 'bold') , width = 20 ).grid(row=3,column=0)
image_3 = Entry(window , font=('calibre',10,'normal') , width = 100 )

label = Label(window, text = 'IMAGE 4', font=('calibre',10, 'bold') , width = 20 ).grid(row=4,column=0)
image_4 = Entry(window , font=('calibre',10,'normal') , width = 100 )

label = Label(window, text = 'IMAGE 5', font=('calibre',10, 'bold') , width = 20 ).grid(row=5,column=0)
image_5 = Entry(window , font=('calibre',10,'normal') , width = 100 )

label = Label(window, text = 'PERIOD NO', font=('calibre',10, 'bold') , width = 20 ).grid(row=6,column=0)
period_1 = Entry(window , font=('calibre',10,'normal') , width = 100 )

text_1 = Text(window , font=('calibre',10,'normal') , width = 100 )

label = Label(window, text = '', font=('calibre',10, 'bold') , width = 20 ).grid(row= 8,column=0)
sub_btn = Button(window,text = 'Submit' , width = 50 , command = submit)
label = Label(window, text = '', font=('calibre',10, 'bold') , width = 20 ).grid(row=10,column=0)

def submit_bind(event) :
    submit()
window.bind('<Return>' , submit_bind )

image_1 .grid( row = 1 , column = 1 )
image_2 .grid( row = 2 , column = 1 )
image_3 .grid( row = 3 , column = 1 )
image_4 .grid( row = 4 , column = 1 )
image_5 .grid( row = 5 , column = 1 )
period_1.grid( row = 6 , column = 1 )
text_1  .grid( row = 7 , column = 1 )
sub_btn .grid( row = 9 , column = 1 )

period_1.focus()
def image_1_down(event) :
      image_2.focus_set()  
      
image_1 .bind('<Down>'  , image_1_down  )

def image_2_up(event) :
      image_1.focus_set()   
def image_2_down(event) :
      image_3.focus_set()     

image_2 .bind('<Up>'    , image_2_up    )
image_2 .bind('<Down>'  , image_2_down  )

def image_3_up(event) :
      image_2.focus_set()   
def image_3_down(event) :
      image_4.focus_set()     

image_3 .bind('<Up>'    , image_3_up    )
image_3 .bind('<Down>'  , image_3_down  )

def image_4_up(event) :
      image_3.focus_set()   
def image_4_down(event) :
      image_5.focus_set()     

image_4 .bind('<Up>'    , image_4_up    )
image_4 .bind('<Down>'  , image_4_down  )

def image_5_up(event) :
      image_4.focus_set()   
def image_5_down(event) :
      period_1.focus_set()     

image_5 .bind('<Up>'    , image_5_up    )
image_5 .bind('<Down>'  , image_5_down  )

def period_1_up(event) :
      image_5.focus_set()
def period_1_down(event) :
      text_1.focus_set() 

period_1.bind('<Up>'    , period_1_up    )
period_1.bind('<Down>'  , period_1_down  )


window.mainloop()



 


'''