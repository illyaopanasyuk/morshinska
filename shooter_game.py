#Створи власний Шутер!

from pygame import *
from random import randint



window = display.set_mode((700,500))
display.set_caption("Шутер")
background = transform.scale(
    image.load("galaxy.jpg"),
        (700,500)
    )


FPS = 60

mixer.init()
mixer.music.load("space.ogg")
fire = mixer.Sound("fire.ogg")
fires = sprite.Group()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_hei):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_hei))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_d]:
            self.rect.x += self.speed
        if key_pressed[K_a]:
            self.rect.x -= self.speed
    def fire(self):
        bullet = Bullet("bullet.png",self.rect.centerx,self.rect.top,3,20,15)
        fires.add(bullet)
    
class Enemy(GameSprite):
    direction = "down"
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 500:
            global lost
            self.rect.x = randint(0, 700)
            self.rect.y = 0
            lost = lost + 1
class Bullet(GameSprite):
    direction = 'up'
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
rocket = Player("rocket.png", 300, 380, 5, 60, 60)

kills = 0
lost = 0
font.init()
font.init()
font.init()
font1 = font.Font(None, 36)
font2 = font.Font(None, 70)
font3 = font.Font(None, 70)
win1 = font2.render("YOU LOSE(", True,(255, 215, 0))
win3 = font3.render("YOU WINER!!!", True,(255, 215, 0))
text_lose = font1.render(
    "Пропушено" + str(lost), 1, (255, 255, 255)
    )
text_win = font1.render("Збито" + str(kills), 1, (255, 255, 255))


ufo1 = Enemy("ufo.png",randint(100,200),randint(150,200),randint(1,3), 100,101)
ufo2 = Enemy("ufo.png",randint(100,200),randint(150,200),randint(1,3), 110,111)

asteroid1 = Enemy("asteroid.png",randint(80,100),randint(100,100),randint(1,2), 100,101)
asteroid2 = Enemy("asteroid.png",randint(80,100),randint(100,100),randint(1,2), 104,109)



ufo = sprite.Group()
ufo.add(ufo1)
ufo.add(ufo2)

ufo.add(asteroid1)
ufo.add(asteroid2)




clock = time.Clock()
game = True
finish = False
while game:
    window.blit(background, (0,0))
    for e in event.get():
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                rocket.fire()
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0,0))
        if sprite.spritecollide(rocket, ufo, False):
            window.blit(win1, (200, 200))
            finish = True
        sprites_list = sprite.groupcollide(fires, ufo, True, True)
        for monster in sprites_list:
            kills = kills + 1
            ufo3 = Enemy("ufo.png",randint(0,600),0,randint(1,3), 100,101)
            ufo.add(ufo3)

        if lost == 20:
            window.blit(win1,(200, 200))
            finish = True
        if kills == 30:
            window.blit(win3,(200, 200))
            finish = True
        text_win = font1.render("Збито" + str(kills), 1, (255, 255, 255))
        text_lose = font1.render("Пропушено" + str(lost), 1, (255, 255, 255))
        rocket.reset()
        rocket.update()
        fires.update()
        ufo.update()
        window.blit(text_lose,(1, 1))
        window.blit(text_win,(1, 30))
        ufo.draw(window)
        fires.draw(window)
        display.update()
        clock.tick(FPS)


