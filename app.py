# (Project 5)

from Operations import Operations
from Image_Histogram import histogram_image
from Dilation import dilate_image
from Dilation_Example import dilate_image_example

if __name__ == '__main__':
    # addition and subtraction operations 
    op = Operations('./images/Lena-256x256.png','./images/Background-256x256.jpg')
    op.display_images()
    op.add(0.90) #alpha = 0.90
    op.sub(0.85) #alpha = 0.85
    # plot histogram Lena-256x256.png
    histogram_image('./images/Lena-256x256.png')
    # dilation operator 
    dilate_image('./images/j.png')
    # dilation example
    dilate_image_example()
    