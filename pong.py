"""
Pong játék a Python beépített turtle moduljával.

Irányítás:
  Bal ütő: W / S
  Jobb ütő: FEL / LE nyíl
  Új játék: R
  Kilépés: Esc
"""

import turtle

from pong_logic import bounce_vertical, clamp_paddle_y, has_won, scoring_player

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_STEP = 30
BALL_STEP = 5
WINNING_SCORE = 5

screen = turtle.Screen()
screen.title("Pong – Python Turtle | K11")
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)

# Szaggatott középvonal
center_line = turtle.Turtle()
center_line.hideturtle()
center_line.color("gray")
center_line.penup()
center_line.goto(0, SCREEN_HEIGHT // 2 - 20)
center_line.setheading(270)
for _ in range(15):
    center_line.pendown()
    center_line.forward(12)
    center_line.penup()
    center_line.forward(10)


def make_paddle(x):
    """Létrehoz egy ütőt az adott x koordinátán."""
    paddle = turtle.Turtle()
    paddle.shape("square")
    paddle.color("white")
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    paddle.penup()
    paddle.goto(x, 0)
    return paddle


left_paddle = make_paddle(-SCREEN_WIDTH // 2 + 40)
right_paddle = make_paddle(SCREEN_WIDTH // 2 - 40)

ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = BALL_STEP
ball.dy = BALL_STEP

score_left = 0
score_right = 0

scoreboard = turtle.Turtle()
scoreboard.hideturtle()
scoreboard.color("white")
scoreboard.penup()
scoreboard.goto(0, SCREEN_HEIGHT // 2 - 70)

message = turtle.Turtle()
message.hideturtle()
message.color("yellow")
message.penup()

game_over = False


def draw_score():
    """Kirajzolja az aktuális pontszámot."""
    scoreboard.clear()
    scoreboard.write(
        f"{score_left}     {score_right}",
        align="center",
        font=("Arial", 28, "normal"),
    )


def move_paddle(paddle, dy):
    """Elmozdítja az ütőt, ha az nem lép ki a pályáról."""
    if game_over:
        return
    limit = SCREEN_HEIGHT // 2 - 60
    paddle.sety(clamp_paddle_y(paddle.ycor(), dy, limit))


def left_up():
    move_paddle(left_paddle, PADDLE_STEP)


def left_down():
    move_paddle(left_paddle, -PADDLE_STEP)


def right_up():
    move_paddle(right_paddle, PADDLE_STEP)


def right_down():
    move_paddle(right_paddle, -PADDLE_STEP)


def reset_ball(direction):
    """Középre helyezi a labdát és beállítja az indulási irányát."""
    ball.goto(0, 0)
    ball.dx = BALL_STEP * direction
    ball.dy = BALL_STEP if ball.dy >= 0 else -BALL_STEP


def finish_game(winner):
    global game_over
    game_over = True
    message.clear()
    message.goto(0, 0)
    message.write(
        f"{winner} nyert!\nÚj játék: R",
        align="center",
        font=("Arial", 24, "bold"),
    )


def restart_game():
    global score_left, score_right, game_over
    score_left = 0
    score_right = 0
    game_over = False
    left_paddle.goto(-SCREEN_WIDTH // 2 + 40, 0)
    right_paddle.goto(SCREEN_WIDTH // 2 - 40, 0)
    message.clear()
    reset_ball(1)
    draw_score()


def update_game():
    global score_left, score_right

    if not game_over:
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Visszapattanás a felső és alsó falról
        top = SCREEN_HEIGHT // 2 - 20
        bottom = -SCREEN_HEIGHT // 2 + 20
        new_y, new_dy = bounce_vertical(ball.ycor(), ball.dy, top, bottom)
        ball.sety(new_y)
        ball.dy = new_dy

        # Ütközés a bal oldali ütővel
        if (
            ball.dx < 0
            and left_paddle.xcor() - 20 <= ball.xcor() <= left_paddle.xcor() + 20
            and abs(ball.ycor() - left_paddle.ycor()) <= 55
        ):
            ball.setx(left_paddle.xcor() + 20)
            ball.dx = abs(ball.dx) + 0.2
            ball.dy += (ball.ycor() - left_paddle.ycor()) * 0.08

        # Ütközés a jobb oldali ütővel
        if (
            ball.dx > 0
            and right_paddle.xcor() - 20 <= ball.xcor() <= right_paddle.xcor() + 20
            and abs(ball.ycor() - right_paddle.ycor()) <= 55
        ):
            ball.setx(right_paddle.xcor() - 20)
            ball.dx = -(abs(ball.dx) + 0.2)
            ball.dy += (ball.ycor() - right_paddle.ycor()) * 0.08

        # Pontszerzés
        if ball.xcor() > SCREEN_WIDTH // 2:
            score_left += 1
            draw_score()
            if has_won(score_left, WINNING_SCORE):
                finish_game("A bal játékos")
            else:
                reset_ball(-1)
        elif ball.xcor() < -SCREEN_WIDTH // 2:
            score_right += 1
            draw_score()
            if has_won(score_right, WINNING_SCORE):
                finish_game("A jobb játékos")
            else:
                reset_ball(1)

    screen.update()
    screen.ontimer(update_game, 16)


screen.listen()
screen.onkeypress(left_up, "w")
screen.onkeypress(left_down, "s")
screen.onkeypress(right_up, "Up")
screen.onkeypress(right_down, "Down")
screen.onkeypress(restart_game, "r")
screen.onkeypress(screen.bye, "Escape")

draw_score()
update_game()
screen.mainloop()
