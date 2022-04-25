

import turtle

# initialize scoring

player1Score = 0
player2Score = 0

wn = turtle.Screen()    
wn.title("Speedy Pong") 
wn.bgcolor('black')    
wn.setup(width=800,height=600) 
wn.tracer(0)

# Left Sided Paddle
leftPaddle = turtle.Turtle()
leftPaddle.speed(0)
leftPaddle.shape('square')
leftPaddle.color('white')
leftPaddle.shapesize(stretch_wid=5,stretch_len=1)
leftPaddle.penup()
leftPaddle.goto(-350,0)

# Right Sided Paddle
rightPaddle = turtle.Turtle()
rightPaddle.speed(0)
rightPaddle.shape('square')
rightPaddle.shapesize(stretch_wid=5,stretch_len=1)
rightPaddle.color('white')
rightPaddle.penup()
rightPaddle.goto(350,0)

#Pong Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0,0)

#Ball Movement 
ball_dx = 1.5   
ball_dy = 1.5

# Game scoring Card 
pen = turtle.Turtle()
pen.speed(0)
pen.color('red')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player 1: 0                    Player 2: 0 ",align="center",font=('Arial',24,"normal"))



# Moving right paddle upwards
def paddleRightUp():
    y = rightPaddle.ycor()
    y = y + 15
    rightPaddle.sety(y)

# Moving right paddle downwards
def paddleRightDown():
    y = rightPaddle.ycor()
    y = y - 15
    rightPaddle.sety(y)

# Moving left paddle upwards
def paddleLeftUp():
    y = leftPaddle.ycor()
    y = y + 15
    leftPaddle.sety(y)

# Moving left paddle downwards
def paddleLeftDown():
    y = leftPaddle.ycor()
    y = y - 15
    leftPaddle.sety(y)


# Keyboard binding modified // Taken from another Pong example
wn.listen()
wn.onkeypress(paddleLeftUp,"w")
wn.onkeypress(paddleLeftDown,"s")
wn.onkeypress(paddleRightUp,"Up")
wn.onkeypress(paddleRightDown,"Down")


# Game Loop

while True:
    wn.update() 

    # Moving the ball to and fro
    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)

    # Game Border

    # Right top paddle Border
    if ball.ycor() > 290:   
        ball.sety(290)
        ball_dy = ball_dy * -1
        
    # Left top paddle Border
    if ball.ycor() < -290:  
        ball.sety(-290)
        ball_dy = ball_dy * -1
        
    # Right side paddle border
    if ball.xcor() > 390:   
        ball.goto(0,0)
        ball_dx = -1 * -1
        player1Score = player1Score + 1
        pen.clear()
        pen.write("Player 1: {}                    Player 2: {} ".format(player1Score,player2Score),align="center",font=('Arial',24,"normal"))
       


    # Left side paddle border
    if(ball.xcor()) < -390: 
        ball.goto(0,0)
        ball_dx = 1 * -1
        player2Score = player2Score + 1
        pen.clear()
        pen.write("Player 1: {}                    Player 2: {} ".format(player1Score,player2Score),align="center",font=('Arial',24,"normal"))
        


    # Ball collision with paddles // Taken from Pong Example as I could not figure it out
    if(ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < rightPaddle.ycor() + 40 and ball.ycor() > rightPaddle.ycor() - 40):
        ball.setx(340)
        ball_dx = ball_dx * -1.5
        

    if(ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < leftPaddle.ycor() + 40 and ball.ycor() > leftPaddle.ycor() - 40):
        ball.setx(-340)
        ball_dx = ball_dx * -1.5
        

    # Scenario if Player 1 wins
    if player1Score >= 5:
        winPen = turtle.Turtle()
        winPen.speed(0)
        winPen.color('red')
        winPen.penup()
        winPen.hideturtle()
        winPen.goto(0,0)
        winPen.write("Player 1 Wins!!!!!!",align="center",font=('Arial',24,"normal"))
        break
    
    #Scenario if Player 2 wins
    if player2Score >= 5:
        winPen = turtle.Turtle()
        winPen.speed(0)
        winPen.color('red')
        winPen.penup()
        winPen.hideturtle()
        winPen.goto(0,0)
        winPen.write("Player 2 Wins!!!!!!",align="center",font=('Arial',24,"normal"))
        break
