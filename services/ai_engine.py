import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

print("API KEY:", api_key)

if not api_key:
    raise ValueError("GROQ_API_KEY is not set. Check your .env file")

client = Groq(api_key=api_key)

MODEL = "llama-3.3-70b-versatile"  # ✅ single place


# ✅ FIXED: clean questions output
def generate_questions(text):
prompt = f"""
You are an experienced interviewer.

Analyze the complete resume below and generate exactly 50 interview questions with answers.

Rules:

* Questions must be based on the resume.
* Cover Skills, Projects, Experience, Education, Certifications, and Technologies.
* Use simple and beginner-friendly language.
* The answer should be short, clear, and easy to understand.
* Avoid complex technical jargon unless mentioned in the resume.
* Format:

Q1: Question
A1: Answer

Q2: Question
A2: Answer

Continue until 50 questions and answers.

Resume:
{text}
"""


    res = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    content = res.choices[0].message.content

    # ✅ Extract only valid questions
    questions = []
    for line in content.split("\n"):
        line = line.strip()
        if line and line[0].isdigit():
            questions.append(line)

    return questions


# ✅ Slightly improved evaluation formatting
def evaluate_answer(q, a):
    prompt = f"""
    Evaluate the answer.

    Question: {q}
    Answer: {a}

    Provide:
    Score: <score>

    Feedback:
    <feedback in 1-2 lines>

    Ideal Answer:
    <ideal answer in 1-2 lines>
    """

    res = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    return res.choices[0].message.content
