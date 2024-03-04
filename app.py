from PIL import Image, ImageDraw, ImageFont
import sqlite3
from time import sleep
from tqdm import tqdm

background_path = "src/card_background.jpg"
code_path = "barcodevan.png"
font_path = "src/ARIALBD.TTF"


def fetch_data_from_database():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM students")
    rows = c.fetchall()
    conn.close()
    return rows


for i in tqdm(range(100)):
    for row in fetch_data_from_database():
        background_image = Image.open(background_path)
        try:
            if row[4]:
                foreground_path = row[4]
                foto_user = Image.open(foreground_path)
            else:
                foto_default = "src/profiles/default.png"
                foto_user = Image.open(foto_default)
        except Exception as e:
            print("Error occurred:", e)

        name_user = row[0]
        id_user = row[1]
        date_user = row[2]
        field_user = row[3]

        foreground_position = (145, 150)
        foto_user = foto_user.resize((225, 300))
        background_image.paste(foto_user, foreground_position)

        draw = ImageDraw.Draw(background_image)
        font = ImageFont.truetype(font_path, 27)
        fontID = ImageFont.truetype(font_path, 40)

        field_position = (611+40, 325+20)
        name_position = (611+40, 265+20)
        id_position = (770, 50)
        date_position = (611+40, 385+20)

        draw.text(name_position, name_user, fill=(
            0, 0, 0), font=font, anchor="ls")
        draw.text(id_position, id_user, fill=(
            255, 255, 255), font=fontID, anchor="ls")
        draw.text(field_position, field_user, fill=(
            0, 0, 0), font=font, anchor="ls")
        draw.text(date_position, date_user, fill=(
            0, 0, 0), font=font, anchor="ls")

        result_path = "output/{name} Cart.jpg".format(name=name_user)
        background_image.save(result_path, format="PNG")

    sleep(0.001)
