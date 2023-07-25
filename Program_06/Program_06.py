"""
Created on Sat Nov 29 12:57:13 2022
@author: Ethan Tecson, Beck Robins, and Henry Shaw
"""
"""
     Author/copyright: Ethan Tecson, Beck Robins, and Henry Shaw.  All rights reserved.
     Date: 29 November 2022
"""
from collections import defaultdict
############################################################
def word_frequencies(filename):
    """  This function opens the file, strips and splits the lines,
         and returns the frequency of the words in the text
         Parameters:
             filename   -- the file inputted by the user that is opened
             and operated on in the for loop
         Returns:
             frequency
    """
    #Dictionary for counting frequency
    frequency=defaultdict(int)
    #open text file with for loop
    with open(filename) as infile:
        for line in infile:
            line = line.strip()
            line_split = line.split()
            for word in line_split:
                frequency[word] += 1
    return frequency
############################################################
def lists(filename):
    """  This function creates the two different sets with dictionaries
         that are matched together. It houses three different for loops
         that match the sets, print the words tagged to the pos, and the
         pos tagged to the words
         Parameters:
             parameter   -- the file inputted by the user that is read
             and converted into the sets of words and poses
         Returns:
             none
    """
    with open(filename) as infile:
        text = infile.read()
        text = text.split()
    #Assignment of dictionaries as set
    set_of_tags = defaultdict(set)
    set_of_words = defaultdict(set)
    #for loop to assign keywords and values to each dictionary
    for token in text:
        words_token = token.split('/')
        set_of_tags[words_token[1]].add(words_token[0])
        set_of_words[words_token[0]].add(words_token[1])
    #prints keyword (word) and its value/s (part of speeches/tags)
    for key,value in sorted(set_of_words.items()):
        print('WORDSTOTAG', key,value)
    print()
    #prints keyword (part of speeches/tags) and its value/s (word/s)
    for key,value in sorted(set_of_tags.items()):
        print('TAGTOWORDS', key,value)

############################################################
def main():
    """  This function prompts the user to input a file to be
         operated on by each of the functions. It also produces our
         list of words frequencies, and prints it out. Lastly, it calls
         the lists function which prints the keywords and its values.
         Parameters:
             none
         Returns:
             none
    """
    filename = input('Enter txt file: ')
    frequency_of_words = word_frequencies(filename)
    frequency_list = []
    for word, frequency in sorted(frequency_of_words.items()):
        frequency_list.append([frequency,word])
    #for loop to print word/tag and its frequencey in alphabetical order
    for word, frequency in sorted(frequency_of_words.items()):
        print(word, frequency)
    print()
    #for loop to print frequencey and then word/tag sorted by frequencey smallest to biggest
    for item in sorted(frequency_list):
        print(item[0],item[1])
    print()
    lists(filename)
############################################################
main()