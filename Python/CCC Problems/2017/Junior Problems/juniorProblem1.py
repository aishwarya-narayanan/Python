#Name: Aishwarya Narayanan
#Date: May 1, 2020
#Purpose: CCC 2017 Problem J1 

#Get the coordinates
x_value= int(input("Enter the x value"))
y_value= int(input("Enter the y value"))

#Check which quadrant the coordinates are in 
if x_value > 0 and y_value > 0:
    print ("1")
elif x_value < 0 and y_value > 0:
    print ("2")
elif x_value < 0 and y_value < 0:
    print ("3")
else:
    print ("4")


