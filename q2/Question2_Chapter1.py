import os, sys
from PIL import Image
import time

#Open the original picture.
image_direction = "chapter1.jpg"
provided_image = Image.open(image_direction)

#Produce the figure
live_time = int(time.time())
produced_number = (live_time % 100) + 50
if produced_number % 2 == 0:
    produced_number += 10

#Make a fresh image that is identical to the first in terms of size and mode
new_image = Image.new("RGB", provided_image.size)

#Get each image's pixel data.
initial_pixels = provided_image.load()
new_pixels = new_image.load()

#Iterate through every pixel, make changes, and figure out how much each red pixel is worth.
red_sum = 0
width, height = provided_image.size
for i in range(width):
    for j in range(height):
        r, g, b = initial_pixels[i, j]
        altered_pixel = (r + produced_number, g + produced_number, b + produced_number)
        new_pixels[i, j] = altered_pixel
        red_sum += altered_pixel[0]  #Build up your red values.

#Save the updated picture.
output_image_path = "chapter1out.jpg"
new_image.save(output_image_path)

#Show a notification that the procedure is finished.
print(f"Updated picture with changed pixels saved as {output_image_path}")
print(f"Sum red pixel values in the updated picture: {red_sum}")
