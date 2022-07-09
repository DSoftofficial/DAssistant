import os
import pyttsx3
# import playsound from playsound
import wikipedia
import webbrowser
import smtplib
import datetime
import playsound
import speech_recognition


# 1.collect Info of the person and wish
# main audio
def speak(audio):
     engine.say(audio)
     engine.runAndWait()

# {voice main source
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)

# name
speak("Enter your name")
name = input("Enter your name : ")

# Wish
hour = (datetime.datetime.now().hour)
if hour >0 and hour<12:
     print("Good morning " + name + '!')
     speak("Good morning " + name + '!')
elif hour >12 and hour<18:
     print("Good Afternoon " + name + '!')
     speak("Good Afternoon " + name + '!')
else:
     print("Good Evening " + name + '!')
     speak("Good Evening " + name + '!')

# how are you
micinput = sr.recognizer
if (help == "How are you?") :
     print("I am fine")

# help
speak("I am D. How may I help you," + name + ':\n')
help = input("I am D. How may I help you," + name + ':\n')

