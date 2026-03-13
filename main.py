from crew import run_research
from config import ensure_required_env


def run(topic: str) -> str:
    ensure_required_env()
    return run_research(topic)


if __name__ == "__main__":
    user_topic = input("Enter an energy research topic: ").strip()
    if not user_topic:
        raise ValueError("Topic cannot be empty.")
    try:
        print(run(user_topic))
    except Exception as exc:
        message = str(exc)
        lowered = message.lower()
        if "insufficient_quota" in message:
            raise RuntimeError(
                "LLM provider quota exceeded for the configured API key. "
                "Add billing/credits or use a different key."
            ) from exc
        if "invalid_api_key" in lowered or "invalid api key" in lowered:
            raise RuntimeError(
                "Invalid GROQ_API_KEY. Use a valid Groq key in your .env file."
            ) from exc
        raise
