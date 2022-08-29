from gtts import gTTS #text to speech converter module
import os

sample = open('sample.txt') #text which will be converted to speech
text = sample.read()


language = "en" #english language

obj = gTTS(text = text,lang=language,slow=True)

obj.save("sample.mp3") # save to mp3 file

os.system('sample.mp3') # open the mp3 file