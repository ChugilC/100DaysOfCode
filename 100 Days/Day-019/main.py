# Etch - A - Sketch
from turtle import Turtle, Screen

# Creates the turtle and screen
tim = Turtle()
screen = Screen()
tim.pensize(3)

# Forwards
def move_forward():
    tim.forward(10)

# Backwards
def move_backward():
    tim.backward(10)

# Turn left
def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

# Turn right
def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

# Clear the screen
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

# Event listeners
screen.listen()
screen.onkey(fun=move_forward, key='w')
screen.onkey(fun=move_backward, key='s')
screen.onkey(fun=turn_left, key='a')
screen.onkey(fun=turn_right, key='d')
screen.onkey(fun=clear, key='c')

# Exit the screen
screen.exitonclick()