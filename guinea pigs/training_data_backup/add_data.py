import numpy as np

import matplotlib.pyplot as plt
import cv2

import os 

mat_anant = np.array(np.load("training_data_anant.npy"))

mat_aryan = np.array(np.load("training_data_aryan.npy"))

mat_chai = np.array(np.load("training_data_chai.npy"))

mat_mainak = np.array(np.load("training_data_mainak.npy"))

mat_rathinn = np.array(np.load("training_data_rathinn.npy"))



file_name = ('final_not_split.npy')

mat_added = []

def add_all():

   for i in range (len(mat_anant)):
      mat_added.append(mat_anant[i])
      print ("added anant")
      print("")

   for i in range (len(mat_aryan)):
      mat_added.append(mat_aryan[i])
      print ("added aryan")
      print("")

   for i in range (len(mat_chai)):
      mat_added.append(mat_chai[i])
      print ("added chai")
      print("")

   for i in range (len(mat_mainak)):
      mat_added.append(mat_mainak[i])
      print ("added mainak")
      print("")

   for i in range (len(mat_rathinn)):
      mat_added.append(mat_rathinn[i])
      print ("added rathinn")
      print("")







   

   

add_all()


np.save(file_name,mat_added)


print ("all done--------------------------------")
   



   
   
