"""
we can open a terminal after installing Python, and use the microphone to convert our speech to text
"""

import speech_recognition

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Say something!")
    audio = recognizer.listen(source)

print("Google Speech Recognition thinks you said:")
print(recognizer.recognize_google(audio))

words = recognizer.recognize_google(audio)

if "hello" in words:
    print("Hello to you too!")
elif "how are you" in words:
    print("I am well, thanks!")
elif "googbye" in words:
    print("Goodbye to you too!")
else:
    print("Huh?")            