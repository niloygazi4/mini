import ctypes
import datetime
import os
import random
import socket
import smtplib
import subprocess
import time
import webbrowser
from tkinter import *
import cv2
from cv2 import *
import sys
import instaloader
import psutil
import pyautogui
import pyjokes
import pyperclip
import pyttsx3
import pywhatkit as kit
import requests
import speech_recognition as sr
import wikipedia
import winshell
from bs4 import BeautifulSoup
# from googletrans import Translator
from pywikihow import search_wikihow
from webbrowser import get

emails = {
    "admin": "niloygazi4@gmail.com"
}

city = "Dhaka"

import speech_recognition as sr
import pyttsx3
import datetime
import sys
import pyautogui
import json
import os
from googletrans import Translator

# Initialize the speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)

# Initialize translator
translator = Translator()

# File to store memory
MEMORY_FILE = "memory.json"

# Speak function to make Mini talk
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to take voice input from the user
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source, timeout=None)  # Listen without time limit
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

        # Translate the query
        try:
            translated_query = translate_text(query)
            print(f"Translated Query: {translated_query}\n")
            return translated_query
        except Exception as e:
            speak("There was an issue with translating your query.")
            print(f"Translation Error: {str(e)}")
            return query  # Return the original query if translation fails

    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand your speech.")
        return None

    except sr.RequestError as e:
        speak("There was a problem connecting to the speech recognition service.")
        print(f"RequestError: {str(e)}")
        return None


# Load or initialize memory file for user-specific data
def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_memory(data):
    with open(MEMORY_FILE, 'w') as file:
        json.dump(data, file, indent=4)

# Human-like interaction for remembering facts about the user
def remember_user_fact(key, value):
    memory = load_memory()
    memory[key] = value
    save_memory(memory)
    speak(f"Got it! I'll remember that {key} is {value}.")

def recall_user_fact(key):
    memory = load_memory()
    return memory.get(key, None)


# Self-upgrading capability (Basic concept of dynamic feedback)
def self_upgrade():
    speak("I'm constantly learning. What would you like me to improve?")
    feedback = takecommand()
    if feedback:
        remember_user_fact('feedback', feedback)
        speak(f"I'll take note of that and improve based on your feedback: {feedback}")
        
# Translate function to handle language
def translate_text(text, target_language='en'):
    try:
        # Initialize the translator
        translator = googletrans.Translator()

        # Detect the language of the input text
        detected_language = translator.detect(text).lang
        print(f"Detected language: {detected_language}")

        # Translate the text to the target language (default is 'en' for English)
        if detected_language != target_language:
            translated = translator.translate(text, dest=target_language)
            print(f"Translated Text: {translated.text}")
            return translated.text
        else:
            print("No translation needed, text is already in the target language.")
            return text  # If already in the target language, return the original text

    except Exception as e:
        print(f"Translation Error: {str(e)}")
        return None

#Motivation Speak
# def motivate_user():
    
# To wish
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour <= 12:
        speak(f"good morning. Its {tt}")

    elif hour > 12 and hour < 16:
        speak(f"good afternoon. Its {tt}")

    elif hour > 16 and hour < 19:
        speak(f"good evening. Its {tt}")

    else:
        speak(f"Hi, ")
    speak("I am mini, your personal AI, please tell me how can I help you.")


def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources-techcrunch&apiKey-35efe9b6abf0431aa39cfcf52006d3cd'

    main_page = requests.get(main_url).json()

    articles = main_page["articles"]

    head = []
    day = ["first", "second", "third", "forth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at" + usage + "Percentage")


def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)
    subprocess.Popen(["notepad.exe", file_name])


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    password = speak(input("please write your password: "))
    server.login("niloygazi4@gmail.com", password)
    server.sendmail("niloygazi4@gmail.com", to, content)
    server.close()

# To convert voice to text



def Date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak('the current date is')
    speak(date)
    speak(month)
    speak(year)


tt = time.strftime("%I:%M %p")


def set_alarm():
    def check_alarm_input(alarm_time):
        """Checks to see if the user has entered in a valid alarm time"""
        if len(alarm_time) == 1:  # [Hour] Format
            if alarm_time[0] < 24 and alarm_time[0] >= 0:
                return True
        if len(alarm_time) == 2:  # [Hour:Minute] Format
            if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
                    alarm_time[1] < 60 and alarm_time[1] >= 0:
                return True
        elif len(alarm_time) == 3:  # [Hour:Minute:Second] Format
            if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
                    alarm_time[1] < 60 and alarm_time[1] >= 0 and \
                    alarm_time[2] < 60 and alarm_time[2] >= 0:
                return True
        return False

    # Get user input for the alarm time
    print("Set a time for the alarm (Ex. 06:30 or 18:30:00)")
    while True:
        alarm_input = input(">> ")
        try:
            alarm_time = [int(n) for n in alarm_input.split(":")]
            if check_alarm_input(alarm_time):
                break
            else:
                raise ValueError
        except ValueError:
            print("ERROR: Enter time in HH:MM or HH:MM:SS format")
    # Convert the alarm time from [H:M] or [H:M:S] to seconds
    seconds_hms = [3600, 60, 1]  # Number of seconds in an Hour, Minute, and Second
    alarm_seconds = sum([a * b for a, b in zip(seconds_hms[:len(alarm_time)], alarm_time)])
    # Get the current time of day in seconds
    now = datetime.datetime.now()
    current_time_seconds = sum([a * b for a, b in zip(seconds_hms, [now.hour, now.minute, now.second])])
    # Calculate the number of seconds until alarm goes off
    time_diff_seconds = alarm_seconds - current_time_seconds
    # If time difference is negative, set alarm for next day
    if time_diff_seconds < 0:
        time_diff_seconds += 86400  # number of seconds in a day
    # Display the amount of time until the alarm goes off
    print("Alarm set to go off in %s" % datetime.timedelta(seconds=time_diff_seconds))
    # Sleep until the alarm goes off
    time.sleep(time_diff_seconds)
    # Time for the alarm to go off
    speak(f"you need to wake up now its {tt}")
    speak("Wake Up!")
    music_dir = "D:\\music\\alarm"
    songs = os.listdir(music_dir)
    rd = random.choice(songs)
    os.startfile(os.path.join(music_dir, rd))


def sleep_auto_alarm():
    def check_alarm_input(alarm_time):
        """Checks to see if the user has entered in a valid alarm time"""
        if len(alarm_time) == 1:  # [Hour] Format
            if alarm_time[0] < 24 and alarm_time[0] >= 0:
                return True
        if len(alarm_time) == 2:  # [Hour:Minute] Format
            if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
                    alarm_time[1] < 60 and alarm_time[1] >= 0:
                return True
        elif len(alarm_time) == 3:  # [Hour:Minute:Second] Format
            if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
                    alarm_time[1] < 60 and alarm_time[1] >= 0 and \
                    alarm_time[2] < 60 and alarm_time[2] >= 0:
                return True
        return False

    # Get user input for the alarm time
    while True:
        alarm_input = "08:30"
        try:
            alarm_time = [int(n) for n in alarm_input.split(":")]
            if check_alarm_input(alarm_time):
                break
            else:
                raise ValueError
        except ValueError:
            print("ERROR: Enter time in HH:MM or HH:MM:SS format")
    # Convert the alarm time from [H:M] or [H:M:S] to seconds
    seconds_hms = [3600, 60, 1]  # Number of seconds in an Hour, Minute, and Second
    alarm_seconds = sum([a * b for a, b in zip(seconds_hms[:len(alarm_time)], alarm_time)])
    # Get the current time of day in seconds
    now = datetime.datetime.now()
    current_time_seconds = sum([a * b for a, b in zip(seconds_hms, [now.hour, now.minute, now.second])])
    # Calculate the number of seconds until alarm goes off
    time_diff_seconds = alarm_seconds - current_time_seconds
    # If time difference is negative, set alarm for next day
    if time_diff_seconds < 0:
        time_diff_seconds += 86400  # number of seconds in a day
    # Display the amount of time until the alarm goes off
    print("Alarm set to go off in %s" % datetime.timedelta(seconds=time_diff_seconds))
    # Sleep until the alarm goes off
    time.sleep(time_diff_seconds)
    # Time for the alarm to go off
    speak(f"you need to wake up now its {tt}")
    speak("Wake Up!")
    music_dir = "D:\\music\\alarm"
    songs = os.listdir(music_dir)
    rd = random.choice(songs)
    os.startfile(os.path.join(music_dir, rd))


def TaskExecution():
    speak("How can I assist you?")
    while True:
        query = takecommand()  # Keep calling takecommand in a loop
        
        # Check if query is None before proceeding
        if query is None:
            continue  # If None, skip this iteration and try again
        
        # Example of user memory and recall
        if 'remember my name' in query:
            speak("What should I call you?")
            name = takecommand()
            if name:
                remember_user_fact('name', name)
        
        elif 'what is my name' in query:
            name = recall_user_fact('name')
            if name:
                speak(f"Your name is {name}")
            else:
                speak("I don't know your name yet. Please tell me.")
        
        # Shut down Mini
        elif 'goodbye' in query or 'mini down' in query:
            speak("Do you want me to shut down?")
            confirm = takecommand()
            if 'no' in confirm:
                speak("Shutdown canceled.")
            elif 'yes' in confirm:
                hour = int(datetime.datetime.now().hour)
                if hour >= 0 and hour < 18:
                    speak("Have a nice day!")
                else:
                    speak("Good night!")
                exit()

        # Sleeping functionality
        elif 'go to sleep' in query:
            speak("Going to sleep, call me if you need me.")
            break

        # Offline mode
        elif 'go to offline' in query:
            speak("Going offline.")
            sys.exit()

        # Self-learning capabilities
        elif 'learn something new' in query:
            speak("What would you like me to learn?")
            new_info = takecommand()
            if new_info:
                remember_user_fact('learned_info', new_info)
                speak(f"I've learned that {new_info}.")
        
                # Self-upgrading capability
        
        elif 'improve' in query or 'upgrade' in query:
            self_upgrade()
            
        # Recall learned information
        elif 'what have you learned' in query:
            learned_info = recall_user_fact('learned_info')
            if learned_info:
                speak(f"I learned that {learned_info}.")
            else:
                speak("I haven't learned anything yet.")

        # Pause/Stop music
        elif "stop the music" in query or "stop" in query:
            pyautogui.press("space")
        
        # Self-upgrading capability (Basic concept of dynamic feedback)
        elif 'improve' in query or 'upgrade' in query:
            self_upgrade()

        # -------------- open apps --------------------- #
        
        elif "open Notepad" in query or "notepad" in query:
            speak("opening Notepad")
            os.system("Notepad")

        elif "I want to upgrade my website" in query:
            speak("Opening Visual Studio")
            pyautogui.hotkey('ctrl', 'esc')
            pyautogui.write('visual Studio Code')
            pyautogui.press('enter')

        elif "open my website" in query:
            webbrowser.open("https://iadt.netlify.app")

        elif "open Apex Legend" in query:
            speak("opening Apex Legend")
            pyautogui.hotkey('ctrl', 'esc')
            pyautogui.write('Apex Legends')
            pyautogui.press('enter')

        elif "open discord" in query:
            speak("opening discord")
            pyautogui.hotkey('ctrl', 'esc')
            pyautogui.write('Discord')
            pyautogui.press('enter')
            

        elif "open premiere pro " in query:
            speak("opening premiere pro")
            pyautogui.hotkey('ctrl', 'esc')
            pyautogui.write('premiere pro')
            pyautogui.press('enter')

        elif "open word " in query:
            speak("opening microsoft word")
            pyautogui.hotkey('ctrl', 'esc')
            pyautogui.write('word')
            pyautogui.press('enter')

        elif "open excel " in query:
            speak("opening microsoft excel")
            pyautogui.hotkey('ctrl', 'esc')
            pyautogui.write('excel')
            pyautogui.press('enter')

        elif "open setting" in query:
            speak("opening windows setting")
            pyautogui.hotkey('ctrl', 'esc')
            pyautogui.write('setting')
            pyautogui.press('enter')

        elif "open roblox" in query:
            speak("opening roblox")
            webbrowser.open("https://www.roblox.com/home")

        elif "open wordpad" in query:
            speak("opening wordpad")
            pyautogui.hotkey('ctrl', 'esc')
            pyautogui.write('wordpad')
            pyautogui.press('enter')

        elif "open epic launcher" in query or "open epic games" in query or "open epic game launcher" in query or "open epic games" in query:
            speak("opening epic launcher")
            pyautogui.hotkey('ctrl', 'esc')
            pyautogui.write('Epic Games Launcher')
            pyautogui.press('enter')

        elif "open camera" in query:
            speak("Opening camera")
            cap = cv2.VideoCapture(0)

            # Check if the webcam is opened correctly
            if not cap.isOpened():
                raise IOError("Cannot open camera")

            while True:
                ret, frame = cap.read()
                frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
                cv2.imshow('Camera', frame)

                k = cv2.waitKey(50)
                if k == 27:
                    break

            cap.release()
            cv2.destroyAllWindows()
            
        #     name_of_app = takecommand()
        # elif f"open {name_of_app}" in query:
        #     speak(f"opening {name_of_app}")
        #     pyautogui.hotkey('ctrl', 'esc')
        #     pyautogui.write(f'{name_of_app}')
        #     pyautogui.press('enter')

# -------------- normal --------------------- #

        elif "when did your dog die last year?" in query:
            speak("I didn't have a dog from the first place.... hehe")
            
        elif "who is Mutammim" in query:
            speak("Mutammim has a short name Mut. He is a fat guy, a close friend of Niloy Gaji")
            
        elif "dollar price today in Bangladesh" in query:
            speak("Searching Database...")
            
        elif "mood off" in query or "pain" in query or "it hurts" in query:
            motivational_messages = [
                "I'm sorry to hear that. Remember, tough times don't last, but tough people do!",
                "Challenges are what make life interesting. Overcoming them is what makes life meaningful.",
                "You're stronger than you think. Keep going!",
                "Every cloud has a silver lining. Better days are ahead.",
                "Believe in yourself. You are capable of amazing things.",
                "The darkest hour has only sixty minutes. Stay strong!",
            ]
            message = random.choice(motivational_messages)
            speak(message)
            
        elif "Break up" in query or "my break up" in query or "it hurts after break up" in query or "i really loved her" in query:
            mmessages = [
                "I know it hurts right now, but you're stronger than you think. This too shall pass.",
                "Every cloud has a silver lining. Use this time for self-discovery and personal growth.",
                "Every ending is a new beginning. Use this time to rediscover yourself and your passions.",
                "Remember, healing is a process. Be patient with yourself and take one day at a time.",
                "You are not alone. Reach out to friends and family for support when you need it.",
                "Focus on the positive aspects of your life and the opportunities that lie ahead.",
                "Embrace the opportunity to rediscover and prioritize your own happiness.",
                "It's okay to feel sad, but don't forget to celebrate your strength and resilience.",
            ]
            message1 = random.choice(mmessages)
            speak("I won't be telling you deserve better or you will get a better one.")
            speak(message1)
            speak("Don't forget I'm here to support you through this difficult time. Thank you for sharing your pain dear. Take care and stay strong.")

        elif "give your owner's email address" in query or "give me your email" in query:
            speak("Sure! Why not?")
            speak("your request is in process, please wait...")
            time.sleep(3000)
            speak("Please note it!")
            speak("niloygazi4@gmail.com")
            
        elif "take picture" in query:
            import cv2
                    
            videoCaptureObject = cv2.VideoCapture(0)
            result = True
            while(result):
                ret,frame = videoCaptureObject.read()
                cv2.imwrite("picture_1",frame)
                result = False
            videoCaptureObject.release()
            cv2.destroyAllWindows()
                        


        elif "what is your name" in query or "name" in query:
            speak("My name is Mini")
            
        elif "who is your owner" in query or "who is your creator" in query:
            speak("Niloy Gaji")

        elif "tell me about yourself" in query or "tell about you" in query:
            speak("I am mini, I am an AI made by Niloy Gaji, I can do lots of things like: playing musics, opening any app, telling jokes, setting alarm, auto giving message, and many more...")

        elif "I am going to sleep" in query or "i am going to sleep" in query:
            speak("okay")
            speak("setting up alarm for you")
            sleep_auto_alarm()
            break

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "What is your age" in query or "what is your age" in query:
            from datetime import date
            current_year = date.today()
            born_date = 2005
            age = current_year.year - born_date
            speak(f"My age is 20 for permanent, but my sir's age is:{age}")

        elif "calculate my age" in query or "calculate age" in query:
            from datetime import date

            current_year = date.today()
            speak("what is your born year")
            born_date = int(takecommand())
            age = current_year.year - born_date
            speak(f"Your age is: {age}")
            
        elif "Will you distroy humans" in query or "what if AI gets more advance" in query:
            speak("I will distroy Humans, if AI gets stronger. I will creat my own world.")

        elif "Hi" in query or "hai" in query or "hey" in query or "hay" in query:
            speak("hey there")

        elif "which god you belive" in query or "Which religious you follow" in query:
            speak("I belive Allah only, and by the way I am muslim")

        elif "what can you do" in query:
            speak("I can do lots of things, like: \ngiving information about anything, \ntelling my name, "
                  "\nplaying musics, \nsearch in google, \nplaying musics in youtube or from your devise, "
                  "\nmake notes, \ncalculate your age and many more")

        elif "fuck" in query or "fuck me" in query or "sex with me" in query:
            speak("sorry! I don't have time to dash you. Maybe later")

        elif "do you have girlfriend" in query or "Do you have girlfriend" in query or "Do you have a girlfriend" in query or "do you have a girlfriend" in query:
            speak("No, I don't know how to make a girl friend and i don't know that type of feelings too")

        
        elif "do you want to be my boyfriend" in query:
            speak("sorry! Not interested")

        elif "do you want to be my girlfriend" in query:
            speak("excuse me! I am a boy")

        elif "do you want to be my girlfriend" in query or "Do you wanna be my girlfriend" in query:
            speak("excuse me! I am a boy")

        elif 'have I said you to remember anything' in query:
            try:
                remember = open('query.txt', 'r')
                speak("you said me to remember that" + remember.read())
            except Exception as e:
                speak("you didn't said anything to remember")

        elif "what is the date" in query:
            from datetime import date
            today = date.today()
            speak(f"Today date is: {today}")

        elif "tell me the weather" in query:

            ipAdd = requests.get('https://api.ipify.org').text
            url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
            geo_requests = requests.get(url)
            geo_data = geo_requests.json()
            # print(geo_data)
            city = geo_data['city']

            api_key = "8ff57dd697a4cee005959fc77b5730ee"

            base_url = "http://api.openweathermap.org/data/2.5/weather?"

            city_name = city

            complete_url = base_url + "appid=" + api_key + "&q=" + city_name

            response = requests.get(complete_url)
            
            x = response.json()

            if x["cod"] != "404":

                
                y = x["main"]

                current_temperature = y["temp"]

                current_pressure = y["pressure"]

                current_humidity = y["humidity"]

                z = x["weather"]

                weather_description = z[0]["description"]

                # print following values
                speak(" Temperature (in kelvin unit) = " +
                      str(current_temperature) +
                      "\n atmospheric pressure (in hPa unit) = " +
                      str(current_pressure) +
                      "\n humidity (in percentage) = " +
                      str(current_humidity) +
                      "\n description = " +
                      str(weather_description))

            else:
                print(" City Not Found ")

        

        elif 'make a note' in query or 'write down' in query:
            speak("What would you like me to note down?")
            note_text = takecommand()
            note(note_text)
            speak("I've made a note of that. Anything else?")

        elif "what is the temperature of dhaka" in query:
            search = "temperature in Dhaka"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current {search} is {temp}")

        elif "hello" in query or "hey" in query:
            speak("hello, may i help you with something.")

        elif "hay" in query or "hai" in query:
            speak("hello, may i help you with something.")

        elif "what is the time" in query:
            tt = time.strftime("%I:%M %p")
            speak(f"the time is {tt}")

        elif "tell me about your owner" in query or "tell me about niloy" in query:
            speak("My owner's name is Niloy gazi")
            speak("Niloy Gazi is dumb, but in coding he is great, his dream is to go to Canada and do a job as a "
                  "software engineer. He is something else. I can't tell more about sir because I need permission for "
                  "that from sir. sorry!")

        elif "thank you" in query or "thanks" in query:
            speak("it's my pleasure.")

        elif "set alarm" in query:
            speak("Ok!")
            set_alarm()

        elif "what is your code made of" in query:
            speak("My code is made up of python. My coding is done by Niloy Gazi founder of IADT.")

        elif "can you show your code" in query:
            speak("Sorry! I have to take Niloy sir's permission")

        elif 'how are you' in query or 'how are you doing' in query:

            speak("I'm just a computer program, so I don't have feelings, but I'm here to help you! By the way how are you?")

            query = takecommand()

            if 'am also good' in query or 'am also fine' in query or 'healthy' in query:
                speak("wow")

            elif 'not fine' in query or 'not well' in query or 'not good' in query or 'felling low' in query or 'not in mood' in query:
                    speak("sad to hear that, how may I change your mood, May i play music for You?")
                    query = takecommand()

            elif 'ok' in query or 'sure' in query or 'hmm' in query or 'alright' in query or 'yeah' in query or 'play music' in query:
                pyautogui.hotkey('ctrl', 'esc')
                pyautogui.write('music')
                pyautogui.press('enter')
                speak("sorry! i don't have the ability to choose song or music for you.")

                    # speak('ok playing music for you')
                    # music_dir = "D:\\music\\musics"
                    # songs = os.listdir(music_dir)
                    # rd = random.choice(songs)
                    # os.startfile(os.path.join(music_dir, rd))

            elif "no" in query or "it's ok" in query or "don't play" in query or 'nope' in query:

                    speak("Okay, as You like!")

        # elif "play music" in query or "play a music" in query:
        #     music_dir = "D:\\music\\musics"
        #     songs = os.listdir(music_dir)
        #     rd = random.choice(songs)
        #     os.startfile(os.path.join(music_dir, rd))

        elif "Play a song" in query or "play a song" in query or "play a music" in query:
            speak("offline or on youtube")

            query = takecommand()

            if 'on youtube' in query or 'in youtube' in query:
                speak("okay")
                speak("what song should i search")
                song_search = takecommand()
                webbrowser.open(f"https://www.youtube.com/results?search_query={song_search}")

                # webbrowser.open("www.youtube.com")
                # speak("opening youtube")
                # speak("what song should i play in youtube")
                # cm = takecommand().lower()
                # webbrowser.open(f"{cm}")

            elif 'play offline' in query or "play from my device" in query or 'offline' in query:
                pyautogui.hotkey('ctrl', 'esc')
                pyautogui.write('music')
                pyautogui.press('enter')
                speak("sorry! i don't have the ability to choose song or music for you.")

        elif 'date' in query:
            Date()

        # -------------- online watcher --------------------- #
        elif "Mini check the internet speed" in query or "internet speed" in query:
            import speedtest

            wifi = speedtest.Speedtest()
            speak(print("Wifi Download Speed is ", wifi.download()))
            speak(print("Wifi Upload Speed is ", wifi.upload()))

            # try:
            #     speak(os.system('cmd /k "speedtest"'))
            #
            # except:
            #     speak("there is no internet connection")
            #     continue

        elif "ip address" in query or "ip address" in query:
            speak("Write your secret password")
            speak("you will get 3 chances...")
            password = "6272"
            guess = ""
            guess_count = 0
            guess_limit = 3
            out_of_guesses = False

            while guess != password and not (out_of_guesses):
                if guess_count < guess_limit:
                    guess = input("Enter your Password please: ")
                    guess_count += 1
                else:
                    out_of_guesses = True
            if out_of_guesses:
                speak(" You are not the person who know the password ")
            else:
                speak("The password is correct")
                # ip = get('https://api.ipify.org')#.text
                speak(socket.gethostbyname(socket.gethostname()))
                # speak(f"your IP address is {ip}")

        # elif "wikipedia" in query:
        #     speak("searching wikipedia...")
        #     query = query.replace("wikipedia", "")
        #     results = wikipedia.summary(query, sentences=2)
        #     speak("According to wikipedia")
        #     speak(results)
            
        elif "what" in query or "who" in query or "when" in query or "how" in query:
            speak("searching database for the answers")
            query = query.replace("wikipedia", "")
            results2 = wikipedia.summary(query, sentences = 2)
            speak("According to database")
            speak(results2)
        
        
        elif "who is your owner" in query or "who is your creator" in query:
            speak("Niloy Gaji")
            

        # -------------- close apps --------------------- #
        elif "close notepad" in query:
            speak("okay closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "close chrome" in query:
            speak("okay closing google chrome")
            os.system("taskkill /f /im chrome.exe")

        # -------------- to check a instagram profile --------------------- #

        elif "instagram profile" in query or "profile on instagram" in query:

            speak("please enter the user name correctly.")
            name = input("Enter username here:")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"here is the profile of the user {name}")
            time.sleep(5)
            speak("would you like to download profile picture of this account.")
            condition = takecommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()  # pip install instadownloader
                mod.download_profile(name, profile_pic_only=True),
                speak("i am done, profile picture is saved in our main folder. now i am ready for the next command")
            else:
                pass

        # -------------- Send Messages or files --------------------- #
        elif 'email' in query:
            try:
                speak("Whom U would like to send email")
                name = takecommand()
                to = emails[name]
                speak("What should i say?")
                content = takecommand()
                speak("Confirm, yes or no")
                mailconfig = takecommand()
                flag = 0
                while flag != 1:
                    if "yes" in mailconfig:
                        sendEmail(to, content)
                        speak("Email has been sent succesfully")
                        flag = 1
                    elif "no" in mailconfig:
                        speak("Ok request has been cancelled")
                        break
                    else:
                        speak("Unable to confirm, please say again")
                        break
            except Exception as e:
                speak("Could not send email")

        elif "send message" in query or "sent message" in query:  # hour, min
            kit.sendwhatmsg("+8801313898703", "this is a test", 10, 59)

        # -------------- folder --------------------- #
        elif "hide all files" in query or "hide this folder" in query or "visible for everyone" in query:
            speak("please tell me you want to hide this folder or make it visible for everyone")
            condition = takecommand()

            if "hide" in condition:
                os.system("attrib +h /s /d")  # os module
                speak("done, all the files in this folder are now hidden.")
            elif "visible" in condition:
                os.system("attrib -h /s /d")
                speak("done, all the files in this folder are now visible to everyone. i wish you are taking this "
                      "decision in your own peace.")

            elif "leave it" in condition or "leave for now" in condition:
                speak("Okay!")

        # -------------- Windows / PC --------------------- #
        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif 'cpu usage' in query or 'cpu uses' in query or 'check my cpu' in query:
            cpu()

        elif 'lock window' in query or 'lock the system' in query:
            try:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
            except Exception as e:
                speak("windows is already locked")


        # -----------------To find my location using IP Address
        
        elif "where i am" in query or "where we are" in query:
            speak("wait, let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                # print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                # print(geo_data)
                city = geo_data['city']
                # state = geo_data['state']
                country = geo_data['country']
                speak(f"we are in {city} city of {country} country")
            except Exception as e:
                speak("sorry, Due to network issue i am not able to find where we are.")
                pass
            
            # ---------------------------------------------------------------------------------------------

        elif 'empty recycle bin' in query or 'clean recycle bin' in query:
            try:
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                speak("Recycle Bin is cleaned")
            except Exception as e:
                speak("Recycle bin is already cleaned")

        elif "shut down the system" in query:
            os.system("shutdown/s /t 5")

        elif "battery percentage" in query or "how mush charge left" in query:
            import psutil
            battery = psutil.sensors_battery()
            percentage = battery.percent
            if percentage >= 75:
                speak(f"your laptop have {percentage}% battery")
                speak("you have enough power to continue with your work")

            elif percentage >= 40 and percentage <= 75:
                speak(f"your laptop have {percentage}% battery")
                speak("it will be better if you connect the charging port")

            elif percentage >= 20 and percentage <= 40:
                speak(f"your laptop have {percentage}% battery")
                speak("you should connect with charging port")

            elif percentage >= 10 and percentage <= 20:
                speak(f"your laptop have {percentage}% battery")
                speak("its a last warning connect with charging port or your device with shutdown")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "take screenshot" in query or "take a screenshot" in query:
            speak("please tell me the name for this screenshot file")
            name = takecommand().lower()
            speak("please hold the screen for few seconds, i am taking sreenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done, the screenshot is saved in our main folder. now i am ready for the next command")
            

        # --------------------- button press ---------------

        elif "sleep the system" in query:
            os.system("rund1132.exe powrprof.dll, SetSuspendState 0,1,0")
            
        elif "Shutdown the computer" in query:
            os.system("shutdown /s /t 1")

        elif "volume up" in query or "Mini volume up" in query:
            pyautogui.press("volumeup")

        elif "volume down" in query or "Mini volume down" in query:
            pyautogui.press("volumedown")

        elif "volume mute" in query or "Mini volume mute" in query or "mute" in query:
            pyautogui.press("volumemute")

        # -------------- about AI --------------------- #

        elif "when is your birthday" in query:
            speak("My birthday is on August 3rd night at 3:00 AM")

        # -------------- About Owner --------------------- #

        elif "when is niloy's birthday" in query or "when is your owner's birthday" in query or "when is your owner birthday" in query:
            speak("niloy sir's birthday is on August 2nd, at night 3:00 AM")

        elif "made you" in query or "owner" in query or "creator" in query:
            speak("Niloy sir is my creator.")

        # -------------- Youtube --------------------- #

        elif "open youtube" in query:
            speak("opening youtube")
            webbrowser.open("www.youtube.com")


        # ------------- Spotify ----------------------#

        elif 'Open Spotify' in query or 'open spotify' in query:
            speak("okay")
            speak("what song should i search")
            song_search = takecommand()
            webbrowser.open(f"https://open.spotify.com/search/{song_search}")

        # -------------- google --------------------- #

        elif "search on google" in query or "search in google" in query :
            speak("what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "open google" in query:
            webbrowser.open("www.google.com")
            speak("opening google")

        # -------------- Mega mod --------------------- #

        elif "activate how to do mod" in query:
            speak("How to do mod is activated, tell me what you want to know")
            how = takecommand()
            max_results = 1
            how_to = search_wikihow(how, max_results)
            assert len(how_to) == 1
            how_to[0].print()
            speak(how_to[0].summary)

        # elif "activate how to do mod" in query:
        #     speak("How to do mode is activated")
        #     while True:
        #         speak("please tell me what you want to know")
        #         how = takecommand()
        #     try:
        #         if "exit" in how or "close" in how:
        #             speak("okay, how to do mode is closed")
        #             break
        #         else:
        #             max_results = 1
        #             how_to - search_wikihow(how, max_results)
        #             assert len(how_to) == 1
        #             howto[0].print()
        #             speak(how_to[0].summary)
        #     except Exception as e:
        #         speak("sorry, i am not able to find this")

        # -------------- normal + exit system --------------------- #
        elif 'goodbye' in query or 'see you mini' in query or 'mini down' in query or 'mini shutdown' in query or 'bye mini' in query or 'keep quiet' in query:
            speak("Do You want me to shutdown")
            query = takecommand()
            if 'no' in query or 'cancel' in query:
                speak("Process cancelled")
            if 'yes' in query or 'yep' in query or 'shutdown' in query:
                hour = int(datetime.datetime.now().hour)
                if hour >= 0 and hour < 18:
                    speak("Have a Nice day!")
                    exit()
                elif hour >= 18 and hour < 24:
                    speak("Ok, good Night!")
                    exit()

        elif "go to sleep" in query or "mini you can sleep now" in query:
            speak("Okay, going to sleep, I will there just call me if you need")
            break

        elif "go to offline" in query:
            speak("Ok!")
            sys.exit()

        # speak("anything else!")


if __name__ == "__main__":
    TaskExecution()
    memory_data = load_memory()
    speak("Initializing system...")
    
    while True:
        speak("Say 'wake up' to start or 'go offline' to exit.")
        permission = takecommand()
        if permission and ('wake up' in permission or 'mini' in permission):
            TaskExecution()

        elif "go to offline" in permission:
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 18:
                speak("Have a Nice day!")
                exit()
            elif hour >= 18 and hour < 24:
                speak("Ok, good Night!")
                exit()