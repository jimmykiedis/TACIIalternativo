import pygame
from pygame.locals import *
from .Settings import *
from .World import *
from .Game import *

SCORE_COUTER = 0
sounds = Settings.setup_mixer()

class Player():
    def __init__(self, x, y):
        self.reset(x, y)

    def reset(self, x, y):
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0

        self.load_sprite_images()
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()  # Mudança aqui
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0
        self.in_air = True

    def update(self, GAME_STATE, TRAP_KILL, POINTS): 
        self.dx = 0
        self.dy = 0  
        if GAME_STATE == 0:
            self.controls()
            self.walk_animation()
            self.gravity()
            TRAP_KILL, POINTS, GAME_STATE = self.check_colision(TRAP_KILL, POINTS, GAME_STATE)
            self.coordinates()
        if TRAP_KILL == True:
            GAME_STATE = -1
            self.image = settings.dead_image
        settings.screen.blit(self.image, self.rect)  # Mudança aqui
        return GAME_STATE, POINTS

    def controls(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.dx -= 5
            self.counter += 1
            self.direction = -1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.dx += 5
            self.counter += 1
            self.direction = 1
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) == False and (keys[pygame.K_RIGHT] or keys[pygame.K_d]) == False:
            self.counter = 0
            self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index]
            if self.direction == -1:
                self.image = self.images_left[self.index]
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            print("Olhando para cima")
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            print("Olhando para baixo")
        if keys[pygame.K_SPACE] and self.jumped == False and self.in_air == False:
            self.vel_y = -15
            self.jumped = True  
        if keys[pygame.K_SPACE] == False:
            self.jumped = False

    def load_sprite_images(self):
        for num in range(1, 4):
            img_right = pygame.image.load(f'resources/image/walk{num}.png')
            img_right = pygame.transform.scale(img_right, (64, 64))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)

    def gravity(self):
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        self.dy += self.vel_y

    def walk_animation(self):
        walk_delay = 5
        if self.counter > walk_delay:
            self.counter = 0    
            self.index += 1
            if self.index >= len(self.images_right):
                self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index]
            if self.direction == -1:
                self.image = self.images_left[self.index]

    def coordinates(self):
        self.rect.x += self.dx  # Mudança aqui
        self.rect.y += self.dy  # Mudança aqui

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.dy = 0

    def check_colision(self, TRAP_KILL, POINTS, GAME_STATE):
        self.in_air = True
        for tile in world.tile_list:
            if tile[1].colliderect(self.rect.x + self.dx, self.rect.y, self.width, self.height):
                self.dx = 0
            if tile[1].colliderect(self.rect.x, self.rect.y + self.dy, self.width, self.height):
                if self.vel_y < 0:
                    self.dy = tile[1].bottom - self.rect.top
                    self.vel_y = 0
                elif self.vel_y >= 0:
                    self.dy = tile[1].top - self.rect.bottom
                    self.vel_y = 0 
                    self.in_air = False
            
        for trap in trapGroup:
            if self.rect.colliderect(trap.rect):
                TRAP_KILL = True
                sounds["gameOver"].play()
                trapGroup.remove(trap)

        for fish in fishGroup:
            if self.rect.colliderect(fish.rect):
                POINTS += 3
                sounds["mordida"].play()
                fishGroup.remove(fish)

        for door in doorGroup:
            if self.rect.colliderect(door.rect) and POINTS>=12:
                GAME_STATE = 1

        for star in starGroup:
            if self.rect.colliderect(star.rect):
                POINTS += 1
                sounds["estrela"].play()
                starGroup.remove(star)

        return TRAP_KILL, POINTS, GAME_STATE

