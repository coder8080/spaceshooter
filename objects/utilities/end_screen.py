from .load_image import *
from .constants import *
from .terminate import *
from random import randint


def end_screen(screen: pygame.Surface, score) -> None:
    TEXT = ['Заключение', 'Броня корабля была на исходе. Подкрепление пришло',
            'вовремя, и вы благополучно вернулись на базу. Стажёру',
            'кончно, сделали выговор, но его чертежы были отправлены',
            'в главное конструкторское бюро федерации.',
            '',
            'Результат тестирования',
            f'Набранные очки: {score.get_value()}',
            f'Враги, которые стали цветами: {score.get_destroyed_enemies()}',
            f'Планеты, на которых теперь есть жизнь: {score.get_destroyed_enemies() // randint(3, 7)}',
            '',
            'Чтобы сыграть ещё раз, нажмите любую клавишу']
    background = load_image(path.join('effects', 'start_heart.png'))
    background = pygame.transform.scale(
        background, (START_WIDTH // 2, START_HEIGHT // 2))
    screen.fill('black')
    rect = background.get_rect()
    rect.bottom = HEIGHT + 80
    rect.left = -80
    screen.blit(background, (rect.x, rect.y))
    font = pygame.font.Font(path.join('resources', 'font.ttf'), 18)
    text_coord = 10
    for line in TEXT:
        text = font.render(line, 0, pygame.Color('white'))
        text_rect = text.get_rect()
        text_rect.top = text_coord
        text_rect.left = 10
        text_coord += text_rect.height + 10
        screen.blit(text, text_rect)
    is_running = True
    clock = pygame.time.Clock()
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
                is_running = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                is_running = False
        pygame.display.flip()
        clock.tick(FPS)
