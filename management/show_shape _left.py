import numpy as np

mat = np.array(np.load("training_data_left.npy"))

for i in range (-1,len(mat),100):
    print (mat[i])

    

