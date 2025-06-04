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
    response = requests.post(deepseek_url, json=payload)
    if response.status_code == 200:
        return response.json().get("response", "No sentiment detected")
    else:
        return f"Error in sentiment analysis:{response.status_code} {response.text}"
## Testing the sentiment analysis function
if __name__ == "__main__":
    #test_text = "I love the new features of this product!Found it to be very useful."
    #test_text = "I did not like the new features of this product!Did not Found it to be very useful."
    test_text = "I am fine with the new features of this product!Found it to be okay."
    sentiment = sentiment_analysis(test_text)
    print(f"Sentiment of the text '{test_text}': {sentiment}")