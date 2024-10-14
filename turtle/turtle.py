import turtle 

screen = turtle.Screen()

screen.bgcolor("green")

square_turtle =turtle.Turtle()

square_turtle.color("blue")
square_turtle.pensize(3)

for _ in range(4):
    square_turtle.forward(100)
    square_turtle.right(90)
    