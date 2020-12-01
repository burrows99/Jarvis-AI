import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowserim
import os
import pywhatkit

#initializing voice settings
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if(hour>=3 and hour<12):
        return('Good morning')
    elif(hour>=12 and hour<16):
        return("Good afternoon")
    else:
        return("Good evening")
def takeCommand():
    query=''
    while(query==''):
        r=sr.Recognizer() #recognizes audio
        with sr.Microphone() as Source:
            print("Listening...")
            r.pause_threshold=1 #not important....if pause is more than 1 sec it completes the phrase.
            audio=r.listen(Source)
        try:
            os.system('cls||clear')
            print('Recognizing...')
            query=r.recognize_google(audio,language='en-in')
            os.system('cls||clear')
        except Exception:
            #speak('Sorry. I did not undertsand')
            query=''
            os.system('cls||clear')
    return(query)
#functions to shorten code
def indices(a,c):
    for i in range(len(a)):
        if(a[i]==c):
            ans=i
            break
        else:
            ans=-1
    return(ans)
def openwebsite(query):
    Query=query.split()
    x=indices(Query,'open')
    website=Query[x+1]
    webbrowser.open('https://'+str(website)+'.com')
def printspeak(s):
    print('Bot: '+s)
    speak(s)
if __name__=="__main__":
    #wishMe()
    while(True):
        query=takeCommand().lower()
        print(query)
        if('wikipedia' in query):
            printspeak('Searching Wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=3)
            os.system('cls||clear')
            printspeak('According to wikipedia,' + str(results))
        elif(('good morning' in query) or ('good afternoon' in query) or ('good evening' in query)):
            printspeak(wishMe())
        elif(('hello' in query) or ('hi' in query) or ('hey there' in query) or ('hola' in query)):
            printspeak('Hello!')
        elif(("What's up" in query) or ('how are you' in query) or ('how is it going' in query) or ('hows it going' in query)):
            printspeak('It is fantastic in here. what about you?')
        elif(('i am fine' in query) or ("everything's good" in query) or ('everything is good' in query) or ('I am good' in query)):
            printspeak('Good to know!')
        elif(('who created you' in query) or ('who made you' in query)):
            printspeak('I was created by Mr. Raunak Burrows and Mr. Abhinandan Dhatwalia.')
        elif(('who are you' in query) or('what is your identity' in query) or ('introduce yourself' in query)):
            printspeak('I am JARVIS. I was created by Mr. Raunak Burrows and Mr. Abhinandan Dhatwalia.')
        elif(('what is your name' in query) or ("what's your name" in query)):
            printspeak('I am JARVIS')
        elif(('thank you' in query) or ('thanks' in query) or ('gratitude' in query) or ('grateful' in query)):
            printspeak('Your welcome.')
        elif(('like pets') in query):
            printspeak('Ofcourse! In fact, turtle is my favourite pet.')
        elif('tell me about your likes and dislikes' in query):
            printspeak('I like singing, painting, playing the voilen, and clicking pictures of the food i cook. Lol. and being a machine, there is nothing I dislike.')
        elif('open' in query):
            printspeak('Opening the website...')
            openwebsite(query)
        elif('play' in query):
            query=query.split('play')
            printspeak('Searching youtube...')
            pywhatkit.playonyt(query[1])
        elif(('date' in query) and (("what's" in query) or ("what is" in query) or ("tell" in query) or ('say' in query))):
            current_time = datetime.datetime.now()
            date=str(current_time)[:10]
            printspeak('The date is: '+date)
        elif(('time' in query) and (("what's" in query) or ("what is" in query) or ("tell" in query) or ('say' in query))):
            current_time = datetime.datetime.now()
            time=str(current_time)[11:]
            hour=time[:2]
            m=' a.m.'
            if(int(hour)>=13 or int(hour)<24):
                m=' p.m.'
                hour=str(int(hour)-12)
            minute=time[3:5]
            time=hour+':'+minute+m
            printspeak('The time is: '+time)
        elif(('stop' in query) or ('bye' in query) or ('sayonara' in query)):
            printspeak('Thankyou for your time here.')
            break
        else:
            webbrowser.open('https://google.com?#q='+str(query))
            try:
                query=query.replace("wikipedia","")
                results=wikipedia.summary(query, sentences=3)
                if(query in results):
                    printspeak('According to wikipedia, '+str(results))
                else:
                    printspeak('Showing Google search results for '+str(query))
            except:
                printspeak('Showing Google search results for '+str(query))
        os.system('cls||clear')
    os.system('cls||clear')
