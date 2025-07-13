from langchain_community.llms import Ollama

llm = Ollama(model="phi3")  # Use "mistral" if preferred

def ask_question(doc_text, user_question):
    short_doc = doc_text[:3000]  # truncate for performance
    prompt = f"""
Answer the following question based only on the content of the document below.
Be clear and concise. Respond in 2–3 lines max.

Document:
{short_doc}

Question:
{user_question}
"""
    return llm(prompt)

