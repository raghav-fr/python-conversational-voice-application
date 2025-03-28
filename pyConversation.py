from google import genai
import speech_recognition as sr
import pyttsx3

client = genai.Client(api_key="<YOUR_API_KEY>")

engine = pyttsx3.init()
chat = client.chats.create(model="gemini-2.0-flash")


def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recog = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recog.adjust_for_ambient_noise(source)
        try:
            audio = recog.listen(source, phrase_time_limit=10, timeout=10)
            text = recog.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            print( "Sorry, I couldn't understand that.")
            return listen()

        except sr.RequestError:
            return "Request error" 

def gemini(prompt):
    response = chat.send_message(prompt)
    return response.text if response else "Sorry, I couldn't process your request."

def main():
    print("Voice Assistant is running... Say 'exit' to stop.")
    while True:
        usr_input = listen()
        if "exit" in usr_input.lower():
            print("You:", usr_input)
            print("Goodbye!")
            speak("Goodbye!")
            break

        if "request error" in usr_input.lower():
            print("Speech recognition service is unavailable.")
            break
        
        print("You:", usr_input)
        response = gemini(usr_input)
        print("Assistant:", response)
        speak(response)

if __name__ == "__main__":
    main()
