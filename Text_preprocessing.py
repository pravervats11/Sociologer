import string
import re
import regex
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

'''
Text preprocessing for feeding into text classifier for it to learn.
This is different from Tweet_preprocessing.py preprocessing.
'''

stopwords = stopwords.words('english')
punctuations = list(string.punctuation)

def preprocess_classifier(data):
    for tweet in data:
        for word in tweet.split():
            if word in stopwords:
                word.replace(word,"")
        for word in tweet:    
            if word in punctuations:
                word.replace(word,"")
        for word in tweet.split():
            if word.startswith("@"):
                word.replace(word,"")
            elif word.startswith("#"):
                word.replace(word,word[1:])
            elif word.startswith("http"):
                word.replace(word,"")
    return data
