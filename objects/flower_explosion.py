from .importer import *

screen_rect = pygame.rect.Rect(0, 0, WIDTH, HEIGHT)


class Partile(pygame.sprite.Sprite):
    images = [load_image(path.join('effects', 'flower.png'))]
    for scale in (10, 20):
        images.append(pygame.transform.scale(images[0], (scale, scale)))
    images = images[1:]

    def __init__(self, pos, dx, dy):
        super().__init__(particles)
        self.image = choice(Partile.images)
        self.rect = self.image.get_rect()
        self.velocity = [dx, dy]
        self.rect.x, self.rect.y = pos
        self.gravity = GRAVITY

    def update(self):
        self.velocity[1] += self.gravity
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if not self.rect.colliderect(screen_rect):
            self.kill()


def generate_flower_explosion(pos):
    particle_count = 20
    numbers = range(-5, 6)
    for _ in range(particle_count):
        Partile(pos, choice(numbers), choice(numbers))
