import turtle
import os

wn = turtle.Screen()
wn.title("pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#  Score
score_a = 0
score_b = 0

#paddle a
paddle_a = turtle.Turtle()
paddle_a.speed()
paddle_a.shape("square")
paddle_a.color("green")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


#paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("green")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350, 0)


#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("yellow")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = .1
ball.dy = .1

# pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("palayer A : {} Player B : {}".format(score_a, score_b), align="center", font=("Courier",24,"normal") )

# function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
    
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
    
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
    
# keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#main game loop
while True:
    wn.update()

    #move ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ ball.dy)

    #border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1 
        score_a += 1
        pen.clear()
        os.system("aplay /home/christo/code/python/bounce.wav&")
        pen.write("palayer A : {} Player B : {}".format(score_a, score_b), align="center", font=("Courier",24,"normal") )

    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        os.system("aplay /home/christo/code/python/bounce.wav&")
        pen.write("palayer A : {} Player B : {}".format(score_a, score_b), align="center", font=("Courier",24,"normal") )

# paddle collision
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1 
        os.system("aplay /home/christo/code/python/bounce.wav&")
    
    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
        os.system("aplay /home/christo/code/python/bounce.wav&")


