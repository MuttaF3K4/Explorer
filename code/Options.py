import pygame,sys
from buttons import Button
from settings import *

class Options:
    def __init__(self, main, display, gameStateManager):
        self.main = main
        self.display = display
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH), pygame.RESIZABLE)
        self.gameStateManager = gameStateManager
        self.menu_font= pygame.font.Font(UI_FONT, 70)
        self.font= pygame.font.Font(UI_FONT, 40)
        
        self.BG = pygame.image.load('../zeldacopy/graphics/background/spiral.png')
        
    def run(self):
        while True:
            self.screen.blit(self.BG,(0,0))
            MOUSE_POINTER = pygame.mouse.get_pos()
            
            
            menu_text = self.menu_font.render("Settings",False,'Purple')
            menu_rect = menu_text.get_rect(center =(640,120))
            menu_outline = self.menu_font.render("Settings",False,'Black')
            outline_rect = menu_outline.get_rect(center =(640,120)).inflate(10,5)
            
            self.screen.blit(menu_outline,outline_rect)
            self.screen.blit(menu_text,menu_rect)
            
            
            S1_text = self.font.render("Settings One",False,'Blue')
            S1_rect =  S1_text.get_rect(center =(640,300))
            S1_outline = self.font.render("Settings One",False,'Black')
            S1_out_rect = S1_outline.get_rect(center =(640,300)).inflate(10,5)
            
            self.screen.blit(S1_outline,S1_out_rect)
            self.screen.blit(S1_text,S1_rect)
            
            S2_text = self.font.render("Settings Two",False,'Blue')
            S2_rect =  S2_text.get_rect(center =(640,400))
            S2_outline = self.font.render("Settings Two",False,'Black')
            S2_out_rect = S2_outline.get_rect(center =(640,400)).inflate(10,5)
            
            self.screen.blit(S2_outline,S2_out_rect)
            self.screen.blit(S2_text,S2_rect)
            
            S3_text = self.font.render("Settings Three",False,'Blue')
            S3_rect =  S3_text.get_rect(center =(640,500))
            S3_outline = self.font.render("Settings Three",False,'Black')
            S3_out_rect = S3_outline.get_rect(center =(640,500)).inflate(10,5)
            
            self.screen.blit(S3_outline,S3_out_rect)
            self.screen.blit(S3_text,S3_rect)
            
            back_outline = self.font.render("< Back", False, 'black')
            back_rect = back_outline.get_rect(center = (150,120)).inflate(10,5)
            
            self.screen.blit(back_outline,back_rect)
            
            
            
            setting_one = Button(image = self.font.render("Settings One", True, 'blue'), pos = (640,300), text_input = "Settings One", font = self.font, base_color='blue', hovering_color='green')
            setting_two = Button(image = self.font.render("Settings Two", True, 'blue'), pos = (640,400), text_input = "Settings Two", font = self.font, base_color='blue', hovering_color='green')
            setting_three = Button(image = self.font.render("Settings Three", True, 'blue'), pos = (640,500), text_input = "Settings Three", font = self.font, base_color='blue', hovering_color='green')            
            Back_button  = Button(image = self.font.render("< Back", True,'blue'), pos = (150,120), text_input = "< Back", font =self.font, base_color = 'blue', hovering_color = 'green')
            
            for button in [setting_one, setting_two, setting_three, Back_button]:
                button.change_color(MOUSE_POINTER)
                button.update(self.screen)
            
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.gameStateManager.set_state('start')
                        self.main.run()
                    
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if setting_one.check_input(MOUSE_POINTER):
                        print('Setting One Pressed')
                    if setting_two.check_input(MOUSE_POINTER):
                        print('Setting Two Pressed')
                    if setting_three.check_input(MOUSE_POINTER):
                        print('Setting Three Pressed')
                    if Back_button.check_input(MOUSE_POINTER):
                        self.gameStateManager.set_state('start')
                        self.main.run()
                    
                    
                pygame.display.update()

        