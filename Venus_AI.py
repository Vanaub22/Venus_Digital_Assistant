#to create a personalized Digital Assistant using Python
# program developed by Anuvab Chakravarty
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)

#funstion to speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#function to greet the user
def greetings():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak('Good Morning Sir!')
    elif(hour>=12 and hour<16):
        speak('Good Afternoon Sir!')
    else:
        speak('Good Evening Sir!')
    speak('I am your Personalized Digital Assistant. How may I help you?')

#function to accept vocal commands from the user
def commandInput():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening intently...')
        r.pause_threshold=1 #period of silence after which it stops listening
        audio=r.listen(source)
    try:
        print('Recognizing...')
        query=r.recognize_google(audio,language='en-in')
        print(f'User said: {query}\n')
    except Exception as e:
        # print(e)
        print('Can you repeat that please...')
        return('Sorry...Unable to recognize command')
    return(query)

#the main function
if __name__=="__main__":
    greetings()
    while(True):
        query=commandInput().lower()
        #to search wikipedia
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=2)
            speak('Here\'s what I got Sir...')
            print(results)
            speak(results)
        #to open youtube.com
        elif 'open youtube' in query:
            speak('Opening youtube.com Sir...')
            webbrowser.open('youtube.com')
        #to open google.com
        elif 'open google' in query:
            speak('Opening google.com Sir...')
            webbrowser.open('google.com')
        #to tell the time
        elif 'the time' in query:
            time=datetime.datetime.now().strftime('%H:%M:%S')
            print(f'The time is {time}')
            speak(f'Sir, the time is {time}')
        #to open the application Virtual Studio Code
        elif 'open code' in query:
            codepath='"C:\\Users\\anucb\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"'
            os.startfile(codepath)
        #to exit
        elif 'shut up' in query or 'bye' in query or 'get lost' in query:
            speak('Thank you Sir! I am leaving...')
            exit(0)
        #introduction
        elif 'who are you' in query or 'what are you' in query:
            speak('I am Venus. Your personalized digital assistant.')

    


