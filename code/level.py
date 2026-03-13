import pygame 
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *
from random import choice, randint
from weapon import Weapon
from ui import UI
from enemy import Enemy
from particles import AnimationPlayer
from magic import MagicPlayer
from upgrade import Upgrade
from GameStateManager import GameStateManager

class Level:
	def __init__(self, main, display, gameStateManager):

		# Game State
		self.display = display
		self.gameStateManager = gameStateManager
		self.main = main


		# get the display surface 
		self.display_surface = pygame.display.get_surface()
		self.game_paused = False

		# sprite group setup
		self.visible_sprites = YSortCameraGroup()
		self.obstacle_sprites = pygame.sprite.Group()

		# Attack sprites
		self.current_attack = None
		self.attack_sprites = pygame.sprite.Group()
		self.attackable_sprites = pygame.sprite.Group()

		# sprite setup
		#self.create_map()

		# User interface
		self.ui = UI()
		self.upgrade = Upgrade(self.player)
  
		# Particles
		self.animation_player = AnimationPlayer()
		self.magic_player = MagicPlayer(self.animation_player)


	def create_map(self):
		layouts = {										# Need to make 'FloorBlocks' for my Links map
			'boundary': import_csv_layout('../zeldacopy/map/map_FloorBlocks.csv'),
			'grass': import_csv_layout('../zeldacopy/map/map_Grass.csv'),
			'object': import_csv_layout('../zeldacopy/map/map_Objects.csv'),
			'entities': import_csv_layout('../zeldacopy/map/map_Entities.csv')
		}
		graphics = {
			'grass': import_folder('../zeldacopy/graphics/grass'),
			'objects': import_folder('../zeldacopy/graphics/objects'),
		} 
     
		for style,layout in layouts.items():
			for row_index,row in enumerate(layout):
				for col_index, col in enumerate(row):
					if col != '-1':
						x = col_index * TILESIZE
						y = row_index * TILESIZE
						if style == 'boundary':
							Tile((x,y),[self.obstacle_sprites,],'invisible')
						if style == 'grass':
							random_grass_image = choice(graphics['grass'])
							Tile(
           						(x,y),
                 				[self.visible_sprites,self.obstacle_sprites,self.attackable_sprites],
                     			'grass',
                        		random_grass_image)

							
						if style == 'object':
							surf = graphics['objects'][int(col)]
							Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'object',surf)
       
						if style == 'entities':
							if col == '394': # number based off placement on tileset
								self.player = Player(
									(x,y),
									[self.visible_sprites],
									self.obstacle_sprites,
									self.create_attack,
									self.destroy_attack,
									self.create_magic
									)
							else:
								if col == '390': monster_name = 'bamboo'
								elif col == '391': monster_name = 'spirit'
								elif col == '392': monster_name = 'raccoon'
								else: monster_name = 'squid'
								Enemy(monster_name,(x,y),
              					[self.visible_sprites, self.attackable_sprites],
              					self.obstacle_sprites,
                   				self.damage_player,
                       			self.trigger_death,
								self.add_exp
                          		)
           							

	def create_attack(self):
		self.current_attack = Weapon(self.player,[self.visible_sprites,self.attack_sprites])


	def destroy_attack(self):
		if self.current_attack:
			self.current_attack.kill()
		self.current_attack = None


	def create_magic(self,style,strength,cost):
		if style == 'heal':
			self.magic_player.heal(self.player,strength,cost,[self.visible_sprites])

		if style == 'flame':						# makes asset visible  makes asset damagable
			self.magic_player.flame(self.player,cost,[self.visible_sprites,self.attack_sprites])
     
  
	def player_attack_logic(self):
		if self.attack_sprites:
			for attack_sprite in self.attack_sprites:
				collision_sprites = pygame.sprite.spritecollide(attack_sprite,self.attackable_sprites,False)#spritecollide(sprite,group,DOKILL[True or False])
				if collision_sprites:
					for target_sprite in collision_sprites:
						if target_sprite.sprite_type == 'grass':
							pos = target_sprite.rect.center
							offset = pygame.math.Vector2(0,50)
							for leaf in range(randint(3,6)):	
								self.animation_player.create_grass_particles(pos - offset,[self.visible_sprites])
							target_sprite.kill()
						else:
							target_sprite.get_damage(self.player,attack_sprite.sprite_type)

  
	def damage_player(self,amount,attack_type):
		if self.player.vulnerable:
			if self.player.health >= 0:
				self.player.health -= amount
			self.player.vulnerable = False
			self.player.hurt_time = pygame.time.get_ticks()
			# spawn particales
			self.animation_player.create_particles(attack_type,self.player.rect.center,[self.visible_sprites])
   
   
		# Change to trigger death
	

	def trigger_death(self,pos,particle_type):
		self.animation_player.create_particles(particle_type,pos,self.visible_sprites)
		
		if self.player.energy >= 50:
			self.player.energy = 60
		else:
			self.player.energy += 15

    
	def player_death(self):
		if self.player.health <= 0:
			self.game_paused = True
			self.main.death_scene()
			del self.create_map
    
    
	def add_exp(self,amount):
		
		self.player.exp += amount
    
	# def reset_player(self):
		# self.reset_health = self.player.stats['health']
		# 
		# print(self.reset_health)
		# return self.player.health == self.reset_health
	# 
	
	def toggle_menu(self):
		self.game_paused = not self.game_paused
    
    
	def run(self):
		# update and draw the game
		self.visible_sprites.custom_draw(self.player)
		self.ui.display(self.player)
		self.player_death()

		if self.game_paused:
			self.upgrade.display()
			self.player.reset_player()
		else:
			self.visible_sprites.update()
			self.visible_sprites.enemy_update(self.player)
			self.player_attack_logic()


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        
        # General setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] //2 
        self.half_height = self.display_surface.get_size()[1] //2 
        self.offset = pygame.math.Vector2(100,-200)
        
        # Creating the Floor										replace ground with finished link map	
        self.fl_surf = pygame.image.load('../zeldacopy/graphics/tilemap/Newground.png').convert() # Dont need convert.alpha() for Tilemap
        self.fl_rect = self.fl_surf.get_rect(topleft = (0,0))
           
    
    def enemy_update(self,player,):
        enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'enemy']
        for enemy in enemy_sprites:
            enemy.enemy_update(player)
    
            
    def custom_draw(self,player):  
        
        # Getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        # Getting the floor offset
        fl_offset_pos = self.fl_rect.topleft - self.offset #(= self.offset makes it invert)
        self.display_surface.blit(self.fl_surf,fl_offset_pos)
        
        
        # for sprite in self.sprites():
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)




























# for row_index,row in enumerate(WORLD_MAP):
				# for col_index, col in enumerate(row):
					# x = col_index * TILESIZE
					# y = row_index * TILESIZE

				# if col == 'x':
					# Tile((x,y),[self.visible_sprites,self.obstacle_sprites])
				# if col == 'p':
					# self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites)