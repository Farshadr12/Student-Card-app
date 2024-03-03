import tkinter as tk
import csv


def submitBtn():
    name = student_name.get()
    student_matricola = student_id.get()
    enrollment_date = student_date.get()
    study_field = student_field.get()

    try:
        with open('database.csv', 'r', newline='') as file:
            try:
                is_empty = not file.read(1)
            except io.UnsupportedOperation:
                is_empty = True

        with open('database.csv', 'a', newline='') as file:
            writer = csv.writer(file, delimiter=";")

            if not is_empty:
                file.seek(0, 2)
                if file.tell() > 0:
                    file.seek(file.tell() - 2, 0)
                    last_char = file.read(1)
                    if last_char != '\n':
                        writer.writerow([])

            writer.writerow(
                [name, student_matricola, enrollment_date, study_field])

    except Exception as e:
        print("Error occurred:", e)

    # Clear input fields
    student_name.delete(0, 'end')
    student_id.delete(0, 'end')
    student_date.delete(0, 'end')
    student_field.delete(0, 'end')


window = tk.Tk()
window.title("Card Maker for University")

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

create_button = tk.Button(window, text="Submit Data", command=submitBtn)
create_button.grid(row=5, column=0, columnspan=2)

window.mainloop()
