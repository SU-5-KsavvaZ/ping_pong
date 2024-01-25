from pygame import *
from time import time as timer

from random import randint

window = display.set_mode((700, 500))
display.set_caption('Pīngpāng：Jīngdiǎn de')
window.fill((232, 232, 232))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_s] and self.rect.y < 390:
            self.rect.y += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_DOWN] and self.rect.y < 390:
            self.rect.y += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

player_left = Player('racket.png', 4, 25, 200, 20, 100)
player_right = Player('racket.png', 4, 675, 200, 20, 100)
ball = GameSprite('tenis_ball.png', 1, 350, 225, 30, 30)

game = True
finish = False

clock = time.Clock()

speed_x = 1
speed_y = randint(-3, 3)
if speed_y == 0:
    speed_y=1

font.init()
font2 = font.SysFont('Arial', 80)
lose = font2.render('YOU LOSE', True, (255, 50, 50))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    if finish != True:
        window.fill((232, 232, 232))
        clock.tick(165)
        player_left.update_left()
        player_right.update_right()
        ball.reset()
        player_left.reset()
        player_right.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(player_left, ball) or sprite.collide_rect(player_right, ball):
            F = randint(0,10)
            if F == 10:
                speed_y = randint(-3, 3)
                if speed_y == 0:
                    speed_y=1
                if speed_x > 0:
                    speed_x += 1
                else:
                    speed_x -= 1
            else:
                speed_x = -speed_x
        if ball.rect.y < 10 or ball.rect.y > 490:
            speed_y = -speed_y
        if ball.rect.x <10 or ball.rect.x >690:
            finish = True
    else:
        window.blit(lose, (200, 250))

