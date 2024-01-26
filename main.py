import pyttsx3
import datetime
import wolframalpha
import sys
import webbrowser
import speech_recognition as sr 
import wikipedia 
import pyaudio

engine = pyttsx3.init()

'''len(voices)-1'''
client = wolframalpha.Client(' IL 61820-7237, USA')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio): 
    print('B Bot: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe ():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 10 and currentH < 3:
        speak('Hi!,Good Morning! Iam a Dream Bot. The time is',currentH)

    elif currentH >= 3 and currentH < 15:
        speak('Hi!,Good Afternoon!')

    elif currentH >= 15 and currentH !=19:
        speak('Hi!,Good Evening!') 

    elif currentH >= 19 and currentH !=10:
        speak('Good Night! It is night')
        speak ('May i help you?')
    
    else:
        print("finish")

greetMe()

speak('Hello Iam a Dream Bot ,How may I help you?')

def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        r.pause_threshold =  0.5
    try:
        query = r.recognize_google(audio).lower()
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry ! TRY Writing your command')
        query = str(input('Command: '))

    return query    

if __name__ == '__main__':

    while True:
    
        query = myCommand()
        query = query.lower()
    
    # Commands
        
        if 'hi' in query:
            speak('hi')

        elif 'how are you' in query:
            speak('iam all ways happy')

        elif 'good morning' in query:
            speak('same to!')

        elif 'good night' in query:
            speak('same to you!')

        elif 'good evining' in query:
            speak('same to you!')

        elif 'hello' in query:
            speak('hello')

    # Finished Commands
            
        else:
            query = query
            speak('Searching...')
            try:
                res = client.query(query)
                results = next(res.results).text
                speak('google says - ')
                speak('Got it.')
                speak(results)
                
            except:
                results = wikipedia.summary(query, sentences=2)
                speak('Got it.')
                speak('Searching!')
                speak(results)
    
        speak('Any Command!')

