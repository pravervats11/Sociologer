import nltk
import string
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

'''
This part will be responsible for removing stop words, letters in lower case, remove tweets with less words.
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

'''
Emoticon relpacement -> build a emoticon dict file with list of emoticons from wikipedia.
Hashtag -> search hashtag on twitter and get classification of hashtag based on hashtag tweets.(hashtag classification will contribute less in getting overall classification on tweet.)
User mention -> Removing User mention and doing exact same as done with hashtags. (classification contribution will be least.)
URL -> URL is to be removed.
'''

</Code>

'''
POS Tagging and other secn level feature extraction. (If necessary)
'''

</Code>
