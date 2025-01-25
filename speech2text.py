import pyttsx3
import speech_recognition as sr

def get():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something:")
        audio=r.listen(source)
        
        print("OK!")
    try:
        text=r.recognize_google(audio)
        print("You said: ",text)
     
        if text == "exit":
            print("Exiting the program. Goodbye!")
            return False  # Signal to stop the loop
        
        else:
            # Optional: Use text-to-speech to repeat what was said
            engine = pyttsx3.init()
            engine.say(f"You said: {text}")
            engine.runAndWait()
            return True     

    except Exception as e:
        print(e)     
        return True       

while True:
    if not get():
        break
       