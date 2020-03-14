# This program contains information about how we are going to edgeDetect of the image.

# Step 1 : In this step we are importing Library for the editing of the image.
from PIL import Image, ImageFilter
image = Image.open("C:/Users/LENOVO/PycharmProjects/Image-Processing/input/princeton_small.jpg")
image.show()

# Step 2 : we are applying Edge detect on the images.
image1 = image.filter(ImageFilter.EDGE_ENHANCE)
image1.show()

# Lets save the image.
image1.save("C:/Users/LENOVO/PycharmProjects/Image-Processing/output/EdgeDetect/EdgeDetect.jpg")

