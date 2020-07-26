import cv2
import numpy as np
import matplotlib.pyplot as plt

def dilate_image(img_path):
    # read the image and convert it to gray image
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # masking
    bw = gray>120
    
    # selement
    selement = np.array([[0,1,0],[1,1,1],[0,1,0]])
    n,m = selement.shape
    k = int(n/2)
    
    # set target indeces
    indeces = list(zip(*np.where(selement == 1)))
    for x in range (len (indeces)):
        indeces[x] = (indeces[x][0] - k , indeces[x][1] - k)

    
    #dilate the image    
    row,col = bw.shape
    dilated_img = np.zeros(bw.shape)
    for x in range(k,row-k):
        for y in range(k,col-k):
            if(bw[x][y]): 
                 dilated_img[x][y] = 1
                 for index in indeces:
                     dilated_img[x+index[0]][y+index[1]] = 1
                     
    # ploting result
    plt.subplot(1,2,1)
    plt.imshow(gray)
    plt.axis(False)
    plt.subplot(1,2,2)
    plt.imshow(dilated_img)
    plt.axis(False)
    plt.show()
