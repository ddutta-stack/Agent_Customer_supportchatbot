# This is a Python script for sentiment analysis using the ___ sentiment analysis tool.
import requests
import gradio as gr

## Deepsek Url
deepseek_url = "http://localhost:11434/api/generate"
# Function to perform sentiment analysis as positive or negative or neutral
def sentiment_analysis(text):
    prompt = f"Classify the sentiment of the following text as positive, negative, or neutral: {text}"
    payload = {
        "model": "deepseek-r1:1.5b",
        "prompt": prompt,
        "stream": False,
    }

