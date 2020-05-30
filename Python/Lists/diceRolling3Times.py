#Name: Aishwarya Narayanan
#Date: April 27, 2020
#Purpose: Roll a 6 sided dice until a 3 is rolled and output the number of rolls to get 3. 

import random
counter = 0

flag = True
while flag == True:
    #Get a random number from 1 to 6 
    number = random.randint (1,6)
    #Show the number rolled
    print ("The number you rolled is", number)
    #Count the number of rolls to get a 3 
    counter += 1
    if (number == 3):
        flag = False
        #Output the number of rolls to get a 3 
        print ("It took", counter, "rolls to get 3")
    

    

