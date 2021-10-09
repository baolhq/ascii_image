import sys
from PIL import Image
import requests
from io import BytesIO

# Pass image URL as command line arguments
image_path = sys.argv[1]

# Load image from URL
response = requests.get(image_path)
img = Image.open(BytesIO(response.content))

# Resize image
width, height = img.size
aspect_ratio = height / width
new_width = 170
new_height = aspect_ratio * new_width * 0.5
img = img.resize((new_width, int(new_height)))

# Convert image to greyscale format
img = img.convert("L")

pixels = img.getdata()
chars = ["B", "S", "#", "&", "@", "$", "%", "*", "!", ":", "."]
new_pixels = [chars[pixel // 25] for pixel in pixels]
new_pixels = ''.join(new_pixels)

# Split string of chars into multiple strings of length equal to new width
new_pixels_count = len(new_pixels)
ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]

# for i in range(len(ascii_image)):
#     sleep(0.1)
#     print(ascii_image[i])

ascii_image = "\n".join(ascii_image)
with open("ascii_image.txt", "w") as f:
    f.write(ascii_image)
    f.close()
print("Image saved")
