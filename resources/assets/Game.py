import pygame
from pygame.locals import *
from .Settings import *
from .Sprites import *
from .Player import *
from .World import *

class NaughtCats:

    def play(self):
        settings.setup()

        player = Player(100, HEIGHT - 115)

        rodando = True
        while rodando:
            
            settings.screen.blit(settings.cenarioExterior, (0,0))
            settings.screen.blit(settings.cenarioInterior, (0,0))

            for evento in pygame.event.get():                   #fechando o jogo
                if evento.type == pygame.QUIT:
                    rodando = False
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        rodando = False
            
            world.draw()
            player.update()
            #world.draw_grid()
            
            settings.clock.tick(50)
            pygame.display.flip()

    pygame.quit()