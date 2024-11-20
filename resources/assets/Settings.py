import pygame
from .World import *
from .Sprites import *

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

    def load_images(self):
        self.cenarioInterior = pygame.image.load ('resources/image/projetoInterior.png')
        self.cenarioExterior = pygame.image.load ('resources/image/projetoExterior.png')
        sheetJogador = pygame.image.load('resources/image/projetoPlayer.png')
        sheetPlataformas = pygame.image.load('resources/image/projetoPlataformas.png')
        sheetObjetos = pygame.image.load('resources/image/projetoObjetos.png')

        self.jogadorSprite = cortarSprite(sheetJogador)
        self.plataformas = cortarSprite(sheetPlataformas)
        self.Objetos = cortarSprite(sheetObjetos)

settings = Settings()