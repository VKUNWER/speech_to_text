#pip install pipwin
#pip install pyaudio
#pip install speechrecognition


import speech_recognition as sr
r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("speak now")
    audio=r.listen(source)
    
    try:
        data = r.recognize_google(audio)
        print(data)
    except:
        print("Please try again")
