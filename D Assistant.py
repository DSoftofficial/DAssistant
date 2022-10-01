# from ast import main
# from ast import Try
import os
import pyttsx3
# import cv2
# import playsound from playsound
import wikipedia
import webbrowser
import smtplib
import datetime
# import playsound
import speech_recognition as sr
import pyaudio
from tkinter import *
# import django
import random
import pyautogui
# import speedtest
# import requests
# import json


# GUI
# gui_root = Tk()



# # geometry
# gui_root.geometry("602x698")

# # min size ~ width x height
# gui_root.minsize(602,698)

# gui_root.title("D Assistant")

# # max size ~ width x height
# gui_root.maxsize(602,698)


# gui_root.iconbitmap("K:\\D Assistant\\D Assistant.ico")

# head_label = Label(text = "D Assistant")
# head_label.pack()
# gui_root.configure(bg="#1a1a1a")
# # guimain
# gui_main_message = Label()




# engines attach
# main audio
def speak(audio):
     engine.say(audio)
     engine.runAndWait()
# {voice main source
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices) # *for testing purpose*
# print(voices[0].id) # *for testing purpose*
engine.setProperty('voice', voices[0].id)

# name
speak("Enter your name")
name = input("Enter your name : ")

# Wish
def wishMe():
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
def howareyou():
     speak("How are you?")
     how_are_you = input("How are you?\n")
     if how_are_you == "I am fine":
          speak("Good to hear!")
          print("Good to hear!")
     elif how_are_you == "I am not fine":
          speak("Take some medicine or else go to doctor")
          print("Take some medicine or else go to doctor")

# speak
def help():
     speak("I am D. How may I help you")

# takeCommand() function
def takeCommand():
     r = sr.Recognizer()
     with sr.Microphone() as source:
          print("Listening...")
          r.pause_threshold = 1
          r.energy_threshold = 298
          audio = r.listen(source,0,4)
     try:
          print("Recognizing...")
          query = r.recognize_google(audio, language='en-in')
          print(f"You said: {query}\n")
     
     except Exception as e:
          # print(exception)
          print("Say that again please...")
          return "None"
     return query

if __name__ == "__main__":
     wishMe()
     howareyou()
     help()
     while True:
          query = takeCommand().lower()  
          # query of wikipedia
          if "wikipedia" in query :
               querytopic = input("Enter the topic which you want to search")
               querytopicreplace = query.replace("wikipedia", querytopic)
               wikipedia_results = wikipedia.summary(querytopic, sentences = 18)
               print(wikipedia_results)
               speak(wikipedia_results)
          # query of opening youtube
          elif "open youtube" in query:
               webbrowser.open("www.youtube.com")
               speak("Opening Youtube")
               speak("Opened Youtube")
          # query of bing search engine
          elif "open bing" in query:
               webbrowser.open("www.bing.com")
               speak("Opening Bing")
               speak("Opened bing")
          # query of google search engine
          elif "open google" in query:
               webbrowser.open("www.google.com")
               speak("Opening Google")
               speak("Opened Google")
          # query of whatsapp
          elif "open whatsapp" in query:
               webbrowser.open("web.whatsapp.com")
               speak("Opening Whatsapp")
               speak("Opened Whatsapp")
          # query to open stackoverflow
          elif "open stack overflow" in query:
               webbrowser.open("www.stackoverflow.com")
               speak("Opening stack overflow")
               speak("Opened stack overflow")
               
     # query to open G-Mail
          elif "open Gmail" in query:
               webbrowser.open("www.gmail.com")
               speak("Opening Gmail")
               speak("Opened Gmail")

          elif "open github" in query:
               webbrowser.open("www.github.com")
               speak("Opening GitHub")
               speak("Opened GitHub")

          # query to open Microsft Outlook in web
          elif "open outlook in web" in query:
               webbrowser.open("www.outlook.com")
               speak("Opening Micrsoft Outlook")
               speak("Opened Micrsoft Outlook")

          elif "play music" in query:
               # music_run = 1
               music_dir = input("Enter music directory folder:\n")
               songs = os.listdir(music_dir)
               # print(songs)
               music_num = random.randint(0,2) 
               # print(music_num) #*for testing purpose*'''
               os.startfile(os.path.join(music_dir, songs[music_num]))
               speak("Playing music")
          # will be created in v2.0.0
          # elif "stop music" in query:
          #      os.close(os.path.join(music_dir, songs[music_num]))
          #      speak("Stopped music")

          elif "open vs code" in query:
               vscodedir2 = "C://Users//DHRUBAJYOTI//AppData//Roaming//Microsoft//Windows//Start Menu//Programs//Visual Studio Code//Visual Studio Code.lnk"
               os.startfile(vscodedir2)
               speak("Opened VS Code")
          # will created in v2.0.0
          # elif "open Word" in query:
          #      pyautogui.press("super")

          #      # pyautogui.typewrite("winword")
          #      # pyautogui.sleep(2)
          #      # pyautogui.press("enter")
               
          # elif "open MS Excel" in query:
          #      MS_Exceldir = "C:\\Users\\DHRUBAJYOTI\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk"
          #      os.startfile(MS_Exceldir)

          # elif "open MS Powerpoint" in query:
          #      MS_Powerpointdir = "C:\\Users\\DHRUBAJYOTI\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Powerpoint.lnk"
          #      os.startfile(MS_Powerpointdir)

          # elif "open MS Access" in query:
          #      MS_Accessdir = "C:\\Users\\DHRUBAJYOTI\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Access.lnk"
          #      os.startfile(MS_Accessdir)

          elif "open C drive" in query:
               C_folder_dir = "C:\\"
               os.startfile(C_folder_dir)
               speak("C drive opened")

          elif "open D drive" in query:
               D_folder_dir = "D:\\"
               os.startfile(D_folder_dir)
               speak("D drive opened")

          elif "open E drive" in query:
               E_folder_dir = "E:\\"
               os.startfile(E_folder_dir)
               speak("E drive opened")

          elif "open F drive" in query:
               F_folder_dir = "F:\\"
               os.startfile(F_folder_dir)
               speak("F drive opened")

          elif "open G drive" in query:
               G_folder_dir = "G:\\"
               os.startfile(G_folder_dir)
               speak("G drive opened")

          elif "open H drive" in query:
               H_folder_dir = "I:\\"
               os.startfile(H_folder_dir)
               speak("H drive opened")

          elif "open I drive" in query:
               I_folder_dir = "I:\\"
               os.startfile(I_folder_dir)
               speak("I drive opened")

          elif "open J drive" in query:
               J_folder_dir = "J:\\"
               os.startfile(J_folder_dir)
               speak("J drive opened")

          elif "open K drive" in query:
               K_folder_dir = "K:\\"
               os.startfile(K_folder_dir)
               speak("K drive opened")

          elif "open L drive" in query:
               L_folder_dir = "L:\\"
               os.startfile(L_folder_dir)
               speak("L drive opened")

          elif "open M drive" in query:
               M_folder_dir = "M:\\"
               os.startfile(M_folder_dir)
               speak("M drive opened")

          elif "open N drive" in query:
               N_folder_dir = "N:\\"
               os.startfile(N_folder_dir)
               speak("N drive opened")

          elif "open O drive" in query :
               O_folder_dir = "O:\\"
               os.startfile(O_folder_dir)
               speak("O drive opened")

          elif "open P drive" in query:
               P_folder_dir = "P:\\"
               os.startfile(P_folder_dir)
               speak("P drive opened")

          elif "open Q drive" in query:
               Q_folder_dir = "Q:\\"
               os.startfile(Q_folder_dir)
               speak("Q drive opened")

          elif "open R drive" in query:
               R_folder_dir = "R:\\"
               os.startfile(R_folder_dir)
               speak("R drive opened")

          elif "open S drive" in query:
               S_folder_dir = "S:\\"
               os.startfile(S_folder_dir)
               speak("S drive opened")

          elif "open T drive" in query:
               T_folder_dir = "T:\\"
               os.startfile(T_folder_dir)
               speak("T drive opened")

          elif "open U drive" in query:
               U_folder_dir = "U:\\"
               os.startfile(U_folder_dir)
               speak("U drive opened")

          elif "open V drive" in query:
               V_folder_dir = "V:\\"
               os.startfile(V_folder_dir)
               speak("V drive opened")

          elif "open W drive" in query:
               W_folder_dir = "W:\\"
               os.startfile(W_folder_dir)
               speak("W drive opened")

          elif "open X drive" in query:
               X_folder_dir = "X:\\"
               os.startfile(X_folder_dir)
               speak("X drive opened")

          elif "open Y drive" in query:
               Y_folder_dir = "Y:\\"
               os.startfile(Y_folder_dir)
               speak("Y drive opened")

          elif "open Z drive" in query:
               Z_folder_dir = "Z:\\"
               os.startfile(Z_folder_dir)
               speak("Z drive opened")

          elif "shutdown pc" in query:
               speak("Do you want to shutdown your PC?")
               choice = "Do you want to shutdown your PC(Yes/No)?"
               print(choice)
               secs = 6
               speak("Shutting down your PC after next 6 seconds")
               print("Shutting down your PC after next 6 seconds")
               os.system('shutdown /s /t 6')
          
          # will be opened in version 2.0
          # {
          # elif in query == "restart pc":
          #      choice = input("Do you want to restart your PC(Y/N)")
          #      if (choice == "Y"):
          #           secs = 6
          #           speak("Restarting your PC after next 6 seconds")
          #           os.system('shutdown /r 6')
          #      else:
          #           pass

          # elif in query == "log off pc":
          #      choice = input("Do you want to log off your PC(Y/N)")
          #      if (choice == "Y"):
          #           secs = 6
          #           speak("Logging off your PC after next 6 seconds")
          #           os.system('shutdown /l 6')
          #      else:
          #           pass
          # }


          elif "open notepad" in query:
               notepad_dir = "C:\\Windows\\notepad.exe"
               os.startfile(notepad_dir)


          elif "remember that" in query:
               rememberMessage = query.replace("remember that", "")
               remember_folder_create = os.mkdir("remember things")
               remember_file_create = open("remember things\\remember.txt", 'a+')
               remember_file_create.write(rememberMessage)
               print("Remembered your thing," + name)
               speak("Remembered your thing," + name)
               remember_file_create.close()
               speak("You told me that " + rememberMessage)
               print("You told me that " + rememberMessage)
     
          elif "what have I remembered" in query:
               remember_file_read = open("remember things\\remember.txt", 'r')
               speak("You told me that" + remember_file_read.read())
               print("You told me that" + remember_file_read.read())
               remember_file_create.close()

          elif "pause" in query:
               pyautogui.press("k")
               speak("video paused")

          elif "play" in query:
               pyautogui.press('k')
               speak("video played")
          elif "rewind" in query:
               pyautogui.press('j')

          elif "fast forward" in query:
               pyautogui.press('l')

          elif "mute" in query:
               pyautogui.press('m')

          elif "unmute" in query:
               pyautogui.press('m')

          elif "close miniplayer" in query:
               pyautogui.press('escape')

          elif "theater mode " in query:
               pyautogui.press('t')

          elif "full screen " in query:
               pyautogui.press('f')

          elif "default view " in query:
               pyautogui.press('t' or 'f')

          elif "next video" in query:
               pyautogui.press('shift+n')

          elif "previous video" in query:
               pyautogui.press('shift+p')

          elif "open Calculator" in query:
               calc_path = "C:\\Windows\\System32\\calc.exe"
               os.startfile(calc_path)
          
          # elif "check internet speed" in query:
               
          elif "take a screenshot" in query:
               screenshot_dir = os.mkdir("screenshots")
               screenshot_take = pyautogui.screenshot("Screenshot(1).jpg")
               screenshot_take.save("Screenshots")

          elif "click my photo" in query:
               pyautogui.press("super")
               pyautogui.typewrite("camera")
               pyautogui.press("enter")
               pyautogui.sleep(2)
               speak("SMILE")
               pyautogui.press("enter")

          elif "version" in query:
               gui_help = Tk()
               gui_help.geometry("220x220")
               gui_help.maxsize(220,220)
               gui_help.minsize(220,220)
               head_label = Label(text = "D Assistant")
               gui_help.iconbitmap("K:\\D Assistant\\D Assistant.ico")
               gui_help.title("Version of D Assistant")
               gui_help.mainloop()
               takeCommand()
          # elif "" in query:
               
          # elif "" in query:

          # elif "" in query:
               
          # elif "" in query:
               
          # elif "" in query:
               
          # elif "" in query:
               
          # elif "" in query:

          # elif "" in query:
               
          # elif "" in query:
               
          # elif "" in query:
               
          # elif "" in query:
               
          # elif "" in query:

          elif "sleep" in query:
               speak("Thankyou, for using me. Bye. We will meet next time!")
               print("Thankyou, for using me. Bye🖐️. We will meet next time!")
               exit()
               
# gui_root.mainloop()