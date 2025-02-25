# Use NVIDIA's CUDA-enabled base image for Python 3.12
FROM nvidia/cuda:12.3.2-runtime-ubuntu22.04

# Set working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl python3 python3-pip python3-dev python3-venv git \
    && rm -rf /var/lib/apt/lists/*

# Install Ollama (latest version)
RUN curl -fsSL https://ollama.com/install.sh | sh



# Copy only the requirements file first (to leverage Docker caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy all project files (bind mount will override this)
COPY . /app

# Expose port for Gradio UI
EXPOSE 7860

# Set NVIDIA environment variables for CUDA support
ENV NVIDIA_VISIBLE_DEVICES=all
ENV NVIDIA_DRIVER_CAPABILITIES=compute,utility

# initialize ollama server, pull ollama model, and start chatbot
CMD ollama serve & sleep 10 && ollama pull llama3.1 && bash

