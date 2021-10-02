#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 10:01:44 2021

LG 467 Language and Computer
Linguistics, Faculty of Liberal Arts
Thammasat University

@author: Sakol Suethanapornkul
"""


# Week 3: Python Basics



# Code 1.1
txt = '''Beautiful is better than ugly. 
Explicit is better than implicit. 
Simple is better than complex. 
Complex is better than complicated. 
Flat is better than nested.'''

txt_ls = txt.split()

l = []

for word in txt_ls:
    if len(word) > 7:
        l.append(word)

#or equivalently        
m = [word for word in txt_ls if len(word) > 7]

print(l) 
print(m)



# Code 1.2
# type() function
type(-7)
type(7 * 2)
type(10e2)
type(3.1415)
type("cool")
type(True)



# Code 1.3
str(7)
int(3.83)
float(12)
str(True)
int(True)

# Will this work?
int("cat")



# Code 1.4
num = 5
an1 = 'cat'
an2 = "dog"
an3 = '''horse'''

pi_approx = 3.14159



# Code 1.5
num = 



# Code 1.6
num = 7



# Code 1.7
name     = 'sakol'
nms_inst = 'sakol'
nms.inst = 'sakol'
names1   = 'sakol'
1names   = 'sakol'
NameInstr = 'sakol'
names@1   = 'sakol'
Name_Inst = 'sakol'



# Code 1.8
# variable names can’t be reserved words. check:
help("keywords")



# Code 1.9
pounds = 150
lbs    = pounds
pounds = 175

pounds # or print(pounds)
lbs    # which value?



# Code 1.10
names    = ['prayut', 'anutin', 'somsak', 'tummanat']
cabinet  = names
names[0] = 'apisit'
names       # or print(names)
cabinet 



# Code 1.11
# Create string variables
name  = 'Sakol'
store = "Teddy's bigger burger"
poem  = '''Two roads diverged in a yellow wood,
And sorry I could not travel both
And be one traveler, long I stood
And looked down one as far as I could
To where it bent in the undergrowth'''



# Code 1.12
# \n for newlines
print("cars, \nMars, \nand some vars")

# \t for tabs
print("cars, \tMars, \tand some vars")

# \" to have double quotes inside double quotes
print("He said: \"I don't know\"")



# Code 1.13
# Let's start with the basics
x = 10
x + 3
x ** 3

# How about strings
rs = "npr"
tv = "pbs"
rs + tv
rs + " " + tv
rs * 3
rs / 3  # What's going to happen here?



# Code 1.14
# print() a function with arguments inside parentheses
print(rs, tv) 
print(rs,tv)

# This is similar to rs + tv
print(rs + tv)

# Combine string variables with texts 
print("I get my news from", rs, "and", tv)



# Code 1.15
phone = "iPhone 12"
phone[0]
phone[3]
phone[-1]



# Code 1.16
# Start is inclusive but end is exclusive (x-1)
phone = "iPhone 12"
phone[0:3]
phone[0: ]
phone[ :3]
phone[-4:-1]
phone[-4:  ]
phone[2:-2]
phone[0:7:2]
phone[::-1]



# Code 1.17 
# This is the same poem in Code 1.11
# .split() returns a list
poem  = '''Two roads diverged in a yellow wood,
And sorry I could not travel both
And be one traveler, long I stood
And looked down one as far as I could
To where it bent in the undergrowth'''

poem.split('\n')
poem.split(' ') #equivalent to poem.split()



# Code 1.18
fairy = "Once upon a time, in a far, far away land. There's a charming princess."

# Case
fairy.lower()
fairy.upper()
fairy.capitalize()

# Replacing: ('old', 'new')
fairy.replace('time', 'century')

# Assign to the original variable to "fix" the original version
fairy = fairy.upper()
fairy = fairy.lower()

# String multiple methods together
fairy.lower().replace('time', 'century')

# But watch out replace() needs an exact match
fairy.upper()
fairy.upper().replace('time', 'century')
fairy.upper().replace('A', 'AN')

# This isn't efficient but does the job
fairy.replace('.', '!').replace(',', ';')

# Frequency counts (exact match)
fairy.count('far')
fairy.count('Far') # Different from the above

# Remove leading & trailing spaces
ad = "     Privacy, simplified    "
ad.strip()

curse = "What the ****!!!?"
curse.strip('*!?')

# Because these methods work with strings...
'Once upon a time, in a far, far away land'.count('far')

'''Two roads diverged in a wood, and I-
I took the one less traveled by,
And that has made all the difference.'''.lower().split()

# And you can embed everything inside print()
print(fairy.lower().split())
print('Once upon a time'.lower().split())



# Code 1.19
len(fairy)

# input() get users to input data into Python
age = input("Enter your age: ")

# or
print("How old are you? Enter your age")
x = input()

# input() and print() are basic I/O in Python
age = input("Enter your age: ")
print("You're", age, "years old!")

# what type is age?