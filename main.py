from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, picture, x, y, width, height, speed):
        super().__init__()
        self.image = transform.scale(image.load(picture), (65,65))
        self.speed = speed
        self.height = height
        self.width = width
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        main_win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def updateRight(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

    def updateLeft(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

font.init()
font_UI = font.Font(None, 36)

speed_x = 3
speed_y = 3

win_width = 700
win_height = 500
main_win = display.set_mode((win_width, win_height))
display.set_caption('Пинг Понг')

ball = GameSprite("xz.png", 250, 250, 20, 20, 5)

bg = transform.scale(image.load('cat.jpg'), (win_width, win_height))

racket1 = Player("racket.png", 20, 250, 50, 50, 5)
racket2 = Player("racket.png", 640, 250, 50, 50, 5)


finish = False
run = True
while run:
    keys = key.get_pressed()
    for e in event.get():
        if e.type == QUIT or keys[K_ESCAPE]:
            run = False
    if not finish:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        main_win.blit(bg, (0,0))



        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1

        if ball.rect.x > win_width:
            finish = True
            text = font_UI.render("Left won", True, (0,0,0))
            main_win.blit(text, (50, 100))

        if ball.rect.x < 0:
            finish = True
            text = font_UI.render("Right won", True, (0,0,0))
            main_win.blit(text, (50, 100))


        ball.update()
        ball.reset()

        racket1.updateRight()
        racket1.reset()

        racket2.updateLeft()
        racket2.reset()


        display.update()
    time.delay(5)