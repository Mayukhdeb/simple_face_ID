import numpy as np

import matplotlib.pyplot as plt


mat = np.array(np.load("training_data_shuffled.npy"))  ## file too large to upload on github


def print_full():
    for i in range (0,len(mat),100):

        print (mat[i])


def print_shape():
    print (mat.shape)

    woop = mat[0]

    print (woop[0].shape)
    
                

  
#print_shape()

print_full()
