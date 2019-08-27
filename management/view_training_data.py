import numpy as np

import matplotlib.pyplot as plt


mat = np.array(np.load("training_data_shuffled.npy", allow_pickle = True))

import cv2

for i in range (0, len(mat), 1000):
    print (mat[i])

  
   
