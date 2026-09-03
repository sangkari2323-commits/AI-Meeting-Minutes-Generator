import os
import json
import urllib.request
import whisper

# -------------------------------
# 1. Load Whisper model
# -------------------------------
whisper_model = whisper.load_model("base")

# -------------------------------
# 2. Transcribe meeting audio
# -------------------------------
result = whisper_model.transcribe("meeting_audio.mp3")
transcript = result["text"]

print("\n--- Meeting Transcript ---\n")
print(transcript)

# -------------------------------
# 3. Generate AI meeting summary
# -------------------------------
api_key = os.environ["OPENROUTER_API_KEY"]

prompt = f"""
You are an AI meeting minutes assistant.

Analyze the following meeting transcript.

Create a clear meeting summary containing:
1. Main topics discussed
2. Important decisions
3. A short overall summary

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

with urllib.request.urlopen(request) as response:
    result = json.loads(response.read().decode("utf-8"))

summary = result["choices"][0]["message"]["content"]

print("\n--- Meeting Summary ---\n")
print(summary)

# -------------------------------
# 4. Extract action items
# -------------------------------
action_prompt = f"""
You are an AI meeting minutes assistant.

Extract all action items from the following meeting transcript.

For each action item, provide:
- Task
- Person responsible
- Deadline

If a deadline is not mentioned, write "Not specified".

Meeting transcript:
{transcript}
"""

action_data = {
    "model": "openrouter/free",
    "messages": [
        {
            "role": "user",
            "content": action_prompt
        }
    ]
}

action_request = urllib.request.Request(
    "https://openrouter.ai/api/v1/chat/completions",
    data=json.dumps(action_data).encode("utf-8"),
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    },
    method="POST"
)

with urllib.request.urlopen(action_request) as response:
    action_result = json.loads(response.read().decode("utf-8"))

action_items = action_result["choices"][0]["message"]["content"]

print("\n--- Action Items ---\n")
print(action_items)