import turtle
import os

#Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

# Draw a border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color('white')
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Create a player turtle 
player = turtle.Turtle()
player.color('blue')
player.shape('triangle')
player.penup()
player.speed(0)
player.setposition(0, -200)
player.setheading(90)

# Moving the player left and right
playerspeed = 15

def move_left():
    # Takes the original corrdinate of x and subtract it by 15 to get x as the current position. 
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

#create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")

















delay = input('Press enter to finsih')