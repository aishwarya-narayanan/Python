#Name: Aishwarya Narayanan
#Date: April 27, 2020
#Purpose: To get a string with at least 3 characters from the user and displays the 3 letters in the middle of the string

import math

#Get a word from the user
word = input("Enter a word that has more than 3 letters")

#Find the length of the word
wordLength= len(word)

#If the word has less than 3 characters, it is invalid
if (wordLength < 3):
    print ("Invalid: the word length has to be at least 3 characters")
else:
    #If the word has 3 letters, print the word again
    if (wordLength == 3):
        print (word)
    #If the word has an even number of letters, it is invalid
    elif (wordLength % 2 == 0):
        print ("Invalid: the word has to have an odd number of letters")
    #If the word has an odd number of letters that is more than 3, find the three middle letters
    else:
        lendiv2 = wordLength/2
        middlechar = math.floor (lendiv2)
        startIndex = middlechar - 1
        endIndex = middlechar + 2
        middlethree= (word [startIndex : endIndex])
        print ("The middle three characters of", word, "are:", middlethree)
        
        
    
    
