import turtle

# creating canvas/paper
turtle.Screen().bgcolor("Orange")

paper = turtle.Screen()
paper.setup(400, 300)

turtle.title("Welcome to Turtle Window")

# turtle object creation
pen = turtle.Turtle()

# creating a square
angle = 360/4 #square has 4 sides, so divided by 4

for i in range(4):
    pen.forward(100)
    pen.left(angle)

turtle.done()