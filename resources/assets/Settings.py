import pygame

WIDTH = 1000
HEIGHT = 1000
    
class Settings:
    def setup(self, debug:bool):
        self.debug = debug
        pygame.init()

        # Inicialização
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.toggle_fullscreen()
        self.clock = pygame.time.Clock()

        # Ocultando o cursor
        pygame.mouse.set_visible(False)

        # Configurando fonte
        self.font = pygame.font.Font(None, 40)

settings = Settings()