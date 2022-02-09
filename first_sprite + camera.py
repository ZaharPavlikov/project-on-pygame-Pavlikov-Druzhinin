import pygame
import random
import time
pygame.init()
pygame.event.set_blocked(None)
pygame.event.set_allowed((pygame.QUIT, pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN))
pygame.event.clear()
size = w,h = 900, 600
screen = pygame.display.set_mode(size)


class Map(pygame.sprite.Sprite):
    mapa = pygame.image.load("data/bgr_fin.png").convert()
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


class Enemy(pygame.sprite.Sprite):
    sheet1 = pygame.image.load("data/stay.png")
    sheet2 = pygame.image.load("data/dei.png")
    sheet3 = pygame.image.load("data/water_att.png")
    sheet3_r = pygame.transform.flip(sheet3, 1, 0)
    sheet4 = pygame.image.load("data/water_run.png")
    sheet4_r = pygame.transform.flip(sheet4, 1, 0)
    def __init__(self, group):
        super().__init__(group)
        self.sheet = self.sheet1
        self.frames = []
        self.cut_sheet(self.sheet, 8, 1)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(224, 112)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(1100, 550, sheet.get_width() // columns, 
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self, x1, y1, val=2):
        old = self.rect
        if val == 1:
            old = self.rect
            self.sheet = self.sheet2
            self.frames = []
            self.cut_sheet(self.sheet, 16, 1)
            self.rect = old
        if val == 3:
            if ass.rect.x > self.rect.center[0]:
                self.sheet = self.sheet4
                self.frames = []
                self.cut_sheet(self.sheet, 8, 1)
                self.rect = old
            elif ass.rect.x <  self.rect.center[0]:
                self.sheet = self.sheet4_r
                self.frames = []
                self.cut_sheet(self.sheet, 8, 1)
                self.rect = old
        if val == 2:
            old = self.rect
            self.sheet = self.sheet1
            self.frames = []
            self.cut_sheet(self.sheet, 8, 1)
            self.rect = old
            self.rect.x = x1
            self.rect.y = y1
        if val == 4:
            if ass.rect.center[0] > self.rect.center[0]:
                self.sheet = self.sheet3
                self.frames = []
                self.cut_sheet(self.sheet, 7, 1)
                self.rect = old
            elif ass.rect.center[0] <  self.rect.center[0]:
                self.sheet = self.sheet3_r
                self.frames = []
                self.cut_sheet(self.sheet, 7, 1)
                self.rect = old
            

class AnimatedSprite(pygame.sprite.Sprite):
    sheet1 = pygame.image.load("data/ass_ran.png")
    sheet2 = pygame.transform.flip(sheet1, 1, 0)
    sheet3 = pygame.image.load("data/pokoi.png")
    q_ab = pygame.image.load("data/Q.png")
    w_ab = pygame.image.load("data/W.png")
    r_ab = pygame.image.load("data/R.png")
    q_ab2 = pygame.transform.flip(q_ab, 1, 0)
    w_ab2 = pygame.transform.flip(w_ab, 1, 0)
    r_ab2 = pygame.transform.flip(r_ab, 1, 0)
    att = pygame.image.load("data/att.png")
    att2 = pygame.transform.flip(att, 1, 0)
    def __init__(self, group):
        super().__init__(group)
        self.sheet = self.sheet1
        self.frames = []
        self.cut_sheet(self.sheet, 8, 1)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(224, 112)
        
    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(-300, 550, sheet.get_width() // columns, 
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self, x1, y1, act=0):
        old = self.rect
        if act == 4:
            if x1 > self.rect.center[0]:
                self.sheet = self.att
                self.frames = []
                self.cut_sheet(self.sheet, 8, 1)
                self.rect = old
            elif x1 <  self.rect.center[0]:
                self.sheet = self.att2
                self.frames = []
                self.cut_sheet(self.sheet, 8, 1)
                self.rect = old
        elif act == 1:
            if x1 > self.rect.center[0]:
                self.sheet = self.q_ab
                self.frames = []
                self.cut_sheet(self.sheet, 8, 1)
                self.rect = old
            elif x1 <  self.rect.center[0]:
                self.sheet = self.q_ab2
                self.frames = []
                self.cut_sheet(self.sheet, 8, 1)
                self.rect = old
        elif act == 2:
            if x1 > self.rect.center[0]:
                self.sheet = self.w_ab
                self.frames = []
                self.cut_sheet(self.sheet, 26, 1)
                self.rect = old
            elif x1 <  self.rect.center[0]:
                self.sheet = self.w_ab2
                self.frames = []
                self.cut_sheet(self.sheet, 26, 1)
                self.rect = old
        elif act == 3:
            if x1 > self.rect.center[0]:
                self.sheet = self.r_ab
                self.frames = []
                self.cut_sheet(self.sheet, 30, 1)
                self.rect = old
            elif x1 <  self.rect.center[0]:
                self.sheet = self.r_ab2
                self.frames = []
                self.cut_sheet(self.sheet, 30, 1)
                self.rect = old
        elif x1 > self.rect.center[0]:
            self.sheet = self.sheet1
            self.frames = []
            self.cut_sheet(self.sheet, 8, 1)
            self.rect = old
        elif x1 <  self.rect.center[0]:
            self.sheet = self.sheet2
            self.frames = []
            self.cut_sheet(self.sheet, 8, 1)
            self.rect = old
        elif x1 == self.rect.center[0] and y1 == self.rect.center[1]:
            self.sheet = self.sheet3
            self.frames = []
            self.cut_sheet(self.sheet, 8, 1)
            self.rect = old


class Hp(pygame.sprite.Sprite):
    hp = pygame.image.load("data/hp.png").convert()
    hp1 = pygame.image.load("data/hp1.png").convert()
    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = self.hp
        self.rect = self.image.get_rect(x = x, y = y)

    def update(self, x1=0, y1=0, val=1):
        global n, x_hp, xx
        if n == 0 and val == 2:
            xx = x1
            n += 1
        if val == 1:
            if hp_die // 10 <= hp_die - hp_now:
                if self.rect.x == x_hp:
                    self.image = Hp.hp1
        elif val == 2:
            self.rect.x = xx
            self.rect.y = y1 - 40
            self.image = Hp.hp
            xx += 7
        else:
            self.rect.x += x1
            self.rect.y += y1
        
            
camera = Camera()
dragon = pygame.sprite.Group()
HP = pygame.sprite.Group()
mapa = Map(dragon)
ass =  AnimatedSprite(dragon)
enemy = Enemy(dragon)
x_hp = enemy.rect.center[0] - 40
y = enemy.rect.center[1]
for i in range(10):
    x_hp += 7
    dragon.add(Hp(HP, x_hp, y))
dragon.draw(screen)
pygame.display.update()
clock = pygame.time.Clock()
draw =False
stay = True
running = True
cam = False
Q = False
W = False
R = False
Die = False
check_attack_q = False
hp_die = 10
count_q = 0
count_w = 0
count_r = 0
xx = 0
att_count = 0
enemy_att_count = 0
enemy_stay = False
attack = False
check_attack = False
tic_q = 0
toc_q = 3
tic_w = 0
toc_w = 6
tic_r = 0
toc_r = 30
n = 0
gg = 0
count_check = 0
toc_dienemy = 0
tic_dienemy = 15
toc_attenemy = 1
tic_attenemy = 0
die = 1
count = 0
i_hp = 0
hp_die = 500
hp_now = hp_die
hero_attack = 100
hero_attab = 0
enemy_attack = False
enemy_run = True
hero_die = False
enemy_q = False
enemy_w = False
enemy_r = False
x_res_enemy = 1350
y_res_enemy = 650
enemy_attack_check = True
while running:
    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]
    if x > 890 and 10 < y < 589:
        camera.update(3, 0)
        x1 -= 3
        x_res_enemy -= 3
        x_hp -= 3
        cam = True
        for sprite in dragon:
            camera.apply(sprite)
        screen.fill(0)
        dragon.draw(screen)
        pygame.display.update()
        clock.tick(60)
    if y > 590 and 10 < x < 889:
        camera.update(0, 3)
        y1 -= 3
        y_res_enemy -= 3
        cam = True
        for sprite in dragon:
            camera.apply(sprite)
        screen.fill(0)
        dragon.draw(screen)
        pygame.display.update()
        clock.tick(60)
    if x < 10 and 10 < y < 589:
        camera.update(-3, 0)
        x1 += 3
        x_hp += 3
        x_res_enemy += 3
        cam = True
        for sprite in dragon:
            camera.apply(sprite)
        screen.fill(0)
        dragon.draw(screen)
        pygame.display.update()
        clock.tick(60)
    if y < 10 and 10 < x < 889:
        camera.update(0, -3)
        y1 += 3
        y_res_enemy += 3
        cam = True
        for sprite in dragon:
            camera.apply(sprite)
        screen.fill(0)
        dragon.draw(screen)
        pygame.display.update()
        clock.tick(60)
    if x > 890 and y > 590:
        camera.update(3, 3)
        x1 -= 3
        y1 -= 3
        x_res_enemy -= 3
        y_res_enemy -= 3
        x_hp -= 3
        cam = True
        for sprite in dragon:
            camera.apply(sprite)
        screen.fill(0)
        dragon.draw(screen)
        pygame.display.update()
        clock.tick(60)
    if y > 590 and 10 > x :
        camera.update(-3, 3)
        x1 += 3
        y1 -= 3
        x_res_enemy += 3
        y_res_enemy -= 3
        x_hp += 3
        cam = True
        for sprite in dragon:
            camera.apply(sprite)
        screen.fill(0)
        dragon.draw(screen)
        pygame.display.update()
        clock.tick(60)
    if x < 10 and 10 > y:
        camera.update(-3, -3)
        x1 += 3
        y1 += 3
        x_res_enemy += 3
        y_res_enemy += 3
        x_hp += 3
        cam = True
        for sprite in dragon:
            camera.apply(sprite)
        screen.fill(0)
        dragon.draw(screen)
        pygame.display.update()
        clock.tick(60)
    if y < 10 and x > 890:
        camera.update(3, -3)
        x1 -= 3
        y1 += 3
        x_res_enemy -= 3
        y_res_enemy += 3
        x_hp -= 3
        cam = True
        for sprite in dragon:
            camera.apply(sprite)
        screen.fill(0)
        dragon.draw(screen)
        pygame.display.update()
        clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            x1, y1 = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
            stay = False
            check_attack_q = True
            draw = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            x1, y1 = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
            stay = False
            draw = False
            W = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            x1, y1 = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
            stay = False
            draw = False
            R = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x1, y1 = event.pos[0], event.pos[1]
            if enemy.rect.center[0] - 10 <= x1 <= enemy.rect.center[0] + 10 and enemy.rect.center[1] + 14 <= y1 <= enemy.rect.center[1] + 56:
                check_attack = True
                stay = False
            else:
                draw = True
                stay = False
                x1, y1 = event.pos[0], event.pos[1]
                y1 = y1 - 28
    if cam:
        t = 80
    if 10 < x < 890 and 10 < y < 590:
        cam = False
        t = 60
    if check_attack:
        if ass.rect.center[0] < enemy.rect.center[0] and enemy.rect.collidepoint(ass.rect.center[0] - 70, ass.rect.center[1]):
            attack = True
            draw = False
            check_attack = False
        elif ass.rect.center[0] > enemy.rect.center[0] and enemy.rect.collidepoint(ass.rect.center[0] + 80, ass.rect.center[1]):
            attack = True
            draw = False
            check_attack = False
        else:
            draw = True
    if check_attack_q:
        if ass.rect.center[0] < enemy.rect.center[0] and enemy.rect.collidepoint(ass.rect.center[0] - 70, ass.rect.center[1]):
            Q = True
            draw = False
            check_attack_q = False
        elif ass.rect.center[0] > enemy.rect.center[0] and enemy.rect.collidepoint(ass.rect.center[0] + 80, ass.rect.center[1]):
            Q = True
            draw = False
            check_attack_q = False
        else:
            draw = True
    if draw:
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        ass.cur_frame = (ass.cur_frame + 1) % len(ass.frames)
        ass.image = ass.frames[ass.cur_frame]
        if x1 != ass.rect.center[0] or y1 != ass.rect.center[1]:
            if x1 > ass.rect.center[0]:
                ass.rect.x += 1
            elif x1 <  ass.rect.center[0]:
                ass.rect.x -= 1
            if y1 >  ass.rect.center[1]:
                ass.rect.y += 1
            elif y1 <  ass.rect.center[1]:
                ass.rect.y -= 1
        else:
            draw = False
            stay = True
            ass.update(x1, y1)
        ass.update(x1, y1)
        screen.fill(0)
        dragon.draw(screen)
        pygame.display.update()
        clock.tick(t)
    if stay:
        x1 = ass.rect.center[0]
        y1 = ass.rect.center[1]
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        ass.cur_frame = (ass.cur_frame + 1) % len(ass.frames)
        ass.image = ass.frames[ass.cur_frame]
        ass.update(x1, y1)
        screen.fill(0)
        dragon.draw(screen)
        pygame.display.update()
        clock.tick(t)
    if Q:
        if toc_q - tic_q >= 3:
            if count_q != 8:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                ass.cur_frame = (ass.cur_frame + 1) % len(ass.frames)
                ass.image = ass.frames[ass.cur_frame]
                ass.update(x1, y1, 1)
                screen.fill(0)
                dragon.draw(screen)
                pygame.display.update()
                clock.tick(t)
                count_q =  count_q + 1
            else:
                hero_attab = 50
                hp_now -= hero_attab
                count = hero_attab // (hp_die // 10)
                for i in range(count):
                    HP.update()
                    x_hp -= 7
                screen.fill(0)
                dragon.draw(screen)
                pygame.display.update()
                clock.tick(t)
                Q = False
                stay = True
                count_q = 0
                tic_q = time.perf_counter()
        else:
            
            stay = True
            Q = False
    if W:
        if toc_w - tic_w >= 6:
            if count_w != 26:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                ass.cur_frame = (ass.cur_frame + 1) % len(ass.frames)
                ass.image = ass.frames[ass.cur_frame]
                ass.update(x1, y1, 2)
                screen.fill(0)
                dragon.draw(screen)
                pygame.display.update()
                clock.tick(t)
                count_w += 1
            else:
                for i in range(2):
                    HP.update(x_hp)
                    x_hp -= 7
                W = False
                stay = True
                count_w = 0
                tic_w = time.perf_counter()
                
        else:
            W = False
            stay = True
    if R:
        if toc_r - tic_r >= 30:
            if count_r != 30:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                ass.cur_frame = (ass.cur_frame + 1) % len(ass.frames)
                ass.image = ass.frames[ass.cur_frame]
                ass.update(x1, y1, 3)
                screen.fill(0)
                dragon.draw(screen)
                pygame.display.update()
                clock.tick(t)
                count_r += 1
            else:
                for i in range(5):
                    HP.update(x_hp)
                    x_hp -= 7
                R = False
                stay = True
                count_r = 0
                tic_r = time.perf_counter()
        else:
            R = False
            stay = True
    if attack:
        if att_count != 8:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            ass.cur_frame = (ass.cur_frame + 1) % len(ass.frames)
            ass.image = ass.frames[ass.cur_frame]
            ass.update(x1, y1, 4)
            screen.fill(0)
            dragon.draw(screen)
            pygame.display.update()
            clock.tick(t)
            att_count += 1
        else:
            attack =False
            stay = True
            att_count = 0
            if not Die:
                print(hp_now, hp_die, count_check)
                hp_now -= hero_attack
                count_check += hero_attack / (hp_die // 10)
                count = int(count_check)
        screen.fill(0)
        dragon.draw(screen)
        pygame.display.update()
        clock.tick(t)

    if i_hp < count:
        print(i_hp, count)
        HP.update()
        x_hp -= 7
        i_hp += 1
    else:
        if i_hp == 10:
            print(1)
            i_hp = 0
            count = 0
            count_check = 0.00000000000002
            Die = True
            enemy_stay = False
            enemy_attack_check = False
            enemy_attack = False
            hp_die = 1100
            hp_now = hp_die

        
   # if hp_now <= 0:
       # Die = True
        #hp_die = 1100
        #hp_now = hp_die

    if Die:
        if die != 8:
            enemy.cur_frame = (enemy.cur_frame + 1) % len(enemy.frames)
            enemy.image = enemy.frames[enemy.cur_frame]
            enemy.update(0, 0, 1)
            screen.fill(0)
            dragon.draw(screen)
            pygame.display.update()
            die += 1
        else:
            gg = 1
            die = 0
            tic_dienemy = time.perf_counter()
            enemy_stay = False
            Die = False
            enemy_attack_check = False
            
    if not enemy_stay and gg == 1:
        if toc_dienemy - tic_dienemy >= 15:
            gg = 0
            enemy.update(x_res_enemy, y_res_enemy, 2)
            HP.update(enemy.rect.center[0] - 40, enemy.rect.center[1] + 40, 2)
            n = 0
            x_hp = enemy.rect.center[0] + 23
            if enemy.rect.center[0] != ass.rect.center[0] or enemy.rect.center[1] != ass.rect.center[1]:
                enemy_run = True
            else:
                enemy_stay = True
            enemy_attack_check = True
        
            
    if enemy_stay:
        enemy.cur_frame = (enemy.cur_frame + 1) % len(enemy.frames)
        enemy.image = enemy.frames[enemy.cur_frame]
        enemy.update(enemy.rect.x, enemy.rect.y, 2)
        screen.fill(0)
        dragon.draw(screen)
        pygame.display.update()
        clock.tick(t)

    if enemy_attack_check:
        if ass.rect.center[0] < enemy.rect.center[0] and enemy.rect.collidepoint(ass.rect.center[0] - 70, ass.rect.center[1]):
            enemy_run = False
            enemy_stay = False
            enemy_attack = True
            enemy_attack_check = False
        elif ass.rect.center[0] > enemy.rect.center[0] and enemy.rect.collidepoint(ass.rect.center[0] + 80, ass.rect.center[1]):
            enemy_run = False
            enemy_stay = False
            enemy_attack = True
            enemy_attack_check = False
        else:
            if not enemy_run:
                enemy_stay = True
            enemy_attack = False
            
    if enemy_attack:
        if toc_attenemy - tic_attenemy > 1:
            if enemy_att_count != 7:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                enemy.cur_frame = (enemy.cur_frame + 1) % len(enemy.frames)
                enemy.image = enemy.frames[enemy.cur_frame]
                enemy.update(enemy.rect.x, enemy.rect.y, 4)
                screen.fill(0)
                dragon.draw(screen)
                pygame.display.update()
                clock.tick(t)
                enemy_att_count += 1
            else:
                tic_attenemy = time.perf_counter()
                enemy_att_count = 0
                enemy_attack = False
                enemy_stay = True
    
    if toc_attenemy - tic_attenemy > 1 and gg == 0:
        enemy_attack_check = True
        

    if enemy_run:
        enemy.cur_frame = (enemy.cur_frame + 1) % len(enemy.frames)
        enemy.image = enemy.frames[enemy.cur_frame]
        if enemy.rect.center[0] != ass.rect.center[0] or enemy.rect.center[1] != ass.rect.center[1]:
            if enemy.rect.center[0] > ass.rect.center[0]:
                enemy.rect.x -= 1
                HP.update(-1, 0, 3)
                x_hp -= 1
            elif enemy.rect.center[0] <  ass.rect.center[0]:
                enemy.rect.x += 1
                HP.update(1, 0, 3)
                x_hp += 1
            if enemy.rect.center[1] >  ass.rect.center[1]:
                enemy.rect.y -= 1
                HP.update(0, -1, 3)
            elif enemy.rect.center[1] <  ass.rect.center[1]:
                enemy.rect.y += 1
                HP.update(0, 1, 3)
        else:
            enemy_run = False
            enemy_stay = True
            enemy.update(x1, y1, 3)
        enemy.update(x1, y1, 3)
        screen.fill(0)
        dragon.draw(screen)
        pygame.display.update()
        clock.tick(t)
        

    if hero_die:
        pass

    if enemy_q:
        pass

    if enemy_w:
        pass

    if enemy_r:
        pass

    toc_q = time.perf_counter()
    toc_w = time.perf_counter()
    toc_r = time.perf_counter()
    toc_dienemy = time.perf_counter()
    toc_attenemy = time.perf_counter()
