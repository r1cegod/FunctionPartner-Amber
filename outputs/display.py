import sys
import time

def show_welcome():
    print("Amber v2.0 (The Architect)")
    print("Type 'exit' or 'quit' to close.")
    print("-" * 30)

def show_thinking():
    print("Amber: Thinking... ", end="\r")

def hide_thinking():
    sys.stdout.write("\033[K")
    sys.stdout.write("\r")
    sys.stdout.write("Amber: ")
    sys.stdout.flush()

def stream_text(text, delay=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_totals(total_input, total_output):
    total = total_input + total_output
    print(f"\n[Session Stats] In: {total_input} | Out: {total_output} | Total: {total}")
