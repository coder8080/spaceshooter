from .importer import *


def singleton(class_):
    class class_w(class_):
        _instance = None

        def __new__(class_, *args, **kwargs):
            if class_w._instance is None:
                class_w._instance = super(class_w,
                                          class_).__new__(class_,
                                                          *args,
                                                          **kwargs)
                class_w._instance._sealed = False
            return class_w._instance

        def __init__(self, *args, **kwargs):
            if self._sealed:
                return
            super(class_w, self).__init__(*args, **kwargs)
            self._sealed = True
    class_w.__name__ = class_.__name__
    return class_w


@singleton
class Score(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(score_group)
        self.value = 0
        self.font = pygame.font.Font(
            path.join('resources', 'font.ttf'), 24)
        self.update()

    def enemy_destroyed(self):
        self.value += 15

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
