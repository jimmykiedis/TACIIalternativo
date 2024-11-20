import pygame
from resources.assets.Settings import *
from pygame.locals import *
from resources.assets.Player import *
from resources.assets.World import *

fps = 60

rodando = True
while rodando:
    world = World()
    world.mapa()
    
    Player.update()
    world.draw()

    for evento in pygame.event.get():                   #fechando o jogo
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                rodando = False
    
    settings.clock.tick(50)
    pygame.display.flip()



pygame.quit()