#Создай собственный Шутер!
#Сам создавай 

from pygame import *
from random import *

window = display.set_mode((700, 500))
display.set_caption("ping-pong")
background = transform.scale(image.load('back.png'),(700, 500))


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, speed_x, speed_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def movement(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed_y
        if keys[K_DOWN] and self.rect.y < 500 - 110:
            self.rect.y += self.speed_y

'''class Enemy(GameSprite):
    def movement(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed_y
        if keys[K_s] and self.rect.y < 500 - 110:
            self.rect.y += self.speed_y'''

class Ball(GameSprite):
    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x 
        
        

player = Player('racket.png', 25, 25, 50, 100, 10, 10)
player1 = Player('racket.png', 625, 400, 50, 100, 10, 10)
ball = Ball('ball.png', 350, 250, 70, 70, 5, 5)

font.init()
font = font.Font(None, 35)
lose1 = font.render('Первый игрок проиграл!', True, (180, 0, 0))
lose2 = font.render('Второй игрок проиграл!', True, (180, 0, 0))

game = True
clock = time.Clock()
finish = False
count1 = 0
count2 = 0

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        point1 = font.render(str(count1), True, (180, 0, 0))
        point2 = font.render(str(count2), True, (180, 0, 0))

        if sprite.collide_rect(player, ball):
            ball.speed_x *= -1
            ball.speed_y *= 1
            count1 += 1

        if sprite.collide_rect(player1, ball):
            ball.speed_x *= -1
            ball.speed_y *= 1
            count2 += 1
        
        if ball.rect.y > 500-70 or ball.rect.y < 0:
                ball.speed_y *= -1

        if ball.rect.x > 700 or ball.rect.x < 0:
            finish = True
            count1 = 0
            count2 = 0

        window.blit(background,(0,0))
        player.movement()
        player.reset()
        #player1.movement()
        player1.reset()
        ball.reset()
        ball.update()
        player1.rect.y = ball.rect.y
        window.blit(point1, (50,100))
        window.blit(point2, (650,100))
    else:
        count1 = 0
        count2 = 0
        player = Player('racket.png', 25, 25, 50, 100, 10, 10)
        player1 = Player('racket.png', 625, 400, 50, 100, 10, 10)
        ball = Ball('ball.png', 350, 250, 70, 70, 5, 5)
        finish = False

    display.update()
    clock.tick(60)