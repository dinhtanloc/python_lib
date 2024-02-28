from turtle import Turtle,Screen

timmy_the_turtle=Turtle()

timmy_the_turtle.shape('turtle') #[turtle,circle,square,triangle]
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

dash_line(timmy_the_turtle=timmy_the_turtle)
square(timmy_the_turtle)
screen =Screen()

screen.exitonclick()