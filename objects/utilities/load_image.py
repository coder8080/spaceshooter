import pygame
from os import path


def load_image(name: str) -> pygame.Surface:
    fullname = path.join('resources', name)
    if not path.exists(fullname):
        print(f'Файл с изображением {fullname} не найден')
        exit(1)
    image = pygame.image.load(fullname)
    return image
