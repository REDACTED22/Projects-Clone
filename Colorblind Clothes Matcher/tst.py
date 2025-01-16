from rembg import remove
from PIL import Image

# Load the image
input_path = "/Users/alexandermcgreevy/Documents/GitHub/Projects-Clone/Colorblind Clothes Matcher/blueshirt2 copy.jpg"
output_path = "BlueShirt_no_bg.png"

# Open and process the image
with open(input_path, "rb") as inp_file:
    input_image = inp_file.read()
    output_image = remove(input_image)

# Save the output
with open(output_path, "wb") as out_file:
    out_file.write(output_image)

print("Background removed and saved to:", output_path)
