# YouTube Video Summarizer

## 📌 Overview
This project is a **YouTube Video Summarizer** that extracts and summarizes transcripts from YouTube videos using **Python, Streamlit, and Hugging Face's BART model**. Users can enter a YouTube video URL, view the full transcript, and generate a summarized version with an estimated processing time.

## 🚀 Features
- **Extracts transcripts** from YouTube videos (if available)
- **Summarizes long transcripts** into concise text using a pre-trained NLP model
- **Displays estimated summary generation time** before processing
- **Interactive UI** built with Streamlit

## 🛠️ Tech Stack
- **Python** (Backend processing)
- **Streamlit** (Frontend UI)
- **Hugging Face Transformers** (Summarization Model: `facebook/bart-large-cnn`)
- **YouTube Transcript API** (Extracts video transcripts)

## 📂 Project Structure
```
📦 youtube-video-summarizer
├── app.py                 # Main Streamlit app
├── requirements.txt       # Dependencies
├── README.md              # Documentation
```

## 🔧 Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/rickyrick23/youtube-video-summarizer.git
cd youtube-video-summarizer
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Run the Application
```sh
streamlit run app.py
```

## 📝 Usage
1. **Enter a YouTube Video URL** in the input box.
2. **View the transcript** (if available for the video).
3. Click the **Summarize** button to generate a summary.
4. **View the estimated time** for summary generation and progress updates.

## ⚠️ Limitations
- Works only for YouTube videos that have **auto-generated or manually uploaded subtitles**.
- Summary generation time depends on transcript length and model processing speed.

## 🤝 Contributing
Pull requests are welcome! Feel free to submit issues or feature requests.

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Acknowledgments
- **Hugging Face Transformers** for NLP models
- **Streamlit** for interactive UI
- **YouTube Transcript API** for fetching video transcripts

