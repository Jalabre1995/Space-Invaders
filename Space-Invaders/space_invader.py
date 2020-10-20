import turtle
import os
import math
import random

#Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("space-invaders_background.gif.")
#Register the shapes
turtle.register_shape('invader.gif')
turtle.register_shape('player.gif')


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
# Set the score = 0
score = 0

# Draw the score 
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color('white')
score_pen.penup()
score_pen.setposition(-290,280)
scorestring = 'Score: %s' %score
score_pen.write(scorestring, False, align= 'left', font=("Arial", 14, "normal"))
score_pen.hideturtle() 

# Create a player turtle 
player = turtle.Turtle()
player.color('blue')
player.shape('player.gif')
player.penup()
player.speed(0)
player.setposition(0, -200)
player.setheading(90)

# Moving the player left and right
playerspeed = 15
# Choose the number of enemies
number_of_enemies = 10
#create an empty list of enemies

enemies = []
# Add enemies to the list 
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())
for enemy in enemies:
    enemy.color('red')
    enemy.shape('invader.gif')
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200,200)
    y = random.randint(100,250)
    enemy.setposition(x,y)

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

def isCollision( t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2 ) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True
    else: 
        return False

#create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right") 
turtle.onkey(fire_bullet, 'space')

# Main game loop 
while True:
    # Create an enemy
    for enemy in enemies:
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x) 
        if enemy.xcor() > 280:
            # Moves all of the enemies down 
            # Create a nested loop within the loops
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1
        if enemy.xcor() < -280:
            #Create a nested loop within the loop
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1
     # check for collision between thr bullet and the enemy
        if isCollision(bullet, enemy):
            bullet.hideturtle()
            bulletstate = 'ready'
            bullet.setposition(0,-400)
            #Reset the enemy
            x = random.randint(-200,200)
            y = random.randint(100,250)
            enemy.setposition(x,y)
            #update the score
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align= 'left', font=("Arial", 14, "normal"))


        if isCollision(player, enemy):
            bullet.hideturtle()
            enemy.hideturtle()
            print('Game Over')
            break
        

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