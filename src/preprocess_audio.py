import librosa
import soundfile as sf
import os

INPUT_DIR = "data/raw_audio"
OUTPUT_DIR = "data/processed_audio"

TARGET_SR = 44100
DURATION = 30

os.makedirs(OUTPUT_DIR, exist_ok=True)

for file in os.listdir(INPUT_DIR):

    if file.endswith(".mp3"):

        path = os.path.join(INPUT_DIR, file)

        audio, sr = librosa.load(path, sr=TARGET_SR)

        audio = audio[: TARGET_SR * DURATION]

        filename = os.path.splitext(file)[0] + ".wav"

        output_path = os.path.join(OUTPUT_DIR, filename)

        sf.write(output_path, audio, TARGET_SR)

        print(f"Processed {file}")

print("Audio preprocessing complete")