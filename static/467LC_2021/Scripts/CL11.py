#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 15:12:41 2021

@author: Sakol
"""


# Week 12 Parsing



# Code 9.1
import nltk

nltk.pos_tag(nltk.word_tokenize("Let's wake up at six"))
# [('Let', 'VB'), ("'s", 'POS'), ('wake', 'VB'), ('up', 'RP'), ('at', 'IN'), ('six', 'CD')]

nltk.pos_tag(nltk.word_tokenize("Let's wake that old man up at six"))
# [('Let', 'VB'), ("'s", 'POS'), ('wake', 'VB'), ('that', 'IN'), ('old', 'JJ'), ('man', 'NN'), ('up', 'RB'), ('at', 'IN'), ('six', 'CD')]



# Code 9.2
from nltk import CFG

grammar_string = """
S -> NP VP
NP -> PRP
VP -> VBD
PRP -> 'I'
VBD -> 'cried'
"""

exercise_grammar = CFG.fromstring(grammar_string)
exercise_grammar



# Code 9.3
test = word_tokenize("I cried")

# Make a parser object with our grammar
parser = nltk.ChartParser(exercise_grammar)

# Parse
trees = parser.parse(test)

for tree in trees:
    print(tree)



# Code 9.4
grammar_string = """
S -> NP VP
NP -> PRP
VP -> VP | VP ADVP | VBD | VBZ VBG RB
ADVP -> RB
PRP -> 'I' | 'He'
VBD -> 'cried'
VBZ -> 'is'
VBG -> 'falling'
RB -> 'fast'
"""

exercise_grammar = CFG.fromstring(grammar_string)

test = word_tokenize("He is falling fast")
parser = nltk.ChartParser(exercise_grammar)
trees = parser.parse(test)

for tree in trees:
    print(tree)
