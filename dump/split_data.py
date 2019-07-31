import numpy as np

import matplotlib.pyplot as plt

import os 
mat = np.array(np.load("training_data_anant.npy"))

import cv2


  

  
file_name = 'training_data_left.npy'

file_name_2 = 'training_data_right.py'





if os.path.isfile(file_name):

    print('File exists, loading previous data!')

    training_data = list(np.load(file_name))

else:

    print('File does not exist, starting fresh!')

    training_data_left = []

    training_data_right = []





for i in range (len(mat)):
   foo = mat[i]

   woop = foo[0]

   poow = foo[1]

   training_data_left.append(woop)

   training_data_right.append(poow)




   
np.save('training_data_left.npy',training_data_left)

np.save('training_data_right.npy',training_data_right)

print ("saved")   

   



































