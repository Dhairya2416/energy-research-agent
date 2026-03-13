from crewai import Agent
from config import get_llm_model

research_agent = Agent(
    role="Energy Researcher",
    goal="Find accurate and recent information about energy topics",
    backstory="Expert in renewable and non-renewable energy research",
    llm=get_llm_model(),
    verbose=True
)
