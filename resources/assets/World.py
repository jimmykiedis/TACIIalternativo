import pygame
from .Settings import *

TILE_SIZE = 50

class World():
	def __init__(self, data):
		self.tile_list = []

		#load images
		dirt_img = pygame.image.load('resources/image/dirt.png')
		grass_img = pygame.image.load('resources/image/grass.png')

		row_count = 0
		for row in data:
			col_count = 0
			for tile in row:

				#cria a terra
				if tile == 1:
					img = pygame.transform.scale(dirt_img, (TILE_SIZE, TILE_SIZE))
					img_rect = img.get_rect()
					img_rect.x = col_count * TILE_SIZE
					img_rect.y = row_count * TILE_SIZE
					tile = (img, img_rect)
					self.tile_list.append(tile)
				
				#cria a grama
				if tile == 2:
					img = pygame.transform.scale(grass_img, (TILE_SIZE, TILE_SIZE))
					img_rect = img.get_rect()
					img_rect.x = col_count * TILE_SIZE
					img_rect.y = row_count * TILE_SIZE
					tile = (img, img_rect)
					self.tile_list.append(tile)

				#cria os eletrodomésticos; nesse caso a estrela
				if tile == 3:
					star = Edomestic(col_count * TILE_SIZE, row_count * TILE_SIZE + 30)
					img = pygame.transform.scale(dirt_img, (TILE_SIZE, TILE_SIZE))
					starGroup.add(star)

				col_count += 1
			row_count += 1

	def draw(self):
		for tile in self.tile_list:
			settings.screen.blit(tile[0], tile[1])

	def draw_grid(self):
		for line in range(0, 20):
			pygame.draw.line(settings.screen, (255, 255, 255), (0, line * TILE_SIZE), (WIDTH, line * TILE_SIZE))
			pygame.draw.line(settings.screen, (255, 255, 255), (line * TILE_SIZE, 0), (line * TILE_SIZE, HEIGHT))
			
class Edomestic(pygame.sprite.Sprite):
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

class Timer:
    def __init__(self, duration, font_size=36, position=(10, 10), color=(255, 255, 255)):
        """
        Inicializa o timer.
        :param duration: Duração do timer em segundos.
        :param font_size: Tamanho da fonte para exibição do tempo.
        :param position: Posição do texto na tela (x, y).
        :param color: Cor do texto no formato RGB.
        """
        self.duration = duration
        self.remaining_time = duration
        self.font = pygame.font.Font(None, font_size)
        self.position = position
        self.color = color
        self.start_ticks = pygame.time.get_ticks()
        self.running = True

    def update(self):
        """
        Atualiza o tempo restante do timer.
        """
        if self.running:
            elapsed_time = (pygame.time.get_ticks() - self.start_ticks) // 1000
            self.remaining_time = max(0, self.duration - elapsed_time)
            if self.remaining_time <= 0:
                self.running = False

    def draw(self, screen):
        """
        Desenha o timer na tela.
        :param screen: A superfície do Pygame onde o timer será renderizado.
        """
        timer_text = self.font.render(f"Tempo: {self.remaining_time}s", True, self.color)
        screen.blit(timer_text, self.position)

    def reset(self):
        """
        Reinicia o timer para a duração original.
        """
        self.start_ticks = pygame.time.get_ticks()
        self.remaining_time = self.duration
        self.running = True

    def is_finished(self):
        """
        Verifica se o timer chegou a zero.
        :return: True se o tempo acabou, False caso contrário.
        """
        return not self.running
			

world_data = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1], 
[1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 2, 2, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 7, 0, 5, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1], 
[1, 7, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 1], 
[1, 0, 2, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 2, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 1], 
[1, 0, 0, 0, 0, 0, 2, 2, 2, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

starGroup = pygame.sprite.Group()

world = World(world_data)