from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y, scale_player_x, scale_player_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (scale_player_x,scale_player_y) )
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
            window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[k_UP] and self.rect.y>5:
            self.rect.y -= self.speed
        if keys [k_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[k_w] and self.rect.y>5:
            self.rect.y -= self.speed
        if keys [k_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

racket1 = Player('tennis-clipart-design-illustration-free-png.png', 30, 20, 180, 50, 150)
racket2 = Player('tennis-clipart-design-illustration-free-png.png', 520, 535, 180, 50, 150)
ball = Player('explosive-bomb-black-png.png', 200, 260, 180, 50, 50)

back = (23, 107, 99)
win_height = 500
win_width = 600
window = display.set_mode((win_width, win_height))
window.fill(back)

clock = time.Clock()
FPS = 61
finish = False
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)






