import faiss
import numpy as np
import json
import os

with open("embeddings/audio_embeddings.json") as f:
    data = json.load(f)

vectors = [d["embedding"] for d in data]

vectors = np.array(vectors).astype("float32")

dimension = vectors.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(vectors)

os.makedirs("vector_store", exist_ok=True)

faiss.write_index(index, "vector_store/audio.index")

print("Vector store created")