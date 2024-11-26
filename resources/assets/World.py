import pygame
import pickle
from .Settings import *
from .Objects import *

TILE_SIZE = 50

class World():
	def __init__(self, data):
		self.tile_list = []

		#load images
		piso_img = pygame.image.load('resources/image/piso.png')
		bloco_img = pygame.image.load('resources/image/bloco.png')
		madeira_img = pygame.image.load('resources/image/madeira.png')

		row_count = 0
		for row in data:
			col_count = 0
			for tile in row:

				#cria a terra
				if tile == 1:
					img = pygame.transform.scale(piso_img, (TILE_SIZE, TILE_SIZE))
					img_rect = img.get_rect()
					img_rect.x = col_count * TILE_SIZE
					img_rect.y = row_count * TILE_SIZE
					tile = (img, img_rect)
					self.tile_list.append(tile)
				
				#cria a grama
				if tile == 2:
					img = pygame.transform.scale(bloco_img, (TILE_SIZE, TILE_SIZE))
					img_rect = img.get_rect()
					img_rect.x = col_count * TILE_SIZE
					img_rect.y = row_count * TILE_SIZE
					tile = (img, img_rect)
					self.tile_list.append(tile)

				#cria os eletrodomésticos; nesse caso a estrela
				if tile == 3:
					stars = Star(col_count * TILE_SIZE, row_count * TILE_SIZE + 30)
					starGroup.add(stars)
				
				if tile == 4:
					traps = Trap(col_count * TILE_SIZE, row_count * TILE_SIZE)
					trapGroup.add(traps)
				
				if tile == 5:
					door = Porta(col_count * TILE_SIZE, row_count * TILE_SIZE - 30)
					doorGroup.add(door)
				
				if tile == 6:
					fish = Fish(col_count * TILE_SIZE, row_count * TILE_SIZE)
					fishGroup.add(fish)
				
				if tile == 7:
					img = pygame.transform.scale(madeira_img, (TILE_SIZE, TILE_SIZE))
					img_rect = img.get_rect()
					img_rect.x = col_count * TILE_SIZE
					img_rect.y = row_count * TILE_SIZE
					tile = (img, img_rect)
					self.tile_list.append(tile)
				col_count += 1
			row_count += 1

	def draw(self):
		for tile in self.tile_list:
			settings.screen.blit(tile[0], tile[1])

	def draw_grid(self):
		for line in range(0, 24):
			pygame.draw.line(settings.screen, (255, 255, 255), (0, line * TILE_SIZE), (WIDTH, line * TILE_SIZE))
			pygame.draw.line(settings.screen, (255, 255, 255), (line * TILE_SIZE, 0), (line * TILE_SIZE, HEIGHT))
			

world_data = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
[7, 5, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 7],
[7, 2, 2, 6, 0, 0, 0, 0, 2, 2, 2, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 2, 2, 7],
[7, 7, 7, 2, 0, 0, 0, 7, 7, 7, 7, 0, 2, 2, 2, 0, 0, 0, 0, 0, 2, 7, 7, 7],
[7, 0, 7, 7, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 7, 7, 7, 7],
[7, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 2, 7, 7, 7, 7, 7],
[7, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 7],
[7, 0, 0, 4, 0, 0, 0, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 7],
[7, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 7],
[7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 7, 7, 7, 7],
[7, 0, 0, 0, 0, 2, 0, 0, 0, 2, 2, 2, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 7],
[7, 0, 3, 0, 0, 0, 0, 0, 7, 7, 7, 7, 0, 0, 7, 7, 7, 7, 0, 0, 0, 0, 0, 7],
[7, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 7],
[7, 7, 7, 0, 0, 3, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 7],
[7, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 7],
[7, 0, 0, 0, 0, 7, 7, 0, 0, 2, 2, 4, 0, 0, 7, 7, 7, 4, 4, 2, 7, 7, 7, 7],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
#with open('level1.pkl', 'wb') as f:
#    pickle.dump(world_data, f)
trapGroup = pygame.sprite.Group()
starGroup = pygame.sprite.Group()
fishGroup = pygame.sprite.Group()
doorGroup = pygame.sprite.Group()
#pickle_in = open('resouces/assets/level/level1.pkl', 'rb')
#world_data = pickle.load(pickle_in)
world = World(world_data)