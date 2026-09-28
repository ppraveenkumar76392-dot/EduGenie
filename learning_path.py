from gemini_client import generate

def get_learning_recommendations(topic: str) -> str:
    return generate(f"""
You are EduGenie, a personalized learning-path assistant.
Create a structured learning path for:

{topic}

Start at beginner level and progress to advanced.
For each stage include key topics, practical activities/projects, and useful resource types.
Mention prerequisites when needed and keep it practical for a student.
""")
