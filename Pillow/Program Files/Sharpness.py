# This program contains information about how we are going to change the Sharpness of the image.

# Step 1 : In this step we are importing Library for the editing of the image.
from PIL import Image, ImageEnhance

# Step 2 : In second step we are giving the address of the image form the "INPUT" folder.
image = Image.open("C:/Users/LENOVO/PycharmProjects/Image-Processing/input/princeton_small.jpg")
image.show()


# Step 3 : In third step we are going to we have to see what operation we want to perform.
en = ImageEnhance.Sharpness(image)

# Step 4 : In fourth step we are giving the value how much Sharpness we want increase.
image = en.enhance(2.0)

# Step 5 : It is use to see the edited image.
image.show()

# Lets save the image.
image.save("C:/Users/LENOVO/PycharmProjects/Image-Processing/output/Sharpen/2.0.jpg")

print("All Done!")
