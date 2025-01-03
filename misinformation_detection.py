from transformers import pipeline

# Load pre-trained BERT model for text classification
classifier = pipeline("text-classification", model="bert-base-uncased")

def detect_misinformation(text):
    result = classifier(text)
    return result

# Example usage
text = "COVID-19 vaccines are causing infertility in women."
result = detect_misinformation(text)
print(result)
