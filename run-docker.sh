#!/bin/bash

# Start Ollama in the background
ollama serve &

# Wait for Ollama to be ready
echo "Waiting for Ollama to start..."
while ! curl -s http://localhost:11434 > /dev/null; do
    sleep 1
done
echo "Ollama started."

# Pull the model
echo "Pulling qwen3:1.7b language model..."
ollama pull qwen3:1.7b
echo "Pulling nomic-embed-text:latest embedding model..."
ollama pull nomic-embed-text:latest

# Start the NiceGUI application
echo "Starting the Hogwarts GUI Chat..."
python agentic-totchef-gui-chat.py --host 0.0.0.0
