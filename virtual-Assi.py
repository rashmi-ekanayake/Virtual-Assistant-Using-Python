import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

# Initialize recognizer and text-to-speech engine
listener = sr.Recognizer()
machine = pyttsx3.init()

# Function to make the assistant speak
def talk(text):
    machine.say(text)
    machine.runAndWait()  # Should be inside the function

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

# Function to process and respond to instructions
def play_Jarvis():
    instruction = input_instruction()
    print(f"Instruction: {instruction}")

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

    else:
        talk("Please repeat the command.")

# Call the assistant
play_Jarvis()
