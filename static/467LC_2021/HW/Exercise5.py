#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 12:23:31 2021

@author: Sakol
"""

# Instructions: 
# 1. Obtain dependency labels for each sentence with SpaCy.
# 2. Store each parse in a dataframe with columns for (1) index numbers, (2) tokens, and (3) dependency labels. 
# 3. For the four dataframes you create (one for each parse), make sure they share the same column names.
# 4. Then, combine the four dataframes into one dataframe using the command: result = pd.concat(df1, df2, df3, df4) (df is an example name).
# 5. Save the variable "result" as a csv file.
# 6. Open the csv file. Add another column to the file. Call it "my_labels". Under this column, add your own dependency analysis


# Save the script using the following convention: yourname_dependency.py
# Submit the script and the CSV file through Microsoft Teams.
# This exercise is worth 10 points.




# sentences:
# 1. The students were asleep in class
# 2. I saw a girl with a knife
# 3. The teacher gave an interesting lecture to the class
# 4. School is meant to be fun and enjoyable




# See this page for help on concatenating dataframes with Pandas 
# https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html