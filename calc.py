import pyttsx3
import speech_recognition as sr
import wolframalpha

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[0].id)
engine.setProperty('rate', 170)


def speak(audio):
    print(" ")
    engine.say(audio)
    print(f": {audio}")
    print(" ")
    engine.runAndWait()


def WolframAlpha(query):
    apikey = "PT6KKG-AE6H74A95Y"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak('There is some error, please say that again to calculate')


def Calc(query):
    Term = str(query)

    Term = Term.replace("calculate", "")
    Term = Term.replace("AI", "")
    
    Term = Term.replace("multiply", "*")
    Term = Term.replace("into", "*")
    
    Term = Term.replace("plus", "+")
    Term = Term.replace("minus", "-")
    
    Term = Term.replace("divide", "/")
    Term = Term.replace("power", "**")

    Final = Term

    try:
        result = WolframAlpha(Final)
        print(f"{result}")
        speak(result)
    except:
        speak("The value is not answerable or there is something wrong, please say that again")


def takeCommand():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 0.5
        r.energy_threshold = 1000
        audio = r.listen(source, 0, 4)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language="en-in")
        print(f"User: {query}")
        return query
    except Exception as e:
        print("Say That Again.....")
        return "None"

disconnect = ["quit","disconnect","sleep"]

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "calculate" in query:
            query = query.replace("calculate", "")
            query = query.replace("bd", "")
            Calc(query)
            
        elif any(word in query for word in disconnect):
            speak('Disconnecting, bye bye')
            break  