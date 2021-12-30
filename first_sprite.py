import pygame
import random
pygame.init()
pygame.event.set_blocked(None)
pygame.event.set_allowed((pygame.QUIT, pygame.MOUSEBUTTONDOWN))
pygame.event.clear()
size = w,h = 500, 500
screen = pygame.display.set_mode(size)


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

    def update(self, x1, y1):
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
            clock.tick(10)
            
dragon = pygame.sprite.Group(AnimatedSprite(pygame.transform.flip(pygame.image.load("data/ass_ran.png"), 0, 0), 8, 1, 224, 112))

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            x1, y1 = event.pos[0], event.pos[1]
            dragon.update(x1, y1)
