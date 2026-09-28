import json
import re
from gemini_client import generate

def clean_json(text: str) -> str:
    text = text.strip()
    text = re.sub(r"^```(?:json)?\s*", "", text, flags=re.I)
    text = re.sub(r"\s*```$", "", text)
    return text.strip()

def generate_quiz(content: str) -> list:
    prompt = f"""
Create exactly 3 multiple-choice questions from this educational content:

{content}

Return ONLY valid JSON:
[
  {{"question":"Question text","options":["A","B","C","D"],"answer":"A"}}
]

Rules:
- exactly 3 questions
- exactly 4 options per question
- answer must be A, B, C, or D
- questions must be based on the supplied content
"""
    data = json.loads(clean_json(generate(prompt)))

    if not isinstance(data, list) or len(data) != 3:
        raise ValueError("Gemini did not return exactly 3 questions.")

    for q in data:
        if not all(k in q for k in ("question", "options", "answer")):
            raise ValueError("Invalid quiz structure.")
        if len(q["options"]) != 4:
            raise ValueError("Each question must have 4 options.")
        if q["answer"] not in ["A", "B", "C", "D"]:
            raise ValueError("Invalid correct answer.")

    return data
