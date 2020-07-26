import numpy as np
import matplotlib.pyplot as plt

def histogram_image(img_path): #plot any image histogram
        img = plt.imread(img_path)
        histogram, bin_edges = np.histogram(img, bins=256, range=(0, 1))
        plt.figure()
        plt.title("Grayscale Histogram")
        plt.xlabel("grayscale value")
        plt.ylabel("pixels")
        plt.xlim([0.0, 1.0])
        plt.plot(bin_edges[0:-1], histogram)
        plt.show()