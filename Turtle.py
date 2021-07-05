from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("DarkGreen")
for _ in range(4):
    tim.forward(100)
    tim.left(90)
    
    
    
#Dotted line
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("DarkGreen")
for _ in range(4):
    tim.forward(20)
    tim.penup()
    tim.forward(20)
    tim.pendown()
    tim.forward(20)
    tim.left(90)
    
    
  # triangle to decagon

import turtle as t
from turtle import Turtle, Screen
import random


colors = ["forest green", "green yellow", "red", "medium spring green", "blue"]
tim = t.Turtle()


def draw_shape(num_of_sides):
    angle = 360 / num_of_sides
    for _ in range(num_of_sides):
        t.forward(100)
        t.right(angle)


for i in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(i)


screen = Screen()
screen.exitonclick()

