# This program contains information about how we are going to change the brightness of the image.

# Step 1 : In this step we are importing Library for the editing of the image.
from PIL import Image, ImageEnhance

# Step 2 : In second step we are giving the address of the image form the "INPUT" folder.
image = Image.open("C:/Users/LENOVO/PycharmProjects/Image-Processing/input/princeton_small.jpg")
image.show()


# Step 3 : In third step we are going to we have to see what operation we want to perform.
en = ImageEnhance.Color(image)

# Step 4 : In fourth step we are giving the value, how much brightness we want increase.
image = en.enhance(0.0)

# Step 5 : It is use to see the edited image.
image.show()

# step 6 : We are going to save the image.
image.save("C:/Users/LENOVO/PycharmProjects/Image-Processing/output/Brightness/0.0.jpg")

# Step 4 : brightness (0.5) and saving the image.
image1 = en.enhance(0.5)
image1.show()
image1.save("C:/Users/LENOVO/PycharmProjects/Image-Processing/output/Brightness/0.5.jpg")

# Step 4 : brightness (2.0) and saving the image.
image2 = en.enhance(2.0)
image2.show()
image2.save("C:/Users/LENOVO/PycharmProjects/Image-Processing/output/Brightness/2.0.jpg")

print("All Done !")
