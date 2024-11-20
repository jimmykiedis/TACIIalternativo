import pygame
from .resources.assets.Settings import *
from pygame.locals import *
from resources.assets import player, Sprites, World

cenarioInterior = pygame.image.load ('resources/image/projetoInterior.png')
cenarioExterior = pygame.image.load ('resources/image/projetoExterior.png')
sheetJogador = pygame.image.load('resources/image/projetoPlayer.png')
sheetPlataformas = pygame.image.load('resources/image/projetoPlataformas.png')
sheetObjetos = pygame.image.load('resources/image/projetoObjetos.png')

jogadorSprite = Sprites.cortarSprite(sheetJogador)
plataformas = Sprites.cortarSprite(sheetPlataformas)
Obejtos = Sprites.cortarSprite(sheetObjetos)

rodando = True
while rodando:

    Settings.screen.blit(cenarioExterior, (0,0))
    Settings.screen.blit(cenarioInterior, (0,0))
    
    player.update()
    World.draw()

    for evento in pygame.event.get():                   #fechando o jogo
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                rodando = False
    

    player.teclas()
    pygame.display.flip()



pygame.quit()