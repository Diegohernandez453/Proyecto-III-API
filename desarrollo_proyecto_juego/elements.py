import pygame
import constants
import os


class Tree:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.wood = 5
        tree_path = os.path.join ('desarrollo_proyecto_juego','assets', 'images', 'objects', 'tree.png')
        self.image = pygame.image.load(tree_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (constants.TREE, constants.TREE))
        self.size = self.image.get_width()

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def chop(self):
        if self.wood > 0:
            self.wood -= 1
            return True
        return False


class SmallStone:
    def __init__(self, x, y ):
        self.x = x
        self.y = y
        self.stone = 1
        small_stone_path = os.path.join ('desarrollo_proyecto_juego', 'assets', 'images', 'objects', 'small_stone.png')
        self.image = pygame.image.load(small_stone_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (constants.SMALL_STONE, constants.SMALL_STONE))
        self.size = self.image.get_width()

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))