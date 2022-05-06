import os
from winreg import HKEY_LOCAL_MACHINE


import random
import json
import pickle
import numpy as np
import wikipedia

import nltk 
from nltk.stem import WordNetLemmatizer

from keras.models import load_model

lemmetizer = WordNetLemmatizer()
intents = json.load(open('intents.json'))

words = pickle.load(open('words.pk1', 'rb'))
classes = pickle.load(open('classes.pk1', 'rb'))
model = load_model('chatbotmodel.h5')


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmetizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1

    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r>ERROR_THRESHOLD]

    results.sort(key = lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability':str(r[1])})
    return return_list

def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in  list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result

os.system('cls')
print("The chat bot is running .......")

run = True
while run:
    message = input('').split()
    if ' '.join(message) == 'exit':
        break
    elif message[0] == 'google' or message[0] == 'Google':
        message.pop(0)
        try:
            print(wikipedia.summary(' '.join(message), sentences = 2))
        except:
            print("unable to find specific data")
    else:
        message = ' '.join(message)
        ints = predict_class(message)
        res = get_response(ints, intents)
        print(res)
