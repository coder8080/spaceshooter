import pygame
from objects.all import *
from objects.utilities.all import *


def spawn_enemies():
    for _ in range(enemy_count):
        Enemy()
    for enemy in enemies:
        enemy.end_computation()
    return enemy_delay


def spend_life():
    player_lasers.empty()
    enemy_lasers.empty()
    enemies.empty()
    global enemy_time_left
    enemy_time_left = enemy_delay


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('SpaceShooter')
    pygame.mouse.set_visible(False)
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)

    start_screen(screen)

    is_running = True
    clock = pygame.time.Clock()
# ------
    Background(0)
    Background(1)
    Player()
    enemy_timer = Timer(spawn_enemies, enemy_delay)
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEMOTION:
                player.update(event)

        enemy_timer.update()
        screen.fill('black')

        backgrounds.update()
        player.update()
        player_lasers.update()
        enemy_lasers.update()
        enemies.update()
        explosions.update()
        power_ups.update()
        particles.update()

        backgrounds.draw(screen)
        player.draw(screen)
        player_lasers.draw(screen)
        enemy_lasers.draw(screen)
        enemies.draw(screen)
        explosions.draw(screen)
        power_ups.draw(screen)
        particles.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
