#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 11:40:26 2021

@author: Sakol
"""



# Week 9 Corpus Exploration



# Code 6.1
# [x for x in y if...]
doubt = "I doubt if this will work".split()

[w for w in doubt]
[w for w in doubt if 'w' in w]
[w for w in doubt if len(w) >= 4]

# [f(x) for x in y if...]
[w.upper() for w in doubt]
[len(w) for w in doubt]
[len(w) for w in doubt if len(w) > 2 and w.startswith(w)]



# Code 6.2
# Open a file with open(); call open() before reading in files
f = open('enable1.txt')         # or
f = open('Files/enable1.txt')

txt = f.read()
f.close()

words = txt.split()
print(words[0:51])



# Code 6.3
f = open('enable1.txt') 

txt = f.read()
txt1 = f.readlines()

f.close()

print(txt[0:11])
print(txt1[0:11])



# Code 6.4 (Answer below...)
# 1. What are the last ten words in the list?


# 2. What are the ten longest words? 


# 3. Select words that start with 'a' and whose length > 15


# 4. Get word length of each word in the entire list


# 5. Get words that begin with and end with 'k'



# Code 6.5
# A smarter way to open and close files automatically
with open('enable1.txt') as f:
    txt = f.read()
    words = txt.split()



# Code 6.6
from nltk.book import FreqDist
from nltk.corpus import brown

# If you get an error
import nltk
nltk.download("book")

# Then, 
from nltk.book import FreqDist


words = brown.words('ca01')
wlist = FreqDist(words)

print(wlist)
# <FreqDist with 848 samples and 2242 outcomes>

wlist.most_common(10)
# [('the', 127), ('.', 88), (',', 87), ('of', 65), ('to', 55), ('a', 50), ('and', 40), ('in', 39), ('``', 34), ("''", 33)]

wlist.max()
wlist.N()

# Because a key-value pair, we can reference them with variables in a for-loop
print("words,", "counts")
for i, j in wlist.most_common():
    print(str(i) + ", " + str(j))

wlist.most_common(15)
wlist.plot()
wlist.plot(cumulative = True)



# Code 6.7
# We can do better
words  = [w.lower() for w in words]
wlist2 = FreqDist(words)

print(wlist2)
# <FreqDist with 800 samples and 2242 outcomes>

wlist2.most_common(10)
# [('the', 155), ('.', 88), (',', 87), ('of', 65), ('to', 55), ('a', 54), ('in', 40), ('and', 40), ('``', 34), ("''", 33)]



# Code 6.8
# good start but the = most frequent
stop     = ['a', 'an', 'the', 'in', 'on', 'at', 'to', 'for', 'of', 'and', '.']
words_sm = [w for w in words if w not in stop] 
wlist3   = FreqDist(words_sm)
wlist3.most_common(10)


from nltk.corpus import stopwords
print(stopwords.words('english'))

stopwords = stopwords.words('english')
words_sm2 = [w for w in words if w not in stopwords] 

wlist4    = FreqDist(words_sm2)



# Code 6.9
len(words_sm2)
len(set(words_sm2))

# Type-token ratio
len(set(words_sm2))/len(words_sm2)



# Code 6.10
# You can import all by: from nltk.book import *
from ntlk.book import text1, text2, text3

print(text1)
print(text2)
print(text3)
print(text2[:31])
print(text3[:31])

len(set(text2))/len(text2)
len(set(text3))/len(text3)



# Code 6.11
# Defining functions

def ttr(lst):
    result = len(set(lst))/len(lst)
    return round(result, 3)

ttr(text1)


def ttr(lst, digits):
    """Compute type-token ratio on a list of strings,
    accepts one list and digits to round."""
    result = len(set(lst))/len(lst)
    return round(result, digits)

ttr(text1, 3)
ttr(text2, 4)
help(ttr)



# Code 6.12
import nltk

nltk.bigrams(text1)

list(nltk.bigrams(text1))

nltk.ngrams(text1, 2)
list(nltk.ngrams(text1, 2))

bigrams = list(nltk.ngrams(text1, 2))
bicount = FreqDist(bigrams)
