from gtts import gTTS
from playsound import playsound
import os

with open("result.txt", "r") as f:
    data = f.read()

sp = gTTS(lang = 'ko', text = data, slow=False)

sp.save("speech.mp3")
playsound("/home/pi/test/speech.mp3")




"""def text_to_speech(text, langauge='en'):
    tts = gTTS(text=text, lang=langauge, slow=False)
    tts.save("output.mp3")
    os.system("start output.mp3")

if __name__ == "__main__":
    input_text = input("text input: ")
    text_to_speech(input_text)
"""