
#Task 2
def theSlope():
    x1 = int(input("Enter the x-coordinate of the first point: "))
    y1 = int(input("Enter the y-coordinate of the first point: "))
    x2 = int(input("Enter the x-coordinate of the second point: "))
    y2 = int(input("Enter the y-coordinate of the second point: "))
    slope = (y2-y1)/(x2-x1)
    return slope

print ("The slope is", theSlope())

    
#Task 3
def yIntercept():
    x1 = int(input("Enter the x-coordinate of the first point: "))
    y1 = int(input("Enter the y-coordinate of the first point: "))
    x2 = int(input("Enter the x-coordinate of the second point: "))
    y2 = int(input("Enter the y-coordinate of the second point: "))
    slope = (y2-y1)/(x2-x1)
    xvalue = x1*slope
    yIntercept = y1-slope
    yIntcoord= (0,yIntercept)
    return yIntcoord

print ("The y-intercept is", yIntercept())

 
#Task 4
def theEquation():
    x1 = int(input("Enter the x-coordinate of the first point: "))
    y1 = int(input("Enter the y-coordinate of the first point: "))
    x2 = int(input("Enter the x-coordinate of the second point: "))
    y2 = int(input("Enter the y-coordinate of the second point: "))
    slope = (y2-y1)/(x2-x1)
    xvalue = x1*slope
    yIntercept = y1-slope
    yIntcoord= (0,yIntercept)
    equation = "y = " + str(slope) + "x + " + str(yIntercept)
    return equation

print ("The equation of the line is", theEquation())









                
    

