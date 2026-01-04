import os
import json

TRANSCRIPTS_DIR = "transcripts"
CHUNKS_DIR = "chunks"

os.makedirs(CHUNKS_DIR, exist_ok=True)

CHUNK_SIZE = 500      # words per chunk
OVERLAP = 100         # overlap words

all_chunks = []

for file in os.listdir(TRANSCRIPTS_DIR):
    if not file.endswith(".txt"):
        continue

    file_path = os.path.join(TRANSCRIPTS_DIR, file)

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    words = text.split()
    total_words = len(words)

    start = 0
    chunk_id = 0

    while start < total_words:
        end = start + CHUNK_SIZE
        chunk_words = words[start:end]

        chunk_text = " ".join(chunk_words)

        chunk_data = {
            "video": file,
            "chunk_id": chunk_id,
            "text": chunk_text
        }

        all_chunks.append(chunk_data)

        chunk_id += 1
        start += CHUNK_SIZE - OVERLAP

# save all chunks to one json file
output_file = os.path.join(CHUNKS_DIR, "all_chunks.json")

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(all_chunks, f, indent=2)

print(f"✅ Chunking complete. Total chunks created: {len(all_chunks)}")
