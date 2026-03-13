import pygame, sys
from pygame.locals import *
from settings import *
from support import *
from level import Level
from GameStateManager import GameStateManager
from StartMenu import StartMenu
from Options import Options
from DeathScene import DeathScene
from PauseScene import PauseScene

# Write a line to change directory automatically

# Create start up menu, make first time players have to open settings with "Censor words" on it




class Game:
	def __init__(self):
		  
		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH), pygame.RESIZABLE)
		pygame.display.set_caption('Man Must Explore')
		self.clock = pygame.time.Clock()
		Level(self)


		# Switching Game States
		self.gameStateManager = GameStateManager('start')
		self.start = StartMenu(self, self.screen, self.gameStateManager)
		self.level = Level(self, self.screen, self.gameStateManager)
		self.option = Options(self, self.screen, self.gameStateManager)
		self.death = DeathScene(self, self.screen, self.gameStateManager)
		self.pause = PauseScene(self, self.screen, self.gameStateManager)
  
		# States Dictionary
		self.states = {'start': self.start, 
                'level': self.level,
                'options': self.option,
                'death': self.death,
                'pause': self.pause 
                }
  
		# Sound
		main_sound = pygame.mixer.Sound('../zeldacopy/audio/main.ogg')
		main_sound.set_volume(0.2)
		main_sound.play(loops = -1) 
			
   
	def start_game(self):
		self.gameStateManager.set_state('level')
		game.run()
		
  		#print(self.gameStateManager)  # Check if gameStateManager is initialized
		#print(hasattr(self.gameStateManager, 'set_state'))  # Check if set_state method exists
		#print(self.gameStateManager.get_state())
  
	def options(self):
		pygame.display.set_caption('Options')
		self.gameStateManager.set_state('options')
		game.run()
  
	def quit(self):
		pygame.quit()
		sys.exit()

	def death_scene(self):
		self.gameStateManager.set_state('death')
		game.run()
  
	def return_to_title(self):
		self.gameStateManager.set_state('start')
		game.run()
	
	def run(self):
		while True: 
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
					
				if event.type == VIDEORESIZE:
					self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
		
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_m:
						self.level.toggle_menu()
    
			
			self.screen.fill(WATER_COLOR)
			Level.create_map(self)
			self.states[self.gameStateManager.get_state()].run()

			#self.level.run()
			pygame.display.update()
			self.clock.tick(FPS)
   

if __name__ == '__main__':
	game = Game()
	game.run()









			

# play_text = self.font.render("Start Your Adventure",False,'Blue')
# play_rect = play_text.get_rect(center =(640,300))
# self.screen.blit(play_text,play_rect)
	
# options_text = self.font.render("Options",False,'Blue')
# options_rect = options_text.get_rect(center =(640,400))
# self.screen.blit(options_text,options_rect)
   
# quit_text = self.font.render("Depart",False,'Blue')
# quit_rect = quit_text.get_rect(center =(640,500))
# self.screen.blit(quit_text,quit_rect)
   
   