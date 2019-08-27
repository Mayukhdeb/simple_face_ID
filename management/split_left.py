import numpy as np



import os


mat = np.array(np.load("final_not_split.npy"))

file_name = 'training_data_left.npy'




if os.path.isfile(file_name):

    print('File exists, loading previous data!')

    training_data_left = list(np.load(file_name))

else:

    print('File does not exist, starting fresh!')

    training_data_left = []







import cv2

for i in range (len(mat)):
   foo = mat[i]

   woop = foo[0]

   training_data_left.append(woop)

   
  
   print (i)
