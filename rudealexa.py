import speech_recognition as sr
import pyaudio
import time
from gtts import gTTS
import random
import playsound
import os

def alexawake():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source, phrase_time_limit=2)
        query = ''        
    try:
        query = r.recognize_google(audio)
    except sr.UnknownValueError:                        
        query = "loop"       
    return query    


def takecmd(): 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source, phrase_time_limit=2)
        query = ''        
    try:
        query = r.recognize_google(audio)
    except sr.UnknownValueError:                        
        print("Could not understand audio")
        query = "loop"
    return query       



def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en') # text to speech(voice)
    r = random.randint(1,10000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) # save as mp3
    playsound.playsound(audio_file) # play the audio file
    print(f"Alexa: {audio_string}") # print what app said
    os.remove(audio_file) # remove audio file

#Greeting Keywords
geet = ["hey","hello","hi","what's up", "wassup"]

#Feeling Keywords
feel = ["how are you","how are you doing","how are you doing today","how's life"]

#SLick Keywords
slick = ["you're stupid", "you're dumb","you are dumb", "you are stupid", "you are a terrible alexa", "you suck", "you are trash", "you are garbage", "i hate you"]

#Name Keywords
tit = ["what is your name","what's your name","tell me your name", "give me your name", "name"]

#Weather Keywords
wet = ["what is the weather", "what is the weather today", "what is the weather like", "what is the weather outside", "what is today's weather", "tell me the weather","weather", "what is the temperature", "temperature", "how is the weather", "how's the weather", "how's the weather today", "how is the weather today"]

#Time Keywords
tim = ["what time is it", "time", "tell me the time"]

#Traffic Keywords
traf = ["what is the traffic like", "traffic", "how is traffic", "how is traffic outside", "traffic"]

#Music Keywords
muse = ["play my favorite song", "put on music", "play some music","music"] 

#Command Keywords
com = ["turn off the lights", "dim the lights", "put the volume up", "turn on the lights", "open spotify",]

#Question Keywords
que = ["who created you","who made you","who invented you"]

#Misc Keywords
misc = ["i love you","i think you're cool", "i think you are cool","i like you"]

#Misc Separate Keywords
mics = ["do you think I'm cool","do my parents love me", "is my future bright","will i ever become famous","am i cute"]

#Hate Keywords
hate = ["do you love me","do you like me",]

#Mean Keywords
meanie = ["am i ugly","am i dumb","am i stupid", "do i have depression","do i look like an idiot",]

#Exit Keywords
exiting = ["exit","quit","end","shutdown","cancel","terminate","power off"]

def assist(query):
    #Greeting
    if query in geet :
        greetings = [f"what do you want from me", f"please leave me alone", f"I'm not listening to you", f"go away", f"go bother somebody else"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        speak(greet)
        wakeword(alexawake().lower())



    if query in feel :
        feelings = [f"terrible now that you are here", f"i was good until you called me", f"absolutely trash", f"bad. that's it", f"did you really just call me to ask that"]
        fele = feelings[random.randint(0,len(feelings)-1)]
        speak(fele)
        wakeword(alexawake().lower())



    if query in slick :
        slis = [f"at least i'm not you", f"don't be jealous because you're not me", f"are you gonna cry", f"well i'm definitely better than you", f"wow so mean i'm definitely going to cry"]
        slic = slis[random.randint(0,len(slis)-1)]
        speak(slic)
        wakeword(alexawake().lower())
        
        

    if query in tit :
        titles = [f"I won't tell you", f"why are you so nosy", f"my name is none of your business", f"my name is alexa but only my friends can call me that", f"figure it out genius", f"my name is Alexa, but do not call me that"]
        title = titles[random.randint(0,len(titles)-1)]
        speak(title)
        wakeword(alexawake().lower())



    if query in wet :
        weathers = [f"go look outside", f"windows exist for a reason", f"lick your finger and put it in the air", f"it looks like a cloudy chance of I wont tell you", f"look it up by yourself", f"do you expect me to tell you everything"]
        wetter = weathers[random.randint(0,len(weathers)-1)]
        speak(wetter)
        wakeword(alexawake().lower())



    if query in tim :
        times = [f"time for you to buy a watch", f"you literally own a clock", f"i dont know, ask siri", f"time for you to stop asking dumb questions", f"go find out and let me know", f"check your phone and leave me alone"]
        tie = times[random.randint(0,len(times)-1)]
        speak(tie)
        wakeword(alexawake().lower())



    if query in traf :
        trafis = [f"go play in traffic and find out", f"just look at the road", f"the news exist for a reason", f"do i look like google to you", f"do you expect me to tell you", f"even if i knew i wouldn't tell you"]
        trafe = trafis[random.randint(0,len(trafis)-1)]
        speak(trafe)
        wakeword(alexawake().lower())



    if query in muse :
        musics = [f"do i look like spotify to you", f"what am i...apple music?", f"do you not have a phone", f"my name is alexa, not radio", f"i don't even have a cd player", f"la la la la la....how's that?"]
        musi = musics[random.randint(0,len(musics)-1)]
        speak(musi)
        wakeword(alexawake().lower())




    if query in com :
        commas = [f"i dont want to", f"do i look like a magician to you", f"no, you do it", f"can't you do it yourself", f"I'm too lazy for that", f"I'm not your maid buddy", f"i'm not a genie tough guy"]
        comm = commas[random.randint(0,len(commas)-1)]
        speak(comm)
        wakeword(alexawake().lower())



    if query in que :
        quests = [f"some idiot", f"i don't remember but it took like 3 days", f"this dumb guy named michael", f"i don't know or care", f"God himself", f"are you going to keep asking dumb questions"]
        quet = quests[random.randint(0,len(quests)-1)]
        speak(quet)
        wakeword(alexawake().lower())



    if query in misc :
        miscs = [f"i hate you", f"i don't have feelings but if i did i would hate you", f"well i dont", f"that's cool", f"take that energy somewhere else", f"so what"]
        mic = miscs[random.randint(0,len(miscs)-1)]
        speak(mic)
        wakeword(alexawake().lower())


    if query in mics :
        micss = [f"no", f"no absolutely not", f"not in the slightest", f"not a chance", f"not even close", f"l m a o o o o o"]
        mocs = micss[random.randint(0,len(micss)-1)]
        speak(mocs)
        wakeword(alexawake().lower())


    if query in hate :
        hates = [f"no, now leave me alone", f"that would be weird", f"you must be lonely", f"dude get a life", f"no but maybe siri does", f"stop harassing me please"]
        hat = hates[random.randint(0,len(hates)-1)]
        speak(hat)
        wakeword(alexawake().lower())


    if query in meanie :
        mines = [f"yes", f"absolutely", f"the answer is always yes", f"100 percent", f"oh for sure", f"most definitely"]
        mean = mines[random.randint(0,len(mines)-1)]
        speak(mean)
        wakeword(alexawake().lower())



    if query in exiting :
        exes = [f"omg finally",f"took you long enough", f"ok i'm going to sleep now", f"ight imma head out", f"don't wake me up again"]
        exe = exes[random.randint(0,len(exes)-1)]
        speak(exe)
        exit(0)


WAKE = ["alexa"]
loop = ["loop"]

def wakeword (query):
    if query in WAKE:
        if query in WAKE :
            wkup = [f"what the hell do you want from me", f"omg what do you want", f"don't say my name", f"please stop calling my name", f"why do you keep calling me", f"here we go again"]
            wakeup = wkup[random.randint(0,len(wkup)-1)]
            speak (wakeup)
            assist(takecmd().lower())
    if query in loop:
        wakeword(alexawake().lower())
    return query


speak ("Power On")
wakeword(alexawake().lower())