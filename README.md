# pydanticai-ollama-chatbot
Pydantic AI Chatbot on Ollama with LLaMA 3.1 in Docker
🚀 A fully containerized chatbot leveraging Pydantic AI framework and Ollama's LLaMA 3.1 LLM.
Easily deployable using Docker, with support for customizable LLM models.

📌 Overview
This project provides the necessary files to deploy a Docker container running Python 3.12, with all dependencies pre-installed via requirements.txt. It features a Pydantic AI-powered chatbot that utilizes Ollama to serve the LLaMA 3.1 LLM.

✨ Key Features:
Pre-configured Docker environment for easy deployment.
Powered by Pydantic AI, ensuring structured responses and seamless interaction.
Uses Ollama as the LLM server, running Meta’s LLaMA 3.1 model.
Easily customizable LLM – swap models by updating the Dockerfile and chatbot_agent.py.
Available as a prebuilt Docker image – just pull and run!

📥 Installation & Deployment

1️⃣ Clone the Repository
```bash
git clone https://github.com/Angelitomuerte/pydanticai-ollama-chatbot.git
cd pydanticai-ollama-chatbot
```
2️⃣ Pull the Prebuilt Docker Image (Recommended)
The chatbot is available as a prebuilt container on Docker Hub:

```bash
docker pull angelmuerte/pydanticai-chatbot:latest
```
3️⃣ Run the Chatbot Container
```bash
docker run --rm -it --gpus all -p 7860:7860 angelmuerte/pydanticai-chatbot:latest
```
🔹 Note: If you are not using a GPU, omit --gpus all. If you want to mount a local project directory, add that directory in the run command as per Docker mount instructions.

🔧 Build & Run Locally (Alternative)
If you prefer building the image manually, follow these steps:

1️⃣ Install Docker (If Not Installed)
🔹 Download & Install Docker

2️⃣ Build the Docker Image
```bash
docker build -t pydanticai-chatbot .
```
🔹 Note: Be sure to copy the dockerfile into your working directory first.
3️⃣ Run the Container
```bash
docker run --rm -it --gpus all -p 7860:7860 pydanticai-chatbot
```
🔄 Customizing the LLM
You can easily swap the default LLaMA 3.1 model for another LLM.

1️⃣ Change the Model in the Dockerfile
Edit Dockerfile and update:

```dockerfile
RUN ollama pull <your_desired_model>
```
2️⃣ Update the Model Call in chatbot_agent.py
Modify the ChatbotAgent class in chatbot_agent.py:

```python
ollama_model = OpenAIModel(model_name='<your_desired_model>', base_url='http://localhost:11434/v1')
```
🔹 Note: base url may vary according to llm model.  Check Ollama documentation for more info.
🤖 Using the Chatbot
Once running, interact via CLI or Gradio UI.

CLI Mode
```bash
python3 main.py
```
Select either "cli" for commandline interface or "ui" for browswer api. 
Type exit to quit.
If you select "cli" a user prompt will appear and you may begin chat with the chatbot in the terminal.
If you select "ui", and follow the next set of instructions.

Web UI (Gradio)
Open your browser and go to:

```arduino
http://localhost:7860
```
Use the interactive web-based chat interface.

⚙️ Project Structure
```bash
pydanticAi_Ollama_Llama3.1/
│── Dockerfile              # Defines the containerized environment
│── requirements.txt        # Lists all dependencies
│── main.py                 # CLI and Gradio interface for chatbot
│── agents/
│   ├── chatbot_agent.py    # Chatbot logic using Pydantic AI
│── tools/
│   ├── utility_tools.py    # Additional tools for chatbot
└── README.md               # This file
```
📜 License
🔹 Apache 2.0

📬 Contact & Support
💬 Questions or issues? Feel free to open an issue.

🔹 🚀 Quick Start: Just Pull & Run!

```bash
docker pull angelmuerte/pydanticai-chatbot:latest
docker run --rm -it --gpus all -p 7860:7860 angelmuerte/pydanticai-chatbot:latest
```
🔥 Now you're running a Pydantic AI-powered chatbot with Ollama’s LLaMA 3.1 inside Docker! 🚀
