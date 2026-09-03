import os
import json
import urllib.request
import tempfile
import whisper
import streamlit as st

st.set_page_config(
    page_title="AI Meeting Minutes Generator",
    page_icon="📝"
)

st.title("📝 AI Meeting Minutes Generator")
st.write("Upload a meeting audio file to generate meeting minutes.")

uploaded_file = st.file_uploader(
    "Upload Meeting Audio",
    type=["mp3", "wav", "m4a"]
)

if uploaded_file is not None:

    if st.button("Generate Meeting Minutes"):

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp3"
        ) as temp_audio:

            temp_audio.write(uploaded_file.getbuffer())
            audio_path = temp_audio.name

        with st.spinner("Transcribing meeting audio..."):

            whisper_model = whisper.load_model("base")
            result = whisper_model.transcribe(audio_path)
            transcript = result["text"]

        st.subheader("📝 Meeting Transcript")
        st.write(transcript)

        api_key = os.environ["OPENROUTER_API_KEY"]

        prompt = f"""
You are an AI meeting minutes assistant.

Analyze the following meeting transcript.

Create a clear meeting summary containing:
1. Main topics discussed
2. Important decisions
3. A short overall summary

Then extract all action items.

For each action item provide:
- Task
- Person responsible
- Deadline

If a deadline is not mentioned, write "Not specified".

Meeting transcript:
{transcript}
"""

        data = {
            "model": "openrouter/free",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }

        request = urllib.request.Request(
            "https://openrouter.ai/api/v1/chat/completions",
            data=json.dumps(data).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            method="POST"
        )

        with st.spinner("Generating meeting minutes..."):

            with urllib.request.urlopen(request) as response:
                ai_result = json.loads(
                    response.read().decode("utf-8")
                )

        meeting_minutes = ai_result["choices"][0]["message"]["content"]

        st.subheader("📋 AI Meeting Summary & Action Items")
        st.markdown(meeting_minutes)

        os.remove(audio_path)