import streamlit as st
from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi
import re
import time

# Load Summarization Model
@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_summarizer()

# Function to extract video ID from URL
def get_video_id(url):
    match = re.search(r"(?:v=|/videos/|embed/|youtu\.be/|/v/|/e/|watch\?v=|&v=|youtu.be/|/embed/|/shorts/)([^#\&\?]*)", url)
    return match.group(1) if match else None

# Function to fetch transcript
def fetch_transcript(video_id):
    try:
        transcript_data = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " ".join([entry['text'] for entry in transcript_data])
        return transcript
    except Exception as e:
        return f"Error fetching transcript: {str(e)}"

# Function to generate summary
def generate_summary(transcript):
    chunk_size = 1000  # Split transcript if too long
    chunks = [transcript[i:i + chunk_size] for i in range(0, len(transcript), chunk_size)]
    summaries = []

    try:
        for i, chunk in enumerate(chunks):
            progress_text = f"Processing chunk {i+1}/{len(chunks)}..."
            st.status(progress_text)
            start_time = time.time()
            
            summary = summarizer(chunk, max_length=300, min_length=100, do_sample=False)[0]['summary_text']
            summaries.append(summary)

            elapsed_time = time.time() - start_time
            remaining_time = elapsed_time * (len(chunks) - (i + 1))
            st.status(f"Estimated time remaining: {int(remaining_time)} seconds")

        return " ".join(summaries)

    except Exception as e:
        return f"Error generating summary: {str(e)}"

# Streamlit UI
st.title("YouTube Video Summarizer")

video_url = st.text_input("Enter YouTube Video URL:")

if video_url:
    video_id = get_video_id(video_url)

    if video_id:
        transcript = fetch_transcript(video_id)

        if "Error" not in transcript:
            st.subheader("Transcript:")
            st.write(transcript)

            # Show "Summarize" button
            if st.button("Summarize"):
                st.status("Estimating time for summary generation...")
                
                # Estimate time based on transcript length
                words_per_second = 5  # Approximate speed of model processing
                estimated_time = len(transcript.split()) / words_per_second
                st.status(f"Summary will be ready in approximately {int(estimated_time)} seconds.")
                
                summary = generate_summary(transcript)
                st.subheader("Summary:")
                st.write(summary)
        else:
            st.error(transcript)
    else:
        st.error("Invalid YouTube URL. Please check the link.")
