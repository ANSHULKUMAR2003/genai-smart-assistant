# 🤖 GenAI Smart Research Assistant (Offline)

This project is a **fully local, offline GenAI assistant** built using **Streamlit**, **LangChain**, and **Ollama**. It helps users interact with PDF documents by answering questions, generating logic-based challenges, and evaluating user responses — all without relying on the OpenAI API or internet access.

---

## 🧠 Features

- 📄 **PDF/Text Upload**  
  Upload any PDF or `.txt` file for instant processing.

- 📝 **Auto Summarization**  
  Generates a short summary (≤150 words) using local LLMs like `phi3`.

- 💬 **Ask Anything**  
  Users can ask free-form questions based on the uploaded document.

- 🧠 **Challenge Me Mode**  
  Automatically generates 3 logic-based or comprehension questions from the file.

- ✅ **Answer Evaluation**  
  User answers are evaluated with feedback in ≤3 lines using local model reasoning.

- 🔒 **Runs 100% Locally**  
  No API key or internet required — uses Ollama + LangChain for inference.

---

## 🏗️ Project Structure
genai_assistant/
├── app.py # Streamlit frontend
├── requirements.txt # Python dependencies
├── .gitignore
├── utils/ # Core logic modules
│ ├── pdf_parser.py
│ ├── summarizer.py
│ ├── qa.py
│ └── question_generator.py


---

## 🛠️ Setup Instructions (Run Locally)

### ✅ Prerequisites
- Python 3.10+
- [Ollama](https://ollama.com) installed (for running local LLMs)
- Git installed (optional but recommended)

### 🧱 Step-by-Step

1. **Clone the repository**  
   ```bash
   git clone https://github.com/YOUR_USERNAME/genai-smart-assistant.git
   cd genai-smart-assistant
2. **Install dependencies**
     pip install -r requirements.txt
   
3. **Pull your local LLM**
     ollama pull phi3

4.  **Run the app**
     streamlit run app.py
    
**⚙️ Architecture & Reasoning Flow**
    1. User uploads PDF → Parsed using PyMuPDF
    2. Summary is generated via LLM prompt (LangChain + Ollama)
    3. In Ask Mode:
       - User inputs question
       - Prompt sent to model with document context
    4. In Challenge Mode:
       - Model generates 3 logic questions
       - User answers each
   - Each answer is evaluated based on document & instructions

**🧪 Example Use Cases**
Quickly analyze academic PDFs

Challenge yourself with logic questions from reports

Prepare for viva or exams using your own notes

Run safe AI assistants without sharing documents online


**🛡️ Security & Privacy**
    ✅ All data is processed locally

    ❌ No internet or cloud used

    🔒 No API keys or tracking


Developed by Anshul Kumar
Internship Project Submission for EZ




