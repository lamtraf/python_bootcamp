color_list = [(253, 251, 247), (253, 247, 250), (236, 252, 244), (249, 232, 19), (199, 12, 31), (195, 67, 21), (213, 13, 9), (32, 91, 188), (234, 151, 39), (232, 229, 5), (48, 219, 59), (35, 33, 154), (240, 246, 251), (14, 205, 222), (18, 27, 60), (244, 42, 159), (71, 8, 51), (55, 24, 11), (228, 165, 9), (61, 200, 232), (16, 153, 16), (226, 19, 118), (98, 75, 9), (244, 44, 17), (66, 241, 159), (223, 140, 207), (248, 11, 9), (10, 97, 61), (5, 38, 33), (65, 221, 153)]
from turtle import Turtle, Screen
import turtle
import random
turtle.colormode(255)
tim = Turtle()
tim.speed('fastest')
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dot = 100
for dot_count in range(1, number_of_dot+1):
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(50)
    tim.pendown()
    if (dot_count % 10 == 0): 
        tim.penup()
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

tim.hideturtle()

screen = Screen()
screen.exitonclick()