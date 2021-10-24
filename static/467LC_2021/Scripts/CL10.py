#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 12:26:03 2021

@author: Sakol
"""


# Week 11 POS tagging



# Code 8.1
from nltk import pos_tag, word_tokenize

txt1  = "The quick brown fox jumps over the lazy dog."
txt2  = "A woman needs a man like a fish needs a bicycle."

pos_tag(word_tokenize(txt1))
pos_tag(word_tokenize(txt2))



# Code 8.2
pos_tag(word_tokenize("A man needs a woman like a fish needs water."))

#[('A', 'DT'), ('man', 'NN'), ('needs', 'VBZ'), ('a', 'DT'), 
# ('woman', 'NN'), ('like', 'IN'), ('a', 'DT'), ('fish', 'JJ'), 
# ('needs', 'NNS'), ('water', 'NN'), ('.', '.')]



# Code 8.3
# Introduction to SpaCy

# Import SpaCy
import spacy

# Load the English model into nlp object
nlp = spacy.load("en_core_web_sm")

# Process a text
doc = nlp("This is an example sentence.")

# Swap #3 with text file
with open('ABC.txt') as f:
    txt = f.read()

doc = nlp(txt)



# Code 8.4
# Print indices, tokens, and tags
[tok.i for tok in doc]
[tok.text for tok in doc]
[tok.lemma_ for tok in doc]
[tok.pos_ for tok in doc]
[tok.tag_ for tok in doc]

for tok in doc:
    print(tok.i, tok.text, tok.lemma_, tok.pos_, tok_tag_)

# If you need help
spacy.explain("DET")
spacy.explain("JJ")



# Code 8.5
from collections import defaultdict

# Create a dict; use default value for unknown key
pos_ct = defaultdict(int)

# Let's check:
print(pos_ct["DET"])

for pos in [tok.pos_ for tok in doc]:
    pos_ct[pos] += 1

# To select tags and counts 
[(t, c) for (t, c) in pos_ct.items()]

for t, c in pos_ct.items():
    print(t, "\t", c)

# You can use .items(), .keys(), .values()