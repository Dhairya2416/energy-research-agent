from crewai import Agent
from config import get_llm_model

writer_agent = Agent(
    role="Technical Writer",
    goal="Create structured and easy-to-read research reports",
    backstory="Writes professional energy research documents",
    llm=get_llm_model(),
    verbose=True
)
