from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

is_game_on=False
user_bet=screen.textinput(title="make a bet", prompt="Who will win the race? Enter a color:")
print(user_bet)
color=["red", "blue", "green", "orange", "yellow", "purple"]
all_turtle=[]
x=0

for index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100 + x)
    x+=40
    all_turtle.append(new_turtle)

if user_bet:
    is_game_on=True

while is_game_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_game_on=False
            winning_color=turtle.pencolor()
            if winning_color == user_bet:
                print(f"you won! The {winning_color} turtle is the winner")
            else:
                print(f"you lost! The {winning_color} turtle is the winner")

        speed=random.randint(0,10)
        turtle.forward(speed)


screen.exitonclick()
