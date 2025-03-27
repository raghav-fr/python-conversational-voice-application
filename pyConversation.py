from google import genai
import speech_recognition as sr
import pyttsx3

client = genai.Client(api_key="AIzaSyDC2603M6IyhlYlGirpom8DpDFSlzyw5Hk")

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    # text = input("Enter your text: ")

    # try:
    #     return text
    
    recog = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recog.adjust_for_ambient_noise(source)
        try:
            audio = recog.listen(source)
            text = recog.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            print( "Sorry, I couldn't understand that.")
            return listen()

        except sr.RequestError:
            return "Speech recognition service is unavailable."

def gemini(prompt):
    response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
    return response.text if response else "Sorry, I couldn't process your request."

def main():
    print("Voice Assistant is running... Say 'exit' to stop.")
    while True:
        usr_input = listen()
        print("You:", usr_input)

        if "exit" in usr_input.lower():
            print("Goodbye!")
            speak("Goodbye!")
            break

        response = gemini(usr_input)
        print("Assistant:", response)
        speak(response)

if __name__ == "__main__":
    main()
