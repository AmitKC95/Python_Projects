import cowsay
import pyttsx3

engine = pyttsx3.init()
this = input("What's thi9? ")
cowsay.cow(this)
engine.say(this)
engine.runAndWait()