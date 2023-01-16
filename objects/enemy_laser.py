from .importer import *
from .abstract_laser import *


class EnemyLaser(AbstractLaser):
    image = load_image(path.join('effects', 'enemy_laser.png'))

    def __init__(self, top: int, center: int):
        super().__init__(top + EnemyLaser.image.get_height(),
                         center,  7, EnemyLaser.image, enemy_lasers)
        self.damage = 10
        play('enemy_laser')
