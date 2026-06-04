import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is not set. Check your .env file")

# Initialize Groq client
client = Groq(api_key=api_key)

MODEL = "llama-3.3-70b-versatile"


def generate_questions(text):
    prompt = f"""
You are an experienced interviewer.

Carefully analyze the complete resume below.

Generate exactly 50 interview questions.

Rules:
- Questions must be based on the resume.
- Cover Skills, Projects, Experience, Education, Certifications, and Technologies.
- Use simple and beginner-friendly language.
- Keep each question on a single line.
- Do not provide answers.
- Do not provide explanations.
- Return only the questions.

Resume:
{text}
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = response.choices[0].message.content

    questions = []

    for line in content.split("\n"):
        line = line.strip()

        if line:
            questions.append(line)

    return questions[:50]


def evaluate_answer(question, answer):
    prompt = f"""
Evaluate the candidate's answer.

Question:
{question}

Answer:
{answer}

Provide:

Score: <score out of 10>

Feedback:
<1-2 lines>

Ideal Answer:
<1-2 lines>
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
