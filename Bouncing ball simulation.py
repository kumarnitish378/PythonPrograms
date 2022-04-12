import turtle
wn = turtle.Screen()
wn.bgcolor("black")
d = 5
turtle.penup()
turtle.goto(-350-d,-200-d)
turtle.pendown()
turtle.color("gray")
turtle.pensize(5)
turtle.forward(700+d)
turtle.left(90)
turtle.forward(500+d)
turtle.left(90)
turtle.forward(700+d)
turtle.left(90)
turtle.forward(500+d)
ball = turtle.Turtle()
ball.shape("circle")
# ball.penup()
ball.color("red")
ball.penup()
ball.speed(0)
ball.goto(0,300)
ball.dy = 0
gravity = 0.9
ball.dy = 0
ball.dx = 1
while True:
    ball.dy -= gravity
    print(ball.dy)
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor()  + ball.dx)
    if ball.ycor() < -200:
          ball.dy *= -1
          ball.color("green")
    if ball.xcor() > 350:
          ball.dx *= -1
          ball.color("red")
    if ball.xcor() < -350:
          ball.dx *= -1
          ball.color("pink")
    if ball.ycor() < -230:
          break
    # print(ball.xcor(),ball.ycor())
