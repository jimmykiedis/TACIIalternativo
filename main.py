import pygame
from pygame.locals import *
from resources.assets import player, sprites

pygame.init()

larguraTela = 1000
alturaTela = 1000

tela = pygame.display.set_mode((larguraTela, alturaTela))
pygame.display.set_caption('Naughty Cat 2.2')
clock = pygame.time.Clock()

cenarioInterior = pygame.image.load ('resources/image/projetoInterior.png')
cenarioExterior = pygame.image.load ('resources/image/projetoExterior.png')
sheetJogador = pygame.image.load('resources/image/projetoPlayer.png')
sheetPlataformas = pygame.image.load('resources/image/projetoPlataformas.png')
sheetObjetos = pygame.image.load('resources/image/projetoObjetos.png')

jogadorSprite = sprites.cortarSprite(sheetJogador)
plataformas = sprites.cortarSprite(sheetPlataformas)
Obejtos = sprites.cortarSprite(sheetObjetos)

player = player(100, alturaTela - 130)

rodando = True
while rodando:

    tela.blit(cenarioExterior, (0,0))
    tela.blit(cenarioInterior, (0,0))
    
    player.update()

    for evento in pygame.event.get():                   #fechando o jogo
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                rodando = False
    

    player.teclas()
    clock.tick(50)
    pygame.display.flip()



pygame.quit()