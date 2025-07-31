from openai import OpenAI
from prompts import get_chat_prompt
import os

load_dotenv(override=True)

openai_api_key = os.getenv('OPENAI_API_KEY')
openai = OpenAI(api_key=openai_api_key)

def get_reply(name, summary, linkedin, message, history):
    system = get_chat_prompt(name, summary, linkedin)
    messages = [{"role": "system", "content": system}] + history + [{"role": "user", "content": message}]
    response = openai.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
    return response.choices[0].message.content
