import numpy as np
import cv2
import os

import time




#training_data_anant.npy
#[1,0,0,0,0]





file_name = 'training_data_anant.npy'



if os.path.isfile(file_name):

    print('File exists, loading previous data!')

    training_data = list(np.load(file_name))

else:

    print('File does not exist, starting fresh!')

    training_data_anant = []




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
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame',gray)

        foo = [1,0,0,0,0]

    
        training_data_anant.append([gray,foo])

        print("captured")


        if len(training_data_anant) % 100 == 0:

                print(len(training_data_anant))
                

                np.save(file_name,training_data_anant)
                print ("saved current chunk")
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

    


    



main()



        



    





























    
