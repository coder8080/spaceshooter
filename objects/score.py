from .importer import *


@singleton
class Score(pygame.sprite.Sprite):
    """ Отображение текущего игрового счёта """

    def __init__(self):
        super().__init__(displays_group)
        self.value = 0
        self.destroyed_enemies = 0
        self.font = pygame.font.Font(
            resource_path(path.join('resources', 'font.ttf')), 24)
        self.update()

    def enemy_destroyed(self):
        self.value += 15
        self.destroyed_enemies += 1

    def enemy_at_base(self):
        self.value -= 30

    def star_collected(self):
        self.value += 30

    def update(self):
        self.image = self.font.render(
            str(self.value), 1, pygame.color.Color('white'))
        self.rect = self.image.get_rect()
        self.rect.left = (WIDTH - self.rect.width) // 2
        self.rect.top = 10

    def get_value(self):
        return self.value

    def get_destroyed_enemies(self):
        return self.destroyed_enemies
