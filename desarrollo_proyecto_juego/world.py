import pygame
import constants
from elements import Tree, SmallStone
import random
import os
from pygame import Surface

class World:
    def __init__(self, width, height):
        self.widht = width
        self.height = height
        self.trees = [Tree(random.randint(0, width-constants.TREE),
                           random.randint(0, height-constants.TREE)) for _ in range(10)]
        self.small_stones = [SmallStone(random.randint(0, width-constants.SMALL_STONE),
                           random.randint(0, height-constants.SMALL_STONE)) for _ in range(20)]

        
        grass_path = os.path.join ('desarrollo_proyecto_juego', 'assets', 'images', 'objects', 'grass.png')
        self.grass_image = pygame.image.load(grass_path).convert()
        self.grass_image = pygame.transform.scale(self.grass_image,
                                                  (constants.GRASS, constants.GRASS))        

        # Sistema día/noche
        self.current_time = constants.MORNING_TIME #Comenzar a las 8:00
        self.day_overlay = Surface((width, height))
        self.day_overlay.fill(constants.DAY_COLOR)
        self.day_overlay.set_alpha(0)

    def update_time(self,dt):
        self.current_time =(self.current_time + dt) % constants.DAY_LENGTH
        alpha = 0
        #Calcular el color y la intesidad basados en la hora del día
        if constants.MORNING_TIME <= self.current_time < constants.DUSK_TIME:
            # Durante el día (8:00 - 18:00)
            self.day_overlay.fill(constants.DAY_COLOR)
            alpha = 0
        elif constants.DAWN_TIME <= self.current_time <constants.MORNING_TIME:
            # Entre  6:00 y 8:00 - Amanecer
            self.day_overlay.fill(constants.NIGHT_COLOR)
            morning_progress = (self.current_time -constants.DAWN_TIME) / (
                        constants.MORNING_TIME - constants.DAWN_TIME)
            alpha = int(constants.MAX_DARKNESS * (1 - morning_progress))
        elif constants.DUSK_TIME <= self.current_time <= constants.MIDNIGHT:
            # Entre 18:00 y 00:00 - Atardecer
            self.day_overlay.fill(constants.NIGHT_COLOR)
            night_progress = (self.current_time - constants.DUSK_TIME) / (constants.MIDNIGHT - constants.DUSK_TIME)
            alpha = int(constants.MAX_DARKNESS * night_progress)
        else:
            # ENTRE LAS 00:00 Y 06:00 - Noche
            self.day_overlay.fill(constants.NIGHT_COLOR)
            alpha = constants.MAX_DARKNESS

        self.day_overlay.set_alpha(alpha)


    def draw(self, screen):
        for y in range(0, self.height, constants.GRASS):
            for x in range(0, self.widht, constants.GRASS):
                screen.blit(self.grass_image, (x, y))

        for small_stone in self.small_stones:
            small_stone.draw(screen)
            
        for tree in self.trees:
            tree.draw(screen)
        
        #Aplicar overlay día/noche
        screen.blit(self.day_overlay, (0,0))

    def draw_inventory(self, screen, character):
        font = pygame.font.Font(None, 24)
        instruction_text = font.render("Press 'I' to open inventory", True, constants.WHITE)
        screen.blit(instruction_text, (10, 10))
        