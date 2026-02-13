import openai
from prompts import RESUME_PROMPT

def generate_resume(api_key, name, role, experience, skills, education):
    openai.api_key = api_key

    prompt = RESUME_PROMPT.format(
        name=name,
        role=role,
        experience=experience,
        skills=skills,
        education=education
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert resume writer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content
