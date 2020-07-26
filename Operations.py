import numpy as np
import matplotlib.pyplot as plt

class Operations:
    def __init__(self,img1_path,img2_path):
        self.img1 = plt.imread(img1_path)
        self.img2 = plt.imread(img2_path)
        
    def add(self,alpha): #img1 + img2
        result = np.zeros((256,256,3))
        for x in range(0,256):
            for y in range(0,256):
                result[x][y] = alpha*self.img1[x][y]+(1-alpha)*self.img2[x][y]
                for z in range(0,3):
                    if(result[x][y][z] > 255): result[x][y][z] = 255
        self.display_image(result)  
        

    def sub(self,alpha): #img1 - img2
        result = np.zeros((256,256,3))
        for x in range(0,256):
            for y in range(0,256):
                result[x][y] = alpha*self.img1[x][y]-(1-alpha)*self.img2[x][y]
                for z in range(0,3):
                    if(result[x][y][z] < 0): result[x][y][z] = 0
        self.display_image(result)  
         
    def display_images(self): #plot img1 & img2
        plt.subplot(1,2,1)
        plt.imshow(self.img1)
        plt.axis(False)
        plt.subplot(1,2,2)
        plt.imshow(self.img2)
        plt.axis(False)
        plt.show()
        
    def display_image(self,img): #plot any image
        plt.imshow(img)
        plt.axis(False)
        plt.show()
        