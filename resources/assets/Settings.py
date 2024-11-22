import pygame

WIDTH = 1000
HEIGHT = 1000

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Settings:
    def setup(self):
        pygame.init()

        # Inicialização
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Naught Cats')
        self.clock = pygame.time.Clock()

        # Ocultando o cursor
        #pygame.mouse.set_visible(False)

        # Configurando fonte
        self.font = pygame.font.Font(None, 40)

        self.load_images()

    def load_images(self):
        self.cenarioInterior = pygame.image.load ('resources/image/projetoInterior.png')
        self.cenarioExterior = pygame.image.load ('resources/image/projetoExterior.png')
        background_image = pygame.image.load("resources/image/grass.png")  # Substitua pelo caminho da sua imagem
        self.background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
        sheetJogador = pygame.image.load('resources/image/projetoPlayer.png')
        #self.jogadorSprite = cortarSprite(sheetJogador)
        sheetPlataformas = pygame.image.load('resources/image/projetoPlataformas.png')
        #self.plataformas = cortarSprite(sheetPlataformas)
        sheetObjetos = pygame.image.load('resources/image/projetoObjetos.png')
        #self.Objetos = cortarSprite(sheetObjetos)


settings = Settings()