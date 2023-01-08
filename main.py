import pygame
from sys import exit
import random

def generate_random_num():
    return random.randint(0, 100)


pygame.init()
screen = pygame.display.set_mode((400, 400))
screen.fill("Gray")
pygame.display.set_caption("Random Number Generator")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 70)

icon = pygame.image.load("?.png")
pygame.display.set_icon(icon)
rand_num = generate_random_num()
text = font.render(str(rand_num), True, "White")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                rand_num = generate_random_num()

    text = font.render(str(rand_num), True, "White")

    screen.fill("Gray")
    screen.blit(text, (170, 170))
    
    pygame.display.update()
    clock.tick(60)