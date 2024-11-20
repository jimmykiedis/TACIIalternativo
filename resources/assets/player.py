import pygame
from pygame.locals import *

class Player():
    def __init__(self, x, y) :
        img = pygame.image.load('resources/image/spriteGato1.png')
        self.image = pygame.transform.scale(img, (64,64))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):                               #desenhar o corno do jogador
        global tela

def teclas():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        print("Movendo para a esquerda")
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        print("Movendo para a direita")
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        print("Olhando para cima")
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        print("Olhando para baixo")
    if keys[pygame.K_SPACE]:
        print("Pulando")
    if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
        print("Correndo")
    if keys[pygame.K_LCTRL] or keys[pygame.K_LCTRL]:
        print("Abaixando")