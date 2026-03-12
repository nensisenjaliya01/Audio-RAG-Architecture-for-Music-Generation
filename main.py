import os

os.system("python src/preprocess_audio.py")

os.system("python src/generate_embeddings.py")

os.system("python src/vector_store.py")

os.system("python src/similarity_search.py")

os.system("python src/music_generation.py")