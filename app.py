from PIL import Image, ImageDraw, ImageFont
from time import sleep
from tqdm import tqdm
import os
from flask import Flask, request

background_path = "src/card_background.jpg"
code_path = "barcodevan.png"
font_path = "src/ARIALBD.TTF"

app = Flask(__name__)
@app.route('/')
def index():
    return open('index.html').read()


def MakeCard():
    with open('users.txt', 'r') as file:
        lines = file.readlines()

    for i in tqdm(range(1)):

        for line in lines:
            row = line.strip().split(',')
            background_image = Image.open(background_path)
            print(row)

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


if __name__ == '__main__':
    app.run(debug=True)