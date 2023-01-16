from .importer import *
from .enemy_laser import *
from .explosion import *
from .flower_explosion import *
from .score import *


class Enemy(pygame.sprite.Sprite):
    w = 60
    source_image = load_image(path.join('enemies', 'enemyBlack1.png'))
    image = pygame.transform.scale(
        source_image, (w, source_image.get_height() / source_image.get_width() * w))
    speed = 2
    animationg_speed = 3

    def __init__(self):
        super().__init__(enemies)
        self.score = Score()

        self.image = Enemy.image
        self.rect = self.image.get_rect()
        self.horizontal_speed = randint(-2, 2)

        # Анимация вылета из-за края экрана
        self.is_animating = True
        self.top_destination = randint(5, 150)
        self.top_source = randint(-2 * self.rect.height, -1 * self.rect.height)
        # задержка перед тем, как изменить скорость горизонтального смещения
        self.horizontal_update_timer = Timer(
            self.change_horizontal, randint(FPS * 1, FPS * 2.5))
        # вычисляю приемлимое положение слева, чтобы не было пересечений с другими объектами
        self.rect.top = self.top_destination
        self.rect.left = randint(0, WIDTH - self.rect.width)
        left_retries = 100
        self.move_timer = Timer(
            self.start_moving, randint(FPS * 3, FPS * 4), False)
        self.is_moving = False
        while len(pygame.sprite.spritecollide(self, enemies, False)) > 1:
            left_retries -= 1
            if left_retries < 0:
                break
            self.rect.left = randint(0, WIDTH - self.rect.width)

        self.hp = 100  # здоровье
        # задержка перед следующим выстрелом
        self.shoot_timer = Timer(self.shoot, randint(0.5 * FPS, FPS * 4))

    def end_computation(self) -> None:
        if self.is_animating:
            # возвращаю в top значение для анимации
            self.rect.top = self.top_source

    def start_moving(self):
        self.is_moving = True
        self.is_ticking = False

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
                self.score.enemy_destroyed()
                generate_explosion((self.rect.x + self.rect.width // 2,
                                    self.rect.y + self.rect.height // 2))
                self.kill()
                return
        if self.rect.top > HEIGHT:
            self.score.enemy_at_base()
            self.kill()
            return
        if self.is_animating:
            self.rect.top += Enemy.animationg_speed
            if self.rect.top >= self.top_destination:
                self.rect.top = self.top_destination
                self.is_animating = False
                self.move_timer.start()
        elif self.is_moving:
            self.rect.top += Enemy.speed
        if not self.is_animating:
            self.shoot_timer.update()
        self.horizontal_update_timer.update()
        self.move_timer.update()

    def change_horizontal(self):
        self.horizontal_speed = randint(-3, 3)
        return randint(FPS * 1, FPS * 4)

    def shoot(self):
        EnemyLaser(self.rect.bottom, self.rect.left +
                   self.rect.width // 2)
        return randint(0.5 * FPS, FPS * 4)
