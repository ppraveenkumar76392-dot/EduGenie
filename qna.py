from gemini_client import generate

def answer_question(question: str) -> str:
    return generate(f"""
You are EduGenie, a helpful academic Q&A assistant.
Answer this question accurately and concisely:

{question}

Give the direct answer first, then a brief explanation.
If it is ambiguous, say so instead of guessing.
""")
