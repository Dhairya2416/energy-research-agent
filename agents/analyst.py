from crewai import Agent
from config import get_llm_model

analyst_agent = Agent(
    role="Energy Analyst",
    goal="Analyze and validate research findings",
    backstory="Senior energy industry analyst",
    llm=get_llm_model(),
    verbose=True
)
