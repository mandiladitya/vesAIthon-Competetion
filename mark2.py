import numpy as np
import cv2
import random

cap = cv2.VideoCapture(0)

i=0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    i+=1
    cv2.imwrite('C:\Users\User\Desktop\tesseract-python-master\frames/{index}.png'.format(index=i),frame)


    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
