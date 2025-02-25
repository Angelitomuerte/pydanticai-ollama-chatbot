import os
import requests
from pydantic_ai.tools import Tool  

@Tool
def search_internet(query: str) -> str:
    """Performs a basic internet search and returns the top result."""
    url = f"https://api.duckduckgo.com/?q={query}&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("AbstractText", "No relevant result found.")
    return "Failed to perform search."

@Tool
def read_file(filepath: str) -> str:
    """Reads and returns the content of a local file."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {e}"

@Tool
def save_file(filename: str, content: str) -> str:
    """Saves provided content to a local file."""
    try:
        save_path = os.path.join("/app/saved_files", filename)
        with open(save_path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"File saved to {save_path}"
    except Exception as e:
        return f"Error saving file: {e}"
