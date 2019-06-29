import speech_recognition as sr
import os
import sys
import pyttsx3
import pyaudio
import subprocess
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')   # getting details of current speaking rate                    #printing current voice rate
engine.setProperty('rate',180) 
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
engine.setProperty('volume',1) 

def speak(audio):
    print('User ' + audio)
    engine.say(audio)
    engine.runAndWait()

def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('Aditya: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing ')
        query = str(input('Command: '))

    return query
        

if __name__ == '__main__':

    while True:
    
        query = myCommand();
        query = query.lower()
        
        if 'Open reading' in query:
            speak('okay')
            os.system('image_example.py')

