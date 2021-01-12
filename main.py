from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard, CenterLine
from tkinter import messagebox
import time


def main():
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor('black')
    screen.title('Pong Game')
    screen.tracer(0)
    score_board = ScoreBoard()
    score_board.display_score()
    CenterLine()
    player1 = Paddle((350, 0))
    player2 = Paddle((-350, 0))
    ball = Ball()
    screen.onkey(player1.move_up, 'Up')
    screen.onkey(player1.move_down, 'Down')
    screen.onkey(player2.move_up, 'w')
    screen.onkey(player2.move_down, 's')
    screen.listen()

    def game_continue():
        if messagebox.askretrycancel("Game Over!!","Wanna play again? "):
            screen.clear()
            main()

    running = True
    while running:
        time.sleep(0.05)
        screen.update()
        if score_board.check_win():
            score_board.final_result()
            ball.hideturtle()
            break
        if ball.ispoint_wait:
            if ball.point_wait < 50:
                ball.point_wait += 1
                continue
            else:
                ball.ispoint_wait = False
                ball.point_wait = 1
        screen.update()
        ball.move()
        # for not repeating collision if the distance is small
        if player1.is_collided:
            if player1.safe_count < 5:
                player1.safe_count += 1
            else:
                player1.is_collided = False
                player1.safe_count = 1
        elif player2.is_collided:
            if player2.safe_count < 5:
                player2.safe_count += 1
            else:
                player2.is_collided = False
                player2.safe_count = 1

        if ball.ycor() > 265 or ball.ycor() < -270:
            ball.wall_collision()

        if ball.xcor() < 370 and ball.distance(player1) < 45 and not player1.is_collided:
            ball.paddle_collision()
            ball.hit_count += 1
            ball.hit = True
            player1.is_collided = True
        elif ball.xcor() > -370 and ball.distance(player2) < 45 and not player2.is_collided:
            ball.paddle_collision()
            ball.hit_count += 1
            ball.hit = True
            player2.is_collided = True

        if ball.hit_count % 2 == 0 and ball.hit_count != 0 and ball.hit:
            if ball.bounce_speed < 0:
                ball.bounce_speed -= 1.5
            else:
                ball.bounce_speed += 1.5
            ball.bounce_x = ball.bounce_speed
            ball.hit = False

        if ball.xcor() > 380:
            score_board.clear()
            score_board.score1 += 1
            score_board.display_score()
            ball.ispoint_wait = True
            ball.ball_reset()

        elif ball.xcor() < -380:
            score_board.clear()
            score_board.score2 += 1
            score_board.display_score()
            ball.ispoint_wait = True
            ball.ball_reset()

    screen.update()
    time.sleep(1)
    game_continue()
    screen.bye()
    screen.exitonclick()


def main_menu():
    screen = Screen()
    screen.bgcolor('black')
    screen.tracer(0)
    text = Turtle()
    text.penup()
    text.hideturtle()
    text.color('white')
    text.write('Press ENTER to Continue', False, align='center', font=("Arial", 20, "normal"))
    text.goto(0, 200)
    text.color('lime')
    text.write("!!The first to score 7 points win!!", False, align='center', font=("Arial", 25, "normal"))
    text.color('cyan')
    text.goto(0, -300)
    text.write("Player1 controls 'w' & 's'\t\t\t\t\t\t\tPlayer2 controls 'Up' & 'Down'",False, align='center', font=("Arial", 10, "normal"))

    def gotomain():
        text.clear()
        screen.clear()
        main()
    screen.update()
    screen.onkey(gotomain, "Return")
    screen.listen()
    screen.exitonclick()

main_menu()