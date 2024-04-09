## Графический Пользовательский Интерфейс Юрия Компьютерова
import pygame

pygame.init()
# Инициализируйте интерфейс
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Юрий Компьютеров')
font = pygame.font.Font('assets/Cyrillic/CYRIL2.TTF', 24)
yuri_img = pygame.image.load('Yuri_photo.png').convert()
screen.blit(yuri_img, (0, 0))
pygame.display.flip()

# Инициализируйте петля
run = True

while (run):
    screen.
# Event Handler
    for event in pygame.event.get():
        if event == pygame.QUIT:
            run = False
pygame.quit()

#MULTIPLE SCREENS IN PYTHON:
# MUlTIPLE FXNS WITH THEIR OWN GAME LOOPS