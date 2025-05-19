import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import requests

# Initialize recognizer and text-to-speech engine
listener = sr.Recognizer()
machine = pyttsx3.init()

# Function to make the assistant speak
def talk(text):
    machine.say(text)
    machine.runAndWait()

# Function to take voice input
def input_instruction():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            instruction = listener.recognize_google(voice)
            instruction = instruction.lower()
            if "jarvis" in instruction:
                instruction = instruction.replace('jarvis', '')
            return instruction
    except:
        return ""

# Function to get weather info
def get_weather():
    city = "Colombo"  
    api_key = "your_openweather_api_key"  
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data.get("main"):
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        talk(f"The current temperature in {city} is {temp} degrees Celsius with {desc}.")
    else:
        talk("Sorry, I couldn't fetch the weather details.")

# Function to process and respond to instructions
def play_Jarvis():
    instruction = input_instruction()
    print(f"Instruction: {instruction}")

    if instruction == "":
        talk("Sorry, I didn't catch that. Please try again.")
        return

    if "hello" in instruction or "hi" in instruction:
        talk("Hello! How can I help you today?")
        return

    if "play" in instruction:
        song = instruction.replace('play', '')
        talk("Playing " + song)
        pywhatkit.playonyt(song)

    elif 'time' in instruction:
        time = datetime.datetime.now().strftime("%I:%M %p")
        talk("Current time is " + time)

    elif 'date' in instruction:
        date = datetime.datetime.now().strftime("%d/%m/%Y")
        talk("Today's date is " + date)

    elif 'how are you' in instruction:
        talk("I am fine, how about you?")

    elif 'what is your name' in instruction:
        talk("I am Jarvis, what can I do for you?")

    elif 'who is' in instruction:
        person = instruction.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'weather' in instruction:
        get_weather()

    else:
        talk("Please repeat the command.")

# Call the assistant
play_Jarvis()
