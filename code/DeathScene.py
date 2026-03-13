import pygame, sys
from settings import *
from buttons import Button

class DeathScene:
    def __init__(self, main, display, gameStateManager):
        self.main = main
        self.display = display
        self.gameStateManager = gameStateManager
        self.display_surf = pygame.display.get_surface()
        
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH),pygame.RESIZABLE)
        self.menu_font= pygame.font.Font(UI_FONT, 70)
        self.font= pygame.font.Font(UI_FONT, 40)
        
        self.BG = pygame.image.load('../zeldacopy/graphics/background/spiral.png')
    
        
    def run(self):
        while True:
            self.screen.blit(self.BG,(0,0))
            
            # Draw a rectangle
            block_rect = pygame.Rect(200,50,850,300)
            pygame.draw.rect(self.screen, (150,150,150), block_rect)
            

            EX_text = self.menu_font.render("You Died", False, 'Purple')
            EX_rect = EX_text.get_rect(center=(640, 120))
            EX_out_text = self.menu_font.render("You Died", False, 'black')
            EX_out_rect = EX_out_text.get_rect(center=(640, 120)).inflate(10,5)
            
            self.screen.blit(EX_out_text, EX_out_rect)
            self.screen.blit(EX_text, EX_rect)
            
            RT_text = self.font.render("Return to Main Menu", False, 'black')
            RT_rect = RT_text.get_rect(center = (640, 250) ).inflate(10,5)
            
            self.screen.blit(RT_text, RT_rect)

            return_button = Button(
                image=self.font.render("Return to Main Menu", True, 'blue'),
                pos=(640, 250) ,
                text_input="Return to Main Menu",
                font=self.font,
                base_color='blue',
                hovering_color='green'
            )

            MOUSE_POINTER = pygame.mouse.get_pos()

            for button in [return_button]:
                button.change_color(MOUSE_POINTER)
                button.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if return_button.check_input(MOUSE_POINTER):
                        self.gameStateManager.set_state('start')
                        return  # Exit the loop to change state

            pygame.display.update()   