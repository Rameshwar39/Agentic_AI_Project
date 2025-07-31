from openai import OpenAI
from prompts import get_eval_prompt, format_eval_input
from pydantic import BaseModel
import os

class Evaluation(BaseModel):
    is_acceptable: bool
    feedback: str

deepseek = OpenAI(
    api_key=GEEKSEEK_API_KEY,
    base_url="https://api.deepseek.com/v1"
    )

def check_reply(name, summary, linkedin, message, reply, history) -> Evaluation:
    system = get_eval_prompt(name, summary, linkedin)
    user_input = format_eval_input(message, reply, history)

    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": user_input}
    ]

    response = deepseek.chat.completions.create(
        model="deepseek-chat",
        messages=messages
    )

    content = response.choices[0].message.content
    return Evaluation.parse_raw(content)
