from .importer import *
from .score import *


class AbstractPowerUp(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface):
        super().__init__(power_ups)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.bottom = 0
        self.rect.left = randint(10, WIDTH - self.rect.width - 10)
        self.speed = 3

    def apply(self):
        pass

    def update(self) -> None:
        self.rect.y += self.speed
        if self.rect.top >= HEIGHT:
            self.kill()
        if pygame.sprite.spritecollideany(self, player):
            self.apply()
            self.kill()


class StarPowerUp(AbstractPowerUp):
    image = load_image(path.join('power-ups', 'star.png'))

    def __init__(self):
        super().__init__(StarPowerUp.image)
        self.score = Score()

    def apply(self):
        self.score.star_collected()

# class Shield(PowerUp):
#     image = load_image(path.join('power-ups', 'shield.png'))

#     def __init__(self):
#         super().__init__(Shield.image)


# class Pill(PowerUp):
#     image = load_image(path.join('power-ups', 'pill.png'))

#     def __init__(self):
#         super().__init__(Pill.image)

def generate_powerup_delay() -> int:
    return randint(POWERUP_DELAY_MIN, POWERUP_DELAY_MAX)


powerup_types = [StarPowerUp]
