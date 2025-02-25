import gradio as gr
from agents.chatbot_agent import ChatbotAgent

def chat_cli():
    """
    CLI interaction mode for chatbot.
    """
    chatbot = ChatbotAgent()
    print("Chatbot initialized. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Exiting chat.")
            break

        response = chatbot.chat(user_input)
        print(f"Chatbot: {response}\n")


def chat_ui(message: str) -> str:
    """
    Gradio UI interaction mode for chatbot.
    """
    chatbot = ChatbotAgent()
    try:
        return chatbot.chat(message)  # Fully synchronous
    except Exception as e:
        return f"Error: {str(e)}"


def main():
    """
    Main function to start the chatbot in CLI or UI mode.
    """
    mode = input("Enter 'cli' for terminal chat or 'ui' for Gradio chat: ").strip().lower()

    if mode == "cli":
        chat_cli()

    elif mode == "ui":
        print("Starting Gradio instance on port 7860...")
        interface = gr.Interface(
            fn=chat_ui,  # Properly launches chatbot UI
            inputs="text",
            outputs="text",
            title="Chatbot UI",
            live=True
        )
        interface.launch(server_name="0.0.0.0", server_port=7860, share=False)

    else:
        print("Invalid mode. Please enter 'cli' or 'ui'.")

if __name__ == "__main__":
    main()
