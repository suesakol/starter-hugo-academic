#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 15:12:41 2021

@author: Sakol
"""


# Week 13 Dependency Parsing



# Code 10.1
# Import SpaCy
import spacy
from spacy import displacy

# Extra bit: import Pandas
import pandas as pd

# Load the model & initialize a pipeline
nlp = spacy.load("en_core_web_sm")

# Apply our pipeline on a text
doc = nlp("December is the last month of the year")



# Code 10.2
# Review: Obtaining POS tags
for tok in doc:
    print(tok.i, tok.text, tok.pos_, tok.tag_)

# Write our analysis to a csv file
df = pd.DataFrame({ 'Tokens':   [tok.text for tok in doc],
                    'UD_tags':  [tok.pos_ for tok in doc],
                    'PTB_tags': [tok.tag_ for tok in doc]
                })

df.to_csv('file.csv')



# Code 10.3
# Dependency tree
for tok in doc:
    print(tok.i, tok.text, tok.dep_, tok.head)

# Something isn't right...
#0 December nsubj is
#1 is ROOT is
#2 the det month
#3 last amod month
#4 month attr is
#5 of prep month
#6 the det year
#7 year pobj of

spacy.explain('pobj')



# Code 10.4
doc1 = nlp("He was hit by a bus yesterday")

for tok in doc1:
    print(tok.i, tok.text, tok.dep_, tok.head)

displacy.serve(doc1, style = 'dep')