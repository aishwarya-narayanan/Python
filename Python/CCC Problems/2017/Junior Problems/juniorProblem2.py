
#Purpose: CCC 2017 Problem J2

#Get the number 
n = int(input("Enter a number"))
#Get the number of times the user wants to shift the number
k = int(input("Enter the number of times you want to shift"))

total = n
newnum = n
#Shift the number 
for counter in range (k):
    newnum = (newnum*10)
    total = total + newnum
#Show the new final number
print (total)
    
