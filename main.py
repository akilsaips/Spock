import random
import turtle

colors = [(213, 154, 96), (52, 107, 132), (179, 77, 31), (202, 142, 31)]
turtle.colormode(255)

sam = turtle.Turtle()

sam.penup()
sam.speed("fastest")
sam.hideturtle()

sam.setheading(225)
sam.forward(300)
sam.setheading(0)


for dot_count in range(1, 101):
    sam.dot(20, random.choice(colors))
    sam.forward(50)

    if dot_count % 10 == 0:
        sam.setheading(90)

        sam.forward(50)
        sam.setheading(180)
        sam.forward(500)
        sam.setheading(0)

screen = turtle.Screen()
screen.exitonclick()
