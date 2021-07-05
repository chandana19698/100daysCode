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
