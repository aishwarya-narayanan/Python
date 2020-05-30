#Name: Aishwarya Narayanan
#Date: April 22, 2020
#Purpose: Canadian Computing Competition Junior Problem #2

#Get the number of people infected with the disease 
p= int(input("Enter the maximum number of people infected with the disease:"))
#Get the number of people with the disease on Day 0
n= int(input("Enter the number of people with the disease on Day 0:"))
#Get the number of people infected by 1 person on the next day
r= int(input("Enter the number of people infected by 1 person on the next day:"))

total = n
day = 0

#Calculate on what day there will be more than "p" people infected
while total <= p:
    n= n*r
    total = total + n
    day = day + 1
print ("On day", day, "there will be more than", p, "people infected")  

    
