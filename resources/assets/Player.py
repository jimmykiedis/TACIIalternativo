import pygame
from pygame.locals import *
from .Settings import *
from .World import *
from .Game import *

SCORE_COUTER = 0

class Player():
    def __init__(self, x, y):
        self.reset(x, y)

    def reset(self, x, y):
        # listas com as imagens sprites
        self.images_player_right = []
        self.images_player_left = []
        self.index = 0
        self.counter = 0

        self.load_sprite_images()
        self.image = self.images_player_right[self.index]
        self.player_rect = self.image.get_rect()            #todos os .player_rect devem ser mudados para apenas .rect
        self.player_rect.x = x
        self.player_rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0
        self.in_air = True


    #desenhar o corno do jogador
    def update(self, GAME_STATE, TRAP_KILL, POINTS): 
        self.dx = 0
        self.dy = 0  
        if GAME_STATE == 0:
            self.controls()
            self.walk_animation()
            self.gravity()
            TRAP_KILL, POINTS, GAME_STATE = self.check_colision(TRAP_KILL, POINTS, GAME_STATE)
            self.coordinates()
        if TRAP_KILL == True:
            GAME_STATE = -1
            self.image = settings.dead_image
        settings.screen.blit(self.image, self.player_rect)
        return GAME_STATE, POINTS

    def controls(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.dx -= 5
            self.counter += 1
            self.direction = -1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.dx += 5
            self.counter += 1
            self.direction = 1
        if keys[pygame.K_LEFT] == False and keys[pygame.K_RIGHT] == False:
            self.counter = 0
            self.index = 0
            if self.direction == 1:
                self.image = self.images_player_right[self.index]
            if self.direction == -1:
                self.image = self.images_player_left[self.index]
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            print("Olhando para cima")
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            print("Olhando para baixo")
        if keys[pygame.K_SPACE] and self.jumped == False and self.in_air == False:
            self.vel_y = -15
            self.jumped = True  
        if keys[pygame.K_SPACE] == False:
            self.jumped = False
            
    def load_sprite_images(self):
        for num in range(1, 4):
            img_player_right = pygame.image.load(f'resources/image/walk{num}.png')
            img_player_right = pygame.transform.scale(img_player_right, (64, 64))
            img_player_left = pygame.transform.flip(img_player_right, True, False)
            self.images_player_right.append(img_player_right)
            self.images_player_left.append(img_player_left)

    def gravity(self):
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        self.dy += self.vel_y
            
    def walk_animation(self):
        walk_delay = 5
        if self.counter > walk_delay:
            self.counter = 0	
            self.index += 1
            if self.index >= len(self.images_player_right):
                self.index = 0
            if self.direction == 1:
                self.image = self.images_player_right[self.index]
            if self.direction == -1:
                self.image = self.images_player_left[self.index]

    def coordinates(self):
        #atualiza coordenadas
        self.player_rect.x += self.dx
        self.player_rect.y += self.dy

        if self.player_rect.bottom > HEIGHT:
            self.player_rect.bottom = HEIGHT
            self.dy = 0

    def check_colision(self, TRAP_KILL, POINTS, GAME_STATE):
        #checar se o corno colidiu
        self.in_air = True
        for tile in world.tile_list:
            #clecar se o corno colidiu no x
            if tile[1].colliderect(self.player_rect.x + self.dx, self.player_rect.y, self.width, self.height):
                self.dx = 0
            #checar a colisão na direção Y
            if tile[1].colliderect(self.player_rect.x, self.player_rect.y + self.dy, self.width, self.height):
                #checar se estám a baixo do piso ou seja pulando
                if self.vel_y < 0:
                    self.dy = tile[1].bottom - self.player_rect.top
                    self.vel_y = 0
                #checar se estám a cima do piso ou seja caindo
                elif self.vel_y >= 0:
                    self.dy = tile[1].top - self.player_rect.bottom
                    self.vel_y = 0 
                    self.in_air = False
            
        for trap in trapGroup:
                if self.player_rect.colliderect(trap.rect):
                    TRAP_KILL = True
                    trapGroup.remove(trap)

        for fish in fishGroup:
            if self.player_rect.colliderect(fish.rect):
                POINTS += 3
                fishGroup.remove(fish)

        for door in doorGroup:
            if self.player_rect.colliderect(door.rect) and POINTS>=12:
                GAME_STATE = 1

        for star in starGroup:
            if self.player_rect.colliderect(star.rect):
                POINTS += 1
                starGroup.remove(star)
                    
        return TRAP_KILL, POINTS, GAME_STATE
