import numpy as np
import matplotlib.pyplot as plt

def getGray():
    return np.array([
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,0,0,0,0,0,1,1,1,0,0],
        [0,1,1,1,1,0,0,0,0,0,1,1,1,1,0,0],
        [0,0,1,1,0,0,0,0,0,1,1,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0],
        [0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0],
        [0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0],
        [0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0],
        [0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0],
        [0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0],
        [0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        ])

def dilate_image_example():
    
    # get gray
    gray = getGray()
    
    # selement
    selement = np.array([[1,1,1],[1,1,1],[1,1,1]])
    n,m = selement.shape
    k = int(n/2)
    
    # set target indeces
    indeces = list(zip(*np.where(selement == 1)))
    for x in range (len (indeces)):
        indeces[x] = (indeces[x][0] - k , indeces[x][1] - k)

    
    #dilate the image    
    row,col = gray.shape
    dilated_img = np.zeros(gray.shape)
    for x in range(k,row-k):
        for y in range(k,col-k):
            if(gray[x][y]): 
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
    