import nltk
import string
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

'''
Function that takes text as parameter and returns list of words without
stopwords and punctuations
'''

def tokenswithoutpuncstop(data):
    tokens = nltk.word_tokenize(data)
    stop = set(stopwords.words('english'))
    withoutstop = []
    for i in range(0,len(tokens)-1):
        if tokens[i] not in stop:
            withoutstop.append(tokens[i])
    punctuations = list(string.punctuation)
    withoutstoppuncstop = []
    for word in withoutstop:
        if word not in punctuations:
            withoutstoppuncstop.append(word)
    return withoutstoppuncstop
