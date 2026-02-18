from inputs.user_input import user_input
from outputs.display import welcome, clear_thinking, show_text, show_token
from processing.brain import brain

def main():
    total_input = 0
    total_output = 0
    total = 0
    welcome()
    while True:
        try:
            user_text = user_input()
            if user_text.lower() in ["exit"]:
                print("Amber: Goodbye")
                show_token(total_input, total_output, total)
                break
            print("Amber: Thinking...", end="\r")
            respond, itoken, utoken = brain(user_text)
            total_input += itoken
            total_output += utoken
            total += itoken + utoken
            clear_thinking()
            show_text(respond)
        except Exception as e:
            print(f"Amber: {e}")
            show_token(total_input, total_output,total)
            break
        except KeyboardInterrupt:
            print("Amber: Goodbye")
            show_token(total_input, total_output, total)
            break
if __name__ == "__main__":
    main()