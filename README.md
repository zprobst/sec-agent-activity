# Agentic Learning Exercise: Security Architecture Review with LangGraph

This exercise will teach you how to build an agentic AI system using LangGraph 
that can analyze software repositories for **architectural and design-level security issues** that SAST/SCA tools cannot detect. 

## Prerequisites

- Python 3.8+
- Ollama installed and running locally
- Basic understanding of Python and software security concepts

## Setup Instructions

1. **Pull a local model**:
   ```bash
   ollama pull llama3.2:3b
   ```

2. **Install Python dependencies**:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   uv venv --python 3.11
   uv pip install -r requirements.txt
   ```

## Activity 0: Getting Started

### Objective
Understand the basic concepts of LangGraph and architectural security analysis.

### Steps

1. **Explore the Agent Structure**
   - Open `agent.py` and examine the existing code.

2. **Run the Basic Agent**
   ```bash
   uv run python agent.py ./test-repo
   ```

Notice the output here is not particularly helpful. We need to add more tools to the agent.
It can only list files in the directory so it cannot develop a comprehensive understanding of the codebase.

## Activity 1: Bind an Existing Tool

### Objective
Learn how to bind an existing tool to an agent.

### Steps

1. **Add a Read File Tool**
   - Open `agent.py` and add the `list_files` tool to the agent.

2. **Run the Agent with the New Tool**

## Activity 2: Build a Tool

### Objective
Learn how to build a tool.

### Steps
1. **Add a Read File Tool**
    - Open `agent.py` and add the `read_file` tool to the agent that takes a file path and returns the contents of the file.
  
2. **Run the Agent with the New Tool**
    - Run the agent again.
    - Notice that the agent can now read files in the directory and start to draw some conclusions.

## Activity 3: Build a Very Basic Human-in-the-Loop Agent

### Objective
    Learn how to build a human-in-the-loop agent to blend the agent's knowledge with expert knowledge.

### Steps

1. **Add a Human-in-the-Loop Tool**
   - Open `agent.py` and add a new tool that allows the agent to ask an expert security professional for more information.
   - For the purposes of this, we can converse via the terminal via an `input()` call. 
   - Take as tool input a `question` and return the answer as a string.

2. **Run the Agent with the New Tool**
    - Notice that the agent may or many not ask for expert help. If you are having trouble, tune the prompt to ask for expert help/confirmation.
