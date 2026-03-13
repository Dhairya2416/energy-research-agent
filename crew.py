from crewai import Crew, Task
from agents.researcher import research_agent
from agents.analyst import analyst_agent
from agents.writer import writer_agent
from tools.search_tool import run_search

task = Task(
    description=(
        "Research and summarize this energy topic: {topic}\n\n"
        "Use this web research context as your source material:\n{web_context}\n\n"
        "Return a final, human-readable report with:\n"
        "1) Key facts\n"
        "2) Current trends\n"
        "3) Brief implications\n"
        "4) Sources section listing referenced links/titles.\n"
        "Do not return tool-call markup."
    ),
    expected_output=(
        "A concise, human-readable research summary with key facts, trends, "
        "implications, and cited sources."
    ),
    agent=research_agent,
)

crew = Crew(
    agents=[research_agent, analyst_agent, writer_agent],
    tasks=[task],
    verbose=True
)


def run_research(topic: str) -> str:
    web_context = run_search(topic)
    result = crew.kickoff(inputs={"topic": topic, "web_context": web_context})
    return str(result)
