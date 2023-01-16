""" Усиления """

from .importer import *
from .score import *


class AbstractPowerUp(pygame.sprite.Sprite):
    """ Общее поведение усилений """

    def __init__(self, image: pygame.Surface):
        super().__init__(power_ups)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.bottom = 0
        self.rect.left = randint(10, WIDTH - self.rect.width - 10)
        self.speed = 3

    def apply(self):
        play('powerup')

    def update(self) -> None:
        self.rect.y += self.speed
        if self.rect.top >= HEIGHT:
            self.kill()
        if pygame.sprite.spritecollideany(self, player):
            self.apply()
            self.kill()


class StarPowerUp(AbstractPowerUp):
    """ Усиление дополнительных очков """
    image = load_image(path.join('power-ups', 'star.png'))

    def __init__(self):
        super().__init__(StarPowerUp.image)
        self.score = Score()

    def apply(self):
        super().apply()
        self.score.star_collected()


class ArmorPowerUp(AbstractPowerUp):
    """ Усиление брони """
    image = load_image(path.join('power-ups', 'shield.png'))

    def __init__(self):
        super().__init__(ArmorPowerUp.image)

    def apply(self):
        super().apply()
        player_sprite = list(player)[0]
        player_sprite.hp = min(player_sprite.hp + 20, 100)


def generate_powerup_delay() -> int:
    return randint(POWERUP_DELAY_MIN, POWERUP_DELAY_MAX)


powerup_types = [StarPowerUp, ArmorPowerUp]
