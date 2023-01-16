from .importer import *


class Explosion(pygame.sprite.Sprite):
    images = [load_image(path.join('explosion', '1.png')), load_image(
        path.join('explosion', '2.png')), load_image(path.join('explosion', '3.png'))]

    def __init__(self, x: int, y: int, duraion: int = 12):
        super().__init__(explosions)
        self.state = 0
        self.image = Explosion.images[0]
        self.rect = self.image.get_rect()
        self.update_coords(x, y)
        self.duration = duraion
        self.state_duration = self.duration // 3
        self.timer = Timer(self.change_stage, self.state_duration)
        play('player_damage')

    def update_coords(self, x: int, y: int):
        self.rect.x = x - self.rect.width // 2
        self.rect.y = y - self.rect.height // 2

    def change_stage(self):
        self.state += 1
        if self.state > 2:
            self.kill()
            return
        self.image = Explosion.images[self.state]
        return self.state_duration

    def update(self):
        self.timer.update()
