# Agentic AI Resume Chatbot

An **agentic AI LLM-based chatbot** that allows users to interact with their **LinkedIn profile (PDF)** and a **summary file**.  
It provides contextual answers through a **Gradio interface** and integrates **Geekseek** for automated response evaluation.

---

## 🚀 Features
- 📄 Upload a **LinkedIn profile PDF** and **summary file**  
- 🤖 **Agentic AI LLM** generates answers based on profile data  
- 💬 **Gradio chatbot** interface for interactive Q&A  
- 📊 **Geekseek evaluator** provides response scoring and feedback  
- 🔑 `.env` file support for managing API keys securely  

---

## 📂 Project Structure
```
├── app.py          # Main entry point (runs Gradio app)
├── chatbot.py      # Chatbot logic (LLM-based response generation)
├── evaluator.py    # Geekseek evaluator integration
├── prompts.py      # Predefined prompts/templates
├── utils.py        # Helper functions (PDF parsing, file handling, etc.)
├── .env            # Environment variables (API keys, configs)
├── requirements.txt# Python dependencies
└── README.md       # Documentation
```

---

## ⚙️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/Rameshwar39/Agentic_AI_Project.git
cd profile-chatbot
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set environment variables**  
Create a `.env` file in the project root:
```
OPENAI_API_KEY=your_openai_api_key
GEEKSEEK_API_KEY=your_geekseek_api_key
```

---

## ▶️ Usage

Run the Gradio app:
```bash
python app.py
```

Then open the **local URL** shown in the terminal (default: `http://127.0.0.1:7860`).

---

## 🧩 Evaluation with Geekseek

- Each chatbot response is passed through **Geekseek** for evaluation.  
- Evaluation includes:  
  - ✅ Relevance  
  - ✅ Accuracy  
  - ✅ Clarity  

Scores and feedback are displayed alongside chatbot answers.

---

## 🛠️ Tech Stack
- **Python 3.9+**  
- **Gradio** → Chatbot interface  
- **OpenAI / HuggingFace LLM** → Core AI responses  
- **Geekseek** → Evaluation module  
- **PyPDF2 / pdfminer** → Resume PDF parsing  

---

## 📌 Future Enhancements
- 🔹 Multi-resume upload (compare different profiles)  
- 🔹 Support for **DOCX** resumes  
- 🔹 Improved evaluator scoring system  
- 🔹 Deployable on **Hugging Face Spaces / Streamlit Cloud**  

---

## 🤝 Contributing
Contributions, issues, and feature requests are welcome!  
Feel free to open a PR or raise an issue.

---

## 📜 License
This project is licensed under the **MIT License**.
