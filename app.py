import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageDraw, ImageFont,ImageTk
from time import sleep
from tqdm import tqdm
import os
from tkinter import filedialog
import shutil

light = "#F2F2F2"
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("University of Campania Student Card App")

        self.configure()

        self.image_path = "src/logovan.jpeg"
        self.image = Image.open(self.image_path)

        self.original_image = Image.open(self.image_path)
        self.resized_image = self.original_image.resize((250, 150))
        self.image_tk = ImageTk.PhotoImage(self.resized_image)

        self.picture_label = tk.Label(self, image=self.image_tk)
        self.picture_label.pack()

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = 500
        window_height = 700
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.background_path = "src/card_background.jpg"
        self.code_path = "barcodevan.png"
        self.font_path = "src/ARIALBD.TTF"

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="Student Card Generator", font=("Helvetica", 32, "bold")).pack(pady=8)
        ttk.Label(self, text="University of Luigi Vanvitelli", font=("Helvetica", 32, "bold")).pack(pady=0)


        

        form_frame = ttk.Frame(self)
        form_frame.pack(padx=20, pady=10)

        self.name_var = tk.StringVar()
        self.id_var = tk.StringVar()
        self.date_var = tk.StringVar()
        self.field_var = tk.StringVar()
        self.picture_var = tk.StringVar()

        ttk.Label(form_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        ttk.Entry(form_frame, textvariable=self.name_var).grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(form_frame, text="ID:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        ttk.Entry(form_frame, textvariable=self.id_var).grid(row=1, column=1, padx=5, pady=5)
        ttk.Label(form_frame, text="Date:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        ttk.Entry(form_frame, textvariable=self.date_var).grid(row=2, column=1, padx=5, pady=5)
        ttk.Label(form_frame, text="Field:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        ttk.Entry(form_frame, textvariable=self.field_var).grid(row=3, column=1, padx=5, pady=5)
        ttk.Label(form_frame, text="Picture Path:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
        ttk.Button(form_frame, text="Select Picture", command=self.select_picture).grid(row=4, column=1, padx=5, pady=5)

        self.select_picture_button = ttk.Button(form_frame, text="Select Picture", command=self.select_picture)
        self.select_picture_button.grid(row=4, column=1, padx=5, pady=5)

        ttk.Button(form_frame, text="Add User", command=self.add_user).grid(row=5, column=0, columnspan=2, padx=5, pady=10)

        

        # Buttons
        button_frame = ttk.Frame(self)
        button_frame.pack(pady=10)

        ttk.Button(button_frame, text="Make Cards", command=self.make_cards).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Exit", command=self.quit).pack(side="right", padx=5)
        ttk.Label(self, text="Created By Farshad Rouzbehi", font=("Helvetica", 12)).pack(pady=10)

    def select_picture(self):
        picture_path = filedialog.askopenfilename(
            initialdir="/",
            title="Select Picture File",
            filetypes=(
                ("JPEG files", "*.jpg"),
                ("PNG files", "*.png"),
                ("All files", "*.*")
            )
        )

        if picture_path:
            destination_path = os.path.join("src/profiles", os.path.basename(picture_path))
            shutil.copyfile(picture_path, destination_path)
            self.picture_var.set(destination_path)
            self.select_picture_button.config(state="disabled")


    def make_cards(self):
        with open('users.txt', 'r') as file:
            lines = file.readlines()

        for i in tqdm(range(len(lines))):
            for line in lines:
                row = line.strip().split(',')
                background_image = Image.open(self.background_path)

                if len(row) >= 5 and os.path.exists(row[4]):
                    foreground_path = row[4]
                    foto_user = Image.open(foreground_path)
                else:
                    foto_default = "src/profiles/default.png"
                    foto_user = Image.open(foto_default)

                name_user = row[0]
                id_user = row[1]
                date_user = row[2]
                field_user = row[3]

                foreground_position = (145, 150)
                foto_user = foto_user.resize((225, 300))
                background_image.paste(foto_user, foreground_position)

                draw = ImageDraw.Draw(background_image)
                font = ImageFont.truetype(self.font_path, 27)
                fontID = ImageFont.truetype(self.font_path, 40)

                field_position = (611+40, 325+20)
                name_position = (611+40, 265+20)
                id_position = (770, 50)
                date_position = (611+40, 385+20)

                draw.text(name_position, name_user, fill=(0, 0, 0), font=font, anchor="ls")
                draw.text(id_position, id_user, fill=(255, 255, 255), font=fontID, anchor="ls")
                draw.text(field_position, field_user, fill=(0, 0, 0), font=font, anchor="ls")
                draw.text(date_position, date_user, fill=(0, 0, 0), font=font, anchor="ls")

                result_path = "output/{name} Cart.jpg".format(name=name_user)
                background_image.save(result_path, format="PNG")

            sleep(0.0001)
        print("Card Generated successfully!")

    def add_user(self):
        user_entry = [
            self.name_var.get(),
            self.id_var.get(),
            self.date_var.get(),
            self.field_var.get(),
            self.picture_var.get()
        ]

        with open('users.txt', 'r') as file:
            last_char = file.read()[-1:]
        if last_char:
            with open('users.txt', 'a') as file:
                file.write('\n')

        with open('users.txt', 'a') as file:
            file.write(','.join(user_entry))

        print("User added successfully!")


if __name__ == '__main__':
    app = App()
    app.mainloop()
