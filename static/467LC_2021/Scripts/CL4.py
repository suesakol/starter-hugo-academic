#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 20:40:59 2021

LG 467 Language and Computer
Linguistics, Faculty of Liberal Arts
Thammasat University

@author: Sakol
"""


# Week 4: Logical test and branching



# Code 2.1
# Here's the first line of Star Spangled Banner (US national anthem)
st1 = "O say can you see, by the dawn's early light"
st1.split()
st1.split(',')
st1.lower().replace('see', 'saw')
st1.replace('?', '') #nothing changes
st1.count('say')
st1.capitalize()
st1.upper()
st1.title() #a new trick here!



# Code 2.2
len(st1)    #count everything including spaces
len(st1.replace(' ', ''))
len(st1.split())

n = int(input("Enter any number:" ))
print("Your magic number today is:", (n*2)**3)

# What's gonna happen here?
n = input("Enter any number: ")
print("Your magic number today is:", (n*2)**3)



# Code 2.3
wg = int(input("Enter your weight in kilograms: "))
ht = float(input("Enter your height in meters such as 1.76, 1.83, 1.90: "))

bmi = wg / (ht ** 2)
bmi = round(bmi, 2)     #round(number, digit) is a built in function

if bmi >= 25:
    print("Your BMI is: " + str(bmi) + ". " + 
    "You're overweight.")
else:
    print("Your BMI is: " + str(bmi) + ". " + 
    "You're healthy!")



# Code 2.4
# Restart: What's going to happen here?

bmi = round(wg / (ht ** 2), 2)

wg = int(input("Enter your weight in kilograms: "))
ht = float(input("Enter your height in meters such as 1.76, 1.83, 1.90: "))


# For functions, what matters is when it's called
# Case 1
def lbs_to_kg(lbs):
    wg = round(lbs / 2.205, 2)
    return wg

def bmi(wg, ht):
    return round(wg / (ht ** 2), 2)

print(bmi(65, 1.73))


# Case 2 
def lbs_to_kg(lbs):
    wg = round(lbs / 2.205, 2)
    return wg

print(bmi(65, 1.73))

def bmi(wg, ht):
    return round(wg / (ht ** 2), 2)



# Code 2.5
weight = int(input("Enter your weight in kilograms: "))
age = int(input("Enter your age: "))

# Notice the colon
if weight >= age:
    print("You're growing too fast.")
else:
    print("You're growing too slowly.")



# Code 2.6
sent = input("Type any sentence: ")
s = sent.split()

if len(s) % 2 == 0:
    if len(s[0]) % 2 == 0:
        print("Everything is perfect")
    else:
        print("Good! The 1st word has", len(s[0]), "characters.")
else:
    if len(s[0]) % 2 == 0:
        print("Okay! The 1st word has", len(s[0]), "characters.")
    else:
        print("Well, better luck next time!")



# Code 2.7
# You can test multiple conditions with 1+ elif (short for else if)
x = 12
y = int(input("Enter a number: "))

if x < y:
    print("Not bad. Just", abs(x - y), "points apart.")
elif x > y:
    print("Close! Just", abs(x - y), "points apart.")
else:
    print("Awesome!")



# Code 2.8
# Comparison operators return True or False
5 > 3
5 < 3
5 >= 3
5 <= 3
5 == 3
5 != 3

# Which type is it?
type(5 > 3)

# What's going to happen?
'a' < 2

# Going beyond: 
s1 = input("Give me one sentence: ")
s2 = s1.replace(' ', '').strip('.!?')
s3 = input("Give me another sentence: ")
s4 = s3.replace(' ', '').strip('.!?')

len(s2) == len(s4)
len(s2) % 2 == 0
len(s4) % 2 != 0

# For multiple comparison
x = 10
y = 19

x < 20 and y > 20
x < 20 and not y > 20
x < 20 or y > 20
5 < x < 15

# and or not are reserved words



# Code 2.9
# Slicing strings
st = "iphone"
st[0]
st[1:]
st[3:-1]
st[::-1]