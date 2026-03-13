import streamlit as st

from config import get_missing_required_env
from crew import run_research
from tools.file_writer import save_report

st.title("Energy Research Agent")

query = st.text_input("Enter an energy research topic:")

if st.button("Run Research"):
    missing = get_missing_required_env()
    if missing:
        st.error(
            "Missing required environment variables: "
            + ", ".join(missing)
        )
        st.info(
            "Set them in your shell before running Streamlit, for example:\n"
            "`$env:GROQ_API_KEY='your_key'`\n"
            "`$env:TAVILY_API_KEY='your_key'`"
        )
        st.stop()

    if not query.strip():
        st.error("Please enter a topic before running research.")
        st.stop()

    try:
        result = run_research(query)
    except Exception as exc:
        message = str(exc)
        lowered = message.lower()
        if "insufficient_quota" in message:
            st.error(
                "LLM provider quota exceeded for the configured API key. "
                "Add billing/credits or use a different key."
            )
        elif "invalid_api_key" in lowered or "invalid api key" in lowered:
            st.error(
                "Invalid GROQ_API_KEY. Use a valid Groq key in your .env file."
            )
        else:
            st.error(f"Research run failed: {message}")
        st.stop()

    save_report(result)
    st.success("Research completed.")
    st.write(result)
