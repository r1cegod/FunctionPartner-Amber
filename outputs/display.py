from time import time
import sys, time

def welcome():
    print("Simple bot Amber!")
    print("Type 'exit' to quit")
    print("--------------------------------")

def clear_thinking():
    sys.stdout.write("\033[K")
    sys.stdout.write("\r")
    sys.stdout.write("Amber: ")

def show_text(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def show_token(total_input, total_output, total):
    print(f"[Token usage] in: {total_input} out: {total_output} total: {total}")