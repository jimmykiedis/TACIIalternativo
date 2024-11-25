import pygame
from pygame.locals import *
from .Settings import *
from .Player import *
from .World import *
from .Timer import *

class NaughtCats:

    def play(self):
        settings.setup()    
        NaughtCats.initialScreen()

    def startGame():
        GAME_OVER = False
        TRAP_KILL = False
        cont_game_over = 0
        player = Player(100, HEIGHT - 115)
        timer = Timer(15, 30, (20, 20), (255, 255, 255))  # Timer de 60 segundos

        rodando = True
        while rodando:
            
            #settings.screen.blit(settings.cenarioExterior, (0,0))
            settings.screen.blit(settings.cenarioInterior, (0,0))

            for evento in pygame.event.get():                   #fechando o jogo
                if evento.type == pygame.QUIT:
                    rodando = False
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        rodando = False
            
            world.draw()

            if GAME_OVER == False:
                trapGroup.draw(settings.screen)
                timer.update()
            starGroup.update()
            starGroup.draw(settings.screen)
            GAME_OVER = player.update(GAME_OVER, TRAP_KILL)
            #world.draw_grid()

            if GAME_OVER == True:
                cont_game_over += 1
                if cont_game_over == 120:
                    NaughtCats.gameOverScreen()
                    cont_game_over = 0
                
            
            # desenhar o timer
            timer.draw(settings.screen)

            # Finalizar o jogo quando o tempo acaba
            if timer.is_finished():
                print("O tempo acabou!")
                #rodando = False

            settings.clock.tick(50)
            pygame.display.flip()

    def initialScreen():
        # Estados do jogo
        STATE_MAIN_MENU = "main_menu"
        STATE_SINGLE_PLAYER_MENU = "single_player_menu"
        current_state = STATE_MAIN_MENU

        # Botões com maior largura e espaçamento
        BUTTON_WIDTH = 300
        BUTTON_HEIGHT = 50
        BUTTON_SPACING = 60
        BUTTON_RADIUS = 10
        button_y_start = 350

        main_menu_buttons = {
            "SINGLE PLAYER": pygame.Rect(WIDTH / 2 - BUTTON_WIDTH / 2, button_y_start, BUTTON_WIDTH, BUTTON_HEIGHT),
            "MULTIPLAYER": pygame.Rect(WIDTH / 2 - BUTTON_WIDTH / 2, button_y_start + BUTTON_HEIGHT + BUTTON_SPACING, BUTTON_WIDTH, BUTTON_HEIGHT),
            "EDITOR": pygame.Rect(WIDTH / 2 - BUTTON_WIDTH / 2, button_y_start + 2 * (BUTTON_HEIGHT + BUTTON_SPACING), BUTTON_WIDTH, BUTTON_HEIGHT),
            "FECHAR": pygame.Rect(WIDTH / 2 - BUTTON_WIDTH / 2, button_y_start + 3 * (BUTTON_HEIGHT + BUTTON_SPACING), BUTTON_WIDTH, BUTTON_HEIGHT),
        }

        # Botões do menu Single Player
        single_player_buttons = {
            "NOVO JOGO": pygame.Rect(WIDTH / 2 - BUTTON_WIDTH / 2, HEIGHT / 2 - BUTTON_HEIGHT - BUTTON_SPACING, BUTTON_WIDTH, BUTTON_HEIGHT),
            "CONTINUAR": pygame.Rect(WIDTH / 2 - BUTTON_WIDTH / 2, HEIGHT / 2 + BUTTON_SPACING, BUTTON_WIDTH, BUTTON_HEIGHT),
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
                            if main_menu_buttons["SINGLE PLAYER"].collidepoint(mouse_pos):
                                current_state = STATE_SINGLE_PLAYER_MENU
                            elif main_menu_buttons["MULTIPLAYER"].collidepoint(mouse_pos):
                                print("Iniciar Multiplayer")
                            elif main_menu_buttons["EDITOR"].collidepoint(mouse_pos):
                                print("Abrir Editor")
                            elif main_menu_buttons["FECHAR"].collidepoint(mouse_pos):
                                running = False
                        elif current_state == STATE_SINGLE_PLAYER_MENU:
                            if single_player_buttons["NOVO JOGO"].collidepoint(mouse_pos):
                                NaughtCats.startGame()
                                # Adicione a lógica para iniciar um novo jogo
                            elif single_player_buttons["CONTINUAR"].collidepoint(mouse_pos):
                                print("Continuar o jogo")
                                # Adicione a lógica para continuar um jogo salvo
                            elif single_player_buttons["<<"].collidepoint(mouse_pos):
                                current_state = STATE_MAIN_MENU

            # Desenhar o fundo
            settings.screen.blit(settings.background_image, (0, 0))

            if current_state == STATE_MAIN_MENU:
                # Desenhar botões do menu principal
                for text, rect in main_menu_buttons.items():
                    draw_rounded_rect(settings.screen, DARK_BROWN, rect, BUTTON_RADIUS, LIGHT_BROWN, 4)
                    draw_text(text, settings.button_font, LIGHT_BROWN, settings.screen, rect.centerx, rect.centery)

            elif current_state == STATE_SINGLE_PLAYER_MENU:
                # Desenhar botões do menu Single Player
                for text, rect in single_player_buttons.items():
                    draw_rounded_rect(settings.screen, DARK_BROWN, rect, BUTTON_RADIUS, LIGHT_BROWN, 4)
                    draw_text(text, settings.button_font, LIGHT_BROWN, settings.screen, rect.centerx, rect.centery)

            # Atualizar a tela
            pygame.display.flip()
    
    def gameOverScreen():
        BUTTON_WIDTH = 300
        BUTTON_HEIGHT = 50
        BUTTON_SPACING = 60
        BUTTON_RADIUS = 10

        STATE_GAME_OVER = "game_over"
        current_state = STATE_GAME_OVER

        game_over_buttons = {
            "REINICIAR": pygame.Rect(WIDTH / 2 - BUTTON_WIDTH / 2, HEIGHT / 2 - BUTTON_HEIGHT - BUTTON_SPACING, BUTTON_WIDTH, BUTTON_HEIGHT),
            "FECHAR": pygame.Rect(WIDTH / 2 - BUTTON_WIDTH / 2, HEIGHT / 2 + BUTTON_SPACING, BUTTON_WIDTH, BUTTON_HEIGHT)
        }

        # Função para desenhar retângulos com bordas arredondadas
        def draw_rounded_rect(surface, color, rect, radius, border_color=None, border_width=0):
            pygame.draw.rect(surface, color, rect, border_radius=radius)
            if border_color and border_width > 0:
                pygame.draw.rect(surface, border_color, rect, border_width, border_radius=radius)
        
        def draw_text(text, font, color, surface, x, y):
            text_obj = font.render(text, True, color)
            text_rect = text_obj.get_rect(center=(x, y))
            surface.blit(text_obj, text_rect)

        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Clique esquerdo
                        mouse_pos = pygame.mouse.get_pos()
                        if current_state == STATE_GAME_OVER:
                            if game_over_buttons["REINICIAR"].collidepoint(mouse_pos):
                                NaughtCats.startGame()
                            elif game_over_buttons["FECHAR"].collidepoint(mouse_pos):
                                pygame.quit()

            settings.screen.blit(settings.background_image, (0, 0))
            
            if current_state == STATE_GAME_OVER:
                    # Desenhar botões da tela game over
                    for text, rect in game_over_buttons.items():
                        draw_rounded_rect(settings.screen, DARK_BROWN, rect, BUTTON_RADIUS, LIGHT_BROWN, 4)
                        draw_text(text, settings.button_font, LIGHT_BROWN, settings.screen, rect.centerx, rect.centery)
        
            # Atualizar a tela
            pygame.display.flip()

    
    pygame.quit()