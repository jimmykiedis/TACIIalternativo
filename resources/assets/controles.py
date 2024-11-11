import pygame
from pygame.locals import *

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