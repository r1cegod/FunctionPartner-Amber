from processing.memory import load_memory
from inputs.user_input import user_input
from outputs.display import welcome, clear_thinking, show_text, show_token
from processing.brain import brain, calculate
from processing.memory import load_memory, save_memory
import json, sys

def main():
    history=load_memory()
    history.append({"role": "system", "content": "you are Amber, a helpful assitant"})
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
            history.append({"role": "user", "content": user_text})
            print("Amber: Thinking...", end="\r")
            while True:
                try:
                    respond_obj, itoken, utoken = brain(history)

                    total_input += itoken
                    total_output += utoken
                    total += itoken + utoken

                    if respond_obj.tool_calls:
                        respond=respond_obj.content
                        tool_call = respond_obj.tool_calls[0]
                        history.append(respond_obj.model_dump())
                        raw_args = tool_call.function.arguments
                        args_dict = json.loads(raw_args)
                        expression = args_dict["expression"]
                        calculate_done=calculate(expression)
                        tool_id = tool_call.id
                        tool_name = tool_call.function.name
                        history.append({
                            "role": "tool", "tool_call_id": tool_id,
                            "name": tool_name, "content": calculate_done
                        })
                    else:
                        respond=respond_obj.content
                        history.append({"role": "assistant", "content": respond})
                        clear_thinking()
                        show_text(respond)
                        save_memory(history)
                        break
                except Exception as e:
                    print(f"Amber: {e}")
                    show_token(total_input, total_output,total)
                    sys.exit()
                except KeyboardInterrupt:
                    clear_thinking()
                    print("Amber: Goodbye")
                    show_token(total_input, total_output, total)
                    break
        except KeyboardInterrupt:
            clear_thinking()
            print("Amber: Goodbye")
            show_token(total_input, total_output, total)
            break

if __name__ == "__main__":
    main()