import tkinter as tk
from tkinter import filedialog
import sqlite3
import os

window = tk.Tk()
window.title("Card Maker for University")


def create_table():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS students
                 (id TEXT PRIMARY KEY, name TEXT, matricola TEXT, enrollment_date TEXT, study_field TEXT)''')
    conn.commit()
    conn.close()


def submitBtn():
    name = student_name.get()
    student_matricola = student_id.get()
    enrollment_date = student_date.get()
    study_field = student_field.get()

    try:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO students (name, matricola, enrollment_date, study_field) VALUES (?, ?, ?, ?)",
                  (name, student_matricola, enrollment_date, study_field))
        conn.commit()
        conn.close()
    except Exception as e:
        print("Error occurred:", e)

    # Clear input fields
    student_name.delete(0, 'end')
    student_id.delete(0, 'end')
    student_date.delete(0, 'end')
    student_field.delete(0, 'end')


def browse_pic():
    file_path = filedialog.askopenfilename()
    selected_profile_pic.set(file_path)


selected_profile_pic = tk.StringVar()


def save_pic():
    result_path = "src/prfilepicture/P{id}.jpg".format(id=student_id.get())

    selected_profile_pic.save(result_path, format="PNG")


create_table()

greeting = tk.Label(window, text="Card maker for university !")
greeting.grid(row=0, column=0, columnspan=2)

name_label = tk.Label(window, text="Student Full Name:")
name_label.grid(row=1, column=0)
student_name = tk.Entry(window)
student_name.grid(row=1, column=1)

id_label = tk.Label(window, text="Student Matricola:")
id_label.grid(row=2, column=0)
student_id = tk.Entry(window)
student_id.grid(row=2, column=1)

field_lable = tk.Label(text="Studnet Course of Study")
field_lable.grid(row=3, column=0)
student_field = tk.Entry(window)
student_field.grid(row=3, column=1)

date_label = tk.Label(window, text="Enrollment Date:")
date_label.grid(row=4, column=0)
student_date = tk.Entry(window)
student_date.grid(row=4, column=1)

pic_label = tk.Label(window, text="Profile Picture:")
pic_label.grid(row=5, column=0)
pic_button = tk.Button(window, text="Browse", command=browse_pic)
pic_button.grid(row=5, column=1)


create_button = tk.Button(window, text="Submit Data", command=submitBtn)
create_button.grid(row=5, column=0, columnspan=2)

window.mainloop()
