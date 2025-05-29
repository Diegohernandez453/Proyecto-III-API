import pygame
import constants
import os

class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.inventory = {"wood":0, "stone":0}
        image_path = os.path.join ('desarrollo_proyecto_juego', 'assets', 'images', 'character', 'character.png')
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (constants.PLAYER, constants.PLAYER))
        self.size = self.image.get_width()

        self.item_images= {
            "wood": self.load_item_image("wood.png"),
            "stone": self.load_item_image("small_stone.png")
        }
    
        self.energy = constants.MAX_ENERGY
        self.food = constants.MAX_FOOD
        self.thirst = constants.MAX_THIRST




    def load_item_image(self, filename):
        path = os.path.join('desarrollo_proyecto_juego', 'assets', 'images', 'objects', filename)
        image = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(image, (40, 40))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        self.draw_status_bars(screen)

    def move(self, dx, dy, world):
        new_x = self.x + dx
        new_y = self.y + dy
        
        for tree in world.trees:
            if self.check_collision(new_x, new_y, tree):
                return
        self.x = new_x
        self.y = new_y
        self.x = max(0, min(self.x, constants.WIDTH - self.size))
        self.y = max(0, min(self.y, constants.HEIGHT - self.size))

        #Cuando se mueve pierde energia
        self.update_energy(-0.1)


    def check_collision(self, x, y, obj):
        return (x < obj.x + obj.size*.75 and x + self.size*.75 > obj.x and y < obj.y + obj.size*.75 and
                y + self.size*.75 > obj.y)

    def is_near(self, obj):
        return (abs(self.x - obj.x) <= max(self.size, obj.size)+5 and
                abs(self.y - obj.y) <= max(self.size, obj.size)+5)
    
    def interact(self, world):
        for tree in world.trees:
            if self.is_near(tree):
                if tree.chop():
                    self.inventory["wood"] += 1
                    if tree.wood == 0:
                        world.trees.remove(tree)
                    return
        
        for stone in world.small_stones:
            if self.is_near(stone):
                self.inventory["stone"] += stone.stone
                world.small_stones.remove(stone)
                return

    def draw_inventory(self, screen):
        background = pygame.Surface((constants.WIDTH, constants.HEIGHT), pygame.SRCALPHA)
        background.fill((0, 0, 0, 128))
        screen.blit(background, (0,0))

        font = pygame.font.Font(None, 36)
        title = font.render("Inventory", True, constants.WHITE)
        screen.blit(title, (constants.WIDTH // 2 - title.get_width()// 2, 20))

        item_font = pygame.font.Font(None, 24)
        y_offset = 80
        for item, quantity in self.inventory.items():
            if quantity > 0:
                screen.blit(self.item_images[item], (constants.WIDTH // 2 - 60, y_offset))
                text = item_font.render(f"{item.capitalize()}: {quantity}", True, constants.WHITE)
                screen.blit(text, (constants.WIDTH // 2 + 10, y_offset + 10))
                y_offset +=  50
        
        close_text = item_font.render("Press 'I' to close de inventory",
                                      True, constants.WHITE)
        screen.blit(close_text, (constants.WIDTH // 2 - close_text.get_width() // 2, constants.HEIGHT - 40))

    def update_energy(self, amount):
        self.energy = max(0, min(self.energy + amount, constants.MAX_ENERGY))

    def update_food(self, amount):
        self.food = max(0, min(self.food + amount, constants.MAX_FOOD))

    def update_thirst(self, amount):
        self.thirst = max(0, min(self.thirst + amount, constants.MAX_THIRST))

    def draw_status_bars(self, screen):
        bar_width = 100
        bar_height = 10
        x_offset = 10
        y_offset = 10

        # Energy bar
        pygame.draw.rect(screen, constants.BAR_BACKGROUND,
                         (x_offset, y_offset, bar_width, bar_height))
        
        pygame.draw.rect(screen, constants.ENERGY_COLOR,
                    (x_offset, y_offset, bar_width * (self.energy / constants.MAX_ENERGY), bar_height))
        
        #Food bar
        y_offset += 15
        pygame.draw.rect(screen, constants.BAR_BACKGROUND,
                         (x_offset, y_offset, bar_width, bar_height))
        
        pygame.draw.rect(screen, constants.FOOD_COLOR,
                    (x_offset, y_offset, bar_width * (self.food / constants.MAX_FOOD), bar_height))
        
        #Thirst bar
        y_offset += 15
        pygame.draw.rect(screen, constants.BAR_BACKGROUND,
                         (x_offset, y_offset, bar_width, bar_height))
        
        pygame.draw.rect(screen, constants.THIRST_COLOR,
                    (x_offset, y_offset, bar_width * (self.thirst / constants.MAX_THIRST), bar_height))

    def update_status(self):
        self.update_food(-1)
        self.update_thirst(-2)

        if self.food < constants.MAX_FOOD * 0.2 or self.thirst < constants.MAX_THIRST * 0.2:
            self.update_energy(-1)
        else:
            self.update_energy(0.5)