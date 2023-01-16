from .load_image import *
from .constants import *
from .terminate import *


def start_screen(screen: pygame.Surface) -> None:
    INTRO_TEXT = ['Предыстория',
                  'Вы - пилот истребителя. Недавно под ваше руководство',
                  'попал новый стажер, который отрицательно относится к',
                  'насилию и к идущей войне с пришельцами. Пока вы помогали',
                  'с починкой варп-двигателя на грузовом корабле друга,',
                  'стажёр заменил лазерные установки в вашем истребителе на',
                  'экспериментальные пушки собственной разработки, которые',
                  'превращают врагов в цветы. Эти цветы устойчивы к условиям',
                  'открытого космоса и пускают корни на первой планете, куда',
                  'попадут. Подмену вы обнаружили только на задании. Ничего',
                  'не остаётся, кроме как протестировать новое оружие!',
                  'Постарайтесь набрать как можно больше очков, и при этом',
                  'не угробить единственный образец!',
                  '',
                  'Правила игры',
                  '- Управление с помощью мыши',
                  '- Превратите в цветы как можно больше врагов',
                  '- Не пропускайте врагов на базу']
    background = load_image(path.join('effects', 'start_heart.png'))
    background = pygame.transform.scale(
        background, (START_WIDTH, START_HEIGHT))

    screen.blit(background, (WIDTH // 3, HEIGHT // 4))
    font = pygame.font.Font(path.join('resources', 'font.ttf'), 18)
    text_coord = 10
    for line in INTRO_TEXT:
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
