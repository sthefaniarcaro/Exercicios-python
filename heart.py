import turtle

# Create a turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
heart = turtle.Turtle()
heart.color("red")
heart.pensize(3)
heart.speed(1)

# Move turtle to starting position
heart.penup()
heart.goto(0, -200)
heart.pendown()

# Draw the heart shape
heart.begin_fill()
heart.left(50)
heart.forward(133)
heart.circle(50, 200)
heart.right(140)
heart.circle(50, 200)
heart.forward(133)
heart.end_fill()

# Hide the turtle
heart.hideturtle()

# Keep the window open until clicked
screen.exitonclick()