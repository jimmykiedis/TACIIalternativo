import pygame
from .Settings import *
from .World import *

TILE_SIZE = 50

class Star(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		star_img = pygame.image.load('resources/image/estrela.png')
		self.image = pygame.transform.scale(star_img, (20, 20))  # Atribuindo para self.image
		self.rect = self.image.get_rect()  # Use self.image aqui
		self.rect.x = x
		self.rect.y = y
		self.move_direction = 1
		self.move_counter = 0
	
	def update(self):		#faz as estrelas andarem de um lado pro outro
		self.rect.x += self.move_direction
		self.move_counter += 1 
		if abs(self.move_counter) > 50:
			self.move_direction *= -1
			self.move_counter *= -1
			

class Trap(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		trap_img = pygame.image.load('resources/image/trap.png')
		self.image = pygame.transform.scale(trap_img, (55, 60))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
        
class Porta(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('resources/image/portaFechada.png')
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
	
	def update(self, POINTS):
		if POINTS>= 12:
			self.image = pygame.image.load('resources/image/portaAberta.png')

class Fish(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('resources/image/peixe.png')
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y