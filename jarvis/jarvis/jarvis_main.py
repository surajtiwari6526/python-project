import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup
import datetime
import os
import pyautogui
import speedtest


for i in range(3):
    a = input("Enter Password to open Jarvis :- ")
    pw_file = open("c:/Users/suraj/OneDrive/Desktop/python project/jarvis/jarvis/password.txt", "r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        print("Try Again")

from Dictapp import speak
from intro import play_gif
play_gif

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",170)

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

def takecommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening......")
        r.pause_threshold=1
        r.energy_threshold=300
        audio=r.listen(source,0,4)


    try:
        print("Understanding.....")
        query = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query} \n")
    except Exception as e:
        print("Say That Again")
        return "None"
    return query

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")


if __name__ == "__main__":
    while True:
        query = takecommand().lower()
        if "wake up" in query:
            from GreetME import greetME
            greetME()

            while True:
                query = takecommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can call anytime")
                    break

                elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is{new_pw}")

                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfact, sir")
                elif "thank you" in query:
                    speak("your welcome ,sir")
                elif "exit" in query:
                    exit()
                
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)                
                    
                    
                elif "temperature" in query:
                     search = "temperature in rajula"
                     url = f"https://www.google.com/search?q={search}"
                     r  = requests.get(url)
                     data = BeautifulSoup(r.text,"html.parser")
                     temp = data.find("div", class_ = "BNeawe").text
                     speak(f"current{search} is {temp}")


                     
                elif "weather" in query:
                     search = "temperature in rajula"
                     url = f"https://www.google.com/search?q={search}"
                     r  = requests.get(url)
                     data = BeautifulSoup(r.text,"html.parser")
                     temp = data.find("div", class_ = "BNeawe").text
                     speak(f"current{search} is {temp}")


                elif "the time" in query:
                      strTime = datetime.datetime.now().strftime("%H:%M")    
                      speak(f"Sir, the time is {strTime}")


                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,sir")


                elif "stop" in query:
                    pyautogui.press("k")
                    speak("video paused")

                elif "play" in query:
                     pyautogui.press("k")
                     speak("video played")

                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")

                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()
                    
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown() 


                elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                         os.system("shutdown /s /t 1")

                    elif shutdown == "no":
                         break



                elif "open" in query:   #EASY METHOD
                    query = query.replace("open","")
                    query = query.replace("jarvis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")  


                
                elif "internet speed" in query:
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}")


                
                