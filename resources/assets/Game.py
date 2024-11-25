import pygame
import pickle
import csv
from pygame.locals import *
from .Settings import *
from .Player import *
from .World import *
from .Timer import *
from .Score import *
from os import path

class NaughtCats:

    def play(self):
        settings.setup()    
        self.initialScreen()

    def startGame(self):
        # GAME_STATE == 0, NORMAL
        # GAME_STATE == -1, GAME OVER
        # GAME_STATE == 1, NEXT LEVEL
        GAME_STATE = 0
        TRAP_KILL = False
        POINTS = 0
        cont_game_state = 0
        self.player = Player(100, HEIGHT - 115)
        if self.pontos != 0:
            self.timer = Timer(self.tempo, (20, 20), (255, 255, 255))
            POINTS = self.pontos
            self.score = Score(POINTS, (1000, 20), (255, 255, 255))
        else:
            self.timer = Timer(40, (20, 20), (255, 255, 255))
            self.score = Score(POINTS, (1000, 20), (255, 255, 255))


        run = True
        while run:
            
            #settings.screen.blit(settings.cenarioExterior, (0,0))
            settings.screen.blit(settings.cenarioInterior, (0,0))

            for evento in pygame.event.get():                   #fechando o jogo
                if evento.type == pygame.QUIT:
                    run = False
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        run = False
                    if evento.key == pygame.K_p:
                        self.pauseScreen()
            
            world.draw()

            if GAME_STATE == 0:
                self.tempo = self.timer.update()
                self.score.update(POINTS)
            self.pontos = POINTS

            trapGroup.draw(settings.screen)
            fishGroup.draw(settings.screen)
            doorGroup.draw(settings.screen)
            starGroup.update()
            doorGroup.update(POINTS)
            starGroup.draw(settings.screen)
            GAME_STATE, POINTS = self.player.update(GAME_STATE, TRAP_KILL, POINTS)
            world.draw_grid()
            

            if GAME_STATE == -1:
                cont_game_state += 1
                if cont_game_state == 120:
                    self.gameOverScreen()
            
            if GAME_STATE == 1:
                cont_game_state += 1
                if cont_game_state == 120:
                    self.winnerScreen()
                
            
            # desenhar o timer
            self.timer.draw(settings.screen)
            self.score.draw(settings.screen)

            # Finalizar o jogo quando o tempo acaba
            if self.timer.is_finished():
                GAME_STATE = -1
            settings.clock.tick(50)
            pygame.display.flip()

    def initialScreen(self):
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
                                self.startGame()
                                # Adicione a lógica para iniciar um novo jogo
                            elif single_player_buttons["CONTINUAR"].collidepoint(mouse_pos):
                                self.loadGame()
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
    
    def gameOverScreen(self):
        BUTTON_WIDTH = 300
        BUTTON_HEIGHT = 50
        BUTTON_RADIUS = 10

        STATE_GAME_OVER = "game_over"
        current_state = STATE_GAME_OVER

        game_over_buttons = {
        "REINICIAR": pygame.Rect(WIDTH / 4 - BUTTON_WIDTH / 2, HEIGHT / 2 - BUTTON_HEIGHT / 2, BUTTON_WIDTH, BUTTON_HEIGHT),
        "FECHAR": pygame.Rect(3 * WIDTH / 4 - BUTTON_WIDTH / 2, HEIGHT / 2 - BUTTON_HEIGHT / 2, BUTTON_WIDTH, BUTTON_HEIGHT)
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
                                self.startGame()
                            elif game_over_buttons["FECHAR"].collidepoint(mouse_pos):
                                pygame.quit()

            settings.screen.blit(settings.background_image, (0, 0))

            # Add a square around the "GAME OVER!" message
            text_rect = settings.title_font.render('GAME OVER!', True, DARK_BROWN).get_rect(center=(WIDTH / 2, HEIGHT / 2 - BUTTON_HEIGHT * 2))
            pygame.draw.rect(settings.screen, LIGHT_BROWN, text_rect.inflate(20, 10), border_radius=10)
            draw_text('GAME OVER!', settings.title_font, DARK_BROWN, settings.screen, WIDTH / 2, HEIGHT / 2 - BUTTON_HEIGHT * 2)
            
            if current_state == STATE_GAME_OVER:
                    # Desenhar botões da tela game over
                    for text, rect in game_over_buttons.items():
                        draw_rounded_rect(settings.screen, DARK_BROWN, rect, BUTTON_RADIUS, LIGHT_BROWN, 4)
                        draw_text(text, settings.button_font, LIGHT_BROWN, settings.screen, rect.centerx, rect.centery)
        
            # Atualizar a tela
            pygame.display.flip()
    
    def winnerScreen(self):
        BUTTON_WIDTH = 300
        BUTTON_HEIGHT = 50
        BUTTON_SPACING = 60
        BUTTON_RADIUS = 10

        STATE_WINER = "winner"
        current_state = STATE_WINER

        winner_buttons = {
            "PROXIMO NIVEL": pygame.Rect(WIDTH / 4 - BUTTON_WIDTH / 2, HEIGHT / 2 - BUTTON_HEIGHT / 2, BUTTON_WIDTH, BUTTON_HEIGHT),
            "FECHAR": pygame.Rect(3 * WIDTH / 4 - BUTTON_WIDTH / 2, HEIGHT / 2 - BUTTON_HEIGHT / 2, BUTTON_WIDTH, BUTTON_HEIGHT)
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
                        if current_state == STATE_WINER:
                            if winner_buttons["PROXIMO NIVEL"].collidepoint(mouse_pos):
                                self.startGame()
                            elif winner_buttons["FECHAR"].collidepoint(mouse_pos):
                                pygame.quit()

            settings.screen.blit(settings.background_image, (0, 0))

            text_rect = settings.title_font.render('VOCÊ VENCEU, PARABÉNS!', True, DARK_BROWN).get_rect(center=(WIDTH / 2, HEIGHT / 2 - BUTTON_HEIGHT * 2))
            pygame.draw.rect(settings.screen, LIGHT_BROWN, text_rect.inflate(20, 10), border_radius=10)
            draw_text('VOCÊ VENCEU, PARABÉNS!', settings.title_font, DARK_BROWN, settings.screen, WIDTH / 2, HEIGHT / 2 - BUTTON_HEIGHT * 2)
            
            if current_state == STATE_WINER:
                    # Desenhar botões da tela game over
                    for text, rect in winner_buttons.items():
                        draw_rounded_rect(settings.screen, DARK_BROWN, rect, BUTTON_RADIUS, LIGHT_BROWN, 4)
                        draw_text(text, settings.button_font, LIGHT_BROWN, settings.screen, rect.centerx, rect.centery)
        
            # Atualizar a tela
            pygame.display.flip()

    def pauseScreen(self):
        BUTTON_WIDTH = 300
        BUTTON_HEIGHT = 50
        BUTTON_RADIUS = 10

        STATE_PAUSE = "pause"
        current_state = STATE_PAUSE

        pause_buttons = {
            "CONTINUAR": pygame.Rect(WIDTH / 2 - BUTTON_WIDTH / 2, 20 + HEIGHT / 2 - BUTTON_HEIGHT * 1.5, BUTTON_WIDTH, BUTTON_HEIGHT),
            "SALVAR JOGO": pygame.Rect(WIDTH / 2 - BUTTON_WIDTH / 2, 20 + HEIGHT / 2, BUTTON_WIDTH, BUTTON_HEIGHT),
            "FECHAR JOGO": pygame.Rect(WIDTH / 2 - BUTTON_WIDTH / 2, 20 + HEIGHT / 2 + BUTTON_HEIGHT * 1.5, BUTTON_WIDTH, BUTTON_HEIGHT)
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
                        if current_state == STATE_PAUSE:
                            if pause_buttons["CONTINUAR"].collidepoint(mouse_pos):
                                running = False  # Sai da tela de pause
                            elif pause_buttons["SALVAR JOGO"].collidepoint(mouse_pos):
                                self.saveGame()
                            elif pause_buttons["FECHAR JOGO"].collidepoint(mouse_pos):
                                pygame.quit()

            settings.screen.blit(settings.background_image, (0, 0))

            # Mensagem de pausa
            text_rect = settings.title_font.render('PAUSE', True, DARK_BROWN).get_rect(center=(WIDTH / 2, HEIGHT / 2 - BUTTON_HEIGHT * 2))
            pygame.draw.rect(settings.screen, LIGHT_BROWN, text_rect.inflate(20, 10), border_radius=10)
            draw_text('PAUSE', settings.title_font, DARK_BROWN, settings.screen, WIDTH / 2, HEIGHT / 2 - BUTTON_HEIGHT * 2)

            if current_state == STATE_PAUSE:
                # Desenhar botões da tela pause
                for text, rect in pause_buttons.items():
                    draw_rounded_rect(settings.screen, DARK_BROWN, rect, BUTTON_RADIUS, LIGHT_BROWN, 4)
                    draw_text(text, settings.button_font, LIGHT_BROWN, settings.screen, rect.centerx, rect.centery)

            # Atualizar a tela
            pygame.display.flip()

    def saveGame(self):
        # Define o nome do arquivo CSV onde o estado do jogo será salvo
        save_file = "resources/assets/naught_cats_save.csv"

        # Exemplo de dados do jogo que serão salvos
        game_data = {
            "score": self.pontos,  # Pontuação do jogador
            "time_elapsed": self.tempo,  # Tempo decorrido no jogo
        }

        # Criação e escrita do arquivo CSV
        try:
            with open(save_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                
                # Escreve os cabeçalhos (nomes das colunas)
                writer.writerow(game_data.keys())
                
                # Escreve os valores correspondentes
                writer.writerow(game_data.values())

            print("Jogo salvo com sucesso!")
        except Exception as e:
            print(f"Erro ao salvar o jogo: {e}")

    def loadGame(self):
        # Nome do arquivo CSV
        save_file = "resources/assets/naught_cats_save.csv"
        
        try:
            with open(save_file, mode='r') as file:
                reader = csv.DictReader(file)
                game_data = next(reader)  # Lê a primeira linha de dados

                # Converte os valores lidos para os tipos apropriados
                self.pontos = int(game_data["score"])
                self.tempo = int(game_data["time_elapsed"])

                # Inicia o jogo com os dados carregados
                self.startGame()
        except FileNotFoundError:
            print("Nenhum jogo salvo encontrado.")
        except Exception as e:
            print(f"Erro ao carregar o jogo: {e}")

    #function to reset level
    def reset_level(self, level):
        self.player.reset(100, HEIGHT - 130)
        trapGroup.empty()
        starGroup.empty()
        fishGroup.empty()
        doorGroup.empty()

        #load in level data and create world
        if path.exists(f'level{level}_data'):
            pickle_in = open(f'level{level}_data', 'rb')
            world_data = pickle.load(pickle_in)
        world = World(world_data)

        return world

    
    pygame.quit()