import pygame
from .Settings import *

class Timer:
    def __init__(self, duration, position=(10, 10), color=(255, 255, 255)):
        """
        Inicializa o timer.
        :param duration: Duração do timer em segundos.
        :param font_size: Tamanho da fonte para exibição do tempo.
        :param position: Posição do texto na tela (x, y).
        :param color: Cor do texto no formato RGB.
        """
        self.duration = duration
        self.remaining_time = duration
        self.font = settings.button_font
        self.position = position
        self.color = color
        self.start_ticks = pygame.time.get_ticks()
        self.running = True

    def update(self):
        """
        Atualiza o tempo restante do timer.
        """
        if self.running:
            elapsed_time = (pygame.time.get_ticks() - self.start_ticks) // 1000
            self.remaining_time = max(0, self.duration - elapsed_time)
            if self.remaining_time <= 0:
                self.running = False
        return self.remaining_time

    def draw(self, screen):
        """
        Desenha o timer na tela.
        :param screen: A superfície do Pygame onde o timer será renderizado.
        """
        timer_text = self.font.render(f"Tempo: {self.remaining_time}s", True, self.color)
        screen.blit(timer_text, self.position)

    def reset(self):
        """
        Reinicia o timer para a duração original.
        """
        self.start_ticks = pygame.time.get_ticks()
        self.remaining_time = self.duration
        self.running = True

    def is_finished(self):
        """
        Verifica se o timer chegou a zero.
        :return: True se o tempo acabou, False caso contrário.
        """
        return not self.running