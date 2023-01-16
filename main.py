from objects.utilities.all import *
from objects.all import *
import pygame


def spawn_enemies():
    for _ in range(ENEMY_COUNT):
        Enemy()
    for enemy in enemies:
        enemy.end_computation()
    return ENEMY_DELAY


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
    play('music')
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
        # laser_sound_timer = Timer(play_laser_sound, LASER_SOUND_DELAY)
        while is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.MOUSEMOTION:
                    player.update(event)

            enemy_timer.update()
            powerup_timer.update()
            # laser_sound_timer.update()
            screen.fill('black')
            update_all_groups()
            draw_all_groups(screen)
            pygame.display.flip()
            clock.tick(FPS)
        clear_all_groups()
        end_screen(screen, score, has_showed_conclusion)
        has_showed_conclusion = True
