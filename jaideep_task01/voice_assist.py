# pyrefly: ignore [missing-import]
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import threading
import random
import re
# pyrefly: ignore [missing-import]
import wikipedia

# Initialize voice engine
engine = pyttsx3.init()
voices = engine.getProperty("voices")
voice_map = {voice.name.lower(): voice.id for voice in voices}
assistant_state = {
    "personality": "neutral",
    "memory": [],
    "reminders": []
}

def speak(text):
    prefix = ""
    if assistant_state["personality"] == "friendly":
        prefix = "Hey friend! "
    elif assistant_state["personality"] == "formal":
        prefix = "At your service. "
    message = prefix + text
    print("Mini:", message)
    engine.say(message)
    engine.runAndWait()


def list_voices():
    return [voice.name for voice in voices]


def set_voice(name):
    key = name.lower()
    if key in voice_map:
        engine.setProperty("voice", voice_map[key])
        speak(f"Voice changed to {name}.")
    else:
        speak("I could not find that voice. Say voice list to hear available options.")


def remember_item(item):
    assistant_state["memory"].append(item)
    speak(f"Okay, I will remember {item}.")


def recall_memory():
    items = assistant_state["memory"]
    if not items:
        speak("You haven't asked me to remember anything yet.")
        return
    spoken = ", ".join(items[-5:])
    speak(f"I remember: {spoken}.")


def reminder_action(message):
    speak(f"Reminder: {message}")


def set_reminder(command):
    match = re.search(r"remind me in (\d+)\s*(second|seconds|minute|minutes|hour|hours)", command)
    if not match:
        speak("Please tell me when to remind you. For example, remind me in 5 minutes.")
        return
    number = int(match.group(1))
    unit = match.group(2)
    seconds = number
    if "minute" in unit:
        seconds *= 60
    elif "hour" in unit:
        seconds *= 3600
    message = command.split(match.group(0), 1)[-1].strip() or "your task"
    timer = threading.Timer(seconds, reminder_action, args=(message,))
    timer.daemon = True
    timer.start()
    assistant_state["reminders"].append((message, seconds))
    speak(f"I will remind you about {message} in {number} {unit}.")


def generate_poem():
    now = datetime.datetime.now()
    season = "summer" if now.month in (6, 7, 8) else "winter" if now.month in (12, 1, 2) else "spring" if now.month in (3, 4, 5) else "autumn"
    lines = [
        f"A quiet {season} breeze flows through the day,",
        "The world whispers secrets in a gentle way,",
        "Mini listens softly and lights your path with play."
    ]
    return " ".join(lines)


def tell_joke():
    jokes = [
        "Why did the computer show up at work late? It had a hard drive.",
        "Why do programmers prefer dark mode? Because light attracts bugs.",
        "What do you call a parade of rabbits hopping backward? A receding hare-line."
    ]
    speak(random.choice(jokes))


def spell_word(command):
    match = re.search(r"spell\s+(\w+)", command)
    if not match:
        speak("Tell me a word to spell. For example, spell hello.")
        return
    word = match.group(1)
    spelled = " ".join(list(word.upper()))
    speak(f"{word} is spelled {spelled}.")


def guess_number_game():
    target = random.randint(1, 20)
    speak("I have picked a number between 1 and 20. Try to guess it.")
    attempts = 0
    while attempts < 6:
        guess_command = take_command()
        if not guess_command:
            continue
        if "exit" in guess_command or "stop" in guess_command:
            speak("Exiting the number game.")
            return
        match = re.search(r"(\d+)", guess_command)
        if not match:
            speak("Please say a number.")
            continue
        guess = int(match.group(1))
        attempts += 1
        if guess == target:
            speak(f"Correct! You guessed my number in {attempts} tries.")
            return
        if guess < target:
            speak("Higher.")
        else:
            speak("Lower.")
    speak(f"The number was {target}. Let's play again later.")


def take_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except Exception:
        speak("Sorry, I did not understand.")
        return ""

def wish_user():
    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good Morning")

    elif hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am Mini, your AI Voice Assistant.")

def run_assistant():
    wish_user()
    while True:
        command = take_command()
        
        if not command:
            continue

        if "hello" in command:
            speak("Hello, how can I help you?")

        elif "what can you do" in command or "help" in command:
            speak("I can tell you the time and date, open websites, search Wikipedia, play a number game, spell words, remember things, set reminders, and even change my voice.")

        elif "voice list" in command:
            available = list_voices()
            speak("I can speak with the following voices:")
            for voice_name in available:
                speak(voice_name)

        elif "set voice" in command:
            name = command.replace("set voice", "").strip()
            if name:
                set_voice(name)
            else:
                speak("Please say the voice name after set voice.")

        elif "be friendly" in command:
            assistant_state["personality"] = "friendly"
            speak("I am now speaking in a friendly way.")

        elif "be formal" in command:
            assistant_state["personality"] = "formal"
            speak("I am now speaking in a formal way.")

        elif "be neutral" in command:
            assistant_state["personality"] = "neutral"
            speak("I am now speaking neutrally.")

        elif "remember" in command and "remember me" not in command:
            item = command.replace("remember", "").strip()
            if item:
                remember_item(item)
            else:
                speak("Please tell me what to remember.")

        elif "what did i ask you to remember" in command or "what do i want you to remember" in command:
            recall_memory()

        elif "remind me in" in command:
            set_reminder(command)

        elif "tell me a joke" in command or "joke" in command:
            tell_joke()

        elif command.startswith("spell") or "spell" in command:
            spell_word(command)

        elif "play number game" in command or "number game" in command:
            guess_number_game()

        elif "poem" in command:
            speak(generate_poem())

        elif "quantum" in command:
            speak("Quantum circuits may be imaginary, but our conversation is very real.")

        elif "time" in command:
            time_now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {time_now}")

        elif "date" in command:
            date_today = datetime.datetime.now().strftime("%d %B %Y")
            speak(f"Today's date is {date_today}")

        elif "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif "wikipedia" in command:
            speak("Searching Wikipedia")
            query = command.replace("wikipedia", "").strip()
            if query:
                try:
                    result = wikipedia.summary(query, sentences=2)
                    speak(result)
                except wikipedia.exceptions.DisambiguationError as e:
                    speak("There are multiple results for this. Please be more specific.")
                except wikipedia.exceptions.PageError:
                    speak("I couldn't find any information on that.")
                except Exception:
                    speak("Sorry, I encountered an error while searching Wikipedia.")
            else:
                speak("What would you like me to search on Wikipedia?")

        elif "exit" in command or "stop" in command:
            speak("Goodbye")
            break

        else:
            speak("Command not recognized. Try saying hello, time, or open google.")


def main():
    try:
        # Test if microphone is accessible
        with sr.Microphone() as source:
            pass
        run_assistant()
    except Exception as e:
        print(f"Error: {e}")
        print("Please make sure your microphone is connected and accessible.")


if __name__ == "__main__":
    main()
