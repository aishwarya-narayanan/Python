import turtle


# This program draws import turtle
# Named constants
START_X = -200
START_Y = 0
radius = 35
angle = 170
ANIMATION_SPEED = 0
#Move the turtle to its initial position.
turtle.hideturtle()
turtle.penup()
turtle.goto(START_X, START_Y)
turtle.pendown()
# Set the animation speed.
turtle.speed(ANIMATION_SPEED)
# Draw 36 lines, with the turtle tilted by 170 degrees after each line is drawn.

for x in range(18):
    turtle.pensize(2)
    turtle.color ("red")
    turtle.forward(500)
    turtle.color ("blue")
    turtle.circle(radius)
    turtle.color ("red")
    turtle.left(angle)

for x in range(18):
    turtle.pensize(2)
    turtle.color ("green")
    turtle.forward(500)
    turtle.color ("magenta")
    turtle.circle(radius)
    turtle.color ("green")
    turtle.left(angle)










    




