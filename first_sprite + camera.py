import pygame
import random
pygame.init()
pygame.event.set_blocked(None)
pygame.event.set_allowed((pygame.QUIT, pygame.MOUSEBUTTONDOWN))
pygame.event.clear()
size = w,h = 900, 600
screen = pygame.display.set_mode(size)


class Map(pygame.sprite.Sprite):
    mapa = pygame.image.load("data/bgr2.png").convert()
    def __init__(self, group):
        super().__init__(group)
        self.image = self.mapa
        self.rect = self.image.get_rect()

class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0
        
    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy
    
    # позиционировать камеру на объекте target
    def update(self, delta_x, delta_y):
        self.dx = 0
        self.dy = 0
        self.dx -= delta_x
        self.dy -= delta_y

class AnimatedSprite(pygame.sprite.Sprite):
    sheet1 = pygame.image.load("data/ass_ran.png")
    sheet2 = pygame.transform.flip(sheet1, 1, 0)
    def __init__(self, group):
        super().__init__(group)
        self.sheet = self.sheet1
        self.frames = []
        self.cut_sheet(self.sheet, 8, 1)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(224, 112)
        
    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns, 
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self, x1, y1):
        old = self.rect
        if x1 > self.rect.center[0]:
            self.sheet = self.sheet1
            self.frames = []
            self.cut_sheet(self.sheet, 8, 1)
            self.rect = old
        elif x1 <  self.rect.center[0]:
            self.sheet = self.sheet2
            self.frames = []
            self.cut_sheet(self.sheet, 8, 1)
            self.rect = old
        while x1 != self.rect.center[0] or y1 != self.rect.center[1]:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]
            if x1 > self.rect.center[0]:
                self.rect.x += 1
            elif x1 <  self.rect.center[0]:
                self.rect.x -= 1
            if y1 >  self.rect.center[1]:
                 self.rect.y += 1
            elif y1 <  self.rect.center[1]:
                 self.rect.y -= 1   
            screen.fill(0)
            dragon.draw(screen)
            pygame.display.update()
            clock.tick(15)

camera = Camera()           
dragon = pygame.sprite.Group()
mapa = Map(dragon)
ass =  AnimatedSprite(dragon)
dragon.draw(screen)
pygame.display.update()
clock = pygame.time.Clock()
running = True
while running:
    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]
    if x > 890 and 10 < y < 589:
        camera.update(3, 0)
        for sprite in dragon:
            camera.apply(sprite)
        screen.fill(0)
        dragon.draw(screen)
        pygame.display.update()
        clock.tick(30)
    if y > 590 and 10 < x < 889:
        camera.update(0, 3)
        for sprite in dragon:
            camera.apply(sprite)
        screen.fill(0)
        dragon.draw(screen)
        pygame.display.update()
        clock.tick(30)
    if x < 10 and 10 < y < 589:
        camera.update(-3, 0)
        for sprite in dragon:
            camera.apply(sprite)
        screen.fill(0)
        dragon.draw(screen)
        pygame.display.update()
        clock.tick(30)
    if y < 10 and 10 < x < 889:
        camera.update(0, -3)
        for sprite in dragon:
            camera.apply(sprite)
        screen.fill(0)
        dragon.draw(screen)
        pygame.display.update()
        clock.tick(30)
    if x > 890 and y > 590:
        camera.update(3, 3)
        for sprite in dragon:
            camera.apply(sprite)
        screen.fill(0)
        dragon.draw(screen)
        pygame.display.update()
        clock.tick(30)
    if y > 590 and 10 > x :
        camera.update(-3, 3)
        for sprite in dragon:
            camera.apply(sprite)
        screen.fill(0)
        dragon.draw(screen)
        pygame.display.update()
        clock.tick(30)
    if x < 10 and 10 > y:
        camera.update(-3, -3)
        for sprite in dragon:
            camera.apply(sprite)
        screen.fill(0)
        dragon.draw(screen)
        pygame.display.update()
        clock.tick(30)
    if y < 10 and x > 890:
        camera.update(3, -3)
        for sprite in dragon:
            camera.apply(sprite)
        screen.fill(0)
        dragon.draw(screen)
        pygame.display.update()
        clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            x1, y1 = event.pos[0], event.pos[1]
            dragon.update(x1, y1 - 28)
            screen.fill(0)
            dragon.draw(screen)
            dragon.update(x1, y1 - 28)
            pygame.display.update()
            clock.tick(30)
