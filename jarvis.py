import pyttsx3
import speech_recognition as sr
import time

engine = pyttsx3.init()
engine.setProperty('rate', 120)

# obtain audio from the microphone
r = sr.Recognizer()

while(True):
    with sr.Microphone(1) as source:
        print("I am listening...!")
        audio = r.listen(source)

    # recognize speech using Sphinx
    try:
        speech = r.recognize_google(audio)
        print(speech)
        if('hello' in speech.lower() or 'jarvis' in speech.lower()):
            engine.say('Yes Sir')
            engine.runAndWait()
        elif('date' in speech.lower() or 'day' in speech.lower()):
            engine.say(time.strftime("%a, %d %b %Y", time.localtime()))
            engine.runAndWait()
        elif ('time' in speech.lower()):
            engine.say(time.strftime("%I:%M %p", time.localtime()))
            engine.runAndWait()

    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Error; {0}".format(e))