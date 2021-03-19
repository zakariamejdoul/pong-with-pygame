import pygame
import sys
import random


def ball_moves():
    global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    # Scores
    if ball.left <= 0:
        score_time = pygame.time.get_ticks()
        player_score += 1

    if ball.right >= screen_width:
        score_time = pygame.time.get_ticks()
        opponent_score += 1

    if ball.colliderect(player) and ball_speed_x > 0:
        if abs(ball.right - player.left) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - player.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - player.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1

    if ball.colliderect(opponent) and ball_speed_x < 0:
        if abs(ball.left - opponent.right) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - opponent.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - opponent.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1


def player_moves():
    player.y = pygame.mouse.get_pos()[1]

    if player.top <= 0:
        player.top = 0

    if player.bottom >= screen_height:
        player.bottom = screen_height


def opponent_moves():
    if opponent.top < ball.y:
        opponent.y += opponent_speed

    if opponent.bottom > ball.y:
        opponent.y -= opponent_speed

    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height


def restart_ball():
    global ball_speed_x, ball_speed_y, ball_move, score_time

    ball.center = (screen_width / 2, screen_height / 2)
    current_time = pygame.time.get_ticks()

    if current_time - score_time < 700:
        number_three = font.render("3", False, componentColor)
        screen.blit(number_three, (screen_width/2 - 10, screen_height/2 + 20))
    if 700 < current_time - score_time < 1400:
        number_two = font.render("2", False, componentColor)
        screen.blit(number_two, (screen_width/2 - 10, screen_height/2 + 20))
    if 1400 < current_time - score_time < 2100:
        number_one = font.render("1", False, componentColor)
        screen.blit(number_one, (screen_width/2 - 10, screen_height/2 + 20))

    if current_time - score_time < 2100:
        ball_speed_y, ball_speed_x = 0, 0
    else:
        ball_speed_x = 7 * random.choice((1, -1))
        ball_speed_y = 7 * random.choice((1, -1))
        score_time = None


pygame.init()
clock = pygame.time.Clock()

# Game window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong Game')

# Color
bgColor = pygame.Color('grey12')
componentColor = (200, 200, 200)

# Game shapes
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height / 2 - 70, 10, 140)

# Game utils
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 7
ball_move = False
score_time = True

# Score
player_score = 0
opponent_score = 0
font = pygame.font.Font('freesansbold.ttf', 32)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ball_moves()
    player_moves()
    opponent_moves()

    # Graphics
    screen.fill(bgColor)
    pygame.draw.rect(screen, componentColor, player)
    pygame.draw.rect(screen, componentColor, opponent)
    pygame.draw.ellipse(screen, componentColor, ball)
    pygame.draw.aaline(screen, componentColor,
                    (screen_width/2, 0), (screen_width/2, screen_height))

    if score_time:
        restart_ball()
    player_text = font.render(f'{player_score}', False, componentColor)
    screen.blit(player_text, (660, 470))

    opponent_text = font.render(f'{opponent_score}', False, componentColor)
    screen.blit(opponent_text, (600, 470))

    pygame.display.flip()
    clock.tick(60)
