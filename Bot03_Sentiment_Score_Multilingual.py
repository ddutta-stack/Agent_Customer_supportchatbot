# This is a Python script for sentiment analysis using the ___ sentiment analysis tool.
import requests
import gradio as gr

## Deepsek Url
deepseek_url = "http://localhost:11434/api/generate"
global output_language
# Function to perform sentiment analysis as positive or negative or neutral
def sentiment_analysis(text,language="English"):
    
    prompt = f"Classify the sentiment of the following text(in {language}) as positive, negative, or neutral: {text}"
    payload = {
        "model": "deepseek-r1:1.5b",
        "prompt": prompt,
        "input_language": language,
        "output_language": output_language,
        "stream": False,
    }
    response = requests.post(deepseek_url, json=payload)
    if response.status_code == 200:
        return response.json().get("response", "No sentiment detected")
    else:
        return f"Error in sentiment analysis:{response.status_code} {response.text}"


# Gradio interface for sentiment analysis
interface = gr.Interface(
    fn=sentiment_analysis,
    inputs=gr.Textbox(lines=5, label="Enter text for sentiment analysis", placeholder="Type your text here..."),
    outputs=gr.Textbox(label="Sentiment Result"),
    title="Sentiment Analysis Tool",
    description="This tool classifies the sentiment of the input text as positive, negative, or neutral using Deepseek web.",
)
# Launch the Gradio interface
if __name__ == "__main__":
    output_language = input("Enter the output language (e.g., English, Spanish, French): ")
    interface.launch()