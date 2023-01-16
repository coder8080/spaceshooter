import pygame
from os import path
from .resource_path import *
from sys import exit
from os import listdir


def load_image(name: str) -> pygame.Surface:
    fullname = resource_path(path.join('resources', name))
    if not path.exists(fullname):
        print(f'Файл с изображением {fullname} не найден')
        exit(1)
    image = pygame.image.load(fullname)
    return image
