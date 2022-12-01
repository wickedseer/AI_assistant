import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("It is " + time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("Today is")
    speak(day)
    speak(month)
    speak(year)


def greet():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon")
    elif hour >= 18:
        speak("Good evening")
    speak("I am your virtual assistant")
    speak("How can i help you?")


def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)
    except Exception as e:
        print(e)
        speak("I'm sorry, i cannot understand you, please speak again")

    return query


def sendEmail(to, msg):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('vridhi.ritesh.sachdev@gmail.com', 'Vridhi@123')
    server.sendmail('vridhi.ritesh.sachdev@gmail.com', to, msg)
    server.close()


def screenshot():
    img = pyautogui.screenshot()
    img.save("ss.png")


def CPU():
    usage = str(psutil.cpu_percent())
    speak("CPU is at" + CPU)
    battery = psutil.sensors_battery()
    speak("battery is at ")
    speak(battery.percent)


def jokes():
    speak(pyjokes.get_joke())


if __name__ == "__main__":
    greet()
    while True:
        query = command().lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'wikipedia' in query:
            speak("Searching ...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)

        elif 'search in chrome' in query:
            speak("What should i search?")
            chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            search = command().lower()
            wb.get(chromepath).open_new_tab(search + '.com')

        elif 'log out' in query:
            os.system("shutdown -l")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'remember that' in query:
            speak("What should i remember?")
            data = command().lower()
            speak("you said me to remember that" + data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()

        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak("you told me to remember that: "+remember.read())

        elif 'send email' in query:
            try:
                speak("What message do you want to send?")
                msg = command()
                to = 'sachdev.ritesh@gmail.com'
                sendEmail(to, msg)
                speak("Email sent succesfullly!")
            except Exception as e:
                print(e)
                speak("Cannot send email!")

        elif 'screenshot' in query:
            screenshot()
            speak("Screenshot done")

        elif 'cpu' in query:
            CPU()

        elif 'joke' in query:
            jokes()

        elif 'bye' in query:
            quit()
