#Space Invaders
import turtle 
import os
import math
import random

win = turtle.Screen()
win.bgcolor("black")
win.title("Turtle Poppers")

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("White")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
        border_pen.fd(600)
        border_pen.lt(90)
border_pen.hideturtle()
border_pen.shape("square")

player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 30

enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)

enemyspeed = 2


number_of_enemies = 5

enemies = []

for i in range(number_of_enemies):
        enemies.append(turtle.Turtle())

for enemy in enemies:
        enemy.color("red")
        enemy.shape("circle")
        enemy.penup()
        enemy.speed(0)
        x = random.randint(-200, 200)
        y = random.randint(100, 250)
        enemy.setposition(x, y)

enemyspeed = 2


bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 40

bulletstate = "ready"




def move_left ():
        x = player.xcor()
        x -= playerspeed
        if x < -280:
                x = -280
        player.setx(x)
        

def move_right ():
        x = player.xcor()
        x += playerspeed
        if x > 280:
                x = 280
        player.setx(x)

def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
            bulletstate = "fire"

            x = player.xcor()
            y = player.ycor() + 10
            bullet.setposition(x, y)
            bullet.showturtle()

def isCollision(t1, t2):
        distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
        if distance < 15:
                return True
        else:
                return False

turtle.listen()
turtle.onkey(move_right, "Right")
turtle.onkey(move_left, "Left")
turtle.onkey(fire_bullet, "space")

while True:

    for enemy in enemies:
            x = enemy.xcor()
            x += enemyspeed
            enemy.setx(x)

            if enemy.xcor() > 280:

                for e in enemies:
                        y = e.ycor()
                        y -= 40
                        e.sety(y)
                enemyspeed *= -1
               

            if enemy.xcor() < -280:
                for e in enemies:
                        y = e.ycor()
                        y -= 40
                        e.sety(y)
                enemyspeed *= -1
                        
                
            if isCollision(bullet, enemy):
                    bullet.hideturtle()
                    bulletstate = "ready"
                    bullet.setposition(0, -400)

                    x = random.randint(-200, 200)
                    y = random.randint(100, 250)
                    enemy.setposition(x, y)

            if isCollision(player, enemy):
                    player.hideturtle()
                    enemy.hideturtle()
                    print("GAME OVER")
                    break

    if bulletstate == "fire":    
            y = bullet.ycor()
            y += bulletspeed
            bullet.sety(y)

    if bullet.ycor() > 275:
            bullet.hideturtle()
            bulletstate = "ready"


delay = input("Press enter to finish")

