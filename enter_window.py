import pygame
import sqlite3

pygame.init()
pygame.event.set_blocked(None)
pygame.event.set_allowed((pygame.QUIT, pygame.MOUSEBUTTONDOWN))
pygame.event.clear()
size = 900, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("DOTA")

pygame.mixer.music.load('data/music/music.wav')
pygame.mixer.music.play(-1)

button_sound1 = pygame.mixer.Sound('data/music/click1.wav')
button_sound2 = pygame.mixer.Sound('data/music/click.wav')

with sqlite3.connect('database.db') as con:
    wins, losses, kills, deaths = con.execute(
        'SELECT * FROM statistic').fetchall()[0]


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
                button_sound1.play()
                break


def game_setting():
    screen.fill('gray12')
    pygame.draw.line(screen, 'white', (450, 0), (450, 460))
    pygame.draw.line(screen, 'white', (0, 75), (900, 75))
    pygame.draw.line(screen, 'white', (0, 460), (900, 460))

    font = pygame.font.Font(None, 40)
    text = font.render('Скины', 1, 'white')
    screen.blit(text, text.get_rect(center=(225, 40)))
    text = font.render('Уровень', 1, 'white')
    screen.blit(text, text.get_rect(center=(675, 40)))

    skins_rect = pygame.Rect(0, 0, 205, 246)
    skins_rect.center = (337, 250)
    pygame.draw.rect(screen, 'yellow', skins_rect, 4)

    choose_skin_rect = pygame.Rect(0, 0, 205, 246)
    choose_skin_rect.center = (112, 250)
    curtain_rect = pygame.Rect(0, 0, 201, 242)
    curtain_rect.center = choose_skin_rect.center
    pygame.draw.rect(screen, 'yellow', choose_skin_rect, 4)

    names = ['Монах', 'Огненный рыцарь', 'Жрица воды', 'Ветер Хашашин']
    coords = []
    font = pygame.font.Font(None, 30)
    for i in range(0, 4):
        y = skins_rect.y + i * 61.5
        coords.append(y)
        row = pygame.Rect(235, y, 205, 61.5)
        pygame.draw.rect(screen, 'yellow', row, 4)
        text = font.render(names[i], 1, (115, 207, 167))
        screen.blit(text, text.get_rect(center=row.center))

    monk_rect = pygame.Rect(235, coords[0], 205, 61.5)
    knight_rect = pygame.Rect(235, coords[1], 205, 61.5)
    pr_rect = pygame.Rect(235, coords[2], 205, 61.5)
    wind_rect = pygame.Rect(235, coords[3], 205, 61.5)

    map_1 = pygame.Rect(470, 127, 410, 61.5)
    map_2 = pygame.Rect(470, 188.5, 410, 61.5)
    text1 = font.render('Уровень "easy"', 1, (115, 207, 167))
    text2 = font.render('Уровень "medium"', 1, (115, 207, 167))

    screen.blit(text1, text1.get_rect(center=map_1.center))
    screen.blit(text2, text2.get_rect(center=map_2.center))
    pygame.draw.rect(screen, 'yellow', map_1, 4)
    pygame.draw.rect(screen, 'yellow', map_2, 4)

    start_button = pygame.Rect(225, 480, 450, 100)
    font = pygame.font.Font(None, 60)
    text = font.render('В бой!', 1, '#FF00FF')
    pygame.draw.rect(screen, '#FF00FF', start_button, 4)
    screen.blit(text, text.get_rect(center=start_button.center))

    image = pygame.image.load('data/pokoi.png').convert_alpha()
    image = pygame.transform.scale(image, (image.get_rect().w * 3,
                                           image.get_rect().h * 3))
    choose_ass = pygame.sprite.Group(
        AnimatedSprite(image, 8, 1, -230, 20))

    image = pygame.image.load('data/stay.png').convert_alpha()
    image = pygame.transform.scale(image, (image.get_rect().w * 3,
                                           image.get_rect().h * 3))
    choose_water = pygame.sprite.Group(
        AnimatedSprite(image, 8, 1, -230, 20))

    image = pygame.image.load('data/stay.png').convert_alpha()
    image = pygame.transform.scale(image, (image.get_rect().w * 3,
                                           image.get_rect().h * 3))
    choose_knight = pygame.sprite.Group(
        AnimatedSprite(image, 8, 1, -230, 20))

    image = pygame.image.load('data/stay.png').convert_alpha()
    image = pygame.transform.scale(image, (image.get_rect().w * 3,
                                           image.get_rect().h * 3))
    choose_monk = pygame.sprite.Group(
        AnimatedSprite(image, 8, 1, -230, 20))

    choose = choose_ass
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if monk_rect.collidepoint(event.pos):
                    button_sound2.play()
                    choose = choose_monk

                elif knight_rect.collidepoint(event.pos):
                    button_sound2.play()
                    choose = choose_knight

                elif pr_rect.collidepoint(event.pos):
                    button_sound2.play()
                    choose = choose_water

                elif wind_rect.collidepoint(event.pos):
                    button_sound2.play()
                    choose = choose_ass

                elif map_1.collidepoint(event.pos):
                    button_sound2.play()
                elif map_2.collidepoint(event.pos):
                    button_sound2.play()
                elif start_button.collidepoint(event.pos):
                    running = False

        pygame.draw.rect(screen, 'gray12', curtain_rect)
        choose.draw(screen)
        choose.update()
        pygame.display.update()
        clock.tick(10)


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__()
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


init(wins, losses, kills, deaths)

game_setting()
