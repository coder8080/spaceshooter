from .importer import *


class AbstractLaser(pygame.sprite.Sprite):
    def __init__(self, bottom: int, center: int, speed: int, image: pygame.Surface, group: pygame.sprite.Group):
        super().__init__(group)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.bottom = bottom
        self.rect.left = center - self.rect.width // 2
        self.speed = speed

    def update(self):
        self.rect.top += self.speed
        if self.rect.bottom < 0 or self.rect.top > HEIGHT:
            self.kill()
