import numpy as np
import cv2
import os

import time

from getkeys import key_check


#training_data_anant.npy
#[0,1,0,0,0]





file_name = 'training_data_aryan.npy'



if os.path.isfile(file_name):

    print('File exists, loading previous data!')

    training_data = list(np.load(file_name))

else:

    print('File does not exist, starting fresh!')

    training_data_aryan = []




cap = cv2.VideoCapture(0)

##while(True):
##    # Capture frame-by-frame
##    ret, frame = cap.read()
##
##    # Our operations on the frame come here
##    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
##
##    # Display the resulting frame
##    cv2.imshow('frame',gray)
##    if cv2.waitKey(1) & 0xFF == ord('q'):
##        break
##
### When everything done, release the capture
##cap.release()
##cv2.destroyAllWindows()


def main():



    for i in list(range(3)[::-1]):     #countdown

        print(i+1)

        time.sleep(1)




    paused = False
    while(True):


        if not paused:
            # Capture frame-by-frame
            ret, frame = cap.read()

            # Our operations on the frame come here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Display the resulting frame
            

            foo = [0,1,0,0,0]

        
            training_data_aryan.append([gray,foo])

            print("captured")


            if len(training_data_aryan) % 100 == 0:

                    print(len(training_data_aryan))
                    

                    np.save(file_name,training_data_aryan)
                    print ("saved current chunk")
            
            

        



        keys = key_check()

        if 'T' in keys:

            if paused:

                paused = False

                print('unpaused!')

                time.sleep(1)

            else:

                print('Paused, not recording')

                paused = True

                

                time.sleep(1)

    


    



main()



        



    





























    
