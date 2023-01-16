from .importer import *


class PowerUp(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface):
        super().__init__(power_ups)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.bottom = randint(-10, -200)
        self.rect.left = randint(10, WIDTH - self.rect.width - 10)
        self.speed = 3

    def update(self):
        self.rect.y += self.speed
        if self.rect.top >= HEIGHT:
            self.kill()


class Shield(PowerUp):
    image = load_image(path.join('power-ups', 'shield.png'))

    def __init__(self):
        super().__init__(Shield.image)


class Pill(PowerUp):
    image = load_image(path.join('power-ups', 'pill.png'))

    def __init__(self):
        super().__init__(Pill.image)
