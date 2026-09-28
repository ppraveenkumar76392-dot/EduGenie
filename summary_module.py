from gemini_client import generate

def summarize_text(content: str) -> str:
    return generate(f"""
You are EduGenie, an educational summarization assistant.
Summarize this content for quick revision:

{content}

Preserve important facts and ideas, remove repetition, and use clear headings or bullet points.
Do not add unsupported information.
""")
