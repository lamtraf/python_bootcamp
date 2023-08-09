from turtle import Turtle, Screen
import random
import turtle
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
"wheat", "SlateGray", "SeaGreen"]
# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape('turtle')
# timmy_the_turtle.color('red')
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)
# timmy_the_turtle.backward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.backward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.backward(100)

# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(90)

# for _ in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()
    # it has other methods to replace penup() and pendown(). This method is change the color of each forward
# for _ in range(3):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(60)
#     timmy_the_turtle.right(60)
# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(360/4)
# for _ in range(5):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(360/5)
# def change_color():
#     R = random.random()
#     G = random.random()
#     B = random.random()
#     turtle.pencolor(R,G,B)
# for i in range(3,11):
#     for _ in range(i):
#         timmy_the_turtle.color(random.choice(colours))
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(360/i)
turtle.colormode(255)
def random_color():
    R = random.randint(0,255)
    G = random.randint(0,255)
    B = random.randint(0,255)
    return (R, G, B)
        
direction = [0,90,180,270, 360]
tim = Turtle()
tim.speed('fastest')


# for _ in range(100):
#     tim.color(random_color())
#     tim.setheading(random.choice(direction))
#     tim.forward(30)
def draw_circle(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_circle(5)

screen = Screen()
screen.exitonclick()