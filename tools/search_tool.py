import json
import os
from tavily import TavilyClient


def run_search(query: str) -> str:
    if not os.getenv("TAVILY_API_KEY"):
        raise RuntimeError("Missing TAVILY_API_KEY. Set it before running search.")

    client = TavilyClient()
    results = client.search(query=query, max_results=5)
    return json.dumps(results, ensure_ascii=False)
