import pygame
from pygame.locals import *
from .Settings import *

class Player():
    def __init__(self, x, y) :
        img = pygame.image.load('resources/image/spriteGato1.png')
        self.image = pygame.transform.scale(img, (64,64))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.jumped = False

    def update(self):                               
        
        dx = 0
        dy = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            print("Movendo para a esquerda")
            dx -= 5

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            print("Movendo para a direita")
            dx += 5

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            print("Olhando para cima")

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            print("Olhando para baixo")

        if keys[pygame.K_SPACE] and self.jumped == False:
            print("Pulando")
            self.vel_y =-15
            self.jumped = True
        if keys[pygame.K_SPACE] == False:
            self.jumped = False

        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            print("Correndo")

        if keys[pygame.K_LCTRL] or keys[pygame.K_LCTRL]:
            print("Abaixando")

        #criando a gravidade
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        #checar se o corno colidiu

        #atualizar as cordenadas do corno
        self.rect.x += dx
        self.rect.y += dy

        if self. rect.bottom > settings.HEIGHT:
            self.rect.bottom = settings.HEIGHT
            dy = 0

        #desenhar o corno do jogador
        settings.screen.blit(self.image, self.rect)