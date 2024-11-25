from .Settings import *

class Score:
    def __init__(self, points, position=(1100, 10), color=(255, 255, 255)):
        self.font = settings.button_font
        self.points = points
        self.position = position
        self.color = color
    
    def update(self, points):
        self.points = points

    def draw(self, screen):
        score_text = self.font.render(f"Score: {self.points}", True, self.color)
        screen.blit(score_text, self.position)