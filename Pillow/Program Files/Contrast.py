# This program contains information about how we are going to change the Contrast of the image.

# Step 1 : In this step we are importing Library for the editing of the image.
from PIL import Image, ImageEnhance

# Step 2 : In second step we are giving the address of the image form the "INPUT" folder.
image = Image.open("C:/Users/LENOVO/PycharmProjects/Image-Processing/input/c.jpg")
image.show()


# Step 3 : In third step we are going to we have to see what operation we want to perform.
en = ImageEnhance.Contrast(image)

# Step 4 : In fourth step we are giving the value, how much Contrast we want increase.
image = en.enhance(-0.5)

# Step 5 : It is use to see the edited image.
image.show()

# step 6 : We are going to save the image.
image.save("C:/Users/LENOVO/PycharmProjects/Image-Processing/output/Contrast/-0.5.jpg")

# Step 4 : Contrast (0.0) and saving the image.
image1 = en.enhance(0.0)
image1.show()
image1.save("C:/Users/LENOVO/PycharmProjects/Image-Processing/output/Contrast/0.0.jpg")

# Step 4 : Contrast (0.5) and saving the image.
image2 = en.enhance(0.5)
image2.show()
image2.save("C:/Users/LENOVO/PycharmProjects/Image-Processing/output/Contrast/0.5.jpg")

# Step 4 : Contrast (2.0) and saving the image.
image2 = en.enhance(2.0)
image2.show()
image2.save("C:/Users/LENOVO/PycharmProjects/Image-Processing/output/Contrast/2.0.jpg")

print("All Done !")
