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


#Random path

import turtle as t
from turtle import Turtle, Screen
import random

tim = t.Turtle()

colors = ["forest green", "green yellow", "red", "medium spring green", "blue"]
directions=[0, 90, 180, 360]
tim.pensize(15)
tim.speed("fastest")




for i in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()


#Spirograph

import turtle
import turtle as t
from turtle import Turtle, Screen
import random

tim = t.Turtle()

def randomColor():
    r=random.randint(0, 255)
    g=random.randint(0, 255)
    b=random.randint(0, 255)
    color = (r, g, b)
    return color

def spirograph(size):
    for i in range(360//size):
        turtle.colormode(255)
        tim.color(randomColor())
        tim.speed("fastest")
        tim.circle(100)
        current_heading=tim.heading()
        tim.setheading(current_heading+size)

spirograph(5)
screen = Screen()
screen.exitonclick()


#Hirst painting 

import turtle
import turtle as t
from turtle import Turtle, Screen
import random

tim = t.Turtle()
turtle.colormode(255)

def randomColor():
    r=random.randint(0, 255)
    g=random.randint(0, 255)
    b=random.randint(0, 255)
    color = (r, g, b)
    return color

tim.speed("fastest")
tim.setheading(230)
tim.penup()
tim.hideturtle()
tim.forward(300)
tim.setheading(0)
number=100

for i in range(1,number+1):
    tim.dot(20,randomColor())
    tim.forward(50)

    if i%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
screen = Screen()
screen.exitonclick()


#Etch a sketch

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.speed("fastest")


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def turn_left():
    new_heading=tim.heading() +10
    tim.setheading(new_heading)


def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
