
#Purpose: CCC 2017 Problem J3

#Get the starting coordinate 
startcoord = input("Enter the starting coordinates with a space")
xp1, yp1 = startcoord.split (" ")

#Get the destination coordinates
destcoord = input("Enter the destination coordinates with a space")
xp2, yp2 = destcoord.split (" ")

#Get the electrical charge of the battery 
t = int(input("Enter the electrical charge of your battery"))

if xp1 == xp2:
    z= int(yp2) - int(yp1)
elif yp1 == yp2:
    z= int(xp2) - int(xp1)
else:
    y= int(yp2) - int(yp1)
    x= int(xp2) - int(xp1)
    z = x+y
    
#Check if it's possible to move with the availble electric charge
if z > t:
    print ("N")
elif z % 2 == t % 2:
    print ("Y") 
else:
    print ("N")
    
        
