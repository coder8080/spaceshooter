import pygame
from os import path
from sys import exit
from random import randint

WIDTH = 600
HEIGHT = 600
BACKGROUND_HEIGHT = 1280 / 720 * WIDTH
PLAYER_STYLE = 'red'
FPS = 60
lifes_left = 3


def terminate() -> None:
    pygame.quit()
    exit()


def load_image(name: str) -> pygame.Surface:
    fullname = path.join('images', name)
    if not path.exists(fullname):
        print(f'Файл с изображением {fullname} не найден')
        exit(1)
    image = pygame.image.load(fullname)
    return image


def start_screen() -> None:
    pass


class Background(pygame.sprite.Sprite):
    source_image = pygame.transform.scale(load_image(
        'background.png'), (WIDTH, BACKGROUND_HEIGHT))
    speed = 5

    def __init__(self, y_offset: int) -> None:
        super().__init__(backgrounds)
        self.image = Background.source_image
        self.rect = self.image.get_rect()
        if y_offset == 0:
            self.rect.top = 0
        else:
            self.rect.top = self.rect.height
        self.rect.left = 0

    def update(self) -> None:
        if self.rect.top >= HEIGHT:
            self.rect.bottom = self.rect.top - self.rect.height
        self.rect.top += self.speed


class AbstractLaser(pygame.sprite.Sprite):
    def __init__(self, bottom: int, center: int, speed: int, image: pygame.Surface, group: pygame.sprite.Group):
        super().__init__(group)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.bottom = bottom
        self.rect.left = center - self.rect.width // 2
        self.speed = speed

    def update(self):
        self.rect.top += self.speed
        if self.rect.bottom < 0 or self.rect.top > HEIGHT:
            self.kill()


class PlayerLaser(AbstractLaser):
    image = load_image(path.join('effects', 'player_laser.png'))

    def __init__(self, *args):
        super().__init__(*args, -20, PlayerLaser.image, player_lasers)
        self.damage = 25


class EnemyLaser(AbstractLaser):
    image = load_image(path.join('effects', 'enemy_laser.png'))

    def __init__(self, top: int, center: int):
        super().__init__(top + EnemyLaser.image.get_height(),
                         center,  7, EnemyLaser.image, enemy_lasers)
        self.damage = 10


class Player(pygame.sprite.Sprite):
    w = 60
    image = pygame.transform.scale(
        load_image(path.join('player', 'red.png')), (w, 303 / 400 * w))
    timing = 5
    damages = [load_image(path.join('damage', '1.png')), load_image(
        path.join('damage', '2.png')), load_image(path.join('damage', '3.png'))]
    for i in range(len(damages)):
        damages[i] = pygame.transform.scale(damages[i], (w, 303 / 400 * w))

    def __init__(self):
        super().__init__(player)
        self.image = Player.image.copy()
        self.rect = self.image.get_rect()
        self.rect.left = WIDTH // 2 - self.rect.width // 2
        self.rect.bottom = HEIGHT - 10
        self.time_left = Player.timing
        self.hp = 100
        self.is_exploding = False
        self.exploding_time_left = 0
        self.applied_damage = 100

    def small_explosion(self):
        Explosion(self.rect.x + self.rect.width // 2,
                  self.rect.y + self.rect.height // 2)

    def update(self, event=None):
        if event is not None and hasattr(event, 'pos'):
            x, y = event.pos
            self.rect.left = min(
                max(x - self.rect.width // 2, 0), WIDTH - self.rect.width)
            self.rect.top = min(max(y - self.rect.height // 2,
                                0), HEIGHT - self.rect.height)
            return
        self.time_left -= 1
        if not self.is_exploding and self.time_left <= 0:
            self.time_left = Player.timing
            PlayerLaser(self.rect.top, self.rect.left +
                        self.rect.width // 2)
        enemy_laser = pygame.sprite.spritecollideany(self, enemy_lasers)
        if enemy_laser:
            self.hp -= enemy_laser.damage
            self.small_explosion()
            enemy_laser.kill()

        colliding_enemy = pygame.sprite.spritecollideany(self, enemies)
        if colliding_enemy:
            self.hp -= 50
            print(self.hp)
            self.small_explosion()
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
            self.ex1 = Explosion(self.rect.x + self.rect.width // 2 - 20,
                                 self.rect.y + self.rect.height // 2 - 20, FPS * 2)
            self.ex2 = Explosion(self.rect.x + self.rect.width // 2 + 20,
                                 self.rect.y + self.rect.height // 2, FPS * 2)
            self.ex3 = Explosion(self.rect.x + self.rect.width // 2 - 20,
                                 self.rect.y + self.rect.height // 2 + 20, FPS * 2)
            self.is_exploding = True
            self.exploding_time_left = FPS * 2
            self.hp = 100
            spend_life()

        if self.is_exploding:
            self.ex1.update_coords(self.rect.x + self.rect.width // 2 - 10,
                                   self.rect.y + self.rect.height // 2 - 20)
            self.ex2.update_coords(self.rect.x + self.rect.width // 2 + 20,
                                   self.rect.y + self.rect.height // 2)
            self.ex3.update_coords(self.rect.x + self.rect.width // 2 - 10,
                                   self.rect.y + self.rect.height // 2 + 20)
            self.exploding_time_left -= 1
            if self.exploding_time_left <= 0:
                self.is_exploding = False
                self.image = Player.image.copy()


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
        self.time_left = self.state_duration

    def update_coords(self, x: int, y: int):
        self.rect.x = x - self.rect.width // 2
        self.rect.y = y - self.rect.height // 2

    def update(self):
        self.time_left -= 1
        if self.time_left <= 0:
            self.state += 1
            if self.state > 2:
                self.kill()
                return
            self.image = Explosion.images[self.state]
            self.time_left = self.state_duration


class Enemy(pygame.sprite.Sprite):
    w = 60
    source_image = load_image(path.join('enemies', 'enemyBlack1.png'))
    image = pygame.transform.scale(
        source_image, (w, source_image.get_height() / source_image.get_width() * w))
    speed = 2

    def __init__(self):
        super().__init__(enemies)
        self.image = Enemy.image
        self.rect = self.image.get_rect()
        self.horizontal_speed = randint(-2, 2)
        # self.time_to_change = randint(FPS * 1, FPS * 4)
        self.time_to_change = 100500
        self.rect.top = randint(5, 150)
        self.rect.left = randint(0, WIDTH - self.rect.width)
        left_retries = 100
        self.delay_to_move = randint(FPS * 3, FPS * 4)
        self.is_moving = False
        while len(pygame.sprite.spritecollide(self, enemies, False)) > 1:
            left_retries -= 1
            if left_retries < 0:
                break
            self.rect.left = randint(0, WIDTH - self.rect.width)
        self.hp = 100
        self.time_to_shoot = randint(1, FPS * 4)

    def update(self):
        self.rect.x += self.horizontal_speed
        if self.rect.left < 0 or self.rect.left > WIDTH - self.rect.width or len(pygame.sprite.spritecollide(self, enemies, False)) > 1:
            self.horizontal_speed = 0
        self.rect.left = max(0, self.rect.left)
        self.rect.left = min(WIDTH - self.rect.width, self.rect.left)
        colliding_laser = pygame.sprite.spritecollideany(self, player_lasers)
        if colliding_laser:
            colliding_laser.kill()
            self.hp -= colliding_laser.damage
            if self.hp <= 0:
                Explosion(self.rect.x + self.rect.width // 2,
                          self.rect.y + self.rect.height // 2)
                self.kill()
                return
        if self.rect.top > HEIGHT:
            self.kill()
            return
        if self.is_moving:
            self.rect.top += Enemy.speed
        else:
            self.delay_to_move -= 1
            if self.delay_to_move <= 0:
                self.is_moving = True
        self.time_to_shoot -= 1
        if self.time_to_shoot <= 0:
            self.time_to_shoot = randint(1, FPS * 4)
            EnemyLaser(self.rect.bottom, self.rect.left + self.rect.width // 2)

        self.time_to_change -= 1
        if self.time_to_change <= 0:
            self.horizontal_speed = randint(-2, 2)
            self.time_to_change = randint(FPS * 1, FPS * 4)


def spend_life():
    player_lasers.empty()
    enemy_lasers.empty()
    enemies.empty()
    global enemy_time_left
    enemy_time_left = enemy_delay


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('SpaceShooter')
    pygame.mouse.set_visible(False)
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    is_running = True
    clock = pygame.time.Clock()
    backgrounds = pygame.sprite.Group()
    player_lasers = pygame.sprite.Group()
    enemy_lasers = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    player = pygame.sprite.Group()
    explosions = pygame.sprite.Group()
    Background(0)
    Background(1)
    Player()
    enemy_delay = FPS * 4
    enemy_time_left = enemy_delay
    enemy_count = 5
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEMOTION:
                player.update(event)
        enemy_time_left -= 1
        if enemy_time_left <= 0:
            enemy_time_left = enemy_delay
            for _ in range(enemy_count):
                Enemy()
        screen.fill('black')
        backgrounds.update()
        player.update()
        player_lasers.update()
        enemy_lasers.update()
        enemies.update()
        explosions.update()
        backgrounds.draw(screen)
        player.draw(screen)
        player_lasers.draw(screen)
        enemy_lasers.draw(screen)
        enemies.draw(screen)
        explosions.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
