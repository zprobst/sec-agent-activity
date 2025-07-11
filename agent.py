import sys
from datetime import datetime
from pathlib import Path
from typing import List

from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama

MODEL_NAME = "llama3.2:3b"
LLM = ChatOllama(model=MODEL_NAME)
ALLOWED_EXTENSIONS = [".py", ".md"]

SYSTEM_PROMPT = """
You are a security analyst.
You are given a directory of code and you need to find security issues in the
code. Your goal is to search for security issues in the code. Focus on
design-level security issues such as authorization gaps, data flow problems,
and design decisions that SAST/SCA tools cannot detect.
"""


@tool
def current_time() -> str:
    """Returns the current date and time

    Returns:
        str: The current date and time in ISO format.
    """
    return datetime.now().isoformat()


@tool
def list_files(path: str) -> List[str]:
    """Reads all the files in a directory and returns a list of file names

    Args:
        path (str): The path to the directory to list files from.

    Returns:
        str: A list of file names in the directory.
    """
    dir = Path(path)
    files = [
        str(p.relative_to(dir))
        for p in dir.rglob("*")
        if p.is_file() and p.suffix in ALLOWED_EXTENSIONS
    ]
    print(f"Found {len(files)} files in {path}")
    return files


def build_agent():
    tools = [current_time]
    agent = create_react_agent(
        model=LLM,
        tools=tools,
        prompt=SYSTEM_PROMPT,
    )
    return agent


def main():
    agent = build_agent()
    directory = sys.argv[1]
    message = f"Search the directory {directory} for security issues."
    input = {"messages": [{"role": "user", "content": message}]}
    state = agent.invoke(input)
    for message in state["messages"]:
        print(message.content)


if __name__ == "__main__":
    main()
