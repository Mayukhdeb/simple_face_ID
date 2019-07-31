import numpy as np

import matplotlib.pyplot as plt


mat = np.array(np.load("training_data_anant.npy"))

import cv2

for i in range (len(mat)):
   foo = mat[i]

   woop = foo[0]

   plt.imshow(woop, cmap="gray")
   plt.show()

  
   
