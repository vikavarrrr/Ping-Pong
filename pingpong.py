from pygame import *

class GameSprite(sprite.Sprite):
        def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
            super().__init__()
            self.image = transform.scale(image.load(player_image), (size_x, size_y))
            self.speed = player_speed
            self.rect = self.image.get_rect()
            self.rect.x = player_x
            self.rect.y = player_y
        def reset(self):
            window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 135:
            self.rect.y += self.speed
    def update_1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 135:
            self.rect.y += self.speed

win_width = 600
win_height = 500
player_img = 'player.png'
ball_img = 'ball.png'
speed_x = 3
speed_y = 3

window = display.set_mode((win_width, win_height))
display.set_caption('Ping Pong')
background = transform.scale(image.load('background.jpg'), (win_width, win_height))

player1 = Player(player_img, 5, 5, 25, 130, 5)
player2 = Player(player_img, 570, 365, 25, 130, 5)
ball = GameSprite(ball_img, 200, 200, 50, 50, 4)

clock = time.Clock()
FPS = 60
game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background, (0,0))
        player1.update_r()
        player2.update_1()

        player1.reset()
        player2.reset()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(ball, player1) or sprite.collide_rect(ball, player2):
            speed_x *= -1

        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

        
        
        ball.reset()

    display.update()
    clock.tick(FPS)




