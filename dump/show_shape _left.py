import numpy as np

mat = np.array(np.load("training_data_left.npy"))

for i in range (len(mat)):
    print (mat[i])

