## Графический Пользовательский Интерфейс Юрия Компьютерова
import pygame, sys

pygame.init()

# Инициализируйте интерфейс
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750
#MULTIPLE SCREENS IN PYTHON:
# MUlTIPLE FXNS WITH THEIR OWN GAME LOOPS

def get_font(size):
    return pygame.font.Font('assets/Cyrillic/CYRIL2.TTF', size)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Юрий Компьютеров')
yuri = pygame.image.load('assets/Yuri_photo.png').convert()
bg_img = pygame.image.load('assets/russian_flag.png').convert()

# Инициализируйте петля
def main_menu():
    while True:
        screen.blit(bg_img, (0, 0))
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TXT = get_font(75).render('ГЛАВНОЕ МЕНЮ ЮРИЯ', True, '#b68f40')
        MENU_SHAPE = MENU_TXT.get_rect(center=(750, 200))
        
        screen.blit(MENU_TXT, MENU_SHAPE)
        
# Event Handler
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()
        
        
main_menu()