import sys, os, time

def text_ani(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

def main():
    while True:
        try:
            text = input("you: ")
            text_ani(text)
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
if __name__ == "__main__":
    main()