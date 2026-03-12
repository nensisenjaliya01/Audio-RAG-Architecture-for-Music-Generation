import os
import json
from dotenv import load_dotenv
from google import genai

from feature_extraction import extract_features


# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


INPUT_DIR = "data/processed_audio"
OUTPUT_FILE = "embeddings/audio_embeddings.json"

embeddings = []


for file in os.listdir(INPUT_DIR):

    if file.endswith(".wav") or file.endswith(".mp3"):

        audio_path = os.path.join(INPUT_DIR, file)

        # Extract features
        features = extract_features(audio_path)

        text_representation = f"""
        tempo: {features['tempo']}
        mfcc: {features['mfcc_mean']}
        spectral: {features['spectral_mean']}
        chroma: {features['chroma_mean']}
        """

        # Generate embedding
        response = client.models.embed_content(
            model="gemini-embedding-2-preview",
            contents=text_representation
        )

        vector = response.embeddings[0].values

        embeddings.append({
            "file": file,
            "features": features,
            "embedding": vector
        })


# Create embeddings directory
os.makedirs("embeddings", exist_ok=True)

# Save embeddings
with open(OUTPUT_FILE, "w") as f:
    json.dump(embeddings, f, indent=4)


print("✅ Gemini embeddings generated successfully")
print("Saved to:", OUTPUT_FILE)