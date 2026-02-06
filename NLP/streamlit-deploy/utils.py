import re
import numpy as np
import pickle
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

labels = {"negative" : 0, "positive" : 1}

def get_model(file_path):
    try:
        with open(file_path, "rb") as file:
            data = pickle.load(file)
    except Exception as e:
        print(f"Cannot load model file due to {e}")
        
    classifier_model = data['classifier']
    embeddings_model = data['embeddings']

    return classifier_model, embeddings_model


def text_processor(text):
    text = text.lower()

    # Removing urls 
    text = re.sub(r'(https?://\S+|www\.\S+)', "", text)
    # Removing HTML Tags
    text = re.sub(r"<.*?>", "", text)
    # Puncuation and special Char
    text = re.sub(r"[^\w\d\s]", " ", text)
    # Remove spaces
    text = text.strip()

    # Stopwords
    text = [word for word in text.split() if word not in ENGLISH_STOP_WORDS]
    text = " ".join(text)
    
    # Lemmatization
    text = lemmatizer.lemmatize(text)

    # Removing single letter from sentence
    text = re.sub(r"\s\w{1}\s", "", text)

    return text

def vectorize( tokens, model):
    vectors = [
        model[word] for word in tokens if word in model
    ]
    if len(vectors) == 0:
        return np.zeros(model.vector_size)

    return np.mean(vectors, axis =0)


def pred_pipe(input_text,model_path):

    classifier_model, embeddings_model = get_model(model_path)

    process_text = text_processor(input_text)

    embeddings = vectorize(process_text.split(), embeddings_model.wv)

    predict = classifier_model.predict([embeddings])
    sentiment = [key for key, value in labels.items() if value == predict[0]]

    return sentiment[0].capitalize()