from turtle import Turtle, Screen 

tim = Turtle()
tim.setheading(0)

def move_forward():
    tim.forward(10)
def move_back():
    tim.backward(10)
def move_counter_clockwise():
    tim.setheading(tim.heading() + 10)
def move_clockwise():
    tim.setheading(tim.heading() - 10)
def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()



screen = Screen()
screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_back)
screen.onkey(key='a', fun=move_counter_clockwise)
screen.onkey(key='d', fun=move_clockwise)
screen.onkey(key='c', fun=clear_screen)
screen.exitonclick()