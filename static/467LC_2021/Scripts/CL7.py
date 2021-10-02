#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 20:02:00 2021

@author: Sakol
"""



# Week 7 Regular Expressions (continued)



# Code 5.1
import re

source = '''I go on too many dates
But I can't make 'em stay
At least that's what people say, mm, mm
That's what people say, mm, mm'''

print(re.split(r"[', ]", source))



# Code 5.2
#re.sub(pat, repl, source)

print(re.sub(r"(\w+)?'\w.?", "BAD! ", source))
print(re.sub(r"mm(?!,)", "urgh", source))



# Code 5.3
from nltk.corpus import brown

brown.fileids()         #files of the corpus
brown.categories()      #categories of the corpus
brown.raw()             #raw content of the corpus
brown.raw(fileids = []) #raw content of the specified files
brown.raw(categories = [])
brown.words()           # word of the whole corpus
brown.words(fileids = [])
brown.words(categories = [])
brown.sents()           #sentences of the whole corpus


# Let's try things out
print(brown.fileids())
print(brown.categories())

textfile = brown.raw(fileids = 'ca01')
wordlist = brown.words(fileids = 'ca01')



# Code 5.4
# In case you're in for some adventure
from nltk.tokenize import word_tokenize

tokens = word_tokenize(textfile)
print(tokens[0:31])


tok = []
for item in tokens:
    raw = re.search(r"([^ ]+)(?=\/)", item)
    if raw:
        tok.append(raw.group())
# We need positive lookahead to match whatever before /
# But there are some tokens with no POS tag, match = None


# Compare
words = brown.words('ca01')



# Code 5.5
# Let's say we want words whose length > 5
long_words = []
for w in tok:
    if len(w) > 5:
        long_words.append(w)

# [word for word in list if .....]
long = [w for w in tok if len(w) > 5]

# If you're confused, try:
same_as_old = [w for w in tok]



# Code 5.6
[w for w in tok if len(w) > 8 and w.endswith('es')]
[w for w in tok if len(w) > 8 or w.endswith('es')]

# Answer below.....



# Code 5.7
# [f(x) for x in list if.....]

[w.lower() for w in tok if len(w) > 5]
[w+"/NN" for w in tok if w.endswith('tion')]



# Code 5.8
from nltk.book import FreqDist

# If you get an error
import nltk
nltk.download("book")

# Then, 
from nltk.book import FreqDist


FreqDist(tok)
all_words = FreqDist([t.lower() for t in tok])

all_words.most_common(10)

# good start but the = most frequent
stop = ['a', 'an', 'the', 'in', 'on', 'at', 'to', 'for', 'of', 'and', '.']
no_stop = [t.lower() for t in tok]
no_stop = [t for t in no_stop if t not in stop]
words = FreqDist(no_stop)
words.most_common(10)






# Code 5.6 (Answer)
[w for w in tok if len(w) > 8 and w.endswith('tion')]
[w for w in tok if re.search(r"^[aeiou]", w) and len(w) > 3]