from PIL import Image, ImageDraw, ImageFont
import csv
from time import sleep
from tqdm import tqdm

background_path = "src/base.png"
code_path = "barcodevan.png"
font_path = "src/font.ttf"


database = open('database.csv', 'r')
csv_reader = csv.reader(database, delimiter=';')


for i in tqdm(range(100)):

    for row in csv_reader:
        background_image = Image.open(background_path)
        if row[3]:
            foreground_path = row[4]
            foto_user = Image.open(foreground_path)
        else:
            foto_default = "src/profiles/default.png"
            foto_user = Image.open(foto_default)

        name_user = row[0]
        id_user = row[1]
        date_user = row[2]
        field_user = row[3]

        code_position = (80, 150, 100, 100)

        foreground_position = (80, 150)
        foto_user = foto_user.resize((225, 300))
        background_image.paste(foto_user, foreground_position)

        draw = ImageDraw.Draw(background_image)
        font = ImageFont.truetype(font_path, 27)

        field_position = (600, 400)
        name_position = (600, 310)
        id_position = (600, 360)

        draw.text(name_position, name_user, fill=(
            0, 0, 0), font=font, anchor="ls")
        draw.text(id_position, id_user, fill=(0, 0, 0), font=font, anchor="ls")
        draw.text(field_position, field_user, fill=(
            0, 0, 0), font=font, anchor="ls")

        result_path = "output/{name} Cart.jpg".format(name=name_user)
        background_image.save(result_path, format="PNG")

    sleep(0.001)

print(f"Images saved successfully as: {result_path}")
