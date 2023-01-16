from .importer import *
from .abstract_laser import *


class PlayerLaser(AbstractLaser):
    """ Продукт выстрела экспериментальной пушки """
    image = pygame.transform.scale(
        load_image(path.join('effects', 'heart.png')), (20, 20))

    def __init__(self, *args):
        super().__init__(*args, -20, PlayerLaser.image, player_lasers)
        self.damage = 25
