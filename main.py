from inputs.user import prompt_user
from processing.brain import brain
from outputs.display import stream_text, show_thinking, hide_thinking, print_totals, show_welcome

def main():
    total_input = 0
    total_output = 0
    show_welcome()
    while True:
        try:
            user_text = prompt_user()
            if user_text.lower() in ["exit", "quit"]:
                print("Amber: Goodbye")
                break
            show_thinking()
            response, i_tok, o_tok = brain(user_text)
            total_input += i_tok
            total_output += o_tok
            hide_thinking()
            stream_text(response)
        except KeyboardInterrupt:
            print("\nForce Exit detected.")
            break
        except Exception as e:
            print(f"\nCRITICAL SYSTEM ERROR: {e}")
            break
    print_totals(total_input, total_output)
if __name__ == "__main__":
    main()