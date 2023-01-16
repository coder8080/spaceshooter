from .importer import *


class Background(pygame.sprite.Sprite):
    """ Движущийся фон во врем игры """
    source_image = pygame.transform.scale(load_image(
        'background.png'), (WIDTH, BACKGROUND_HEIGHT))
    speed = 5

    def __init__(self, y_offset: int) -> None:
        super().__init__(backgrounds)
        self.image = Background.source_image
        self.rect = self.image.get_rect()
        if y_offset == 0:
            self.rect.top = 0
        else:
            self.rect.top = self.rect.height
        self.rect.left = 0

    def update(self) -> None:
        if self.rect.top >= HEIGHT:
            self.rect.bottom = self.rect.top - self.rect.height
        self.rect.top += self.speed
