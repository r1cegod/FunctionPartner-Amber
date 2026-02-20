from inputs.user_input import user_input
from outputs.display import welcome, clear_thinking, show_text, show_token
from processing.main_graph import final_state

def main():
    total_input = 0
    total_output = 0
    total = 0
    welcome()
    while True:
        try:          
            user_text = user_input()
            if user_text.lower() in ["exit"]:
                clear_thinking()
                show_text("Goodbye")
                show_token(total_input, total_output, total)
                break
            print("Amber: Thinking...", end="\r")
            final = final_state(user_text)
            respond = final['messages'][-1]
            metadata = respond.response_metadata
            if "token_usage" in metadata:
                usage = metadata["token_usage"]
                itoken = usage["prompt_tokens"]
                utoken = usage["completion_tokens"]
            else:
                itoken = 0
                utoken = 0
            total_input += itoken
            total_output += utoken
            total += itoken + utoken
            clear_thinking()
            show_text(f"{respond.content}")
        except KeyboardInterrupt:
            clear_thinking()
            show_text("Goodbye")
            show_token(total_input, total_output, total)
            break

if __name__ == "__main__":
    main()