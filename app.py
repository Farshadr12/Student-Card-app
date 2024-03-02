from PIL import Image, ImageDraw, ImageFont
import csv


# Define image paths and text
id_txt = "B340003005"
background_path = "src/base.png"
foreground_path = "profile.jpg"
code_path = "barcodevan.png"
major_txt = "Data Analytics"
name_txt = "Hadi Hadiiii"
font_path = "src/font.ttf"


database = open('database.csv', 'r')
csv_reader = csv.reader(database, delimiter=';')


for row in csv_reader:
    print(row[0])


# Open images
background_image = Image.open(background_path)
foreground_image = Image.open(foreground_path)


# print("Background image:", background_image.format,
#       background_image.mode, background_image.size)
# print("Barcode image:", barcode_image.format,
#       barcode_image.mode, barcode_image.size)


code_position = (80, 150, 100, 100)

# background_image.paste(barcode_image, code_position)

foreground_position = (80, 150)
foreground_image = foreground_image.resize((225, 300))
background_image.paste(foreground_image, foreground_position)


draw = ImageDraw.Draw(background_image)
font = ImageFont.truetype(font_path, 27)  # Adjust font size as needed

# texts here
major_position = (600, 400)
name_position = (600, 310)
id_position = (600, 360)
draw.text(name_position, name_txt, fill=(0, 0, 0), font=font, anchor="ls")
draw.text(id_position, id_txt, fill=(0, 0, 0), font=font, anchor="ls")
draw.text(major_position, major_txt, fill=(0, 0, 0), font=font, anchor="ls")

result_path = "output/combined_image.jpg"
background_image.save(result_path, format="PNG")


print(f"Image saved successfully as: {result_path}")
