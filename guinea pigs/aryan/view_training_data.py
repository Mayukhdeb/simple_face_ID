import numpy as np

import matplotlib.pyplot as plt


mat = np.array(np.load("training_data_aryan.npy"))

import cv2

for i in range (1,len(mat),100):
   foo = mat[i]

   woop = foo[0]

   plt.imshow(woop, cmap="gray")
   plt.show()

  
   
