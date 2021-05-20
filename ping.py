#Создай собственный Шутер!
#Сам создавай 

from pygame import *
from random import *

speed = 10

window = display.set_mode((700, 500))
display.set_caption("ping-pong")
background = transform.scale(image.load('back.png'),(700, 500))


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def movement(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500 - 110:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def movement(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500 - 110:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        self.rect.y += self.speed
        self.rect.y += self.speed

player = Player('racket.png', 25, 25, 50, 100, 10)
player1 = Enemy('racket.png', 625, 400, 50, 100, 10)
ball = Ball('ball.png', 350, 250, 70, 70, 10)

game = True
clock = time.Clock()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire_sound.play()
                player.shoot()
    
    window.blit(background,(0,0))
    player.movement()
    player.reset()
    player1.movement()
    player1.reset()
    ball.reset()
    ball.update()
    
    display.update()
    clock.tick(60)