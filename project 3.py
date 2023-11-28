import turtle
import random
import math

#SCREEN
screen = turtle.Screen()
screen.title("Alien Invasion")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

num_stars = 100
for _ in range(num_stars):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    size = random.uniform(0.1, 0.5)
    turtle.penup()
    turtle.goto(x, y)
    turtle.dot(size, "white")


#TURTLE
player = turtle.Turtle()
player.color("paleturquoise")
player.shape("triangle")
player.penup()
player.speed(0)
player.setheading(90)
player.goto(0, -250)
playerspeed = 20


bullet = turtle.Turtle()
bullet.color("gold2")
bullet.shape("circle")
bullet.penup()
bullet.speed(0)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()
bullet.setheading(90)
bulletspeed = 20
bulletstate = "ready"


alien = turtle.Turtle()
alien.color("red", "grey")
alien.shape("circle")
alien.shapesize(3,1)
alien.penup()
alien.speed(0)
alien.setheading(90)
alien.goto(random.randint(-280, 280), random.randint(100, 250))
alienspeed = 2

#FUNCTIONS
def move_left():
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
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        bullet.goto(player.xcor(), player.ycor() + 10)
        bullet.showturtle()

def is_collision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) + math.pow(t1.ycor()-t2.ycor(), 2))
    return distance < 15


screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(fire_bullet, "space")

#GAME LOOP
while True:
    screen.update()
    
    alien.sety(alien.ycor() - alienspeed)
    if alien.ycor() < -280:
        alien.goto(random.randint(-280, 280), random.randint(100, 250))

    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    if is_collision(bullet, alien):
        bullet.hideturtle()
        bulletstate = "ready"
        alien.goto(random.randint(-280, 280), random.randint(100, 250))

    if is_collision(player, alien):
        player.color("red")
        break

#ENDGAME
game_over = turtle.Turtle()
game_over.color("red")
game_over.hideturtle()
game_over.write("Game Over!", align="center", font=("Courier", 24, "normal"))

turtle.done()
exit.onclick()
