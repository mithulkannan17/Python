# speaking plank timer

import time
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Welcome to the exercise timer!")
speak("Enter your name ")
name = input("Enter your name: ")
speak(f"Hello {name}")  # Corrected f-string usage
speak("Do you want to start?")
print("Do you want to start?")
options = input("Yes or No: ").lower()

if options == "yes":
    speak(f"{name}, Enter the number of sets")  # Corrected f-string usage
    sets = int(input("Enter the number of sets: "))

    speak("Enter the number of seconds")
    seconds = int(input("Enter the time in seconds: "))
    speak("Timer started")
    for i in range(sets):
        speak(f"Starting set {i + 1}")  # Corrected speak usage
        print(f"Starting set: {i + 1}")
        for j in range(seconds):
            speak(f"{seconds - j}")
            print(f"{seconds - j}", end="\r")
            time.sleep(1)

        speak(f"Completed set {i + 1}")
        print(f"Completed set: {i + 1}")
        if i < sets - 1:
            speak("Resting time")
            print("Resting time:")
            for k in range(30):
                print(f"{30 - k}", end="\r")
                time.sleep(1)
                if (30 - k) <= 3:
                    speak(f"{30 - k}")

            speak("Rest over")
            print("Rest over")
    speak("Workout complete!")
    print("Workout complete!")
elif options == "no":
    speak("Timer terminated")
    print("Timer terminated")
else:
    speak("Invalid input")
    print("Invalid input")