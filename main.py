import pygame
from os import path
from sys import exit

WIDTH = 600
HEIGHT = 600
BACKGROUND_HEIGHT = 1280 / 720 * WIDTH


def terminate() -> None:
    pygame.quit()
    exit()


def load_image(name: str) -> pygame.Surface:
    fullname = path.join('images', name)
    if not path.exists(fullname):
        print(f'Файл с изображением {fullname} не найден')
        exit(1)
    image = pygame.image.load(fullname)
    return image


def start_screen() -> None:
    pass


class Background(pygame.sprite.Sprite):
    source_image = pygame.transform.scale(load_image(
        'background.png'), (WIDTH, BACKGROUND_HEIGHT))
    speed = 5

    def __init__(self, y_offset: int) -> None:
        super().__init__(backgrounds)
        self.image = Background.source_image
        self.rect = self.image.get_rect()
        self.rect.top = y_offset
        self.rect.left = 0

    def update(self) -> None:
        if self.rect.top >= HEIGHT:
            self.rect.bottom = 0
        self.rect.top += self.speed


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('SpaceShooter')
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    is_running = True
    clock = pygame.time.Clock()
    backgrounds = pygame.sprite.Group()
    Background(0)
    Background(HEIGHT)
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        screen.fill('black')
        backgrounds.update()
        backgrounds.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
