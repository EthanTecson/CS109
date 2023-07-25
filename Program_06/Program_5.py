"""
Created on Sat Nov 14 6:38:12 2022

@author: ethantecson
"""
"""
     Author/copyright: Ethan Tecson.  All rights reserved.
     Used with permission and modified by: WhoeverModifiesIt
     Date: 14 November 2022
"""

import string

############################################################
def stopwords_function(filename):
     """
        This function will open a text file and read the entire file
        in one step. It then splits and prints the text read.
        Parameters:
            filename -- the name of the file to be read
        Returns:
            stop_data: the text split into a list
    """
     with open(filename) as infile:
         stop_data = infile.read()
         stop_data = stop_data.split()
         print(stop_data)

         return stop_data
############################################################
def main():
    """
        This main function will create a keyword in context with 5 word list.
        Any 5 world list that has a keyword (middle word/index 2)
        that is a stopword will not be printed. The function will print
        the 5 word list sorted in alphabetical order.
        Parameters:
            none
        Returns:
            none
    """
    #Implement and print stoplist
    stoplist_file = input('Enter Stoplist Filename: ')
    stoplist = stopwords_function(stoplist_file)
    #Implement text file to be read and output all words in one list
    text_filename = input('Enter Text Filename: ')
    with open(text_filename) as reading:
        text = reading.read()
    #lower case and remove punctuation
    text = text.lower()
    for punct in string.punctuation:
        text = text.replace(punct,' ')
    #Split and print text
    text = text.split()
    print(text)
    #Create biglist that outputs kerowrd index, keyword, and 5 word list
    length = len(text)
    biglist = []
    for sub in range(2, length - 2):
        if text[sub] not in stoplist:
            slice = text[sub - 2: sub + 3]
            biglist.append([text[sub], sub, slice])
    #Remove 5 word list with stopword as keyword
    for item in biglist:
        if item[0] in stoplist:
            print(' ')
    #Sort 5 word list by aplphabetical order depending on keyword
    for item in sorted(biglist):
        print(item[1], item[0], item[2])
############################################################
main()



