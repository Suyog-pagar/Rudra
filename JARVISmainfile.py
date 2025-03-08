

import random, pywhatkit, pyttsx3, datetime, sys, time, os, pyautogui, requests, serial
from PyQt5 import QtGui
from PyQt5.QtCore import QThread
import speech_recognition as sr
from PyQt5.QtWidgets import QApplication, QMainWindow
from bs4 import BeautifulSoup
from jarvisChitChat import jarvyChatBot
from JARVISmainfileGUI import Ui_JARVISmainUI
from langdetect import detect
from googletrans import Translator
import math


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 175)
temp = False


.32

def googlesearch(self, query):
    query = query.replace("search", "")
    query = query.replace("google", "")
    query = query.replace("on google", "")

    URL = f"https://www.google.com/search?q=" + query
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    info = requests.get(URL, headers=headers)
    soupify = BeautifulSoup(info.content, 'html.parser')    
    results = soupify.find_all('div', class_='wvKXQ').get_txt()
    ui.terminalPrint(results)
    speak(results)





def speak(audio):
    ui.updateMoviesDynamically("speaking")
    engine.say(audio)
    engine.runAndWait()


def wishing():
    ui.updateMoviesDynamically("loading")
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        ui.terminalPrint("Rudra says ->: Good Morning BOSS")
        speak("Good Morning BOSS")
    elif 12 <= hour < 17:
        ui.terminalPrint("Rudra says ->: Good Afternoon BOSS")
        speak("Good Afternoon BOSS")
    elif 17 <= hour < 21:
        ui.terminalPrint("Rudra says ->: Good Evening BOSS")
        speak("Good Evening BOSS")
    else:
        ui.terminalPrint("Rudra says ->: Good Night BOSS")
        speak("Good Night BOSS")



def playSong():
    from os import startfile, listdir, path
    from random import choice
    songsPath = "gui_tools\\audio lib"
    songsList = listdir(songsPath)
    songName = choice(songsList)
    songName = songName.lstrip(".mp3")
    startfile(path.join(songsPath, songName))
    ui.jarvisPrint(f"Playing {songName[:20]}")
    speak(f"Playing {songName}")


def wakeUpCommands():
    ui.updateMoviesDynamically("sleeping")
    ui.terminalPrint("Rudra is Sleeping...")
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 0.5
            r.adjust_for_ambient_noise(source,duration=0.5)
            audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-in')
            ui.terminalPrint(f"You just said: {query}\n")
        except:
            query = "none"
        if "wake up" in query:
            break


class jarvisCodingClass(QThread):
    def __init__(self):
        super(jarvisCodingClass, self).__init__()
        self.fanStatus = True
        self.lightStatus = True
        self.isIronHomeConnected = self.ConnectIronHome()


    def run(self):
        if self.isIronHomeConnected:
           ui.UpdateIronHomeLabels("ironHomeONLINE")
        else:
           ui.UpdateIronHomeLabels("ironHomeOFFLINE")
        self.executeJARVIS()


    def filterTheQueryForSpecificWord(self, queryToBeFiltered):
        queryToBeFiltered = queryToBeFiltered.replace("rudra",'')
        query = queryToBeFiltered.replace("Rudra",'')
        query = query.replace("hey",'')
        query = query.replace("can",'')
        query = query.replace("please",'')
        query = query.replace("bro",'')
        query = query.replace("pro",'')
        query = query.replace("baba",'')
        query = query.replace("Rudra",'')
        query = query.replace("ok",'')
        query = query.replace("now",'')
        query = query.replace("you",'')
        query = query.replace("no",'')
        query = query.replace("the",'')
        query = query.replace("to",'')
        query = query.replace("do",'')
        query = query.replace("this",'')

        return query

    def listenWithoutFilter(self):
        ui.updateMoviesDynamically("listening")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            ui.terminalPrint("Listening...")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)
        try:
            ui.terminalPrint("Wait for few Moments..")
            ui.updateMoviesDynamically("loading")
            self.query = r.recognize_google(audio, language='en-in')
            ui.terminalPrint(f"You just said: {self.query}")
            ui.terminalPrint("")
        except:
            ui.terminalPrint("Please tell me again")
            speak("Please tell me again")
            self.query = ""

        return self.query

    def listen(self):
        ui.updateMoviesDynamically("listening")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            ui.terminalPrint("Listening...")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)
        try:
            ui.terminalPrint("Wait for few Moments..")
            ui.updateMoviesDynamically("loading")
            self.query = r.recognize_google(audio, language='en-in')
            ui.terminalPrint(f"You just said: {self.query}")
            ui.terminalPrint("")
            self.query = self.query.lower()
            self.query = self.query.replace("Rudra", "")
            self.query = self.query.replace("rudra", '')
            self.query = self.query.replace("hey", '')
            self.query = self.query.replace("can", '')
            self.query = self.query.replace("please", '')
            self.query = self.query.replace("bro", '')
            self.query = self.query.replace("pro", '')
            self.query = self.query.replace("baby", '')
            self.query = self.query.replace("Rudra", '')

        except:
            ui.terminalPrint("Please tell me again")
            speak("Please tell me again")
            self.query = ""

        return self.query


    def minimise(self):
        pyautogui.hotkey('win', 'down')
        pyautogui.hotkey('win', 'down')
        ui.jarvisPrint("Recent window was minimised sir")
        speak("Recent window was minimised sir")
    def maximise(self):
        pyautogui.hotkey('win', 'up')
        pyautogui.hotkey('win', 'up')
        ui.jarvisPrint("Recent window was maximised sir")
        speak("Recent window was maximised sir")

    def filterAndType(self, searchQuery):
        try:
            filteredQuery = searchQuery.replace("search", "")
            filteredQuery = filteredQuery.replace("please", "")
            filteredQuery = filteredQuery.replace("google", "")
        except:
            filteredQuery = searchQuery
            print("filter error")
        time.sleep(0.5)
        pyautogui.write(filteredQuery)
        time.sleep(0.5)

    def ConnectIronHome(self):
        print("Connecting Smart Home")
        try:
            self.serialCom = serial.Serial('COM10', 9600, timeout=1)
            print("Smart Home Online")
            isIronHomeConnected = True
            temp = True
            self.serialCom.write(b'j')
        except:
            print("Bluetooth not connected")
            temp = False
            isIronHomeConnected = False

        return isIronHomeConnected

    def LightSwitch(self, lightStatus):
        try:
            if lightStatus:
                self.serialCom.write(b'b')
                self.lightStatus = True
                ui.UpdateIronHomeLabels("lightON")
            elif not lightStatus:
                self.serialCom.write(b'a')
                self.lightStatus = False
                ui.UpdateIronHomeLabels("lightOFF")
        except:
            speak("Unable to Switch Fan Sir")

    def FanSwitch(self, fanStatus):
        try:
            if fanStatus:
                self.serialCom.write(b'd')
                self.fanStatus = True
                ui.UpdateIronHomeLabels("fanON")
            elif not fanStatus:
                self.serialCom.write(b'c')
                self.fanStatus = False
                ui.UpdateIronHomeLabels("fanOFF")
        except:
            speak("Unable to Switch Fan Sir")

    def executeJARVIS(self):
        # wakeUpCommands()


        wishing()
        while True:
            self.query = self.listen()
            if self.query:
                self.commands()
            else:
                pass

    def commands(self):

        if 'time' in self.query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            ui.jarvisPrint(f"Sir, the Time is {strTime}")
            speak(f"Sir, the Time is {strTime}")
        elif self.query == 'exit program' or self.query == 'exit the program' or self.query == 'exit':
            ui.jarvisPrint("I'm Quiting sir. BYEE!")
            speak("I'm Quiting sir. BYEE!")
            ui.jarvisPrint("Program quited")
            ui.close()
        elif 'wikipedia' in self.query:
            wikiQuery = self.query
            speak("Searching in Wikipedia")
            try:
                ui.updateMoviesDynamically("loading")
                from wikipedia import summary
                filteredQuery = wikiQuery.replace("wikipedia", "")
                results = summary(filteredQuery, sentences=1)
                speak("According to Wikipedia,")
                ui.jarvisPrint(results)
                speak(results)
            except Exception as e:
                ui.jarvisPrint(e)
                speak("No Results found Sir...")
                ui.jarvisPrint("No results Found sir")
        elif self.query == 'play music' or self.query == 'put some music' or 'music' in self.query or 'song' in self.query:
            speak("Yes sir, as you wish")
            ui.jarvisPrint("Yes sir, as you wish")
            playSong()
            while True:
                query = self.listen().lower()
                if "change" in query or "next" in query or "forward" in query:
                    speak("Changing song")
                    ui.jarvisPrint("changing song")
                    playSong()
                elif "stop" in query or "exit" in query:
                    pyautogui.hotkey('alt', 'f4')
                    speak("Music turned off")
                    ui.jarvisPrint("Music turned off")
                    speak("Seems like you're out of mood now")
                    ui.jarvisPrint("Seems like you're out of mood now")
                    break
                elif "pause" in query or "play" in query or 'pass' in query:
                    pyautogui.press('space')
                elif 'mute' in query or 'sleep' in query:
                    ui.jarvisPrint("I'm going to sleep sir")
                    speak("I'm going to sleep sir")
                    wakeUpCommands()
                    break
                else:
                    pass
        elif self.query == "mute" or self.query == "sleep" or 'go to sleep' in self.query or 'mute' in self.query:
            ui.jarvisPrint("I'm going to sleep sir")
            speak("I'm going to sleep sir")
            wakeUpCommands()
        elif 'close this tab' in self.query or 'exit this tab' in self.query or 'close the tab' in self.query or 'exit the tab' in self.query:
            pyautogui.hotkey('ctrl', 'w')
            ui.jarvisPrint("Recent tab was closed sir")
            speak("Recent tab was closed sir")
        elif 'close this window' in self.query or 'exit this window' in self.query or 'close the window' in self.query or 'exit the window' in self.query or 'close all window' in self.query:
            pyautogui.hotkey('alt', 'f4')
            ui.jarvisPrint("Recent window was closed sir")
            speak("Recent window was closed sir")
        elif 'minimise this window' in self.query or 'minimise this window' in self.query or 'minimise the window' in self.query or 'minimise the window' in self.query\
                or 'minimize this window' in self.query or 'minimize this window' in self.query or 'minimize the window' in self.query or 'minimize the window' in self.query:
            self.minimise()
        elif 'minimize all windows' in self.query:
            pyautogui.hotkey('win', 'd')
            ui.jarvisPrint("All windows are minimised sir")
            speak("All windows are minimised sir")
        elif 'maximise this window' in self.query or 'maximise this window' in self.query or 'maximise the window' in self.query or 'maximise the window' in self.query \
                or 'maximize this window' in self.query or 'maximize this window' in self.query or 'maximize the window' in self.query or 'maximize the window' in self.query:
            self.maximise()
        elif self.query.startswith('open'):
            query = self.query.replace("open", "")
            query = query.replace("my","")
            query = query.replace("for me", "")
            ui.jarvisPrint(f"Opening {query}")
            speak(f"Opening {query}")
            pyautogui.hotkey('win', 's')
            time.sleep(0.2)
            pyautogui.write(query)
            pyautogui.press('enter')
            ui.jarvisPrint("It's on your screen sir")
            speak("It's on your screen sir")
        elif 'google' in self.query or 'browse' in self.query or 'browser' in self.query or 'search' in self.query:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
            ui.jarvisPrint("What should I search sir...")
            speak("What should I search sir...")
            browserQuery = self.listen().lower()
            if 'close this tab' in browserQuery or 'exit this tab' in browserQuery or 'close the tab' in browserQuery or 'exit the tab' in browserQuery:
                pyautogui.hotkey('ctrl', 'w')
                speak("closing browser sir")
            elif 'close this window' in browserQuery or 'exit this window' in browserQuery or 'close the window' in browserQuery or 'exit the window' in browserQuery or 'close all window' in browserQuery:
                pyautogui.hotkey('alt', 'f4')
            elif "minimise" in browserQuery or "minimize" in browserQuery:
                pyautogui.hotkey('win', 'down', 'down')
            elif "maximise" in browserQuery or "maximize" in browserQuery:
                pyautogui.hotkey('win', 'up', 'up')
            else:
                self.filterAndType(browserQuery)
                pyautogui.press('enter')
                ui.jarvisPrint("Here's what I found!")
                speak("Here's what I found!")
        elif 'screenshot' in self.query or 'screen shot' in self.query:
            pyautogui.hotkey('win', 'alt', 'prtsc')
            ui.jarvisPrint("Screenshot saved sir")
            speak("Screenshot saved sir")
        elif 'joke' in self.query:
            from pyjokes import get_joke
            from jarvisChitChat import jokeReplyQuery
            ui.jarvisPrint("Yes sir")
            speak("Yes sir")
            joke = get_joke('en')
            ui.jarvisPrint(joke)
            speak(joke)
            reply = random.choice(jokeReplyQuery)
            ui.jarvisPrint(reply)
            speak(reply)
        elif 'location' in self.query or 'find me' in self.query:
            ui.jarvisPrint("Fetching details sir")
            speak("Fetching details sir")
            ipAdd = requests.get('https://api.ipify.org').text
            url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
            locDetails = requests.get(url)
            locDetails2 = locDetails.json()
            city = locDetails2['city']
            state = locDetails2['region']
            country = locDetails2['country']
            ui.jarvisPrint(f" Sir, You're in {city} city which is inside {state} State of {country} country")
            speak(f" Sir, You're in {city} city which is inside {state} State of {country} country")

        elif 'youtube' in self.query and 'play' in self.query:
            try:
                filQuery = self.query.replace("play", "")
                filQuery = filQuery.replace("youtube", "")
                filQuery = filQuery.replace("go to", "")
                filQuery = filQuery.replace("and", "")
            except:
                filQuery = self.query
            ui.jarvisPrint(f"Playing{filQuery}")
            speak(f"Playing{filQuery}")
            pywhatkit.playonyt(self.query)
        elif 'write a note' in self.query or 'notepad' in self.query:
            os.startfile("C:\\Windows\\system32\\notepad.exe")
            speak("Opened Notepad application sir")
            speak("Please dictate me what should I write")
            while True:
                query = self.listenWithoutFilter()
                pyautogui.write(query)
                filteredQuery = self.filterTheQueryForSpecificWord(self.query)
                if self.query.startswith('exit') or self.query.startswith('stop') or self.query.startswith('close'):
                    speak('okay sir')
                    pyautogui.hotkey('ctrl', 'w')
                    pyautogui.press('tab')
                    pyautogui.press('enter')
                    break
                elif 'save' in filteredQuery:
                    pyautogui.hotkey('ctrl', 's')
                    currTime = datetime.datetime.now().strftime("%H:%M:%S")
                    fileName = str(currTime).replace(":","-") + ".jarvis.txt"
                    time.sleep(0.4)
                    pyautogui.write(fileName)
                    pyautogui.press('enter')
                    ui.jarvisPrint("file Saved successfully sir")
                    speak("file Saved successfully sir")
                    break
        elif 'weather' in self.query or 'climate' in self.query:
            from weatherAPI import weatherCheck
            try:
                temp, tempFeelsLike, hum, pressure, weatherReport, wind = weatherCheck()
                ui.jarvisPrint(f"The temperature is around {temp} Degree celsius")
                speak(f"The temperature is around {temp}")
            except:
                ui.jarvisPrint("Sorry sir. Error while performing weather update")
                speak("Sorry sir. Error while performing weather update")
        elif self.query.startswith('type'):
            self.query.replace('type', '')
            pyautogui.write(self.query)

        elif 'light on' in self.query or 'lights on' in self.query or 'turn on light' in self.query:
            if self.isIronHomeConnected:
                self.LightSwitch(True)
                speak("Lights are ON sir")
            else:
                speak("Iron Home offline sir")

        elif 'light off' in self.query or 'lights off' in self.query or 'turn off light' in self.query:
            if self.isIronHomeConnected:
                self.LightSwitch(False)
                speak("Lights are OFF sir")
            else:
                speak("Iron Home offline sir")

        elif 'fan on' in self.query or 'turn fan on' in self.query or 'turn on fan' in self.query:
            if self.isIronHomeConnected:
                self.FanSwitch(True)
                speak("Fan ON sir")
            else:
                speak("Iron Home offline sir")

        elif 'fan off' in self.query or 'turn fan off' in self.query or 'turn off fan' in self.query:
            if self.isIronHomeConnected:
                self.FanSwitch(False)
                speak("Fan OFF sir")
            else:
                speak("Iron Home offline sir")

        elif 'connect' in self.query:
            speak("Connecting Iron Home")
            self.ConnectIronHome()
            if self.isIronHomeConnected:
                speak("Iron Home Online")
            else:
                speak("Unable to Connect Sir")

        else:
            if self.query == "":
                pass
            else:
                chatting = jarvyChatBot(self.query)
                ui.jarvisPrint(chatting)
                speak(chatting)



# Assuming self.speak and self.listenWithoutFilter are defined elsewhere in your class
def paint_feature(self):
    try:
        # Open Microsoft Paint
        os.startfile("C:\\Windows\\system32\\mspaint.exe")
        self.speak("Opened Microsoft Paint. Let me know what to draw.")
        time.sleep(1)  # Allow Paint to open fully

        def draw_circle(center_x, center_y, radius, steps=100):
            self.speak("Drawing a circle.")
            pyautogui.moveTo(center_x + radius, center_y)
            pyautogui.mouseDown()

            for i in range(steps + 1):
                angle = (2 * math.pi / steps) * i
                x = center_x + radius * math.cos(angle)
                y = center_y + radius * math.sin(angle)
                pyautogui.moveTo(x, y, duration=0.01)

            pyautogui.mouseUp()
            self.speak("Circle completed.")

        def clear_canvas():
            self.speak("Clearing the canvas.")
            pyautogui.hotkey('ctrl', 'a')  # Select all
            pyautogui.press('delete')  # Delete everything

        def save_drawing():
            self.speak("Saving your drawing.")
            pyautogui.hotkey('ctrl', 's')
            curr_time = datetime.datetime.now().strftime("%H-%M-%S")
            file_name = f"{curr_time}.jarvis-paint.png"
            time.sleep(0.5)  # Wait for the save dialog to open
            pyautogui.write(file_name)
            pyautogui.press('enter')
            self.speak(f"Your drawing has been saved as {file_name}.")

        while True:
            query = self.listenWithoutFilter().lower()

            if 'draw a circle' in query:
                draw_circle(center_x=600, center_y=400, radius=100)

            elif 'clear' in query:
                clear_canvas()

            elif 'save' in query:
                save_drawing()
                break

            elif 'exit' in query or 'close' in query:
                self.speak("Closing Paint.")
                pyautogui.hotkey('alt', 'f4')  # Close Paint
                break

            else:
                self.speak("I didn't understand. Please repeat.")

    except FileNotFoundError:
        self.speak("It seems Microsoft Paint is not installed on your system.")

    except Exception as e:
        self.speak(f"An error occurred: {str(e)}")







jarvisBackend = jarvisCodingClass()


class Ui_JARVIS(QMainWindow):
    def __init__(self):
        super(Ui_JARVIS, self).__init__()
        self.jarvisui = Ui_JARVISmainUI()
        self.jarvisui.setupUi(self)

        self.jarvisui.exitButton.clicked.connect(self.close)
        self.jarvisui.enterButton.clicked.connect(self.manuallyCoded)
        self.runallMovies()


    def terminalPrint(self, text):
        self.jarvisui.terminalOutputBox.appendPlainText(text)

    def terminalPrintUserInput(self, text):
        self.jarvisui.terminalOutputBox.appendPlainText(f">>> {text}")

    def jarvisPrint(self, text):
        self.jarvisui.terminalOutputBox.appendPlainText(f"Rudra says ->: {text}")

    def manuallyCoded(self):
        if self.jarvisui.terminalInputBox.text():
            var = self.jarvisui.terminalInputBox.text()
            self.jarvisui.terminalInputBox.clear()
            self.terminalPrintUserInput(var)
            if var == "Exit":
                ui.close()
            elif var == "help":
                self.terminalPrint("I can perform various tasks which is programmed inside me by IT Students.\n"
                                   "Examples are: Time, Wikipedia, Play music, minimize/maximize/close windows, open any system applications,"
                                   " Google search, screenshot, Joke, Play YouTube video, type anything you say, Sleep well or else i'll chit chat")
            elif var == "features":
                self.terminalPrint("Time, Wikipedia, Play music, minimize/maximize/close windows, open any system applications,"
                                   " Google search, screenshot, Joke, Play YouTube video, type anything you say, Sleep well or else i'll chit chat")
            elif var == 'exit':
                self.terminalPrint("Quiting")
                self.close()

            else:
                pass


    def updateMoviesDynamically(self, state):
        if state == "speaking":
            self.jarvisui.jarvisSpeakingLabel.raise_()
            self.jarvisui.smartHomeFrame.raise_()
            self.jarvisui.jarvisSpeakingLabel.show()    #
            self.jarvisui.listeningLabel.hide()
            self.jarvisui.jarvisLoadingLabel.hide()
            self.jarvisui.sleepingLabel.hide()
        elif state == "listening":
            self.jarvisui.listeningLabel.show()    #
            self.jarvisui.listeningLabel.raise_()
            self.jarvisui.smartHomeFrame.raise_()
            self.jarvisui.jarvisSpeakingLabel.hide()
            self.jarvisui.jarvisLoadingLabel.hide()
            self.jarvisui.sleepingLabel.hide()
        elif state == "loading":
            self.jarvisui.jarvisLoadingLabel.show()
            self.jarvisui.jarvisLoadingLabel.raise_()
            self.jarvisui.smartHomeFrame.raise_()
            self.jarvisui.jarvisSpeakingLabel.hide()
            self.jarvisui.listeningLabel.hide()
            self.jarvisui.sleepingLabel.hide()
        elif state == "sleeping":
            self.jarvisui.sleepingLabel.raise_()
            self.jarvisui.smartHomeFrame.raise_()
            self.jarvisui.sleepingLabel.show()
            self.jarvisui.listeningLabel.hide()
            self.jarvisui.jarvisSpeakingLabel.hide()
            self.jarvisui.jarvisLoadingLabel.hide()


        else:
            pass

    def runallMovies(self):

        self.jarvisui.listeningMovie = QtGui.QMovie("gui_tools\\listening.gif")
        self.jarvisui.listeningLabel.setMovie(self.jarvisui.listeningMovie)
        self.jarvisui.listeningMovie.start()

        self.jarvisui.speakingMovie = QtGui.QMovie("gui_tools\\speaking.gif")
        self.jarvisui.jarvisSpeakingLabel.setMovie(self.jarvisui.speakingMovie)
        self.jarvisui.speakingMovie.start()

        self.jarvisui.arcMovie = QtGui.QMovie("gui_tools\\techcircle.gif")
        self.jarvisui.arcLabel.setMovie(self.jarvisui.arcMovie)
        self.jarvisui.arcMovie.start()

        self.jarvisui.backgroundMovie = QtGui.QMovie("gui_tools\\background-cropped.gif")
        self.jarvisui.backgroundgifLabel.setMovie(self.jarvisui.backgroundMovie)
        self.jarvisui.backgroundMovie.start()

        self.jarvisui.loadingMovie = QtGui.QMovie("gui_tools\\tech loading-cropped.gif")
        self.jarvisui.jarvisLoadingLabel.setMovie(self.jarvisui.loadingMovie)
        self.jarvisui.loadingMovie.start()

        self.jarvisui.sleepingMovie = QtGui.QMovie("gui_tools\\sleepmode.gif")
        self.jarvisui.sleepingLabel.setMovie(self.jarvisui.sleepingMovie)
        self.jarvisui.sleepingMovie.start()

        self.jarvisui.ironHomeReactorMOVIE = QtGui.QMovie(
            "E:\\CODING\\Artificial_Intelligence\\Ultimate JARVIS with GUI YT  Playlist files\\gui_tools\\smarthomereactor.gif")
        self.jarvisui.ironHomeReactorLabel.setMovie(self.jarvisui.ironHomeReactorMOVIE)
        self.jarvisui.ironHomeReactorMOVIE.start()

        jarvisBackend.start()

    def UpdateIronHomeLabels(self, status):
        if status == "lightON":
            self.jarvisui.IHLightsONLabel.show()
            self.jarvisui.IHLightsOFFLabel.hide()
            self.jarvisui.IHLightsON.show()
            self.jarvisui.IHLightsOFF.hide()
        elif status == "lightOFF":
            self.jarvisui.IHLightsONLabel.hide()
            self.jarvisui.IHLightsOFFLabel.show()
            self.jarvisui.IHLightsON.hide()
            self.jarvisui.IHLightsOFF.show()
        elif status == "fanON":
            self.jarvisui.IHFanONLabel.show()
            self.jarvisui.IHFanOFFLabel.hide()
            self.jarvisui.IHFanON.show()
            self.jarvisui.IHFanOFF.hide()
        elif status == "fanOFF":
            self.jarvisui.IHFanONLabel.hide()
            self.jarvisui.IHFanOFFLabel.show()
            self.jarvisui.IHFanON.hide()
            self.jarvisui.IHFanOFF.show()
        elif status == "ironHomeONLINE":
            self.jarvisui.smartHomeFrame.raise_()
            self.jarvisui.IHOnlineLabel.show()
            self.jarvisui.IHOfflineLabel.hide()
            self.jarvisui.IHLightsON.show()
            self.jarvisui.IHLightsOFF.hide()
            self.jarvisui.IHFanON.show()
            self.jarvisui.IHFanOFF.hide()
            self.jarvisui.IHLightsONLabel.show()
            self.jarvisui.IHLightsOFFLabel.hide()
            self.jarvisui.IHFanOFFLabel.show()
            self.jarvisui.IHFanOFFLabel.hide()
        elif status == "ironHomeOFFLINE":
            self.jarvisui.smartHomeFrame.raise_()
            self.jarvisui.IHOfflineLabel.show()
            self.jarvisui.IHOnlineLabel.hide()
            self.jarvisui.IHLightsON.hide()
            self.jarvisui.IHLightsOFF.show()
            self.jarvisui.IHFanON.hide()
            self.jarvisui.IHFanOFF.show()
            self.jarvisui.IHLightsONLabel.hide()
            self.jarvisui.IHLightsOFFLabel.hide()
            self.jarvisui.IHFanONLabel.hide()
            self.jarvisui.IHFanOFFLabel.hide()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Ui_JARVIS()
    ui.show()
    sys.exit(app.exec_())
