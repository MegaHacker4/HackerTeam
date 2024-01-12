#Создай собственный Шутер!
from random import *
from pygame import *
import time as time2

propusk = 0
health = 3
level = 1
pula = 0
bullets = sprite.Group()
class GameSprite(sprite.Sprite):
    def __init__(self,im,speed,x,y,w,h):
        super().__init__()
        self.image = transform.scale(image.load(im),(w,h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(sprite.Sprite):
    def __init__(self,im,speed,x,y,w,h):
        super().__init__()
        self.image = transform.scale(image.load(im),(w,h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 670:
            self.rect.x += self.speed
    def fire(self):
        keys_pressed = key.get_pressed()
        global pula
        global level
        global health
        if keys_pressed[K_SPACE]:
            if pula >= 5:
                global bullets
                sprite_center_x = self.rect.centerx 
                sprite_top = self.rect.top
                bullets.add(bullet('bullet.png',10,sprite_center_x,sprite_top,10,50))
                pula = 0
        if level >= 3:
            health = 999999
            if keys_pressed[K_SPACE]:
                if pula == 1:
                    sprite_center_x = self.rect.centerx 
                    sprite_top = self.rect.top
                    bullets.add(bullet('bullet.png',10,sprite_center_x,sprite_top,10,50))
                    pula = 0
class bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Bot(sprite.Sprite):
    def __init__(self,im,w,h):
        super().__init__()
        self.speed = randint(1,2)
        self.y = 0
        self.image = transform.scale(image.load(im),(w,h))
        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = randint(40,660)
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 600:
            self.reset2()
            global propusk
            propusk += 1
            global text_lose
            text_lose = font1.render('Пропущено:'+str(propusk),True,(255,255,255))
    def reset2(self):
        self.speed = randint(1,2)
        self.rect.y = 0
        self.rect.x = randint(40,660)
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    def reset3(self):
        self.speed = randint(3,4)
        self.rect.y = 0
        self.rect.x = randint(40,660)
player = Player('rocket.png',7,325,420,80,80)
bot1 = Bot('asteroid.png',50,50)
bot2 = Bot('asteroid.png',50,50)
bot3 = Bot('asteroid.png',50,50)
bot4 = Bot('asteroid.png',50,50)
bot5 = Bot('asteroid.png',50,50)
mixer.init()
font.init()
font1 = font.SysFont('Arial',40)
text_lose = font1.render('Пропущено:'+str(propusk),True,(255,255,255))
mixer.music.load('space.ogg')
text_level = font1.render('Уровень:'+str(level),True,(255,255,255))
mixer.music.play()
clock = time.Clock()
window = display.set_mode((700,500))
display.set_caption('Шутер')
background = transform.scale(image.load('galaxy.jpg'),(700,500))
FPS = 60
game = True
bots = sprite.Group()
bots.add(bot1)
bots.add(bot2)
bots.add(bot3)
bots.add(bot4)
bots.add(bot5)
bots.add(Bot('asteroid.png',50,50))
bots.add(Bot('asteroid.png',50,50))
bots.add(Bot('asteroid.png',50,50))
bots.add(Bot('asteroid.png',50,50))
bots.add(Bot('asteroid.png',50,50))
bots.add(Bot('asteroid.png',50,50))
bots.add(Bot('asteroid.png',50,50))
bots.add(Bot('asteroid.png',50,50))
bots.add(Bot('asteroid.png',50,50))
bots.add(Bot('asteroid.png',50,50))
bots.add(Bot('asteroid.png',50,50))
target = 0
text_lose2 = font1.render('ВЫ ПРОИГРАЛИ!',True,(255,255,255))
text_health = font1.render('HP:'+str(health),True,(255,255,255))
text_win = font1.render('Cчет:'+str(target),True,(255,255,255))
while game:
    if pula != 20:
        pula += 1
    text_level = font1.render('Уровень:'+str(level),True,(255,255,255))
    text_health = font1.render('HP:'+str(health),True,(255,255,255))
    sprite_list = sprite.groupcollide(bots,bullets,False,True)
    for i in sprite_list:
        i.reset2()
        target += 1
        text_win = font1.render('Cчет:'+str(target),True,(255,255,255))
    bullets.update()
    sprite_collide = sprite.spritecollide(player,bots,True)
    for i in sprite_collide:
        if health > 0:
            health -= 1
        else:
            text_lose2 = font1.render('ВЫ ПРОИГРАЛИ!',True,(255,255,255))
            window.blit(text_lose2,(250,250))
            display.update()
            time2.sleep(5)
            game = False
    if target == 10:
        bot10=Bot('ufo.png',50,50)
        bots.add(bot10)
        bot10.reset3()
        target = 11
    if target == 20:
        bot20=Bot('ufo.png',50,50)
        bots.add(bot20)
        bot20.reset3()
        target = 21
    if target == 30:
        bot30=Bot('ufo.png',50,50)
        bots.add(bot30)
        bot30.reset3()
        target = 31
    if target == 40:
        bot40=Bot('ufo.png',50,50)
        bots.add(bot40)
        bot40.reset3()
        target = 41
    if target == 50:
        bot50=Bot('ufo.png',50,50)
        bots.add(bot50)
        bot50.reset3()
        target = 51
    if target == 60:
        bot60=Bot('ufo.png',50,50)
        bots.add(bot60)
        bot60.reset3()
        target = 61
    if target == 70:
        bot70=Bot('ufo.png',50,50)
        bots.add(bot70)
        bot70.reset3()
        target = 71
    if target == 80:
        bot80=Bot('ufo.png',50,50)
        bots.add(bot80)
        bot80.reset3()
        target = 81
    if target == 90:
        bot90=Bot('ufo.png',50,50)
        bots.add(bot90)
        bot90.reset3()
        target = 91
    if target >= 100:
        win = font1.render('ВЫ ВЫЙГРАЛИ!!!',True,(0,255,0))
        window.blit(win,(250,250))
        display.update()
        time2.sleep(5)
        target = 0
        level += 1
    if propusk >= 1000:
        text_lose2 = font1.render('ВЫ ПРОИГРАЛИ!',True,(255,255,255))
        window.blit(text_lose2,(250,250))
        display.update()
        time2.sleep(5)
        game = False
    player.fire()
    bots.draw(window)
    bots.update()
    bullets.draw(window)
    player.update()
    player.reset()
    clock.tick(FPS)
    display.update()
    text_level = font1.render('Уровень:'+str(level),True,(255,255,255))
    window.blit(background,(0,0))
    window.blit(text_lose,(0,0))
    window.blit(text_win,(0,50))
    window.blit(text_health,(0,100))
    window.blit(text_level,(0,150))
    for e in event.get():
        if e.type == QUIT:
            game = False