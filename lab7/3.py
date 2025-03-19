import pygame
import sys

pygame.init()

screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ball Movement")

ball_radius = 25
ball_color = (255, 0, 0)  
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_speed = 20

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP] and ball_y - ball_radius > 0:
        ball_y -= ball_speed
    if keys[pygame.K_DOWN] and ball_y + ball_radius < screen_height:
        ball_y += ball_speed
    if keys[pygame.K_LEFT] and ball_x - ball_radius > 0:
        ball_x -= ball_speed
    if keys[pygame.K_RIGHT] and ball_x + ball_radius < screen_width:
        ball_x += ball_speed

    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    pygame.display.flip()

    clock.tick(60)
