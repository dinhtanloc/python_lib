from turtle import Turtle,Screen
import turtle as turtle_module
import random as rd

turtle_module.colormode(255)
tim = turtle_module.Turtle()
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
    r = rd.randint(0, 255)
    g = rd.randint(0, 255)
    b = rd.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########

def draw_spirograph(size_of_gap):
    screen =Screen()
    screen.colormode(255)
    for _ in range(int(360 / size_of_gap)):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_of_gap)


def random_dot(number_of_dots,timmy_the_turtle):
    color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
    timmy_the_turtle.setheading(225)
    timmy_the_turtle.forward(300)
    timmy_the_turtle.setheading(0)

    for dot_count in range(1, number_of_dots + 1):
        tim.dot(20, rd.choice(color_list))
        tim.forward(50)

        if dot_count % 10 == 0:
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)


# draw_spirograph(5)
random_dot(number_of_dots=500,timmy_the_turtle=tim)

# random_walk(timmy_the_turtle,color)
screen =Screen()
# screen.colormode(255)
screen = turtle_module.Screen()

screen.exitonclick()