# Helper utilities
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def writeDoubleImage(img, name): 
    img = (img/np.max(np.abs(img)))*255.0*10    # normalized and scaling
    img = np.clip(img, 0, 255) #lets ignore the negatives   clipped to range (0,255)
    plt.imsave(name, img, cmap="plasma")   # saved image using matplotlib function
    