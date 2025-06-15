import pygame 
import sys
import constants
from character import Character
from world import World

#inicializar pygame
pygame.init()


screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
pygame.display.set_caption("Juego educativo")

def main():
    clock = pygame.time.Clock()
    world = World(constants.WIDTH, constants.HEIGHT)
    character = Character(constants.WIDTH // 2, constants.HEIGHT // 2)
    show_inventory = False

    status_update_timer = 0

    # Variables para la cámara
    camera_x = 0
    camera_y = 0


    while True:
        dt = clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
#Funciones al presionar alguan tecla
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    character.interact(world)
                if event.key == pygame.K_i:
                    show_inventory = not show_inventory
                if event.key == pygame.K_f:
                    character.update_food(20)
                if event.key == pygame.K_t:
                    character.update_thirst(20)  

        dx = dy = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            dx = -5
        if keys[pygame.K_RIGHT]:
            dx = 5
        if keys[pygame.K_UP]:
            dy = -5
        if keys[pygame.K_DOWN]:
            dy = 5
        character.move(dx, dy, world)

        # La cámara sigue al personaje
        camera_x = character.x - constants.WIDTH // 2
        camera_y = character.y - constants.HEIGHT // 2

        # Actualizar los chunks basado en la posición del personaje
        world.uptade_chunks(character.x, character.y)

        #Actualizar el tiempo del día
        world.update_time(dt)

        status_update_timer += dt
        if status_update_timer >= constants.STATUS_UPDATE_INTERVAL:
            character.update_status()
            status_update_timer = 0

        if character.energy <= 0 or character.food <= 0 or character.thirst <= 0:
            print("Game over!")
            pygame.quit()
            sys.exit()

        # Limpiar pantalla
        screen.fill((0, 0, 0))

        # Dibujar mundo con effset de la cámara
        world.draw(screen, camera_x, camera_y)

    
        character.draw(screen, camera_x, camera_y)
        if show_inventory:
            character.draw_inventory(screen)

        font = pygame.font.Font(None, 24)
        energy_text = font.render(f"Energy: {int(character.energy)}", True, constants.WHITE)
        food_text = font.render(f"Food: {int(character.food)}", True, constants.WHITE)
        thirst_text = font.render(f"Thirst: {int(character.thirst)}", True, constants.WHITE)
        # Añadir indicador de tiempo
        time_of_day = (world.current_time / constants.DAY_LENGTH) * 24 # Concertir a formato 24 horas
        time_text = font.render(f"Time: {int(time_of_day):02d}:00", True, constants.WHITE)

        screen.blit(energy_text, (10, constants.HEIGHT - 90))
        screen.blit(food_text, (10, constants.HEIGHT - 65))
        screen.blit(thirst_text, (10, constants.HEIGHT - 40))
        screen.blit(time_text, (10, constants.HEIGHT - 15))

        pygame.display.flip()







if __name__ == "__main__":  
    main()