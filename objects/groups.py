import pygame

backgrounds = pygame.sprite.Group()
player_lasers = pygame.sprite.Group()
enemy_lasers = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player = pygame.sprite.Group()
explosions = pygame.sprite.Group()
power_ups = pygame.sprite.Group()
particles = pygame.sprite.Group()
score_group = pygame.sprite.Group()

all_groups = [backgrounds, player_lasers, enemy_lasers, enemies,
              player, explosions, power_ups, particles, score_group]


def update_all_groups() -> None:
    for group in all_groups:
        group.update()


def draw_all_groups(screen: pygame.surface) -> None:
    for group in all_groups:
        group.draw(screen)


def clear_all_groups() -> None:
    for group in all_groups:
        group.empty()
