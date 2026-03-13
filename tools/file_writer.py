def save_report(content):
    with open("knowledge_base/energy_reports.md", "a", encoding="utf-8") as f:
        f.write("\n\n---\n\n")
        f.write(str(content))
