#from nltk.corpus import brown
from nltk.corpus import stopwords
import operator
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import nltk
import argparse
import numpy as np
import matplotlib.pyplot as plt
import math

wordsAndWeights = {}
ps = PorterStemmer()
nltk.download('stopwords')
nltk.download('punkt')
stop_words = set(stopwords.words('english'))
parser = argparse.ArgumentParser(prog='nlphw0.py',description='A program that Normalizaes Text in a text file', epilog='By Joshua Pagonas')
parser.add_argument('filename', help='Text file to be read')
parser.add_argument('-l','--lower', help='Turns all words into lowercase present in the text file', action='store_true')
parser.add_argument('-s','--stem', help='Stems all words present in the text file', action='store_true')
parser.add_argument('-sw','--stopword', help='Removes all stopwords present in the text file', action='store_true')
parser.add_argument('-ran','--removenonalphnum', help='Removes all non-alphanumeric characters present in the text file', action='store_true')
args = parser.parse_args()

try:
    with open(args.filename, 'r', encoding="utf-8") as file:
        text = file.read()
        if args.lower:
            text = text.lower()
        if args.stem:
            text = ps.stem(text)
        words = word_tokenize(text)
        #words = text.split()

        for word in words:
            if args.stopword and word in stop_words:
                continue

            if args.removenonalphnum:
                word = ''.join(s for s in word if s.isalnum())
                if not word:
                    continue

            if word not in wordsAndWeights:
                wordsAndWeights[word] = 1
            else:
                wordsAndWeights[word] += 1
            
    sortedWordsAndWeights = dict(sorted(wordsAndWeights.items(), key=operator.itemgetter(1), reverse=True))
    for word,weight in sortedWordsAndWeights.items():
        print(word,weight)

    x = list(range(len(sortedWordsAndWeights.keys())))
    '''
    for i in x:
        x[i] += 1
    x = [math.log10(i) for i in x]
    '''
    y = list(sortedWordsAndWeights.values())
    y = [math.log10(i) for i in y]

    plt.plot(x, y, marker='o')

    plt.title("Sample Word and Weight Plot")
    plt.xlabel("Words")
    plt.ylabel("Weights")

    plt.grid(True)
    plt.show(block=True)
except KeyboardInterrupt:
    print('Program Closed By User')

'''
#lowercase
for word in brown.words(categories='hobbies'):
    capturedWord = word.casefold()

    if capturedWord not in wordList:
        wordList.add(capturedWord)
        wordsAndWeights[capturedWord] = 1
    else:
        wordsAndWeights[capturedWord] += 1

    sortedWordsAndWeights = dict(sorted(wordsAndWeights.items(), key=operator.itemgetter(1), reverse=True))

    for word,weight in sortedWordsAndWeights.items():
        print(word,weight)
'''

'''
#stemming
for word in brown.words(categories='hobbies'):
    stemmedWord = ps.stem(word)
    if stemmedWord not in wordList:
        wordList.add(stemmedWord)
        wordsAndWeights[stemmedWord] = 1
    else:
        wordsAndWeights[stemmedWord] += 1

sortedWordsAndWeights = dict(sorted(wordsAndWeights.items(), key=operator.itemgetter(1), reverse=True))

for word,weight in sortedWordsAndWeights.items():
    print(word,weight)
'''

'''
#stop word removal
filtered_sentence = []
for word in brown.words(categories='hobbies'):
    if word not in stop_words:
        filtered_sentence.append(word)

for word in filtered_sentence:
    if word not in wordList:
        wordList.add(word)
        wordsAndWeights[word] = 1
    else:
        wordsAndWeights[word] += 1

sortedWordsAndWeights = dict(sorted(wordsAndWeights.items(), key=operator.itemgetter(1), reverse=True))
for word,weight in sortedWordsAndWeights.items():
    print(word,weight)
'''

'''
#Removing punctuation and non-alphanumeric characters
filtered_words = []
for word in brown.words(categories='hobbies'):
    # list comprehension that filters out bad characters
    filtered_word = [s for s in word if s.isalnum() or s.isspace() and not s.isspace()]

    # rejoin intermediate list into a string
    filtered_word = "".join(filtered_word)

    # Check if the filtered_word is not empty (contains at least one alphanumeric character)
    if filtered_word.strip():
        filtered_words.append(filtered_word)

for word in filtered_words:
    if word not in wordList:
        wordList.add(word)
        wordsAndWeights[word] = 1
    else:
        wordsAndWeights[word] += 1

sortedWordsAndWeights = dict(sorted(wordsAndWeights.items(), key=operator.itemgetter(1), reverse=True))
for word,weight in sortedWordsAndWeights.items():
    print(word,weight)
'''

'''
#wordList = set()
#stopWordInvoked = False
#removeNonAlphNum = False
#filtered_words = []

if args.stopword:
        stopWordInvoked = True
        for word in words:
            if word not in stop_words:
                filtered_words.append(word)
    if args.removenonalphnum:
        removeNonAlphNum = True
        if stopWordInvoked:
            length = len(filtered_words)
            for word in filtered_words:
                filtered_word = [s for s in word if s.isalnum() or s.isspace() and not s.isspace()]

                # rejoin intermediate list into a string
                filtered_word = "".join(filtered_word)

                # Check if the filtered_word is not empty (contains at least one alphanumeric character)
                if filtered_word.strip():
                    filtered_words.append(filtered_word)
            del filtered_words[0:length - 1]
        else:
            for word in words:
                # list comprehension that filters out bad characters
                filtered_word = [s for s in word if s.isalnum() or s.isspace() and not s.isspace()]

                # rejoin intermediate list into a string
                filtered_word = "".join(filtered_word)

                # Check if the filtered_word is not empty (contains at least one alphanumeric character)
                if filtered_word.strip():
                    filtered_words.append(filtered_word)
    if stopWordInvoked or removeNonAlphNum:
        for word in filtered_words:
            if word not in wordList:
                wordList.add(word)
                wordsAndWeights[word] = 1
            else:
                wordsAndWeights[word] += 1
    else:
        for word in words:
            if word not in wordList:
                wordList.add(word)
                wordsAndWeights[word] = 1
            else:
                wordsAndWeights[word] += 1
'''