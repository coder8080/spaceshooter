import pygame
from sys import exit


def terminate() -> None:
    """ Завершить программу из любого состояния """
    pygame.quit()
    exit()
