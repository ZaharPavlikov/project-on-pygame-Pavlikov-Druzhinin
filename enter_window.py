import pygame

pygame.init()
pygame.event.set_blocked(None)
pygame.event.set_allowed((pygame.QUIT, pygame.MOUSEBUTTONDOWN))
pygame.event.clear()
size = 900, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("DOTA")

pygame.mixer.music.load('data/music/music.wav')
pygame.mixer.music.play(-1)


def init(wins, losses, kills, deaths):
    bg = pygame.image.load('data/bg.jpeg').convert()
    rect = screen.get_rect().fit(bg.get_rect())
    image = pygame.transform.smoothscale(bg.subsurface(rect), size, screen)
    font = pygame.font.Font(None, 50)
    text = font.render('WELCOME TO DOTA!', 1, '#FFD700')
    screen.blit(text, text.get_rect(center=(450, 40)))

    font = pygame.font.Font(None, 40)
    screen.blit(font.render('Statistics:', 1, '#FFD700'),
                (30, 100))
    screen.blit(font.render('Wins - ', 1, '#FFD700'),
                (70, 150))
    screen.blit(font.render(str(wins), 1, 'white'),
                (270, 150))
    screen.blit(font.render('Losses - ', 1, '#FFD700'),
                (70, 190))
    screen.blit(font.render(str(losses), 1, 'white'),
                (270, 190))

    screen.blit(font.render('Kills - ', 1, '#FFD700'),
                (70, 270))
    screen.blit(font.render(str(kills), 1, 'white'),
                (270, 270))
    screen.blit(font.render('Deaths - ', 1, '#FFD700'),
                (70, 310))
    screen.blit(font.render(str(deaths), 1, 'white'),
                (270, 310))

    button = pygame.Rect(0, 0, 300, 70)
    button.center = (450, 540)
    pygame.draw.rect(screen, '#FF00FF', button, 5)

    font = pygame.font.Font(None, 60)
    text = font.render('Play', 1, '#FF00FF')
    screen.blit(text, text.get_rect(center=button.center))

    pygame.display.update()

    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(event.pos):
                # pygame.mixer.music.load('data/music/click1.wav')
                # pygame.mixer.music.play(1)
                break


def game_setting():
    screen.fill('gray12')
    pygame.draw.line(screen, 'white', (450, 0), (450, 900))
    # pygame.draw.line(screen, 'white', (0, 34), (450, 34))
    pygame.draw.line(screen, 'white', (0, 300), (450, 300))

    font = pygame.font.Font(None, 40)
    text = font.render('Скины', 1, 'white')
    screen.blit(text, text.get_rect(center=(225, 20)))
    text = font.render('Способность', 1, 'white')
    screen.blit(text, text.get_rect(center=(675, 20)))

    skins_rect = pygame.Rect(0, 0, 205, 246)
    skins_rect.center = (337, 167)
    pygame.draw.rect(screen, 'yellow', skins_rect, 4)

    choose_skin_rect = pygame.Rect(0, 0, 205, 246)
    choose_skin_rect.center = (112, 167)
    pygame.draw.rect(screen, 'yellow', choose_skin_rect, 4)

    names = ['Монах', 'Огненный рыцарь', 'Жрица воды', 'Ветер Хашашин']
    coords = []
    font = pygame.font.Font(None, 30)
    for i in range(0, 4):
        y = 44 + i * 61.5
        coords.append(y)
        row = pygame.Rect(235, y, 205, 61.5)
        pygame.draw.rect(screen, 'yellow', row, 4)
        text = font.render(names[i], 1, (115, 207, 167))
        screen.blit(text, text.get_rect(center=row.center))

    monk_rect = pygame.Rect(235, coords[0], 205, 61.5)
    knight_rect = pygame.Rect(235, coords[1], 205, 61.5)
    pr_rect = pygame.Rect(235, coords[2], 205, 61.5)
    wind_rect = pygame.Rect(235, coords[3], 205, 61.5)

    choose = pygame.sprite.Group(
        AnimatedSprite('data/Monk_sprite/idle/idle', 6,
                       choose_skin_rect.center, 4))

    pygame.mixer.music.load('data/music/click.wav')

    pygame.display.update()
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if monk_rect.collidepoint(event.pos):
                    pygame.mixer.music.play(1)
                    choose = pygame.sprite.Group(
                        AnimatedSprite('data/Monk_sprite/idle/idle', 6,
                                       choose_skin_rect.center, 4))
                elif knight_rect.collidepoint(event.pos):
                    pygame.mixer.music.play(1)
                    choose = pygame.sprite.Group(
                        AnimatedSprite('data/Knight_sprite/idle/idle', 8,
                                       choose_skin_rect.center, 3))
                elif pr_rect.collidepoint(event.pos):
                    pygame.mixer.music.play(1)
                    choose = pygame.sprite.Group(
                        AnimatedSprite('data/Priestess_sprite/idle/other/idle', 8,
                                       choose_skin_rect.center, 3))
                elif knight_rect.collidepoint(event.pos):
                    pygame.mixer.music.play(1)
                    choose = pygame.sprite.Group(
                        AnimatedSprite('data/Knight_sprite/idle/other/idle', 8,
                                       choose_skin_rect.center, 3))

        curtain_rect = pygame.Rect(0, 0, 197, 238)
        curtain_rect.center = choose_skin_rect.center
        pygame.draw.rect(screen, 'gray12', curtain_rect)
        choose.draw(screen)
        choose.update()
        pygame.display.update()
        clock.tick(10)


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, way, frames, pos, s=1):
        super().__init__()
        self.frames = []
        self.cut_sheet(way, frames, s)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect.center = pos

    def cut_sheet(self, way, frames, s):
        for i in range(1, frames + 1):
            image = pygame.image.load(f'{way}_{i}.png').convert_alpha()
            image = pygame.transform.scale(image, (image.get_rect().w * s,
                                                   image.get_rect().h * s))
            self.rect = image.get_rect()
            self.frames.append(image)

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


init(0, 0, 0, 0)

game_setting()


# clock = pygame.time.Clock()
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     screen.fill((128, 128, 128))
#     dragon.draw(screen)
#     dragon.update()
#     pygame.display.update()
#     clock.tick(10)