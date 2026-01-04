import joblib
import numpy as np
from sentence_transformers import SentenceTransformer
from answer_generator import generate_answer

EMBEDDINGS_FILE = "embeddings/chunk_embeddings.pkl"

print("Loading embeddings...")
df = joblib.load(EMBEDDINGS_FILE)

model = SentenceTransformer("all-MiniLM-L6-v2")


def search(query, top_k=3, min_score=0.25):
    query_embedding = model.encode(query)

    embeddings = np.array(df["embedding"].tolist())
    scores = np.dot(embeddings, query_embedding)

    top_indices = scores.argsort()[-top_k:][::-1]

    results = []
    for idx in top_indices:
        if scores[idx] < min_score:
            continue

        results.append({
            "video": df.iloc[idx]["video"],
            "chunk_id": df.iloc[idx]["chunk_id"],
            "text": df.iloc[idx]["text"][:400] + "...",
            "score": float(scores[idx])
        })

    return results


if __name__ == "__main__":
    while True:
        query = input("\nAsk a question (or type 'exit'): ").strip()

        if not query:
            print("❌ Please type a question.")
            continue

        if query.lower() == "exit":
            break

        top_chunks = search(query)

        if not top_chunks:
            print("\n⚠️ I could not find a confident answer from the course content.")
            continue

        final_answer = generate_answer(query, top_chunks)

        print("\n" + "=" * 50)
        print("FINAL ANSWER:\n")
        print(final_answer)

        print("\nSOURCE:")
        shown = set()
        for chunk in top_chunks:
            if chunk["video"] not in shown:
                print(f"- {chunk['video']}")
                shown.add(chunk["video"])

        print("=" * 50)
