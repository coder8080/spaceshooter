from .importer import *


@singleton
class HealthDisplay(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(displays_group)
        self.value = 100
        self.font = pygame.font.Font(
            resource_path(path.join('resources', 'font.ttf')), 24)
        self.update()

    def set_value(self, value: int):
        self.value = max(value, 0)

    def update(self):
        self.image = self.font.render(
            str(self.value) + '%', 1, pygame.color.Color('white'))
        self.rect = self.image.get_rect()
        self.rect.top = 10
        self.rect.right = WIDTH - 10

    def get_value(self):
        return self.value
