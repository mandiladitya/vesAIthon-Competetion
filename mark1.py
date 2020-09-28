import requests
import numpy as np
import cv2
import random


i=1
while(i):
    # Capture frame-by-frame
    req = requests.get('http://192.168.43.1:8080/shot.jpg')
    arr = np.asarray(bytearray(req.content), dtype=np.uint8)
    img = cv2.imdecode(arr, -1)
    i=0
    cv2.imwrite(r"C:\Users\User\Desktop\tesseract-python-master/{index}.png".format(index=i),img)
    exit()
    
    cv2.imshow('frame',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture

cv2.destroyAllWindows()

from PIL import Image
import pytesseract


im = Image.open("0.png")

text = pytesseract.image_to_string(im, lang = 'eng')

print(text)

