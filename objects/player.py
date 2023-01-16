from .importer import *
from .explosion import *
from .player_laser import *
from .flower_explosion import *


class Player(pygame.sprite.Sprite):
    w = 60
    image = pygame.transform.scale(
        load_image(path.join('player', 'red.png')), (w, 303 / 400 * w))
    timing = 5
    damages = [load_image(path.join('damage', '1.png')), load_image(
        path.join('damage', '2.png')), load_image(path.join('damage', '3.png'))]
    for i in range(len(damages)):
        damages[i] = pygame.transform.scale(damages[i], (w, 303 / 400 * w))

    def __init__(self, end_game):
        super().__init__(player)
        self.end_game = end_game
        self.image = Player.image.copy()
        self.rect = self.image.get_rect()
        self.rect.left = WIDTH // 2 - self.rect.width // 2
        self.rect.bottom = HEIGHT - 10
        self.shoot_timer = Timer(self.shoot, Player.timing)
        self.hp = 100
        self.applied_damage = 100

    def small_explosion(self):
        Explosion(self.rect.x + self.rect.width // 2,
                  self.rect.y + self.rect.height // 2)

    def flower_explosion(self):
        generate_flower_explosion((self.rect.x + self.rect.width // 2,
                                   self.rect.y + self.rect.height // 2))

    def shoot(self):
        PlayerLaser(self.rect.top, self.rect.left +
                    self.rect.width // 2)
        return Player.timing

    def refresh_image(self):
        self.image = Player.image.copy()

    def update(self, event=None):
        if event is not None and hasattr(event, 'pos'):
            x, y = event.pos
            self.rect.left = min(
                max(x - self.rect.width // 2, 0), WIDTH - self.rect.width)
            self.rect.top = min(max(y - self.rect.height // 2,
                                0), HEIGHT - self.rect.height)
            return

        enemy_laser = pygame.sprite.spritecollideany(self, enemy_lasers)
        if enemy_laser:
            self.hp -= enemy_laser.damage
            self.small_explosion()
            enemy_laser.kill()

        colliding_enemy = pygame.sprite.spritecollideany(self, enemies)
        if colliding_enemy:
            self.hp -= 50
            self.flower_explosion()
            colliding_enemy.kill()
        if self.hp != self.applied_damage:
            self.image = Player.image.copy()
            if self.hp < 25:
                self.image.blit(Player.damages[2], (0, 0))
            if self.hp < 50:
                self.image.blit(Player.damages[1], (0, 0))
            if self.hp < 75:
                self.image.blit(Player.damages[0], (0, 0))
            self.applied_damage = self.hp

        if self.hp <= 0:
            self.hp = 100
            self.end_game()
        self.shoot_timer.update()
