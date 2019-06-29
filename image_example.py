import os 
os.system('1.py')
from PIL import Image
import pytesseract
import pyttsx3
o=pyttsx3.init()
volume=o.getProperty('volume')
o.setProperty('volume',1)
voices=o.getProperty('voices')
o.setProperty('voice',voices[1].id)
rate=o.getProperty('rate')
o.setProperty('rate',140)



im = Image.open("0.png")

text = pytesseract.image_to_string(im, lang = 'eng')

print(text)
o.say(text)
o.runAndWait()
o.stop()
"""

# Import the required module for text 
# to speech conversion 
from gtts import gTTS 

# This module is imported so that we can 
# play the converted audio 
import os 



# Language in which you want to convert 
language = 'en'

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed 
myobj = gTTS(text, lang=language, slow=False) 

# Saving the converted audio in a mp3 file named 
# welcome 
myobj.save("welcome.mp3") 

# Playing the converted file 
from pygame import mixer
mixer.init()
mixer.music.load("welcome.mp3")
mixer.music.play()"""
