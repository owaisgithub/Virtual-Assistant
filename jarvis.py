import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir!")

    elif hour >= 12 and hour < 18:
        speak('Good Afternoon sir!')

    else:
        speak('Good Evening sir!')

    speak("I am cluster")

def takeCommond():
    # It takes microphone input form the user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n ")

    except Exception as e:
        print(e)

        exit()
        # print('Say that again please')
        return 'None'
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('owais.mfos@gmail.com', '1223314142')
    server.sendmail('owais.mfos@gmail.com', to , content)
    server.close()


if __name__ == '__main__':
    wishMe()
    takeCommond()

   # while True:
    if 1:
        query = takeCommond().lower()

        # Logic for executing tasks based on query.
        if 'wikipedia' in query:
            speak('Searching wikipedia....')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            print(results)
            speak(results)

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'play music' in query:
            music_dir = 'D:\\your dir path'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'sir the time is {strTime}')
            print(strTime)

        elif 'open code' in query:
            codePath = "C:\\Users\\Owais Ansari\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open chrome' in query:
            codePath = '"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"'
            os.startfile(codePath)

        elif 'send email to sohail' in query:
            try:
                speak('sir, what content whould you like to send')
                content = takeCommond()
                to = 'owais.net655@gmail.com'
                #sentEmail(to, content)
                speak('Email has been sent!')
            except Exception as e:
                print(e)
                speak('sir email has not been sent, I think some problem there.')

        elif 'shut down' in query:
            speak('cluster is quiting')
            exit()

