import pygame

WIDTH = 1200
HEIGHT = 950


# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BROWN = (206, 142, 143)
DARK_BROWN = (147, 79, 56)

TRAP_KILL = False

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
        self.load_font()

    def load_images(self):
        cenarioInterior = pygame.image.load ('resources/image/projetoInterior.png')
        self.cenarioInterior = pygame.transform.scale(cenarioInterior, (WIDTH, HEIGHT))
        self.cenarioExterior = pygame.image.load ('resources/image/projetoExterior.png')
        background_image = pygame.image.load('resources/image/imageAbertura.png')
        self.background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
        cat_dead = pygame.image.load('resources/image/catDead.png')
        self.dead_image = pygame.transform.scale(cat_dead, (80, 80))
        sheetJogador = pygame.image.load('resources/image/projetoPlayer.png')
        #self.jogadorSprite = cortarSprite(sheetJogador)
        sheetPlataformas = pygame.image.load('resources/image/projetoPlataformas.png')
        #self.plataformas = cortarSprite(sheetPlataformas)
        sheetObjetos = pygame.image.load('resources/image/projetoObjetos.png')
        #self.Objetos = cortarSprite(sheetObjetos)

    def load_font(self):
                # Fonte personalizada ou padrão
        try:
            self.button_font = pygame.font.Font("resources/assets/font/PressStart2P-Regular.ttf", 20)  # Fonte pixelada
            self.title_font = pygame.font.Font("resources/assets/font/PressStart2P-Regular.ttf", 40)
        except FileNotFoundError:
            self.button_font = pygame.font.Font(None, 40)  # Fonte padrão do sistema
            self.title_font = pygame.font.Font(None, 60)

class ImageButton:
    def __init__(self, image_path, x, y):
        self.image = pygame.image.load(image_path).convert_alpha()  # Carregar a imagem com transparência
        self.rect = self.image.get_rect(topleft=(x, y))  # Definir posição inicial do botão

    def draw(self, surface):
        surface.blit(self.image, self.rect)  # Desenhar a imagem na tela

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)  # Verificar se o botão foi clicado

settings = Settings()