from PIL import Image, ImageDraw, ImageFont
import bargen

# Define image paths and text
id_txt = "B340003005"
bargen.bcode_gen(id_txt)
background_path = "base.png"
foreground_path = "profile.jpg"
code_path = "Mycode.png"
major_txt = "Data Analytics"
name_txt = "Farshad Rouzbehi"
font_path = "font.ttf"  # Replace with your desired font path

# Open images
background_image = Image.open(background_path)
background_image = background_image.convert('RGB')
foreground_image = Image.open(foreground_path)
#foreground_image = foreground_image.convert ('RGBA')
barcode_image = Image.open(code_path)
#barcode_image = barcode_image.convert('RGBA')

print("Background image:", background_image.format, background_image.mode, background_image.size)
print("Barcode image:", barcode_image.format, barcode_image.mode, barcode_image.size)


code_position = (80, 150, 100 , 100)

background_image.paste(barcode_image, code_position)

foreground_position = ( 80, 150)
foreground_image = foreground_image.resize((225, 300))
background_image.paste(foreground_image, foreground_position)


draw = ImageDraw.Draw(background_image)
font = ImageFont.truetype(font_path, 27)  # Adjust font size as needed

major_position = (600, 400)
name_position = (600, 310)
id_position = (600, 360)
draw.text(name_position, name_txt, fill=(0, 0, 0), font=font, anchor="ls")
draw.text(id_position, id_txt, fill=(0, 0, 0), font=font, anchor="ls")
draw.text(major_position, major_txt, fill=(0, 0, 0), font=font, anchor="ls")

result_path = "combined_image.jpg"
background_image.save(result_path, format="PNG")


print(f"Image saved successfully as: {result_path}")
