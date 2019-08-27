# balance_data.py



import numpy as np


from random import shuffle



train_data = np.load('final_not_split.npy')



print ("shuffling")


shuffle(train_data)







print("saving")



np.save('training_data_shuffled.npy', train_data)
print ("saved!!!")







