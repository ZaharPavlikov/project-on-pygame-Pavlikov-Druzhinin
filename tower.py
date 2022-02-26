class Tower(pygame.sprite.Sprite):
    image = pygame.image.load('data/tower2.png').convert_alpha()
    image = pygame.transform.scale(image, (image.get_rect().w / 5,
                                           image.get_rect().h / 5))

    def __init__(self, group, pos):
        super().__init__(group)
        self.rect = self.image.get_rect(center=(pos))
        shoot_zone = pygame.Rect(0, 0, 20, 20)
        shoot_zone.center = self.rect.center

    def center(self):
        return self.rect.center


class Shell(pygame.sprite.Sprite):
    image = pygame.image.load('data/shell3.png').convert_alpha()
    image = pygame.transform.scale(image, (image.get_rect().w / 5,
                                           image.get_rect().h / 5))

    def __init__(self, group, start_pos):
        super().__init__(group)
        self.rect = self.image.get_rect(center=start_pos)
        self.start_pos = start_pos

    def update(self, enemy_pos):
        x, y = self.rect.x, self.rect.y
        x_en, y_en = enemy_pos
        if abs(x - x_en) > 5 and abs(y - y_en) > 5:
            if x_en > x and y_en > y:
                move = (1, 1)
            elif x_en < x and y_en > y:
                move = (-1, 1)
            elif x_en < x and y_en < y:
                move = (-1, -1)
            elif x_en > x and y_en < y:
                move = (1, -1)
            self.rect.move(x + move[0], y + move[1])
        else:
            self.rect.center = self.start_pos