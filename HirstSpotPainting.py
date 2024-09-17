import turtle as t
from turtle import Turtle, Screen
import random
t.colormode(255)
timmy = Turtle()
timmy.shape("turtle")
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()


timmy.left(225)
timmy.forward(350)
timmy.setheading(0)

for dot_count in range(1,101) :
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    timmy.dot(20, (r,g,b))
    timmy.forward(50)

    if dot_count % 10 == 0 :
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)
    

print(timmy)


my_screen = Screen()
my_screen.exitonclick()