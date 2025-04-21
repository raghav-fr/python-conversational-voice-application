import re
from google import genai
import speech_recognition as sr
import pyttsx3
import threading


client = genai.Client(api_key="<GEMINI_API_KEY>")
chat = client.chats.create(model="gemini-2.0-flash")

speak_thread = None
speak_lock = threading.Lock()
is_speaking = threading.Event()
current_engine = None


def speak(text):
    global current_engine
    local_engine = pyttsx3.init()
    current_engine = local_engine
    with speak_lock:
        is_speaking.set()
        try:
            local_engine.say(text)
            local_engine.runAndWait()
        except Exception as e:
            print(f"[Speech error] {e}")
        

def interrupt_speech():
    global current_engine
    if is_speaking.is_set() and current_engine:
        current_engine.stop()
        is_speaking.clear()

    

def listen():
    recog = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recog.adjust_for_ambient_noise(source)
        try:
            audio = recog.listen(source, phrase_time_limit=10)
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
    global speak_thread

    while True:
        usr_input = listen()

        if not usr_input:
            continue

        if "exit" in usr_input.lower():
            interrupt_speech()
            print("Assistant: Goodbye!" )
            speak("Goodbye!")
            break

        interrupt_speech()

        response = gemini(usr_input)
        filtered_resoponse = re.sub(r"[^a-zA-Z\s,.!:0-9]", "", response)

        print("Assistant:", filtered_resoponse)

        speak_thread = threading.Thread(target=speak, args=(filtered_resoponse,))
        speak_thread.start()

if __name__ == "__main__":
    main()
