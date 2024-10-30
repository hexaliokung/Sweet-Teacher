import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1600, 960))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/horrorbg.jpg")

def get_font(size):
    return pygame.font.Font("assets/MisterBrush-GOmvy.ttf", size)


WHITE = 255, 255, 255
BLACK = 0, 0, 0
GREY  = 128, 128, 128
RED = 255, 0, 0


def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(50), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

    

        PLAY_BUTTON = Button(image=pygame.image.load("assets/menu_inv_button.png"), pos=(640, 250), 
                            text_input="ENDING", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
       

        for button in [PLAY_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()