import pygame
from objects.utilities.all import *
from objects.all import *
from os import listdir


def spawn_enemies():
    for _ in range(enemy_count):
        Enemy()
    for enemy in enemies:
        enemy.end_computation()
    return ENEMY_DELAY


def increase_enemies():
    global enemy_count
    enemy_count += 1
    return INCREASE_ENEMIES_DELAY


def spawn_powerup():
    PowerUpType = choice(powerup_types)
    PowerUpType()
    return generate_powerup_delay()


def end_game():
    player_lasers.empty()
    enemy_lasers.empty()
    enemies.empty()
    global enemy_time_left
    enemy_time_left = ENEMY_DELAY


if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption('SpaceShooter')
    pygame.mouse.set_visible(False)
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    start_screen(screen)
    has_showed_conclusion = False
    while True:
        is_running = True

        def end_game():
            global is_running
            is_running = False

        clock = pygame.time.Clock()
        Background(0)
        Background(1)
        Player(end_game)
        score = Score()
        enemy_timer = Timer(spawn_enemies, ENEMY_DELAY)
        powerup_timer = Timer(spawn_powerup, generate_powerup_delay())
        increase_timer = Timer(increase_enemies, INCREASE_ENEMIES_DELAY)
        while is_running:
            update_music()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
            enemy_timer.update()
            powerup_timer.update()
            increase_timer.update()
            screen.fill('black')
            player.update(pygame.mouse.get_pos())
            update_all_groups()
            draw_all_groups(screen)
            pygame.display.flip()
            clock.tick(FPS)
        stop('music')
        clear_all_groups()
        end_screen(screen, score, has_showed_conclusion)
        has_showed_conclusion = True
