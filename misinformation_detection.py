from transformers import pipeline


classifier = pipeline("text-classification", model="bert-base-uncased")

def detect_misinformation(text):
    result = classifier(text)
    return result


text = "COVID-19 vaccines are causing infertility in women."
result = detect_misinformation(text)
print(result)
