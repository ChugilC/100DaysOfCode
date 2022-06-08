# Turtle racing game
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

is_game_on = False
user_guess = screen.textinput(title="Make a bet!", prompt="Which turtle will win the race? Enter the color: ")
colors = ["red", "green", "blue", "yellow", "pink", "orange"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_guess:
    is_game_on = True

while is_game_on:

    for turtle in all_turtles:

        if turtle.xcor() > 230:
            is_game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_guess:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You lost! The {winning_color} is the winner.")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# Exit the screen
screen.exitonclick()