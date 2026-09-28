from gemini_client import generate

def explain_concept(topic: str) -> str:
    return generate(f"""
You are EduGenie, an educational assistant.
Explain this topic in simple, clear language for a student:

{topic}

Use a short definition, step-by-step explanation, and a simple example when useful.
Avoid unnecessary jargon and do not invent facts.
""")
