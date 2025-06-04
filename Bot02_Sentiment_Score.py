# This is a Python script for sentiment analysis score using the ___ sentiment analysis tool.
import requests
import gradio as gr

## Deepsek Url
deepseek_url = "http://localhost:11434/api/generate"
# Function to perform sentiment analysis as positive or negative or neutral
def sentiment_analysis(text):
    prompt = f"Classify the sentiment of the following text as positive, negative, or neutral: {text}. But, try to rate the sentiment on a scale of 0 to 1, where 0 is negative, 0.5 is neutral, and 1 is positive."
    payload = {
        "model": "deepseek-r1:1.5b",
        "prompt": prompt,
        "stream": False,
    }
    response = requests.post(deepseek_url, json=payload)
    if response.status_code == 200:
        return response.json().get("response", "No sentiment detected")
    else:
        return f"Error in sentiment analysis:{response.status_code} {response.text}"

# Gradio interface for sentiment Score analysis
interface = gr.Interface(
    fn=sentiment_analysis,
    inputs=gr.Textbox(lines=5, label="Enter text for sentiment analysis", placeholder="Type your text here..."),
    outputs=gr.Textbox(label="Sentiment Result"),
    title="Sentiment Analysis Tool",
    description="This tool classifies the sentiment of the input text as positive, negative, or neutral using Deepseek web.",
)
# Launch the Gradio interface
if __name__ == "__main__":
    interface.launch()