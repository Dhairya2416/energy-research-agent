import os
from dotenv import load_dotenv

load_dotenv()
required_env = ["GROQ_API_KEY", "TAVILY_API_KEY"]
default_llm_model = "groq/llama-3.1-8b-instant"


def get_missing_required_env() -> list[str]:
    return [name for name in required_env if not os.getenv(name)]


def ensure_required_env() -> None:
    missing = get_missing_required_env()
    if missing:
        missing_list = ", ".join(missing)
        raise RuntimeError(
            f"Missing required environment variables: {missing_list}. "
            "Set them before running the app."
        )


def get_llm_model() -> str:
    return os.getenv("LLM_MODEL", default_llm_model)
