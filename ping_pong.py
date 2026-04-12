import turtle
import random
import time

WIDTH, HEIGHT = 800, 600

wn = turtle.Screen()
wn.title("Turtle Ping Pong")
wn.bgcolor("black")
wn.setup(width=WIDTH, height=HEIGHT)
wn.tracer(0)

def make_paddle(x_pos):
    p = turtle.Turtle()
    p.speed(0)
    p.shape("square")
    p.color("white")
    p.shapesize(stretch_wid=5, stretch_len=1)
    p.penup()
    p.goto(x_pos, 0)
    return p

paddle_a = make_paddle(-350)
paddle_b = make_paddle(350)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.22 * random.choice((1, -1))
ball.dy = 0.18 * random.choice((1, -1))

score_a = 0
score_b = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, (HEIGHT // 2) - 40)
pen.write("Player A: 0    Player B: 0", align="center", font=("Courier", 24, "normal"))

def paddle_a_up():
    y = paddle_a.ycor() + 30
    if y > (HEIGHT//2 - 50):
        y = HEIGHT//2 - 50
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor() - 30
    if y < -(HEIGHT//2 - 50):
        y = -(HEIGHT//2 - 50)
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() + 30
    if y > (HEIGHT//2 - 50):
        y = HEIGHT//2 - 50
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() - 30
    if y < -(HEIGHT//2 - 50):
        y = -(HEIGHT//2 - 50)
    paddle_b.sety(y)

def update_score():
    pen.clear()
    pen.write(f"Player A: {score_a}    Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

def reset_ball(direction=1):
    ball.goto(0, 0)
    ball.dx = 0.22 * direction
    ball.dy = 0.18 * random.choice((1, -1))

def quit_game():
    wn.bye()

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(quit_game, "q")

while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Top and bottom collisions
    if ball.ycor() > (HEIGHT//2 - 10):
        ball.sety(HEIGHT//2 - 10)
        ball.dy *= -1

    if ball.ycor() < -(HEIGHT//2 - 10):
        ball.sety(-(HEIGHT//2 - 10))
        ball.dy *= -1

    # Right paddle collision
    if (ball.xcor() > 330 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(330)
        ball.dx *= -1
        ball.dx *= 1.03

    # Left paddle collision
    if (ball.xcor() < -330 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-330)
        ball.dx *= -1
        ball.dx *= 1.03

    # Ball goes out right
    if ball.xcor() > (WIDTH//2 - 10):
        score_a += 1
        update_score()
        reset_ball(direction=-1)

    # Ball goes out left
    if ball.xcor() < -(WIDTH//2 - 10):
        score_b += 1
        update_score()
        reset_ball(direction=1)

    time.sleep(0.01)
