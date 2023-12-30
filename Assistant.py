import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import os
import smtplib
import webbrowser

engine = pyttsx3.init('sapi5')  # for using the voice
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Kapil Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Kapil Sir!")
    else:
        speak("Good evening Kapil Sir!")
    speak("I am Mark. please tell me how can i help you!")


def takeCommand(): # it takes microphone input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said :{query}\n")

    except Exception as e:
        print("Exception ",e)
        speak("I think You are not Kapil Sir Please Say it again!")
        return "None"
    return query

def sendEmail(to,content): # this is the sending the email
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.login("kapilkatiyar590@gmail.com","Kapil@123")
    server.sendmail("kapilkatiyar590@gmail.com",to,content)
    server.close


if __name__  == "__main__":
    wishme()
   
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=6) #results = wikipedia.summary(query,sentences=2) add sentences line number of lines 
            speak("According to Wikipedia")
            speak(results)

        elif 'youtube' in query:
            speak("i am open youtube for you")
            webbrowser.open("youtube.com")

        elif 'google' in query:
            speak("i am open google for you")
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            speak("i am open stack over flow for you")
            webbrowser.open("stackoverflow.com")

        elif 'cricket score' in query:
            speak("i am open cricket score for you")
            webbrowser.open("https://www.cricbuzz.com/")

        elif 'play music' in query:
            music_dir = "E:\\python\\music\\"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")


        elif 'open chat gpt' in query:
            codepath = "F:\\ChatGPT.exe"
            os.startfile(codepath)

        elif 'how are you' in query:
            speak("I am Fine What about you kapil Sir")

        elif 'email to kapil' in query:
            try:
                speak("What should I say??")
                content = takeCommand()
                to = "Kapil.katiyar.8017@gmail.com"
                sendEmail(to,content)
                speak("Email has been send!")

            except Exception as e:
                print(e)
                speak("Sorry i try to send but i am not able to send the mail")

        elif 'close your program' in query:
            speak("Thnking you Kapil Sir for your valuable time!")
            exit(0)

        elif 'reboot' in query:
            speak("Do you want to rebot your System yes no")
            reboot = takeCommand()
            if 'yes' or 'yas' in reboot:
                print(reboot)
                speak("reboot the System!")
                os.system("shutdown /r /t 1")
            else:
                speak("Ok")

        elif 'shut down' in query:
            speak("Do you want to shut down your System yes no")
            shutdown = takeCommand()
            if 'yes' or 'yas' in shutdown:
                print(shutdown)
                speak("Shut Down the System!")
                os.system("shutdown /s /t 1")
            else:
                speak("Ok")




