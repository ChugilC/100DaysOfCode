import turtle
import pandas

# Screen SetUp
screen = turtle.Screen()
screen.title("U.S States Game")

image = "100 Days/Day-025/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("100 Days/Day-025/50_states.csv")
all_states = data["state"].to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title="Guess the state", prompt="What's the state name?").title()

    if answer_state == "Exit":
        missed_states = []
        for state in all_states:
            if state not in guessed_states:
                missed_states.append(state)
        
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("missed_states.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        state_data = data[data["state"] == answer_state]

        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
