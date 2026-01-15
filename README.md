# Agentic Totchef

![logo](static/logo.svg)

A minimal **AI Agent** example for managing recipes and kindergarten activities using **Ollama** locally for reasoning and tool calling. This project demonstrates building generative agents with minimal dependencies.

## Key Features

- **ReAct Agent with Ollama**: Utilizes Ollama for advanced reasoning and tool-calling capabilities.
- **Multiple Toolsets**: Includes specialized tools for home kitchen recipes (`HomeKitchenTools.py`) and kindergarten activities (`KindergartenTools.py`).
- **Flexible LLM Providers**: Supports various LLM providers through `LLMProviderFactory.py`.
- **Modular Architecture**: Clearly separated concerns for adapters, commons, core logic, and integration.
- **Works offline**: Designed to work with local Ollama models.
- **Robust error handling**: Implemented for graceful operation.
- **Verbose tracing**: Provides insights into the agent's reasoning and tool calls.

## Prerequisites

- **Python 3.10+**
- **Ollama** installed and running (`ollama serve`)
- Ollama models with tools or thinking feature (e.g., `qwen3:latest`)
- Ollama models with embedding support (e.g., `nomic-embed-text:latest`)
- `.env` file with all properties specified in the Configuration section.

## Installation

```bash
git clone https://github.com/carmelolg/agentic-totchef.git # Update with actual repo if different
cd agentic-totchef
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Create the `.env` file with the variables listed in prerequisites.

## Configuration

Edit `.env` to customize:

```
# Required
EMBEDDING_MODEL=nomic-embed-text:latest
LANGUAGE_MODEL=qwen3:latest
THINKING_MODE=True
LLM_PROVIDER=ollama

# Optional - Example API configurations (adjust as per actual services)
HOME_KITCHEN_API_HOST=http://localhost:8000/kitchen # Example placeholder
KINDERGARTEN_API_HOST=http://localhost:8000/kindergarten # Example placeholder
```

## Running the Agent

Start the interactive agent:

```bash
python agentic-totchef-chat.py # Command line chat interface
# OR
python agentic-totchef-gui-chat.py # GUI chat interface, typically available on http://localhost:8080 or similar
```
The agent will reason step-by-step, call necessary tools, and return the response.

## Running on Docker    
Create this shell script (e.g., `run-docker.sh`):
```shell
#!/bin/bash
docker build . -t agentic-totchef
docker run -d -p8080:8080 agentic-totchef
```

Run on the terminal the following commands:
```shell
chmod +x run-docker.sh
./run-docker.sh
```

## Usage Examples

**Home Kitchen Query**:

```
Input: "Give me the home kitchen vegetable available"
Output: Here the list of vegetable: ... (example output)
```

**Kindergarten Menu Query**:

```
Input: "Give me the Tuesday menu from the second week of the nursery."
Output: Main Course: Grilled Chicken with Rice, Side: Steamed Vegetables, Dessert: Fruit Salad. (example output)
```

**Generate Menu Plan**:

```
Input: "Create a healthy weekly menu plan based on the first week of the kindergarten menu."

Output:
    Monday:
      - Breakfast: Oatmeal with fresh fruits
      - Lunch: Quinoa salad with mixed vegetables
      - Dinner: Vegetable stir-fry with tofu
    ...
```  

## Project Architecture

```
.
├── lib/
│   ├── adapters/
│   │   └── outbound/
│   │       ├── LLMExecutor.py          # Executes LLM interactions and tool calls
│   │       └── ...
│   ├── commons/
│   │   ├── Constants.py                # Project-wide constants
│   │   ├── EnvironmentVariables.py     # Manages environment variables
│   │   └── MathUtils.py                # Utility functions
│   ├── core/
│   │   ├── prompts/
│   │   │   └── PromptManager.py        # Manages system prompts
│   │   ├── providers/
│   │   │   ├── LLMProvider.py          # Interface for LLM providers
│   │   │   ├── LLMProviderFactory.py   # Factory for creating LLM providers
│   │   │   ├── OllamaProvider.py       # Ollama specific LLM provider
│   │   │   └── model/                  # LLM provider configuration models
│   │   ├── service/
│   │   │   └── KnowledgeService.py     # Orchestrates knowledge retrieval and tool execution
│   │   └── tools/
│   │       ├── HomeKitchenTools.py     # Tools for home kitchen domain
│   │       └── KindergartenTools.py    # Tools for kindergarten domain
│   └── integration/
│       └── http/
│           ├── HomeKitchenHttpService.py   # HTTP client for home kitchen APIs
│           └── KindergartenHttpService.py  # HTTP client for kindergarten APIs
├── agentic-totchef-chat.py             # Command-line interface for the agent
├── agentic-totchef-gui-chat.py         # GUI interface for the agent
├── Dockerfile                          # Dockerization setup
├── run-docker.sh                       # Script to build and run Docker container
├── requirements.txt                    # Project dependencies
├── static/                             # Static assets (e.g., logo)
└── .env.example                        # Example environment variables file
```

- **OllamaLLM + Embeddings**: Local models for reasoning and context.
- **Custom tools**: Pure HTTP calls with docstrings for tool calling.
- **AgentExecutor**: Handles reasoning-action-observation loop (managed by `LLMExecutor.py` and `KnowledgeService.py`).

# License

![CC BY-NC-ND 4.0](https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png)

This project is licensed under the **Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)**.

See `LICENSE.md` for the full license text.
