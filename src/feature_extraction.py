import os
import librosa
import numpy as np


RAW_AUDIO_PATH = "data/raw_audio"


def extract_features(audio_path):

    y, sr = librosa.load(audio_path)

    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)

    mfcc = librosa.feature.mfcc(y=y, sr=sr)

    spectral = librosa.feature.spectral_centroid(y=y, sr=sr)

    chroma = librosa.feature.chroma_stft(y=y, sr=sr)

    features = {
        "tempo": float(tempo),
        "mfcc_mean": float(np.mean(mfcc)),
        "spectral_mean": float(np.mean(spectral)),
        "chroma_mean": float(np.mean(chroma))
    }

    return features


def process_dataset():

    for file in os.listdir(RAW_AUDIO_PATH):

        if file.endswith(".wav") or file.endswith(".mp3"):

            audio_path = os.path.join(RAW_AUDIO_PATH, file)

            features = extract_features(audio_path)

            print("\nAudio File:", file)
            print("Features:", features)


if __name__ == "__main__":
    process_dataset()