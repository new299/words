import csv
import random
import time
import os
import sys
import ctypes

# Function to clear the console screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to hide the cursor
def hide_cursor():
    if os.name == 'nt':  # Windows
        ctypes.windll.kernel32.SetConsoleCursorInfo(ctypes.windll.kernel32.GetStdHandle(-11), ctypes.pointer(ctypes.windll.kernel32.CONSOLE_CURSOR_INFO(0, 0)))
    else:  # Unix/Linux/Mac
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()

# Function to show the cursor
def show_cursor():
    if os.name == 'nt':  # Windows
        ctypes.windll.kernel32.SetConsoleCursorInfo(ctypes.windll.kernel32.GetStdHandle(-11), ctypes.pointer(ctypes.windll.kernel32.CONSOLE_CURSOR_INFO(1, 1)))
    else:  # Unix/Linux/Mac
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()

# Function to read CSV and store words, hiragana, and meanings
def load_words():
    words = []
    with open('words.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            words.append({
                'word': row['Word'],
                'hiragana': row['Hiragana'],
                'meaning': row['English meaning']
            })
    return words

# Main function to display the words in the specified format
def display_words(words):
    hide_cursor()  # Hide the cursor
    try:
        while True:
            word = random.choice(words)

            clear_screen()
            print(word['word'])
            time.sleep(2)

            print(word['hiragana'])
            time.sleep(2)

            print(word['meaning'])
            time.sleep(2)

    finally:
        show_cursor()  # Ensure the cursor is shown after exiting

if __name__ == '__main__':
    words = load_words()
    display_words(words)

