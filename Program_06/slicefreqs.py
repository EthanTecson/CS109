
"""
Created on Sat Nov 29 12:57:13 2022

@author: Ethan Tecson, Beck Robins, and Henry Shaw
"""
"""
     Author/copyright: Ethan Tecson, Beck Robins, and Henry Shaw.  All rights reserved.
     Used with permission and modified by: WhoeverModifiesIt
     Date: 29 November 2022
"""

from collections import defaultdict

############################################################
def word_frequencies(filename):
    frequency=defaultdict(int)
    with open(filename) as infile:
        for line in infile:
            line=line.strip()
            line_split=line.split()
            for word in line_split:
                frequency[word]+=1
    return frequency
############################################################
def lists(filename):
    with open(filename) as infile:
        text = infile.read()
        text = text.split()
        print(text)
    set_of_words = defaultdict(set)
    words_set = {}
    set_of_pos = defaultdict(set)
    pos_set = {}
    for token in text:
        words_token = token.split('/')
        #Create dictionaries with part of speech as keyword
        #and the word as its value and vice versa
        set_of_words[words_token[1]] = (words_token[0])
        set_of_pos[words_token[0]] = (words_token[1])
  #  print(set_of_words)
  #  print(set_of_pos)
    for key, value in set_of_words.items():
        print(key,':',value)
############################################################
def main():
    filename = input('Enter txt file: ')
    frequency_of_words=word_frequencies(filename)
    for word, frequency in sorted(frequency_of_words.items()):
        print(frequency,word)
    lists(filename)
############################################################
main()

