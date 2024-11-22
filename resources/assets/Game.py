import pygame
from pygame.locals import *
from .Settings import *
from .SpritesCutter import *
from .Player import *
from .World import *

class NaughtCats:

    def play(self):
        settings.setup()

        player = Player(100, HEIGHT - 115)
        timer = Timer(10)  # Timer de 60 segundos

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
            starGroup.draw(settings.screen)
            starGroup.update()
            player.update()
            #world.draw_grid()
            
            # Atualizar e desenhar o timer
            timer.update()
            timer.draw(settings.screen)

            # Finalizar o jogo quando o tempo acaba
            if timer.is_finished():
                print("O tempo acabou!")
                #rodando = False

            settings.clock.tick(50)
            pygame.display.flip()

    pygame.quit()