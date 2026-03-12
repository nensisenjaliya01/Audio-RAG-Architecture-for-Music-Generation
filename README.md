# 🎵 Audio RAG Architecture for Music Generation

## 📌 Project Overview

This project implements an **Audio Retrieval-Augmented Generation (Audio RAG) system** that generates music using **text prompts and audio embeddings**.

The system converts audio files into embeddings, stores them in a vector database, retrieves similar audio embeddings, and generates new music inspired by them using an open-source music generation model.

This architecture demonstrates how **retrieval systems and generative AI models can work together for creative AI applications**.

---

# 🚀 Key Features

* Convert audio files into embeddings using Gemini Embedding models
* Store embeddings in a vector database
* Perform similarity search to retrieve relevant audio
* Generate new music using AI
* Accept user prompts for music generation
* Save generated music automatically
* Modular architecture for experimentation and research

---

# 🧠 Architecture

The system follows an **Audio RAG pipeline**:

```
Audio Dataset
      ↓
Audio Preprocessing
      ↓
Feature Extraction
      ↓
Gemini Embedding Model
      ↓
Vector Store
      ↓
Similarity Retrieval
      ↓
Music Generation Model
      ↓
Generated Audio Output
```

---

# 📂 Project Structure

```
Audio-RAG-Music-Generation
│
├── data/                     # Input audio dataset
├── embeddings/               # Stored embeddings
├── generation/               # Generated music output
│
├── src/
│   ├── preprocess_audio.py
│   ├── feature_extraction.py
│   ├── generate_embeddings.py
│   ├── vector_store.py
│   ├── similarity_search.py
│   └── music_generation.py
│
├── main.py
├── requirements.txt
├── .env.example
└── README.md
```

---

# ⚙️ Technologies Used

* Python
* Gemini Embedding Models
* FAISS Vector Database
* Meta MusicGen
* PyTorch
* Audiocraft
* FFmpeg

---

# 🔬 How the System Works

### 1️⃣ Audio Preprocessing

Audio files are collected and cleaned.

Tasks performed:

* Convert audio format
* Normalize audio
* Prepare audio segments

---

### 2️⃣ Feature Extraction

Audio features are extracted using signal processing techniques such as:

* Spectrogram
* MFCC
* Frequency features

These features represent the **structure of audio signals**.

---

### 3️⃣ Embedding Generation

The extracted features are converted into **vector embeddings** using the Gemini embedding model.

Embeddings represent audio in **high-dimensional vector space**.

Example:

```
Audio → Embedding Vector
[0.32, -0.91, 0.11, 0.45, ...]
```

---

### 4️⃣ Vector Storage

Embeddings are stored in a **vector database (FAISS)**.

This enables fast similarity search across audio embeddings.

---

### 5️⃣ Similarity Retrieval

When a new query arrives:

```
User Prompt → Embedding → Vector Search
```

The system retrieves **similar audio embeddings**.

---

### 6️⃣ Music Generation

The retrieved context is used by the **MusicGen model** to generate new music.

The generated waveform is saved as:

```
generation/music_timestamp.wav
```

---

# 🎹 Running the Music Generator

Run the script:

```
python src/music_generation.py
```

Then enter a prompt:

```
Enter music prompt: south indian festival drums
```

The system generates music and saves it in:

```
generation/
```

Example output:

```
Music generated and saved: generation/music_1710256823.wav
```

---

# 🧪 Example Prompts

You can experiment with prompts such as:

```
lofi chill study music
south indian temple festival drums
epic cinematic orchestra
indian classical flute melody
fast garba dance music
```

---

# 🛠 Installation

### 1️⃣ Clone Repository

```
git clone <repo_url>
cd audio-rag-music-generation
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv .venv
```

Activate environment:

```
.venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Install FFmpeg

Install FFmpeg and add it to system PATH.

This is required for saving generated audio.

---

# ⚠️ Issues Faced During Development

### 1️⃣ Pydantic Version Conflict

Problem:

```
pydantic.errors.PydanticImportError
```

Cause:

* Audiocraft requires **Pydantic v1**
* New libraries installed **Pydantic v2**

Solution:

```
pip install "pydantic<2"
```

---

### 2️⃣ Missing FFmpeg

Problem:

```
FileNotFoundError: ffmpeg
```

Solution:

* Install FFmpeg
* Add it to system PATH

---

### 3️⃣ Virtual Environment Not Activated

Problem:

```
ModuleNotFoundError: audiocraft
```

Solution:

Activate environment:

```
.venv\Scripts\activate
```

---

### 4️⃣ HuggingFace Model Download Delay

The MusicGen model downloads around **800MB** during the first run.

Solution:

Wait for download to complete.

---

# 🌍 Real-World Applications

This architecture can be used in:

* AI music composition
* Game soundtrack generation
* Film background music creation
* Personalized music generation
* Audio search systems
* Creative AI tools
* Music recommendation systems

---

# 🔮 Future Improvements

Possible upgrades:

* Add web UI for prompt input
* Stream music generation
* Use larger MusicGen models
* Integrate real audio retrieval
* Use GPU acceleration
* Deploy as API service

---

# 📚 Learning Outcomes

This project demonstrates practical knowledge of:

* Retrieval-Augmented Generation
* Vector embeddings
* Generative AI for audio
* AI system architecture
* AI pipeline engineering

---

# 👩‍💻 Author

Developed as part of an **AI research project exploring Audio RAG systems for music generation**.

---

# ⭐ If You Like This Project

Give it a star on GitHub and share feedback!
