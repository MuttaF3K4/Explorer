import pygame, sys
from pygame.locals import *
from settings import *
from buttons import Button


class StartMenu():
	def __init__(self, main, display, gameStateManager):
		# GameStateManager.__init__(self)
		self.main = main
		self.display = display
		self.gameStateManager = gameStateManager
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH), pygame.RESIZABLE)
		self.menu_font= pygame.font.Font(UI_FONT, 70)
		self.font= pygame.font.Font(UI_FONT, 40)
		
  
		self.BG = pygame.image.load('../zeldacopy/graphics/background/spiral.png')
  
		

	def run(self):
     
		# self.screen.fill("Blue")
  
		while True:
			pygame.display.set_caption('Man Must Explore')
			self.screen.blit(self.BG,(0,0))
			MOUSE_POINTER = pygame.mouse.get_pos()

			####Title Text
			menu_text = self.menu_font.render("MAN MUST EXPLORE",False,'Purple')
			menu_rect = menu_text.get_rect(center =(640,120))
			menu_outline = self.menu_font.render("MAN MUST EXPLORE",False,'Black')
			outline_rect = menu_outline.get_rect(center =(640,120)).inflate(10,5)
	
			self.screen.blit(menu_outline,outline_rect)
			self.screen.blit(menu_text,menu_rect)

			####Outline Text
			play_out_text = self.font.render("Start Your Adventure",False,'Black')
			play_out_rect = play_out_text.get_rect(center =(640,300)).inflate(10,5)
			options_out = self.font.render("Options",False,'Black')
			options_out_rect = options_out.get_rect(center =(640,400)).inflate(10,5)
			quit_out = self.font.render("Depart",False,'Black')
			quit_out_rect = quit_out.get_rect(center =(640,500)).inflate(10,5)
 
			self.screen.blit(play_out_text,play_out_rect)
			self.screen.blit(options_out,options_out_rect)
			self.screen.blit(quit_out,quit_out_rect)
	
	
			######Menu Buttons
			play_button = Button(image = self.font.render("Start Your Adventure", True, 'blue'), pos = (640,300), text_input = "Start Your Adventure", font = self.font, base_color='blue', hovering_color='green')
			options_button = Button(image = self.font.render("Options", True, 'blue'), pos = (640,400), text_input = "Options", font = self.font, base_color='blue', hovering_color='green')
			quit_button = Button(image = self.font.render("Depart", True, 'blue'), pos = (640,500), text_input = "Depart", font = self.font, base_color='blue', hovering_color='green')
	

			for button in [play_button, options_button, quit_button]:
				button.change_color(MOUSE_POINTER)
				button.update(self.screen)


			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
 
				if event.type == pygame.MOUSEBUTTONDOWN:
					if play_button.check_input(MOUSE_POINTER):
						self.main.start_game()
						print('pressed')
					if options_button.check_input(MOUSE_POINTER):
						self.main.options()
						print('pressed')
					if quit_button.check_input(MOUSE_POINTER):
						self.main.quit()
						print('pressed')
      
			
	
				
				pygame.display.update()