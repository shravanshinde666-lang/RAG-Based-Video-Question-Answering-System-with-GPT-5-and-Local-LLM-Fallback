🎥 RAG-Based Video Question Answering System
with GPT-5 and Local LLM Fallback

A Retrieval-Augmented Generation (RAG) system that allows users to ask natural language questions over video content.
The system transcribes videos, creates embeddings, performs semantic search, and generates accurate answers using GPT-5, with an automatic local LLM fallback when API quota is unavailable.

🚀 Features

🎧 Speech-to-Text using OpenAI Whisper

🧩 Chunking of transcripts with metadata

🔎 Semantic Search using sentence embeddings

🧠 Answer Generation

GPT-5 (via OpenAI API)

Local LLM fallback (Flan-T5) when API quota is exceeded

📚 Source citation from video transcripts

🔐 Safe against hallucinations (answers only from retrieved context)

🏗️ Project Architecture
Videos
   ↓
Whisper Transcription
   ↓
Chunking + Metadata
   ↓
Embeddings (Sentence Transformers)
   ↓
Semantic Search
   ↓
Answer Generator (GPT-5 / Local LLM)

📂 Folder Structure
RAG_PROJECT_CLEAN/
│
├── videos/               # Input video files
├── audios/               # Extracted audio files
├── transcripts/          # Whisper transcriptions
├── chunks/               # Chunked transcript JSON
├── embeddings/           # Saved embeddings (.pkl)
│
├── speech_to_text.py     # Video/audio → text
├── chunk_transcripts.py # Chunking logic
├── create_embeddings.py # Embedding generation
├── semantic_search.py   # Query + retrieval
├── answer_generator.py  # GPT-5 / local LLM answers
│
├── requirements.txt
├── .gitignore
└── README.md

⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/shravanshinde666-lang/RAG-Based-Video-Question-Answering-System-with-GPT-5-and-Local-LLM-Fallback.git
cd RAG-Based-Video-Question-Answering-System-with-GPT-5-and-Local-LLM-Fallback

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

🔑 OpenAI API Setup (Optional but Recommended)
Set API Key (Windows PowerShell)
setx OPENAI_API_KEY "your_api_key_here"


Restart terminal after setting the key.

If no API key is found, the system automatically switches to the local LLM.

▶️ How to Run the Pipeline
1️⃣ Transcribe Videos
python speech_to_text.py

2️⃣ Chunk Transcripts
python chunk_transcripts.py

3️⃣ Create Embeddings
python create_embeddings.py

4️⃣ Ask Questions 🎯
python semantic_search.py

💬 Example Interaction
Ask a question: What is the purpose of semantic tags?

FINAL ANSWER:
Semantic tags help define the structure of a webpage, improve SEO, 
and enhance accessibility by allowing browsers and screen readers 
to better understand content.

SOURCE:
- 11_Semantic_Tags__in_HTML.txt

🧠 Models Used
Component	Model
Speech-to-Text	OpenAI Whisper
Embeddings	all-MiniLM-L6-v2
Primary LLM	GPT-5
Fallback LLM	google/flan-t5-base
🛡️ Safety & Reliability

Answers are generated ONLY from retrieved transcript chunks

If no relevant chunks are found, the system refuses to answer

Prevents hallucination and off-topic responses

🌱 Future Improvements

⏱ Timestamp-level answers

🌐 Web UI (Streamlit / React)

⚡ FAISS for faster retrieval

🗂 Multi-course / multi-folder support

📈 Confidence-scored answers

👨‍💻 Author

Shravan Shinde
B.Tech CSE | AI & Data Science
GitHub: https://github.com/shravanshinde666-lang

⭐ If you like this project

Give it a ⭐ on GitHub — it really helps!
