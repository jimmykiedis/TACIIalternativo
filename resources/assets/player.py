import pygame
from pygame.locals import *
from .Settings import *

class Player():
    def __init__(self, x, y):
        img_player = pygame.image.load('resources/image/spriteGato1.png')
        self.img_player = pygame.transform.scale(img_player, (64,64))
        self.player_rect = self.img_player.get_rect()
        self.player_rect.x = x
        self.player_rect.y = y
        self.vel_y = 0

    def update(self):                           #desenhar o corno do jogador
        dx = 0
        dy = 0
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx -= 5
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx += 5
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            print("Olhando para cima")
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            print("Olhando para baixo")
        if keys[pygame.K_SPACE]:
            self.vel_y = -15
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            print("Correndo")
        if keys[pygame.K_LCTRL] or keys[pygame.K_LCTRL]:
            print("Abaixando")

                                                #gravidade
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        self.player_rect.x += dx
        self.player_rect.y += dy

        if self.player_rect.bottom > HEIGHT:
            self.player_rect.bottom = HEIGHT
            dy = 0

        settings.screen.blit(self.img_player, self.player_rect)

    def controls(self):
        pass

    
