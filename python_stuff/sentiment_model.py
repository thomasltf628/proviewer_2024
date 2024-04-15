import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch.nn.functional as F

def getting_label_sentiment(sentence):
    model_directory = r'C:\Users\Administrator\proviewer_2024\python_stuff\my_awesome_model'
    #model_directory = r'C:\Users\super\OneDrive\桌面\adcademic\Capstone\Proviewer Full\python_stuff\my_awesome_model'
    model = AutoModelForSequenceClassification.from_pretrained(model_directory)
    tokenizer = AutoTokenizer.from_pretrained(model_directory)
    inputs = tokenizer(f"{sentence}", return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)

    # Apply softmax to logits to get probabilities
    probabilities = F.softmax(outputs.logits, dim=-1)

    # Get the highest scoring labels and scores
    predicted_label_idx = torch.argmax(probabilities, dim=-1).item()
    predicted_label = model.config.id2label[predicted_label_idx]
    predicted_score = probabilities[0][predicted_label_idx].item()
    unpredicted_label_idx = torch.argmin(probabilities, dim=-1).item()
    unpredicted_label = model.config.id2label[unpredicted_label_idx]
    unpredicted_score = probabilities[0][unpredicted_label_idx].item()

    response = [
    [
        {"label": predicted_label, "score": predicted_score},
        {"label": unpredicted_label, "score": unpredicted_score}
    ]
    ]

    return (response)

