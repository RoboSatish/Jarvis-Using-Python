import datetime
import subprocess
import pyttsx3
import speech_recognition as sr

# engine = pyttsx3.init()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    audio = ''
    with sr.Microphone() as source:
        print("Jarvis : Listening ... ")
        audio = r.listen(source, phrase_time_limit=5)
    print("Jarvis : Processing ... ")
    try:
        text = r.recognize_google(audio, language='en-US')
        print("Sir : ", text)
        return text

    except Exception as e:
        print("Error " + str(e))
        print("Jarvis : Sir, Could not understand you, PLease try again!")
        speak("Sir, Could not understand you, PLease try again!")
        return 0


def wishMe():
    hour = int(datetime.datetime.now().hour)
    Time = datetime.datetime.now().strftime("%I %M %p")
    # print(hour)
    # print(Time)
    if hour >= 6 and hour < 12:
        speak("Good Morning Sir")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir")

    elif hour >= 18 and hour < 24:
        speak("Good Evening Sir")

    else:
        speak("Good Night Sir")

    speak("The Time is {0}".format(Time))


def get_app(Q):
    if Q == "time":
        Time = datetime.datetime.now().strftime("%I %M %p")
        print(Time)
        speak(Time)
    elif Q == "notepad":
        speak("Opening Notepad")
        subprocess.call(['Notepad.exe'])
    elif Q == "calculator":
        speak("Opening Calculator")
        subprocess.call(['calc.exe'])
    elif Q == "stikynot":
        speak("Opening stikyNot")
        subprocess.call(['StikyNot.exe'])
    elif Q == "shell":
        speak("Starting Powershell for you")
        subprocess.call(['powershell.exe'])
    elif Q == "paint":
        speak("Enjoy Painting Sir")
        subprocess.call(['mspaint.exe'])
    elif Q == "cmd" or Q == "command prompt":
        speak("Command line Interface is Online")
        subprocess.call(['cmd.exe'])
    elif Q == "browser":
        speak("browser is Starting")
        subprocess.call(['C:\\Program Files\\Internet Explorer\\iexplore.exe'])
    elif "exit" in str(Q) or "bye" in str(Q) or "go" in str(Q) or "sleep" in str(Q):
        speak("Ok bye")
         #break
    else:
        print("Jarvis : Sorry Sir Try Again")
        engine.say("Sorry Sir Try Again")
        engine.runAndWait()

    return


if __name__ == '__main__':
    wishMe()
    while True:
        speak("Jarvis at your Service Sir. Please tell me how can I help You ")
        query = takecommand().lower()
        get_app(query)
