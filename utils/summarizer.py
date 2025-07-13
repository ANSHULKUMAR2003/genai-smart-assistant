from langchain_community.llms import Ollama


llm = Ollama(model="phi3")  # or "mistral"

def generate_summary(doc_text):
    prompt = f"Summarize the following document in no more than 150 words:\n\n{doc_text}"
    return llm(prompt)
