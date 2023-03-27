import speech_recognition as sr 
import webbrowser
import time 
import playsound
import os
import random
from gtts import gTTS
from time import ctime

r = sr.Recognizer()


def words_spoken(terms, voice_data):
    for term in terms:
        if term in voice_data:
            return True





def record_audio(ask = " "):
    with sr.Microphone() as source:
        if ask:
            Eira_speak(ask)
        audio = r.listen(source, 5, 5)
        print("Done Listening")
        voice_data = ' '
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            Eira_speak('Sorry,I did not get that')
        except sr.RequestError:
            Eira_speak('Sorry, My speech service is down')
        print(">>", voice_data.lower())    
        return voice_data.lower()




def Eira_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)        
    
    
    
    
    
    
    #hello's
def  respond(voice_data):
    if words_spoken(['hey, Eira', 'Hi, Eira', 'Hello, Eira']):
        greetings = ["mmmhmm", "yes", "how can I help you?", "what's up ", "i'm listening"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        Eira_speak(greet)
    if words_spoken(["what is your name?", "Whats your Name", "tell me your name"]):
        Eira_speak('My name is Eira')
    if words_spoken(["How are you doing", "What's up", "How are you"]):
        Eira_speak("I'm feeling very well, thank you for asking")  
       
       
       
    
    
        #time  
    if words_spoken(["What time is it","what's the time", "Tell me the time"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] =="00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = hours + "hours and " + minutes + "minutes"
        Eira_speak(time) 

       
       
       
        #search         
    if words_spoken(["search for", "search", "look up"]):
        search_term = voice_data.split("for")[-1]  
        url = "https://google.com/search?q=" + search_term 
        webbrowser.get().open(url)
        Eira_speak('Here is what I found for' + search_term + " on google")
       
       
       
       
        #location
    if  'find location' in voice_data:
        location_term =voice_data.split("for")[-1]   
        url = 'https://google.nl/maps/place/' +location_term + '/&amp;'
        webbrowser.get().open(url)
        Eira_speak('Here is the location of ' + location_term) 
       
       
       
        # weather
    if words_spoken(["weather"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        Eira_speak("Here is what I found on google")

       
       
       
        #goodbye
    if words_spoken(["stop", "bye"]):
        Eira_speak('Bye')
        exit()




time.sleep(1)


while (1):
    voice_data = record_audio()
    respond(voice_data)
