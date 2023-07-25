"""
Created on Sat Nov 5 12:52:34 2022

@author: ethantecson
"""
"""
     Author/copyright: Ethan Tecson.  All rights reserved.
     Used with permission and modified by: WhoeverModifiesIt
     Date: 5 November 2022
"""
"""
    Part of this code is from Professor Duncan Buell's code, filereading1.py

    Title: filereading1.py
    Author: Duncan Buell
    Date: October 7, 2022
    Code Version: 3.10.7
    Availability: https://courses.denison.edu/courses/4537/files/186146?module_item_id=27377
"""
#123456789 123456789 123456789 123456789 123456789 123456789 123456789
######################################################################
def file_analysis(filename):
    """
        This main function will open a file and read the entire file
        in one step. It then takes this file, calculates, and outputs the
        total words, total sentences, and average words per sentence.
        Parameters: 
            filename -- the name of the file to be read
        Returns:
            None
    """
    #Opens file and reads it
    with open(filename) as infile:
        the_data = infile.read()
    #Computation for counting words based off of spaces
    file = the_data
    total_words = file.split()
    total_words = len(total_words)
    print('Number of Words in Text File: ', total_words)
    #Computation for counting sentences based off of punctuation
    punctuation1 = file.split('.')
    count1 = len(punctuation1) - 1
    punctuation2 = file.split('!')
    count2 = len(punctuation2) - 1
    punctuation3 = file.split('?')
    count3 = len(punctuation3) - 1
    total_sentences = count1 + count2 + count3
    print('Number of Sentences in Txt File: ', total_sentences)
    #Computation for calculation of avg. words per sentence
    average = total_words/total_sentences
    sss = f'{average:4.2f}'
    print('Average Words Per Sentence: ', sss)
    print(the_data)

######################################################################
def main():
    #Will ask user to input file 
    """
        This main function will prompt the user to enter the name of the
        text file, and will then call back to the file_analysis() function.
    """
    input_filename = input('Enter a file name: ')
    result = file_analysis(input_filename)
    print(result)

######################################################################
main()


