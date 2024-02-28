from turtle import Turtle,Screen

timmy_the_turtle=Turtle()

timmy_the_turtle.shape('turtle') #[turtle,circle,square,triangle]
# timmy_the_turtle.color('red')
# timmy_the_turtle.forward(500) # cho rùa tiến về phía trước
# timmy_the_turtle.right(90) # cho rùa quay sang phải 90 độ

# #  Vẽ một hình vuông
# for _ in range(4):
#     timmy_the_turtle.forward(100) # cho rùa tiến về phía trước
#     timmy_the_turtle.right(90) # cho rùa quay sang phải 90 độ

for _ in range(15):
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()

screen =Screen()

screen.exitonclick()