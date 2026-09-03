# AI Meeting Minutes Generator

AI-powered system for generating meeting minutes from meeting audio.

## Project Overview

The AI Meeting Minutes Generator is a smart meeting assistant that converts meeting audio into text and automatically generates useful meeting minutes.

## Objectives

- Convert meeting audio to text using Speech-to-Text technology.
- Generate a concise meeting summary.
- Extract action items, responsible persons, and deadlines.

## Technologies Used

- Python
- OpenAI Whisper
- OpenRouter AI
- Streamlit

## System Workflow

Meeting Audio
↓
Whisper Speech-to-Text
↓
Meeting Transcript
↓
OpenRouter AI
↓
Meeting Summary + Action Items
↓
Streamlit Application

## Features

### 1. Speech-to-Text
The system uses Whisper to convert uploaded meeting audio into a text transcript.

### 2. Meeting Summary
The AI analyzes the transcript and generates:
- Main topics discussed
- Important decisions
- Overall meeting summary

### 3. Action Items
The AI extracts:
- Task
- Person responsible
- Deadline

### 4. User Interface
Users can upload an MP3, WAV, or M4A meeting recording through the Streamlit interface and generate meeting minutes.

## How to Run

Install the required packages:

```bash
pip install -r requirements.txt