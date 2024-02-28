from turtle import Turtle,Screen
import random as rd
timmy_the_turtle=Turtle()

timmy_the_turtle.shape('turtle') #[turtle,circle,square,triangle]
color = ['CornflowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'wheat', 'SlateGray', 'SeaGreen']
# timmy_the_turtle.color('red')
# timmy_the_turtle.forward(500) # cho rùa tiến về phía trước
# timmy_the_turtle.right(90) # cho rùa quay sang phải 90 độ

# #  Vẽ một hình vuông
def square(timmy_the_turtle):
    for _ in range(4):
        timmy_the_turtle.forward(100) # cho rùa tiến về phía trước
        timmy_the_turtle.right(90) # cho rùa quay sang phải 90 độ

# Vẽ đường nét liền
def dash_line(timmy_the_turtle):
    for _ in range(15):
        timmy_the_turtle.forward(10)
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(10)
        timmy_the_turtle.pendown()


def draw_tangle(num_slides):
    angle = 360/num_slides
    for _ in range(num_slides):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)

# for shape_side_n in (3,11):
#     timmy_the_turtle.color(rd.choice(color))
#     draw_tangle(shape_side_n)


# dash_line(timmy_the_turtle=timmy_the_turtle)
# square(timmy_the_turtle)


def random_walk(timmy_the_turtle, color):
    directions = [0, 90, 180, 270]
    timmy_the_turtle.pensize(15)
    timmy_the_turtle.speed("fastest")
    for _ in range(200):
        timmy_the_turtle.color(rd.choice(color))
        timmy_the_turtle.forward(30)
        timmy_the_turtle.setheading(rd.choice(directions))

def random_color():
    timmy_the_turtle.colormode(255)
    r = rd.randint(0, 255)
    g = rd.randint(0, 255)
    b = rd.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_of_gap)

draw_spirograph(5)

random_walk(timmy_the_turtle,color)
screen =Screen()

screen.exitonclick()