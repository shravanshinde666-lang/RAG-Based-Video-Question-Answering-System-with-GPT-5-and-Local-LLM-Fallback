from openai import OpenAI
from transformers import pipeline
import os

client = OpenAI()

# Load local LLM once
local_llm = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_new_tokens=120
)

def generate_answer(question, top_chunks):
    context = " ".join([c["text"] for c in top_chunks])

    prompt = f"""
Answer the question briefly using ONLY the context below.
If the answer is not in the context, say "I don't know".

Context:
{context}

Question:
{question}

Answer:
"""

    # 1️⃣ Try GPT-5 first
    try:
        response = client.responses.create(
            model="gpt-5",
            input=prompt
        )
        return response.output_text.strip()

    # 2️⃣ Fallback to local LLM
    except Exception as e:
        print("⚠️ GPT-5 unavailable → using local LLM")
        return local_llm(prompt)[0]["generated_text"].strip()
