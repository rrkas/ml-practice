# memory.py
class ResearchMemory:
    """Simple in-process memory for storing notes during multi-step research."""

    def __init__(self):
        self.notes = []

    def add(self, text):
        self.notes.append(text)

    def dump(self):
        return "\n\n".join(self.notes)


# tools.py
from langchain.tools import tool
from duckduckgo_search import DDGS
import requests
from bs4 import BeautifulSoup


# ---------------------
# 1) Web Search Tool
# ---------------------
@tool
def web_search(query: str, max_results: int = 5) -> list:
    """Search the web and return a list of results (title, link, snippet)."""
    results = DDGS().text(query, max_results=max_results)
    return results


# ---------------------
# 2) Web Page Scraper
# ---------------------
@tool
def scrape_url(url: str) -> str:
    """Scrapes visible text from a webpage."""
    try:
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        text = soup.get_text(separator="\n")
        return text[:5000]  # limit to 5k chars
    except:
        return "Failed to scrape URL."


global_memory = ResearchMemory()


@tool
def write_memory(note: str) -> str:
    """Store research notes into memory."""
    global_memory.add(note)
    return "Memory stored."


# agent.py
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_core.prompts import ChatPromptTemplate


# ---------------------------------------
# 1) LLM — GPT-4/5 with tool calling
# ---------------------------------------
llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0,
)


# ---------------------------------------
# 2) Tools available to the agent
# ---------------------------------------
tools = [web_search, scrape_url, write_memory]


# ---------------------------------------
# 3) Prompt Template (self-planning agent)
# ---------------------------------------
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an autonomous research agent.

Your job:
1. Break the query into smaller research subtasks.
2. Use the tools (web_search, scrape_url) when needed.
3. Store key findings into memory using the FORMAT below.
4. After finishing all steps, generate a structured final report.

You are an autonomous research agent.

When you find an important point, call the tool `write_memory` like:
    {"tool": "write_memory", "note": "<text>"}

Do NOT write MEMORY: in plain text.
Always use the memory tool for saving notes.

Final output MUST be a structured JSON report:
{
   "summary": "...",
   "key_points": [...],
   "references": [...]
}
""",
        ),
        ("user", "{query}"),
    ]
)


# ---------------------------------------
# 4) Create Agent (Tool Calling Agent)
# ---------------------------------------
agent = create_agent(llm, tools, system_prompt=prompt, debug=True)

# run.py

query = """
Research the latest progress on multimodal AI agents in 2024-2025.
Focus on:
- open-source frameworks
- tool-using agents
- autonomous web-research agents
Produce a structured summary.
"""

result = agent.invoke({"query": query})

print("\n\n=== FINAL REPORT ===\n")
print(result["output"])

print("\n\n=== INTERNAL MEMORY ===\n")
print(global_memory.dump())
