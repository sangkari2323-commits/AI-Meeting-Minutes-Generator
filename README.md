import whisper

# Load the Whisper model
model = whisper.load_model("base")

# Transcribe the meeting audio
result = model.transcribe("meeting_audio.mp3")

# Display the transcript
print("\n--- Meeting Transcript ---\n")
AI-powered system for generating meeting minutes from meeting audio.
print(result["text"])