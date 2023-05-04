import os
import time
import pyaudio
import playsound
from gtts import gTTS
import openai
import speech_recognition as sr

api_key = ""

lang = 'en'

openai.api_key = api_key

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone(device_index=2) as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)

            if "Friend" in said:
                completion = openai.Completion.create(engine="text-davinci-002", prompt=said, max_tokens=1024)
                text = completion.choices[0].text
                speech = gTTS(text=text, lang=lang, slow=False, tld="com.au")
                speech.save("welcome1.mp3")
                playsound.playsound("welcome1.mp3")

        except Exception as e:
            print("Exception: ", e)
        except sr.UnknownValueError:
            print("Google Speech Recognition couldn't understand audio")
        except sr.RequestError as e:
            print("Couldn't request results from Google Speech Recognition service; {0}".format(e))

    return said

while True:
    get_audio()

