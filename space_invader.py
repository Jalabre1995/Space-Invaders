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

# Create an enemy
enemy = turtle.Turtle()
enemy.color('red')
enemy.shape('circle')
enemy.penup()
enemy.speed(0)
enemy.setposition(-200,250)

enemyspeed = 2

# Create the players weapon 
bullet = turtle.Turtle()
bullet.color('yellow')
bullet.shape('triangle')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed = 20
#Define bullet stae
#ready - ready to fire
# fire- bullet is firing
bulletstate = 'ready'


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

def fire_bullet():
    #Declare bulletsate as a global if it needs changed
    global bulletstate
    if bulletstate == 'ready':
        bulletstate = 'fire'
        # Move the bullet to the just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x , y)
        bullet.showturtle()

#create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right") 
turtle.onkey(fire_bullet, 'space')

# Main game loop 
while True:
    # Move the enemy
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)
    # Move the enemy back and down 
    if enemy.xcor() > 280:
        y = enemy.ycor()
        y -= 40
        enemyspeed *= -1
        enemy.sety(y)
    if enemy.xcor() < -280:
        y = enemy.ycor()
        y -= 40
        enemy.sety(y)
        enemyspeed *= -1

    #Move the bullet
    if bulletstate == 'fire':
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)
    #Check to see if the bullet reached the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = 'ready'

    


















delay = input('Press enter to finsih')