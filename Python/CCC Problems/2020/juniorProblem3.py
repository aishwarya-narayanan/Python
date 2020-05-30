#Name: Aishwarya Narayanan
#Date: April 22, 2020
#Purpose: Canadian Computing Competition Junior Problem #3

#Get the number of drops of paint
n = int(input("Enter the number of drops of paint:"))

x= [ ]
y= [ ]

#Get the coordinates of the paint drops
for count in range(n):
       coord = input("Enter the coordinates using a comma")
       xp, yp = coord.split (",")
       x.append(int(xp))
       y.append(int(yp))
       
#Calculate the canvas coordinates 
print (f"{min(x)-1},{min(y)-1}")
print (f"{max(x)+1},{max(y)+1}")   

    

