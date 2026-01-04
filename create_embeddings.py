import json
import pandas as pd
from sentence_transformers import SentenceTransformer
import joblib
import os

CHUNKS_FILE = "chunks/all_chunks.json"
EMBEDDINGS_DIR = "embeddings"
os.makedirs(EMBEDDINGS_DIR, exist_ok=True)

print("Loading chunks...")
with open(CHUNKS_FILE, "r", encoding="utf-8") as f:
    chunks = json.load(f)

print(f"Total chunks loaded: {len(chunks)}")

texts = [chunk["text"] for chunk in chunks]

print("Loading embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Creating embeddings...")
embeddings = model.encode(texts, show_progress_bar=True)

df = pd.DataFrame(chunks)
df["embedding"] = embeddings.tolist()

output_path = os.path.join(EMBEDDINGS_DIR, "chunk_embeddings.pkl")
joblib.dump(df, output_path)

print(f"✅ Embeddings saved to {output_path}")
