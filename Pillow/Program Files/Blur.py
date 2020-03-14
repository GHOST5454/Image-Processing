# This program contains information about how we are going to change the blur of the image.

# Step 1 : In this step we are importing Library for the editing of the image.
from PIL import Image, ImageFilter
image = Image.open("C:/Users/LENOVO/PycharmProjects/Image-Processing/input/princeton_small.jpg")

# Simple Blur is working but it does not effect the image so a human can easily find out.So i have used GaussianBlur.

# Step 2.1 : we are applying Gaussian Blur on the images Blur(0.125).
image1 = image.filter(ImageFilter.GaussianBlur(0.125))
image1.show()

# Step 2.2 : we are applying Gaussian Blur on the images Blur(2).
image2 = image.filter(ImageFilter.GaussianBlur(2))
image2.show()

# Step 2.3 : we are applying Gaussian Blur on the images Blur(8).
image3 = image.filter(ImageFilter.GaussianBlur(8))
image3.show()

# Know lets save these images.
image1.save("C:/Users/LENOVO/PycharmProjects/Image-Processing/output/Blure/0.125.jpg")
image2.save("C:/Users/LENOVO/PycharmProjects/Image-Processing/output/Blure/2.jpg")
image3.save("C:/Users/LENOVO/PycharmProjects/Image-Processing/output/Blure/8.jpg")

print("All Done !")
