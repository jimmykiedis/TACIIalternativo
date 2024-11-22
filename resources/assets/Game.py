import pygame
from pygame.locals import *
from .Settings import *
from .SpritesCutter import *
from .Player import *
from .World import *
from .Timer import *

class NaughtCats:

    def play(self):
        settings.setup()
        self.initialScreen()

    def startGame():
        player = Player(100, HEIGHT - 115)
        timer = Timer(15, 30, (20, 20), (255, 255, 255))  # Timer de 60 segundos

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

    def initialScreen(self):
        # Carregar imagem de fundo
        background_image = pygame.image.load("resources/image/grass.png")  # Substitua pelo caminho da sua imagem
        background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

        # Fonte personalizada ou padrão
        try:
            button_font = pygame.font.Font("resources/assets/font/PressStart2P-Regular.ttf", 20)  # Fonte pixelada
            title_font = pygame.font.Font("resources/assets/font/PressStart2P-Regular.ttf", 40)
        except FileNotFoundError:
            button_font = pygame.font.Font(None, 40)  # Fonte padrão do sistema
            title_font = pygame.font.Font(None, 60)

        # Botões com maior largura e espaçamento
        BUTTON_WIDTH = 300
        BUTTON_HEIGHT = 50
        BUTTON_SPACING = 60
        BUTTON_RADIUS = 20
        button_y_start = 350

        # Estados do jogo
        STATE_MAIN_MENU = "main_menu"
        STATE_SINGLE_PLAYER_MENU = "single_player_menu"
        current_state = STATE_MAIN_MENU

        main_menu_buttons = {
            "Single Player": pygame.Rect(WIDTH / 2 - BUTTON_WIDTH / 2, button_y_start, BUTTON_WIDTH, BUTTON_HEIGHT),
            "Multiplayer": pygame.Rect(WIDTH / 2 - BUTTON_WIDTH / 2, button_y_start + BUTTON_HEIGHT + BUTTON_SPACING, BUTTON_WIDTH, BUTTON_HEIGHT),
            "Editor": pygame.Rect(WIDTH / 2 - BUTTON_WIDTH / 2, button_y_start + 2 * (BUTTON_HEIGHT + BUTTON_SPACING), BUTTON_WIDTH, BUTTON_HEIGHT),
            "Quit": pygame.Rect(WIDTH / 2 - BUTTON_WIDTH / 2, button_y_start + 3 * (BUTTON_HEIGHT + BUTTON_SPACING), BUTTON_WIDTH, BUTTON_HEIGHT),
        }

        # Botões do menu Single Player
        single_player_buttons = {
            "Novo Jogo": pygame.Rect(WIDTH / 2 - BUTTON_WIDTH / 2, HEIGHT / 2 - BUTTON_HEIGHT - BUTTON_SPACING, BUTTON_WIDTH, BUTTON_HEIGHT),
            "Continuar": pygame.Rect(WIDTH / 2 - BUTTON_WIDTH / 2, HEIGHT / 2 + BUTTON_SPACING, BUTTON_WIDTH, BUTTON_HEIGHT),
            "<<": pygame.Rect(20, 20, 50, 30)  # Botão "<<" no canto superior esquerdo
        }

        # Função para desenhar retângulos com bordas arredondadas
        def draw_rounded_rect(surface, color, rect, radius, border_color=None, border_width=0):
            pygame.draw.rect(surface, color, rect, border_radius=radius)
            if border_color and border_width > 0:
                pygame.draw.rect(surface, border_color, rect, border_width, border_radius=radius)

        # Função para exibir texto centralizado
        def draw_text(text, font, color, surface, x, y):
            text_obj = font.render(text, True, color)
            text_rect = text_obj.get_rect(center=(x, y))
            surface.blit(text_obj, text_rect)

        # Loop principal
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Clique esquerdo
                        mouse_pos = pygame.mouse.get_pos()
                        if current_state == STATE_MAIN_MENU:
                            if main_menu_buttons["Single Player"].collidepoint(mouse_pos):
                                current_state = STATE_SINGLE_PLAYER_MENU
                            elif main_menu_buttons["Multiplayer"].collidepoint(mouse_pos):
                                print("Iniciar Multiplayer")
                            elif main_menu_buttons["Editor"].collidepoint(mouse_pos):
                                print("Abrir Editor")
                            elif main_menu_buttons["Quit"].collidepoint(mouse_pos):
                                running = False
                        elif current_state == STATE_SINGLE_PLAYER_MENU:
                            if single_player_buttons["Novo Jogo"].collidepoint(mouse_pos):
                                NaughtCats.startGame()
                                # Adicione a lógica para iniciar um novo jogo
                            elif single_player_buttons["Continuar"].collidepoint(mouse_pos):
                                print("Continuar o jogo")
                                # Adicione a lógica para continuar um jogo salvo
                            elif single_player_buttons["<<"].collidepoint(mouse_pos):
                                current_state = STATE_MAIN_MENU

            # Desenhar o fundo
            settings.screen.blit(background_image, (0, 0))
            
            if current_state == STATE_MAIN_MENU:
                # Mensagem de "Bem Vindo"
                draw_text("Bem-vindo ao Naught Cats", title_font, WHITE, settings.screen, WIDTH // 2, 150)

                # Desenhar botões do menu principal
                for text, rect in main_menu_buttons.items():
                    draw_rounded_rect(settings.screen, WHITE, rect, BUTTON_RADIUS, BLACK, 2)  # Botão com borda preta
                    draw_text(text, button_font, BLACK, settings.screen, rect.centerx, rect.centery)

            elif current_state == STATE_SINGLE_PLAYER_MENU:
                # Mensagem "Single Player"
                draw_text("Single Player", title_font, WHITE, settings.screen, WIDTH // 2, 150)

                # Desenhar botões do menu Single Player
                for text, rect in single_player_buttons.items():
                    draw_rounded_rect(settings.screen, WHITE, rect, BUTTON_RADIUS, BLACK, 2)
                    draw_text(text, button_font, BLACK, settings.screen, rect.centerx, rect.centery)

            # Atualizar a tela
            pygame.display.flip()
    
    pygame.quit()