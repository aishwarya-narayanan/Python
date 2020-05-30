#Name: Aishwarya Narayanan
#Date: May 6, 2020
#Purpose: Data about 50 random integers in a list

import random

#Create a python list called fiftyIntegers
fiftyIntegers = []

#Append 50 random integers in the range 75 to 125
for counter in range (50):
    number = random.randint (75,125)
    fiftyIntegers.append(number)
    
#Show the list
print (fiftyIntegers)

#Find out how many numbers are in the list
print ("There are", len(fiftyIntegers), "numbers in the list")

#Find out the smallest number in the list 
print ("The smallest number in the list is", min(fiftyIntegers))

#Find out the largest number in the list
print ("The largest number in the list is", max(fiftyIntegers))

#Find out the sum of the numbers in the list
print ("The sum of the numbers in the list is", sum(fiftyIntegers))

#Find out the average of the numbers in the list 
averagenum = (sum(fiftyIntegers))/(len(fiftyIntegers))
print ("The average of the numbers in the list is", averagenum)





