import os
import time
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write

# create generation folder
OUTPUT_DIR = "generation"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# load model
model = MusicGen.get_pretrained("facebook/musicgen-small")

model.set_generation_params(duration=10)

user_prompt = input("Enter music prompt: ")

prompt = [user_prompt]

# generate music
audio = model.generate(prompt)

# create unique filename
filename = f"music_{int(time.time())}"

# full output path
output_path = os.path.join(OUTPUT_DIR, filename)

# save audio
audio_write(output_path, audio[0].cpu(), model.sample_rate)

print(f"Music generated and saved: {output_path}.wav")