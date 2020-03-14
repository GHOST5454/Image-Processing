# This program contains information about how we are going to change the Scaling of the image.

# Step 1 : In this step we are importing Library for the editing of the image.
from PIL import Image
image = Image.open("C:/Users/LENOVO/PycharmProjects/Image-Processing/input/scaleinput.jpg")
image.show()

# lets scale image using bilinear scaling.
image.thumbnail((800, 800), Image.BILINEAR)
image.show()
image.save("C:/Users/LENOVO/PycharmProjects/Image-Processing/output/Scaling/Bilinear-scaling.jpg")

# lets scale image using Nearest scaling.It also known as point scaling.
image.thumbnail((800, 800), Image.NEAREST)
image.show()
image.save("C:/Users/LENOVO/PycharmProjects/Image-Processing/output/Scaling/Point-scaling.jpg")

# lets scale image using Bicubic scaling.
image.thumbnail((800, 800), Image.BICUBIC)
image.show()
image.save("C:/Users/LENOVO/PycharmProjects/Image-Processing/output/Scaling/Bicubic-scaling.jpg")

print("All Done !")
