""" This is a 
    Author/copyright: Oghap Kim, Robins, Tecson
    All rights reserved.
    Date: 11 December 2022
"""

# Assinging Global variables for Flesch-Kincaid Equation
WORD = 0.39
SYLLABLE = 11.8
SUBTRACTION = 15.59

import string
######################################################################
def sentences(filename):
    """  This function calculates the average number of words in a sentence
        within the text file and then proceeds to store every sentence from
        the text into individual list and prints them out
         Parameters:
            file_name - the name of the file

        Return:
            length - average words per sentence
    """

    # Opens file and reads it.
    # Removes blank spaces and replaces all capitalized letters with
    # Lowercase words
    file = open(filename, "r")
    txt = file.read()
    txt = txt.replace('\n', ' ')
    txt = txt.lower()

    # Defines what punctuation is
    punct = '''()-[]{};:'"\,<>/@#$%^&*_~'''

    # Replaces random characters with blank for every word in the text
    for word in txt:
        if word in punct:
            txt = txt.replace(word, " ")

    txt = txt.split()

    # Variables to keep track of # of words and # of sentences
    num_words = 0
    num_sentences = 0

    # Create list to add sentences to
    sentence = []
    # For loop that identifies every word as a token
    for line in txt:
        num_words += 1
        # Adds word to list until last character in word is punctuated
        sentence.append(line)
        if (line[-1] == "." or line[-1] == "!" or line[-1] == "?"):
            num_sentences += 1
            print("SENTENCE", sentence)
            sentence = []

    # Calculation to find average words per sentence
    length = float(num_words/num_sentences)
    length = round(length, 4)

    print("\nAVERAGE LENGTH", length, "\n")

    return(float(length))

######################################################################
def syllables(filename):
    """  This function calculates the number of syllables, vowels,
        pairs, and ends of every single word and prints out every word
        with its data.
         Parameters:
            file_name - the name of the file

        Return:
            average_syl - Average amount of syllables per word
    """
    # Opens file and reads it.
    # Removes blank spaces and replaces all capitalized letters with
    # Lowercase words
    file = open(filename, "r")
    txt = file.read()
    txt = txt.replace('\n', ' ')
    txt = txt.lower()

    # Defines what punctuation is
    punct = '''()-[]{};:'"\,<>.!?/@#$%^&*_~'''

    # Replaces punctuation with blank for every word in the text
    for word in txt:
        if word in punct:
            txt = txt.replace(word, " ")

    txt = txt.split()

    #defines what vowel is
    vowel = 'aeiou'

    # Create big_list to store syllables, vowels, pairs, and ends
    big_list = []
    words = len(txt)
    total_syl = 0

    # For loop that tokenizes every word in text
    for word in txt:

        syl = 0
        vowels = 0
        pairs = 0
        ends = 0

        # For loop that tokenizes every index in every word
        # This speciial for loop calculates every vowel in a word
        for index in range(len(word)):
            if word[index] in vowel:
                vowels += 1
                syl += 1

        # This for loop calculates every pair in a word
        for index in range(1, len(word)):
            if word[index] in vowel and word[index - 1] in vowel:
                pairs += 1
                syl -= 1

        # Identifies if word ends with 'e'
        if word.endswith('e'):
            ends = 1
            syl -= 1

        # No word has 0 syllables so this block is used to fix that
        if syl == 0:
            syl += 1

        total_syl += syl

        # Appends all data to big_list
        big_list.append([word, syl, vowels, pairs, ends])

    average_syl = float(total_syl/words)

    print("\nAVERAGE SYLLABLE", average_syl, "\n")

    return (average_syl)

######################################################################
def main():
    """  This main function brings together the sentences() and
        syllables() function to input into the Flesch-kincaid equation
        to calculate the reading level of the given text file.
    """
    filename = input('Enter filename:  READ FROM    ')

    word_count = sentences(filename)
    syllable_count = syllables(filename)


    f_k = WORD*word_count + SYLLABLE*syllable_count - SUBTRACTION

    print("\nAVERAGE LENGTH", word_count)
    print("AVERAGE SYLLABLE", syllable_count)
    print("GRADE LEVEL", f_k)

######################################################################
main()