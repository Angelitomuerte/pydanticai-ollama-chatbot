import requests

class ChatbotAgent:
    def __init__(self, model_name="llama3.1"):
        """
        Initialize the chatbot agent with the specified model.
        """
        self.base_url = "http://localhost:11434/v1/chat/completions"
        self.model_name = model_name

    def chat(self, message: str) -> str:
        """
        Process user input and return the chatbot's response in one full response.
        """
        try:
            payload = {
                "model": self.model_name,
                "messages": [{"role": "user", "content": message}]
            }
            headers = {"Content-Type": "application/json"}
            
            response = requests.post(self.base_url, json=payload, headers=headers)
            response_json = response.json()

            # Extracting the assistant's response
            if "choices" in response_json and response_json["choices"]:
                return response_json["choices"][0]["message"]["content"]
            else:
                return "Error: No valid response from the model."

        except Exception as e:
            return f"Error: {str(e)}"
