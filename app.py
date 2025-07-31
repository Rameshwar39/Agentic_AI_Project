import gradio as gr
from dotenv import load_dotenv
from utils import read_pdf_text, read_text_file
from chatbot import get_reply
from evaluator import check_reply
import os

load_dotenv()

name = "Rameshwar"
summary = read_text_file("me/summary.txt")
linkedin = read_pdf_text("me/linkedin.pdf")

def chat(message, history):
    reply = get_reply(name, summary, linkedin, message, history)
    evaluation = check_reply(name, summary, linkedin, message, reply, history)

    if evaluation.is_acceptable:
        return reply
    else:
        print("response rejected.")
        print("Feedback :", evaluation.feedback)
        # simple retry
        return get_reply(name, summary, linkedin, message, history)

gr.ChatInterface(chat, type="messages").launch()
