#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chyas
#
# Created:     06/02/2025
# Copyright:   (c) chyas 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from pathlib import Path
import os
import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

# Function to record text using the microphone
def record_text():
    try:
        with sr.Microphone() as source2:
            print("Adjusting for ambient noise...")
            r.adjust_for_ambient_noise(source2, duration=1)  # Adjust for ambient noise (increased duration)

            print("Listening for speech...")
            audio2 = r.listen(source2)

            # Trying speech recognition
            print("Recognizing speech...")
            mytext = r.recognize_google(audio2)  # Recognize speech and return as text

            print(f"Recognized Text: {mytext}")  # Output the recognized text
            return mytext

    except sr.RequestError as e:
        print(f"Could not request results; {e}")  # More specific error message for API issues
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Function to output text to a file
def output_text(text):
    folder_path = Path.cwd()  # Get the current working directory
    output_folder = folder_path / 'output_folder'  # Set the folder path to save the file

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)  # Create the folder if it doesn't exist

    file_path = output_folder / 'output.txt'  # Define the full file path
    with open(file_path, 'a') as f:
        f.write(text + "\n")  # Write the text with a newline at the end
    print(f"Text written to {file_path}.")

# Main execution loop (runs only once)
def main():
    text = record_text()  # Get speech input
    if text:  # Check if text was recognized
        output_text(text)  # Write the text to a file
    print("Program executed successfully. Exiting...")

if __name__ == "__main__":
    main()
