import turtle
from turtle import Screen

import pandas

screen = Screen()
screen.title("US State Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
screen.tracer(0)

states = pandas.read_csv("50_states.csv")
states_list = states.state.to_list()

guessed = []
tot_states = len(guessed)

def goto(data):
    if data in states_list:
        if data not in guessed:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            row = states[states.state == data]
            t.goto(int(row.x),int(row.y))
            t.write(data)
        guessed.append(data)

while tot_states < 50:

    screen.update()
    data = screen.textinput(title=f"{tot_states}/50 States", prompt="Enter the Name of the State?!")
    data.title()
    goto(data)

    tot_states = len(guessed)
    if data == "Exit":
        print(f"You have Guessed {tot_states} in the 50 states.")
        for i in states_list:
            goto(i)

        tot_states = 50



screen.exitonclick()