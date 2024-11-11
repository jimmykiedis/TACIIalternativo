import pygame

largura_sprite = 64
altura_sprite = 64
colunas = 10
linhas = 10

def cortarSprite(spritesheet):
    """
    Função para cortar uma spritesheet em múltiplos sprites organizados em uma matriz 2D.

    :param spritesheet: Imagem da spritesheet carregada.
    :param largura_sprite: Largura de cada sprite (em pixels).
    :param altura_sprite: Altura de cada sprite (em pixels).
    :param colunas: Número de colunas de sprites na spritesheet.
    :param linhas: Número de linhas de sprites na spritesheet.
    :return: Matriz (lista de listas) com as imagens de cada sprite.
    """
    sprites = []
    for linha in range(linhas):
        linha_sprites = []  # Criar uma lista para armazenar os sprites de cada linha
        for coluna in range(colunas):
            # Calculando a posição do sprite na spritesheet
            x = coluna * largura_sprite
            y = linha * altura_sprite

            # Cortando a imagem da spritesheet
            sprite = spritesheet.subsurface(pygame.Rect(x, y, largura_sprite, altura_sprite))
            linha_sprites.append(sprite)
        sprites.append(linha_sprites)  # Adiciona a linha de sprites na matriz

    return sprites