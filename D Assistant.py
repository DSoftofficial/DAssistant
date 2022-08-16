import os
import pyttsx3
import cv2
# import playsound from playsound
import wikipedia
import webbrowser
import smtplib
import datetime
# import playsound
# import speech_recognition as sr
# import pyaudio
from tkinter import *
import django
import random
# engines attach
# 1. main audio
def speak(audio):
     engine.say(audio)
     engine.runAndWait()
# {voice main source
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)

# will be created in ver 1.1.0{
# 2. micinput
# def takeCommand():
#      r = sr.Recognizer
#      with sr.Microphone() as source:
#           print("Listening...")
#           r.pause_threshold = 1
#           audio = r.listen(source)
#      try:
#           print("Recognizing...")
#           query = r.recognize_bing(audio, language='en-in')
#           print(f"User said: {query}\n")
     
#      except Exception as exception:
#           # print(exception)
#           print("Say that again please...")
#           return "None"
#      return query
# }

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
how_are_you = input("How are you?")
if (how_are_you == "I am fine." or "Going good"):
     speak("Good to hear!")
     print("Good to hear!")
elif (how_are_you == "I am not fine" or "I am sick"):
     speak("Take some medicine or else go to doctor")
     print("Take some medicine or else go to doctor")

# speak
speak("I am D. How may I help you," + name)
helpinput = input("I am D. How may I help you," + name + ':\n')
# query of wikipedia
if helpinput == "wikipedia":
     helpinputtopic = input("Enter the topic which you want to search")
     helpinputtopicreplace = helpinput.replace("wikipedia", helpinputtopic)
     help_input_topic_results = wikipedia.summary(helpinputtopic, sentences = 20)
     print(help_input_topic_results)
     speak(help_input_topic_results)
# query of opening youtube
elif helpinput == "open youtube":
     webbrowser.open("www.youtube.com")
     speak("Opening Youtube")
     speak("Opened Youtube")
# query of bing search engine
elif helpinput == "open bing":
     webbrowser.open("www.bing.com")
     speak("Opening Bing")
     speak("Opened bing")
# query of google search engine
elif helpinput == "open google":
     webbrowser.open("www.google.com")
     speak("Opening Google")
     speak("Opened Google")
# query of whatsapp
elif helpinput == "open whatsapp":
     webbrowser.open("web.whatsapp.com")
     speak("Opening Whatsapp")
     speak("Opened Whatsapp")
# query to open stackoverflow
elif helpinput == "open stackoverflow":
     webbrowser.open("www.stackoverflow.com")
     speak("Opening Youtube")
     speak("Opened Youtube")

# query to open G-Mail
elif helpinput == "open Gmail":
     webbrowser.open("www.gmail.com")
     speak("Opening Gmail")
     speak("Opened Gmail")

# query to open Microsft Outlook in web
elif helpinput == "open microsoft outlook in web":
     webbrowser.open("www.outlook.com")
     speak("Opening Micrsoft Outlook")
     speak("Opened Micrsoft Outlook")

elif helpinput == "play music" or "play some music" or "play a music" or "play a sweet song" or "play song" or "play a song":
     music_dir = input("Enter music directory folder:\n")
     songs = os.listdir(music_dir)
     # print(songs)
     music_num = random.randint(1, 10)
     # print(music_num) # ''' *for testing purpose* '''
     os.startfile(os.path.join(music_dir, songs[music_num]))
     speak("Playing music")

elif helpinput == "open vs code" or "code ." or "open VS Code":
     vscodedir2 = "C://Users//DHRUBAJYOTI//AppData//Roaming//Microsoft//Windows//Start Menu//Programs//Visual Studio Code//Visual Studio Code.lnk"
     os.startfile(vscodedir2)
     speak("Opened VS Code")

elif helpinput == "open MS Word":
     MS_Worddir = "C:\\Users\\DHRUBAJYOTI\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk"
     os.startfile(MS_Worddir)
elif helpinput == "open MS Excel":
     MS_Exceldir = "C:\\Users\\DHRUBAJYOTI\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk"
     os.startfile(MS_Exceldir)

elif helpinput == "open MS Powerpoint":
     MS_Powerpointdir = "C:\\Users\\DHRUBAJYOTI\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Powerpoint.lnk"
     os.startfile(MS_Powerpointdir)

elif helpinput == "open MS Access":
     MS_Accessdir = "C:\\Users\\DHRUBAJYOTI\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Access.lnk"
     os.startfile(MS_Accessdir)

elif helpinput == "open C drive":
     C_folder_dir = "C:\\"
     os.startfile(C_folder_dir)
     speak("C drive opened")

elif helpinput == "open D drive":
     D_folder_dir = "D:\\"
     os.startfile(D_folder_dir)
     speak("D drive opened")

elif helpinput == "open E drive":
     E_folder_dir = "E:\\"
     os.startfile(E_folder_dir)
     speak("E drive opened")

elif helpinput == "open F drive":
     F_folder_dir = "F:\\"
     os.startfile(F_folder_dir)
     speak("F drive opened")

elif helpinput == "open G drive":
     G_folder_dir = "G:\\"
     os.startfile(G_folder_dir)
     speak("G drive opened")

elif helpinput == "open H drive":
     H_folder_dir = "I:\\"
     os.startfile(H_folder_dir)
     speak("H drive opened")

elif helpinput == "open I drive":
     I_folder_dir = "I:\\"
     os.startfile(I_folder_dir)
     speak("I drive opened")

elif helpinput == "open J drive":
     J_folder_dir = "J:\\"
     os.startfile(J_folder_dir)
     speak("J drive opened")

elif helpinput == "open K drive":
     K_folder_dir = "K:\\"
     os.startfile(K_folder_dir)
     speak("K drive opened")

elif helpinput == "open L drive":
     L_folder_dir = "L:\\"
     os.startfile(L_folder_dir)
     speak("L drive opened")

elif helpinput == "open M drive":
     M_folder_dir = "M:\\"
     os.startfile(M_folder_dir)
     speak("M drive opened")

elif helpinput == "open N drive":
     N_folder_dir = "N:\\"
     os.startfile(N_folder_dir)
     speak("N drive opened")

elif helpinput == "open O drive":
     O_folder_dir = "O:\\"
     os.startfile(O_folder_dir)
     speak("O drive opened")

elif helpinput == "open P drive":
     P_folder_dir = "P:\\"
     os.startfile(P_folder_dir)
     speak("P drive opened")

elif helpinput == "open Q drive":
     Q_folder_dir = "Q:\\"
     os.startfile(Q_folder_dir)
     speak("Q drive opened")

elif helpinput == "open R drive":
     R_folder_dir = "R:\\"
     os.startfile(R_folder_dir)
     speak("R drive opened")

elif helpinput == "open S drive":
     S_folder_dir = "S:\\"
     os.startfile(S_folder_dir)
     speak("S drive opened")

elif helpinput == "open T drive":
     T_folder_dir = "T:\\"
     os.startfile(T_folder_dir)
     speak("T drive opened")

elif helpinput == "open U drive":
     U_folder_dir = "U:\\"
     os.startfile(U_folder_dir)
     speak("U drive opened")

elif helpinput == "open V drive":
     V_folder_dir = "V:\\"
     os.startfile(V_folder_dir)
     speak("V drive opened")

elif helpinput == "open W drive":
     W_folder_dir = "W:\\"
     os.startfile(W_folder_dir)
     speak("W drive opened")

elif helpinput == "open X drive":
     X_folder_dir = "X:\\"
     os.startfile(X_folder_dir)
     speak("X drive opened")

elif helpinput == "open Y drive":
     Y_folder_dir = "Y:\\"
     os.startfile(Y_folder_dir)
     speak("Y drive opened")

elif helpinput == "open Z drive":
     Z_folder_dir = "Z:\\"
     os.startfile(Z_folder_dir)
     speak("Z drive opened")

elif helpinput == "shutdown pc":
     choice = input("Do you want to shutdown your PC(Y/N)")
     if (choice == "Y"):
          secs = 6
          speak("Shutting down your PC after next 6 seconds")
          os.system('shutdown /s /t 6')
     else:
          pass

# will be opened in version 1.1.0
# {
# elif helpinput == "restart pc":
#      choice = input("Do you want to restart your PC(Y/N)")
#      if (choice == "Y"):
#           secs = 6
#           speak("Restarting your PC after next 6 seconds")
#           os.system('shutdown /r 6')
#      else:
#           pass

# elif helpinput == "log off pc":
#      choice = input("Do you want to log off your PC(Y/N)")
#      if (choice == "Y"):
#           secs = 6
#           speak("Logging off your PC after next 6 seconds")
#           os.system('shutdown /l 6')
#      else:
#           pass
# }


elif helpinput == "open notepad":
     notepad_dir = "C:\\Windows\\notepad.exe"
     os.startfile(notepad_dir)

else:
     print("No such command!")
     speak("No such command!")
# elif helpinput == "":
     
# elif helpinput == "":
     
# elif helpinput == "":
     
# elif helpinput == "":
     
# elif helpinput == "":
     
# elif helpinput == "":
     
