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
   mat_added.append(mat_anant)

   print ("added anant")

   mat_added.append(mat_aryan)

   print ("added aryan")

   mat_added.append(mat_chai)

   print ("added chai")

   mat_added.append(mat_mainak)

   print ("added mainak")

   mat_added.append(mat_rathinn)

   print ("added rathinn")



np.save(file_name,training_data_anant)
   



   
   
