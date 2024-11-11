import pygame
from pygame.locals import *
from resources.assets import controles

pygame.init()

larguraTela = 1000
alturaTela = 640

tela = pygame.display.set_mode((larguraTela, alturaTela))
pygame.display.set_caption('Naughty Cat 2.2')
clock = pygame.time.Clock()

cenarioInterior = pygame.image.load ('resources/image/projetoInterior.png')
cenarioExterior = pygame.image.load ('resources/image/projetoExterior.png')
jogador = pygame.image.load('resources/image/skinPlayer1.png')

cenarioInterior

rodando = True
while rodando:

    tela.blit(cenarioExterior, (0,0))
    tela.blit(cenarioInterior, (0,0))
    tela.blit(jogador, (100,0))

    for evento in pygame.event.get():                   #fechando o jogo
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                rodando = False
    
    controles.teclas()
    clock.tick(50)
    pygame.display.flip()



pygame.quit()