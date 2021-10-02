#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 20:04:57 2021

LG 467 Language and Computer
Linguistics, Faculty of Liberal Arts
Thammasat University

@author: Sakol
"""



# Week 6 Regular Expressions



# Code 4.1
import re

# In Python, a regex search is written as
# x = re.match(pat, str)

result = re.match('this', 'this is a cat')
result
result.group()

# or 
re.match('this', 'this is a cat').group()



# Code 4.2
# match() finds exact beginning match
str1 = "you're okay?"
str2 = "How are you?"

a = re.match('you', str1)
b = re.match('you', str2)

# To extract the match use .group()
a.group()
b.group()



# Code 4.3
# search() finds first match anywhere in source string
str1 = "You're about to find out how powerful regex is"

re.search('find')
re.match('find')    # compare



# Code 4.4
song = '''If you’re happy and you know it,
Clap your hands.
If you're happy and you know it,
Clap your hands.

If you're happy and you know it,
And you really want to show it,
If you're happy and you know it,
Clap your hands.'''

# Answer below....



# Code 4.5
str1 = "Where are we? Who are we? Why are we here? We aren't sure!"

re.findall('we', str1)  # obtain a list



# Code 4.6
str = '''I'd like to go for a walk every day. 
I walked 3 kilos yesterday. My friend loves 
walking too. She walks a lot.'''

re.findall(r'walk(s|ed|ing|)', str)
re.findall(r'(walk(s|ed|ing|))', str)

# or
for i in re.findall(r'(walk(s|ed|ing|))', str):
    print(i[0])



# Code 4.7
head = '''From sakol.suethana@staff.tu.ac.th Sat Dec  12 09:14:16 2015'''
pat  = re.compile(r"@([\w+.]*)")
pat2 = re.compile(r"@([^ ]*)")
pat3 = re.compile(r"From (.*)@([\w+.]*)")

re.findall(pat, head)
re.findall(pat2, head)

print("Usernames\t", "Hosts")
for i in re.findall(pat3, head):
    print(i[0], "\t", i[1])



# Code 4.8
source = '''I go on too many dates
But I can't make 'em stay
At least that's what people say, mm, mm
That's what people say, mm, mm'''

print(re.split(r"[', ]", source))
