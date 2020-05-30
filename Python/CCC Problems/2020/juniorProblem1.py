#Name: Aishwarya Narayanan
#Date: April 22, 2020
#Purpose: Canadian Computing Competition Junior Problem #1

#Ask how many of each treat Barley had
small= int(input("How many small treats did Barley eat?"))
medium= int(input("How many medium treats did Barley eat?"))
large= int(input("How many large treats did Barley eat?"))

#Calculate Barley's happiness
happiness = (small + (2*medium) + (3*large))

#Decide is Barley is happy or sad
if happiness >= 10:
    print ("happy")
else:
     print ("sad")
    


