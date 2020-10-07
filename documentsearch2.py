#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 16:08:59 2020

@author: magnus
"""

# -*- coding: utf-8 -*-
# %%
'''
Document search

In this exercise, you must implement a document search algorithm. The text file 
  'animals.txt' contains a number of small "documents" on different animals 
  taken from Wikipedia. Each document also has a title, which is the name of
  the animal.
⋆ You must implement an algorithm that allows you to search the documents using
  a search query.
⋆ The algoritm must score each document and display the top-5 matching 
  documents.
⋆ Start by implementing the TF-IDF algorithm.
⋆ Next, implement the Okapi BM 25 algorithm, and experiment with the 
  parameters.
'''

# %% Import libraries
import numpy as np
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize as tokenize
stem = nltk.stem.PorterStemmer().stem

# %% 
# 1. Loading in the data from the text file 'animals.txt'

# TASK 1:
#  - Run the code below and examine the variables 'title', 'text', and 'N'. 
#    What do they contain?

# Read the text in the file.
file = open('animals.txt', encoding='utf-8'); 
lines = file.read().splitlines(); 
file.close()

# Make two lists (title and text) which contain the title (name of animal) and 
# text (description of animal) for each entry in the text file
title = lines[0::4]
text = lines[2::4]

# Number of documents
N = len(title)

# %% 
# 2. Tokenization and stemming
#    The functions tokenize() and stem() can be used to tokenize and stem
#    the text

# TASK 2:
#  - Try the function tokenize() by running it on a couple of different
#    strings, e.g. tokenize('I love giraffes!') in the console. Note how it 
#    converts a string to a list of tokens.
#  - Try the function stem() by running it on a couple of different tokens, 
#    e.g. stem('giraffes')
#  - Run the code below and examine the variable 'tokens'. What does it contain?

# Tokenize and stem all data
tokens = [[stem(w) for w in tokenize(t)] for t in text]

# %% 
# 3. Implement TF-IDF and Okapi BM-25 document search

# TASK 3:
#  - Examine the code below and see how it
#     * defines, tokenizes and stems a query text.
#     * comptues the average document length.
#  - Insert your own code below to implement TF-IDF.
#    Hints: 
#     * The text for each animal is stored in the list 'tokens'. Each element 
#       in 'tokens' is a list of stemmed words for that animal.
#     * You can use the y.count(x) function to count the number of elements in  
#       the list y that take the value x.
#     * You can write 'x in y' to check if the value x occurs in the list y.
#  - Insert your own code below to implement BM-25. 


# Define query    
query_raw = 'stripes hills'

# Tokenize and stem query
query = [stem(w) for w in tokenize(query_raw)]

# Average document length
avgdl = np.mean([len(t) for t in tokens])

# Create empty arrays for TF-IDF and BM25 scores
TFIDF = np.zeros(N)
BM25 = np.zeros(N)

# Constants used in BM-25
k1 = 1.2
b = 0.75

# Loop over all query words
nt = 0
for q in query:
    for i in range(N):
        if q in text[i]==True:
            nt +=1
    # Compute how many documents contain the query word q
    print(nt)
 