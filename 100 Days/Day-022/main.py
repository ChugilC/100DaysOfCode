import time
from turtle import Screen
from paddle import Paddle
from  ball import Ball
from scoreboard import ScoreBoard

GAME_SCORE = 10

# Screen SetUp
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

# Paddle 
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
 
# Ball
ball = Ball()

# ScoreBoard
scoreboard = ScoreBoard()

# Event listeners
screen.listen()
screen.onkeypress(r_paddle.go_up, 'Up')
screen.onkeypress(r_paddle.go_down, 'Down')
screen.onkeypress(l_paddle.go_up, 'w')
screen.onkeypress(l_paddle.go_down, 's')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 290 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    
    # Detech L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    # Game over scenario
    if scoreboard.l_score == GAME_SCORE:
        scoreboard.end_game("Left Player is the Winner")
        game_is_on = False
    elif scoreboard.r_score == GAME_SCORE:
        scoreboard.end_game("Right Player is the Winner")
        game_is_on = False

screen.exitonclick()