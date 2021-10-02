#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 20:04:57 2021

LG 467 Language and Computer
Linguistics, Faculty of Liberal Arts
Thammasat University

@author: Sakol
"""



# Week 5 Tokenization with NLTK



# Code 3.1
sent1 = '''You need to calm down 
        you are being too loud'''

print(sent1.split())

# By default, split() uses spaces as a separator
# Provide a different separator to split by as an argument

sent2 = '''And I'm just like oh-oh, 
        oh-oh, oh-oh, oh-oh, oh-oh'''

print(sent2.split('-'))
print(sent2.split(','))



# Code 3.2
# Create a list
ls_1 = "man, can, ham".split(',')
ls_2 = ['man', 'can', 'ham', 'man']
ls_3 = ['man', 12, 4.0, True]
ls_4 = ['walk', ['sing', 'yell'], 'sleep']



# Code 3.3
# Like strings, we can index & slice items from lists
thai_pm = ['Samak', 'Somchai', 'Apisit', 'Yingluk', 'Prayut']

thai_pm[0]
thai_pm[-1]
thai_pm[0:2]
thai_pm[-3:-1]
thai_pm[0:-2]
thai_pm[3:7]    #slicing items out of range
thai_pm[7]



# Code 3.4
# strings vs lists
a = 'ice'
b = a           #what is b?
b = 'cream'     #what is a now?

ls1 = ['a', 'b', 'c']
ls2 = ls1
ls2[1] = 'g'
ls1             #what do you think will happen?
ls3 = list(ls1) #create a copy; changing ls3 won't change ls1


# string vs. list methods
a.upper()       #doesn't change a
a.lower()
a.replace('i', 'sli')

thai_pm.reverse()
thai_pm.pop()
print(thai_pm)



# Code 3.5
desserts = ['cakes', 'cakes', 'cookies', 'donuts']
desserts.append('ice creams')
desserts.remove('cakes')
desserts.remove('pastries')     #what will happen here?
desserts.pop()
desserts.pop(1)                 #work with index
desserts.clear()

desserts.count('cakes')
desserts.count('cake')          #exact match; 0 here



# Code 3.6
ex = ['a', 'd', 'd', 'b', 'e', 'c', 'a', 'b', 'd']

sorted(ex)
sorted(ex, reverse = True)

len(ex)
len(set(ex))                    #change lists to sets & get unique values



# Code 3.7
from nltk.tokenize import word_tokenize

# if you get an error message about punkt
import nltk
nltk.download('punkt')

# import 1+ functions/classes
from nltk.tokenize import word_tokenize, TweetTokenizer
from nltk.stem import snowball, WordNetLemmatizer

# change the function names
from nltk.tokenize import word_tokenize as wt
from nltk.tokenize import TweetTokenizer as tt



# Code 3.8
sent = '''If you’re happy and you know it, clap your hands.'''
sent2 = '''I didn't wanna go into detail how these things've been done!'''

word_tokenize(sent)
word_tokenize(sent2)

# Answer:
['If', 'you', '’', 're', 'happy', 'and', 'you', 'know', 'it', ',', 'clap', 'your', 'hands', '.']

# Answer:
['I', 'did', "n't", 'wan', 'na', 'go', 'into', 'detail', 'how', 'these', 'things', "'ve", 'been', 'done', '!']


tweet = '''@MayorBowser @DOEE_DC @DCDPW @capitalweather @washingtonpost
Been #flooding like this for years no help from the #DCgovernment #cafritz #connecticutavenue'''

twt = TweetTokenizer()
twt.tokenize(tweet)



# Code 3.9
# for first for loop
for i in range(1,10):
    print(i)
print("Finished counting")


index = 0
for number in [13, 15, 17, 19, 21, 23]:
    number = number + 5
    index += 1
    print("Index:", index, "Value:", number)

# or equivalently
num = [13, 15, 17, 19, 21, 23]
for index, number in zip(range(1,len(num)), num):
    number = number + 5
    print("Index:", index, "Value:", number)


sent = '''If you’re happy and you know it, clap your hands.'''
sent_tok = word_tokenize(sent)


for i, w in zip(range(1, len(sent_tok)), sent_tok):
    print(i, w)



# Code 3.10
# Let's try snowball (don't forget to import snowball from nltk.stem)
snow = snowball.SnowballStemmer('english')

# stemmers work with one "word" at a time
text = "construction workers built and constructed many buildings in major cities"
text_tok = word_tokenize(text)

for t in text_tok:
    print(snow.stem(t))



# Code 3.11
wn = WordNetLemmatizer()
for t in text_tok:
    print(wn.lemmatize(t))