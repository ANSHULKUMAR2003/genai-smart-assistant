from langchain_community.llms import Ollama


llm = Ollama(model="phi3")  # or "mistral"

def generate_challenge_questions(doc_text):
    prompt = f"Generate 3 logic-based or comprehension-focused questions based on this document:\n\n{doc_text}"
    return llm(prompt)
