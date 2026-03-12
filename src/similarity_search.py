import faiss
import numpy as np
import json

index = faiss.read_index("vector_store/audio.index")

with open("embeddings/audio_embeddings.json") as f:
    data = json.load(f)

query_vector = np.array([data[0]["embedding"]]).astype("float32")

distances, indices = index.search(query_vector, 3)

print("Similar audio files:\n")

for i in indices[0]:
    print(data[i]["file"])