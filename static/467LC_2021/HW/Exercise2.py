#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 20:29:18 2021
@author: Sakol
"""

# Instructions: 
# Write a Python script that takes input from the keyboard and then checks whether a string is a palindrome or not.
# Save the script using the following convention: yourname_palindrome.py
# Submit the script through Microsoft Teams.
# This exercise is worth 10 points.


# ----------------------------------
# Palindrome examples in English
# civic, level, radar, kayak, refer, racecar
# Taco cat, A Toyota, Top spot, My gym, Hannah
# Was it a car or a cat I saw?, No lemon, no melon
# Madam, I'm Adam.
# ----------------------------------



# Below, you'll see a set of requirements this program needs to have:
# 1. Take input from the keyboard.                                      (1 point)
# Ask users to type in a word or a phrase 

# 2. Check the length.                                                  (3 points)
# If a test word is 2+ characters, proceed to check if it a palindrome.
# If not, tell the user the word is too short.
# HINT: This should be the outermost if statement

# 3. Process strings.                                                   (3 points)
# 3.1 Lowercase the string, remove any punctuation and space, strip any leading or trailing characters.
# HINT: Don't forget to assign this new string to a variable 

# 4. Get the reverse                                                    (1 point)
# HINT: Don't forget to assign the reverse to a variable

# 5. Check to see if the processed string is equal to its reverse       (2 points)
# If yes, print out a statement that says the original input is a palindrome.
# If not, print out a statement that says the original input is not a palindrome.




# This is an example:

test_text = "kayak"

test_reverse = test_text[...]


if test_text == test_reverse:
    print("The word", test_text, "is a palindrome.")
else:
    print("The word", test_text, "is not a palindrome.")