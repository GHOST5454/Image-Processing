# This program contains information about how we are going to change the Composite of the image.

# Step 1 : In this step we are importing Library for the editing of the image.
from PIL import Image

# Step 2 : In second step we are giving the address of the image form the "INPUT" folder.
image1 = Image.open("C:/Users/LENOVO/PycharmProjects/Image-Processing/input/comp_background.jpg").convert("RGBA")
image2 = Image.open("C:/Users/LENOVO/PycharmProjects/Image-Processing/input/comp_foreground.jpg").convert("RGBA")
image3 = Image.open("C:/Users/LENOVO/PycharmProjects/Image-Processing/input/comp_mask.jpg").convert("RGBA")

# Lets make composite of these images .
Image.composite(image1, image2, image3).save("C:/Users/LENOVO/PycharmProjects/Image-Processing/output/Composite/Cp.png")

print("All Done !")
