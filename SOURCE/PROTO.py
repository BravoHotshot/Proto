# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 08:15:07 2020

@author: Shreyas
"""
"""--------------------------------------------------------INITIALISATION------------------------------------------------------"""
import sys, os
import pygame as p

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

from random import randint
try:
    file = open(resource_path("hs.txt"), "r+")
except:
    file = open(resource_path("hs.txt"), "w")
    file.close()
    file = open(resource_path("hs.txt"), "r+")
p.mixer.pre_init(44100, -16, 2, 512)
p.init()
p.display.set_caption("PROTO")
run = True
clock = p.time.Clock()
win = p.display.set_mode((700, 700))
bg = p.image.load(resource_path("Files/Sprites/Background.png"))
bgm = p.mixer.music.load(resource_path("Files/Sounds/Background.mp3"))
gover = p.mixer.Sound(resource_path("Files/Sounds/Game Over.ogg"))
die = p.mixer.Sound(resource_path("Files/Sounds/Die.ogg"))
punch = p.mixer.Sound(resource_path("Files/Sounds/Hit.ogg"))
miss = p.mixer.Sound(resource_path("Files/Sounds/Miss.ogg"))
font = p.freetype.Font(resource_path("Files/Font.ttf"), 30)
enemies_fromLeft = []
enemies_fromRight = []
enemies_fromUp = []
enemies_fromDown = []
enemies = [enemies_fromDown, enemies_fromLeft, enemies_fromRight, enemies_fromUp]
denemies_fromLeft = []
denemies_fromRight = []
denemies_fromUp = []
denemies_fromDown = []
denemies = [denemies_fromDown, denemies_fromLeft, denemies_fromRight, denemies_fromUp]
sound = True

"""-----------------------------------------------------------CLASSES----------------------------------------------------------"""
class character(object):
    def __init__(self):
        self.frame = 0
        self.w = 60
        self.h = 80
        self.x = int((700 / 2) - (self.w / 2))
        self.y = int((700 / 2) - (self.h / 2))
        self.hit = False
        self.hitc = 0
        self.hit_left = False
        self.hit_right = False
        self.hit_up = False
        self.hit_down = False
        self.r = False
        self.l = False
        self.u = False
        self.d = False
        self.left = (p.image.load(resource_path("Files/Sprites/Character L1.png")),
                     p.image.load(resource_path("Files/Sprites/Character L2.png")),
                     p.image.load(resource_path("Files/Sprites/Character L3.png")),
                     p.image.load(resource_path("Files/Sprites/Character L2.png")),
                     p.image.load(resource_path("Files/Sprites/Character LH1.png")),
                     p.image.load(resource_path("Files/Sprites/Character LH2.png")))

        self.d_left = (p.image.load(resource_path("Files/Sprites/Character L Death1.png")),
                       p.image.load(resource_path("Files/Sprites/Character L Death2.png")),
                       p.image.load(resource_path("Files/Sprites/Character L Death3.png")),
                       p.image.load(resource_path("Files/Sprites/Character L Death4.png")),
                       p.image.load(resource_path("Files/Sprites/Character L Death5.png")),
                       p.image.load(resource_path("Files/Sprites/Character L Death6.png")))

        self.right = (p.image.load(resource_path("Files/Sprites/Character R1.png")),
                      p.image.load(resource_path("Files/Sprites/Character R2.png")),
                      p.image.load(resource_path("Files/Sprites/Character R3.png")),
                      p.image.load(resource_path("Files/Sprites/Character R2.png")),
                      p.image.load(resource_path("Files/Sprites/Character RH1.png")),
                      p.image.load(resource_path("Files/Sprites/Character RH2.png")))

        self.d_right = (p.image.load(resource_path("Files/Sprites/Character R Death1.png")),
                        p.image.load(resource_path("Files/Sprites/Character R Death2.png")),
                        p.image.load(resource_path("Files/Sprites/Character R Death3.png")),
                        p.image.load(resource_path("Files/Sprites/Character R Death4.png")),
                        p.image.load(resource_path("Files/Sprites/Character R Death5.png")),
                        p.image.load(resource_path("Files/Sprites/Character R Death6.png")))

        self.down = (p.image.load(resource_path("Files/Sprites/Character D1.png")),
                     p.image.load(resource_path("Files/Sprites/Character D2.png")),
                     p.image.load(resource_path("Files/Sprites/Character D3.png")),
                     p.image.load(resource_path("Files/Sprites/Character D2.png")),
                     p.image.load(resource_path("Files/Sprites/Character DH1.png")),
                     p.image.load(resource_path("Files/Sprites/Character DH2.png")))

        self.d_down = (p.image.load(resource_path("Files/Sprites/Character D Death1.png")),
                       p.image.load(resource_path("Files/Sprites/Character D Death2.png")),
                       p.image.load(resource_path("Files/Sprites/Character D Death3.png")),
                       p.image.load(resource_path("Files/Sprites/Character D Death4.png")),
                       p.image.load(resource_path("Files/Sprites/Character D Death5.png")),
                       p.image.load(resource_path("Files/Sprites/Character D Death6.png")))

        self.up = (p.image.load(resource_path("Files/Sprites/Character U1.png")),
                   p.image.load(resource_path("Files/Sprites/Character U2.png")),
                   p.image.load(resource_path("Files/Sprites/Character U3.png")),
                   p.image.load(resource_path("Files/Sprites/Character U2.png")),
                   p.image.load(resource_path("Files/Sprites/Character UH1.png")),
                   p.image.load(resource_path("Files/Sprites/Character UH2.png")))

        self.d_up = (p.image.load(resource_path("Files/Sprites/Character U Death1.png")),
                     p.image.load(resource_path("Files/Sprites/Character U Death2.png")),
                     p.image.load(resource_path("Files/Sprites/Character U Death3.png")),
                     p.image.load(resource_path("Files/Sprites/Character U Death4.png")),
                     p.image.load(resource_path("Files/Sprites/Character U Death5.png")),
                     p.image.load(resource_path("Files/Sprites/Character U Death6.png")))

    def draw(self, win):
        if self.r:
            if self.hit_right:
                if self.frame < 2:
                    win.blit(self.right[4], (self.x, self.y))

                    self.frame += 1

                elif self.frame < 5:
                    win.blit(self.right[5], (self.x, self.y))

                    self.frame += 1

                else:
                    self.hit_right = False

                    self.frame = 0

                    win.blit(self.right[0], (self.x, self.y))

            elif self.hit:
                if self.frame != 0 and not self.hitc:
                    self.frame = 0

                if (self.frame + 1) < 24:
                    win.blit(self.d_right[self.frame//4], (self.x, self.y))

                    self.frame += 1
                    self.hitc = 1

                else:
                    self.hit = False

            else:
                if (self.frame + 1) < 24:
                    win.blit(self.right[self.frame // 6], (self.x, self.y))

                    self.frame += 1

                else:
                    self.frame = 0

                    win.blit(self.right[0], (self.x, self.y))

        elif self.l:
            if self.hit_left:
                if self.frame < 2:
                    win.blit(self.left[4], (self.x, self.y))

                    self.frame += 1

                elif self.frame < 5:
                    win.blit(self.left[5], (self.x, self.y))

                    self.frame += 1

                else:
                    self.hit_left = False

                    self.frame = 0

                    win.blit(self.left[0], (self.x, self.y))

            elif self.hit:
                if self.frame != 0 and not self.hitc:
                    self.frame = 0

                if (self.frame + 1) < 24:
                    win.blit(self.d_left[self.frame//4], (self.x, self.y))

                    self.frame += 1
                    self.hitc = 1

                else:
                    self.hit = False

            else:
                if (self.frame + 1) < 24:
                    win.blit(self.left[self.frame // 6], (self.x, self.y))

                    self.frame += 1

                else:
                    self.frame = 0

                    win.blit(self.left[0], (self.x, self.y))

        elif self.u:
            if self.hit_up:
                if self.frame < 2:
                    win.blit(self.up[4], (self.x, self.y))

                    self.frame += 1

                elif self.frame < 5:
                    win.blit(self.up[5], (self.x, self.y))

                    self.frame += 1

                else:
                    self.hit_up = False

                    self.frame = 0

                    win.blit(self.up[0], (self.x, self.y))

            elif self.hit:
                if self.frame != 0 and not self.hitc:
                    self.frame = 0

                if (self.frame + 1) < 24:
                    win.blit(self.d_up[self.frame//4], (self.x, self.y))

                    self.frame += 1
                    self.hitc = 1

                else:
                    self.hit = False

            else:
                if (self.frame + 1) < 24:
                    win.blit(self.up[self.frame // 6], (self.x, self.y))

                    self.frame += 1

                else:
                    self.frame = 0

                    win.blit(self.up[0], (self.x, self.y))

        elif self.d:
            if self.hit_down:
                if self.frame < 2:
                    win.blit(self.down[4], (self.x, self.y))

                    self.frame += 1

                elif self.frame < 5:
                    win.blit(self.down[5], (self.x, self.y))

                    self.frame += 1

                else:
                    self.hit_down = False

                    self.frame = 0

                    win.blit(self.down[0], (self.x, self.y))

            elif self.hit:
                if self.frame != 0 and not self.hitc:
                    self.frame = 0

                if (self.frame + 1) < 24:
                    win.blit(self.d_down[self.frame//4], (self.x, self.y))

                    self.frame += 1
                    self.hitc = 1

                else:
                    self.hit = False

            else:
                if (self.frame + 1) < 24:
                    win.blit(self.down[self.frame // 6], (self.x, self.y))

                    self.frame += 1

                else:
                    self.frame = 0

                    win.blit(self.down[0], (self.x, self.y))

    def hit_status(self, d):
        if d > 0:
            if d == 1:
                return self.hit_right

            else:
                return self.hit_up

        else:
            if d == (-1):
                return self.hit_left

            else:
                return self.hit_down

    def reset(self):
        self.frame = 0
        self.r = True
        self.l = False
        self.u = False
        self.d = False
        self.hit = False
        self.hitc = 0
        self.hit_right = False
        self.hit_right = False
        self.hit_up = False
        self.hit_down = False
        punch.stop()
        miss.stop()

class enemy(object):
    def __init__(self, d):
        self.fade = False
        self.frame = 0
        self.w = 60
        self.h = 80
        self.vel = 4 + (m.c ** 0.1)
        self.d = d
        self.pos_lim()
        self.go_right = (p.image.load(resource_path("Files/Sprites/Enemy R1.png")),
                         p.image.load(resource_path("Files/Sprites/Enemy R2.png")),
                         p.image.load(resource_path("Files/Sprites/Enemy R3.png")),
                         p.image.load(resource_path("Files/Sprites/Enemy R4.png")),
                         p.image.load(resource_path("Files/Sprites/Enemy KO TR.png")),
                         p.image.load(resource_path("Files/Sprites/Enemy KO BR.png")))

        self.go_rightfade = (p.image.load(resource_path("Files/Sprites/Enemy R Fade1.png")),
                             p.image.load(resource_path("Files/Sprites/Enemy R Fade2.png")),
                             p.image.load(resource_path("Files/Sprites/Enemy R Fade3.png")),
                             p.image.load(resource_path("Files/Sprites/Enemy R Fade4.png")),
                             p.image.load(resource_path("Files/Sprites/Enemy R Fade5.png")),
                             p.image.load(resource_path("Files/Sprites/Enemy R Fade6.png")))

        self.go_left = (p.image.load(resource_path("Files/Sprites/Enemy L1.png")),
                        p.image.load(resource_path("Files/Sprites/Enemy L2.png")),
                        p.image.load(resource_path("Files/Sprites/Enemy L3.png")),
                        p.image.load(resource_path("Files/Sprites/Enemy L4.png")),
                        p.image.load(resource_path("Files/Sprites/Enemy KO TL.png")),
                        p.image.load(resource_path("Files/Sprites/Enemy KO BL.png")))

        self.go_leftfade = (p.image.load(resource_path("Files/Sprites/Enemy L Fade1.png")),
                            p.image.load(resource_path("Files/Sprites/Enemy L Fade2.png")),
                            p.image.load(resource_path("Files/Sprites/Enemy L Fade3.png")),
                            p.image.load(resource_path("Files/Sprites/Enemy L Fade4.png")),
                            p.image.load(resource_path("Files/Sprites/Enemy L Fade5.png")),
                            p.image.load(resource_path("Files/Sprites/Enemy L Fade6.png")))

        self.go_up = (p.image.load(resource_path("Files/Sprites/Enemy UD1.png")),
                      p.image.load(resource_path("Files/Sprites/Enemy UD2.png")),
                      p.image.load(resource_path("Files/Sprites/Enemy UD3.png")),
                      p.image.load(resource_path("Files/Sprites/Enemy UD4.png")),
                      p.image.load(resource_path("Files/Sprites/Enemy KO TR.png")),
                      p.image.load(resource_path("Files/Sprites/Enemy KO TL.png")))

        self.go_updownfade = (p.image.load(resource_path("Files/Sprites/Enemy UD Fade1.png")),
                              p.image.load(resource_path("Files/Sprites/Enemy UD Fade2.png")),
                              p.image.load(resource_path("Files/Sprites/Enemy UD Fade3.png")),
                              p.image.load(resource_path("Files/Sprites/Enemy UD Fade4.png")),
                              p.image.load(resource_path("Files/Sprites/Enemy UD Fade5.png")),
                              p.image.load(resource_path("Files/Sprites/Enemy UD Fade6.png")))

        self.go_down = (p.image.load(resource_path("Files/Sprites/Enemy UD1.png")),
                        p.image.load(resource_path("Files/Sprites/Enemy UD2.png")),
                        p.image.load(resource_path("Files/Sprites/Enemy UD3.png")),
                        p.image.load(resource_path("Files/Sprites/Enemy UD4.png")),
                        p.image.load(resource_path("Files/Sprites/Enemy KO BR.png")),
                        p.image.load(resource_path("Files/Sprites/Enemy KO BL.png")))

    def pos_lim(self):
        if self.d > 0:
            if self.d == 1:
                self.x = 700
                self.y = int((700 / 2) - (self.h / 2))
                self.limit = int((700 / 2) + (60 / 32))
                self.hlimit = int((700 / 2) + (60 / 2))

            else:
                self.x = int((700 / 2) - (self.w / 2))
                self.y = 0 - self.h
                self.limit = int((700 / 2) - (80 / 32))
                self.hlimit = int((700 / 2) - (80 / 2))

        else:
            if self.d == (-1):
                self.x = 0 - self.w
                self.y = int((700 / 2) - (self.h / 2))
                self.limit = int((700 / 2) - (60 / 32))
                self.hlimit = int((700 / 2) - (60 / 2))

            else:
                self.x = int((700 / 2) - (self.w / 2))
                self.y = 700
                self.limit = int((700 / 2) + (80 / 32))
                self.hlimit = int((700 / 2) + (80 / 2))

    def draw(self, win):
        if not self.fade:
            self.move()

            if self.d > 0:
                if self.d == 1:
                    if (self.frame + 1) < 24:
                        win.blit(self.go_left[self.frame // 6], (self.x, self.y))

                        self.frame += 1

                    else:
                        self.frame = 0

                        win.blit(self.go_left[0], (self.x, self.y))

                else:
                    if (self.frame + 1) < 24:
                        win.blit(self.go_down[self.frame // 6], (self.x, self.y))

                        self.frame += 1

                    else:
                        self.frame = 0

                        win.blit(self.go_down[0], (self.x, self.y))

            else:
                if self.d == (-1):
                    if (self.frame + 1) < 24:
                        win.blit(self.go_right[self.frame // 6], (self.x, self.y))

                        self.frame += 1

                    else:
                        self.frame = 0

                        win.blit(self.go_right[0], (self.x, self.y))

                else:
                   if (self.frame + 1) < 24:
                        win.blit(self.go_up[self.frame // 6], (self.x, self.y))

                        self.frame += 1

                   else:
                       self.frame = 0

                       win.blit(self.go_up[0], (self.x, self.y))

        else:
            if self.d > 0:
                if self.d == 1:
                    if (self.frame + 1) < 24:
                        win.blit(self.go_leftfade[self.frame // 4], (self.x, self.y))

                        self.frame += 1

                else:
                    if (self.frame + 1) < 24:
                        win.blit(self.go_updownfade[self.frame // 4], (self.x, self.y))

                        self.frame += 1

            else:
                if self.d == (-1):
                    if (self.frame + 1) < 24:
                        win.blit(self.go_rightfade[self.frame // 4], (self.x, self.y))

                        self.frame += 1

                else:
                   if (self.frame + 1) < 24:
                        win.blit(self.go_updownfade[self.frame // 4], (self.x, self.y))

                        self.frame += 1

    def move(self):
        if self.d > 0:
            if self.d == 1:
                if self.x > self.limit:
                    self.x -= self.vel

            else:
                if (self.y + self.h) < self.limit:
                    self.y += self.vel

        else:
            if self.d == (-1):
                if (self.x + self.w) < self.limit:
                    self.x += self.vel

            else:
                if self.y > self.limit:
                    self.y -= self.vel

    def hit_r(self):
        if hero.hit_status(1) and (self.x <= self.hlimit):
            if sound:
                miss.stop()
                punch.play()

            return True

    def hit_l(self):
        if hero.hit_status(-1) and ((self.x + self.w) >= self.hlimit):
            if sound:
                miss.stop()
                punch.play()

            return True

    def hit_u(self):
        if hero.hit_status(2) and ((self.y + self.h) >= self.hlimit):
            if sound:
                miss.stop()
                punch.play()

            return True

    def hit_d(self):
        if hero.hit_status(-2) and (self.y <= self.hlimit):
            if sound:
                miss.stop()
                punch.play()

            return True

class denemy(object):
    def __init__(self, d, corner):
        self.d = d
        self.frame = 0
        self.fade = False
        self.corner = corner
        self.w = 60
        self.h = 80
        self.pos()
        self.destroy = False
        self.vel = 4 + (m.c ** 0.1)
        self.go_right = (p.image.load(resource_path("Files/Sprites/Enemy KO TR.png")),
                         p.image.load(resource_path("Files/Sprites/Enemy KO BR.png")))

        self.go_left = (p.image.load(resource_path("Files/Sprites/Enemy KO TL.png")),
                        p.image.load(resource_path("Files/Sprites/Enemy KO BL.png")))

        self.go_up = (p.image.load(resource_path("Files/Sprites/Enemy KO TR.png")),
                      p.image.load(resource_path("Files/Sprites/Enemy KO TL.png")))

        self.go_down = (p.image.load(resource_path("Files/Sprites/Enemy KO BR.png")),
                        p.image.load(resource_path("Files/Sprites/Enemy KO BL.png")))

        self.tr_fade = (p.image.load(resource_path("Files/Sprites/Enemy KO TR Fade1.png")),
                        p.image.load(resource_path("Files/Sprites/Enemy KO TR Fade2.png")),
                        p.image.load(resource_path("Files/Sprites/Enemy KO TR Fade3.png")),
                        p.image.load(resource_path("Files/Sprites/Enemy KO TR Fade4.png")),
                        p.image.load(resource_path("Files/Sprites/Enemy KO TR Fade5.png")),
                        p.image.load(resource_path("Files/Sprites/Enemy KO TR Fade6.png")))

        self.tl_fade = (p.image.load(resource_path("Files/Sprites/Enemy KO TL Fade1.png")),
                        p.image.load(resource_path("Files/Sprites/Enemy KO TL Fade2.png")),
                        p.image.load(resource_path("Files/Sprites/Enemy KO TL Fade3.png")),
                        p.image.load(resource_path("Files/Sprites/Enemy KO TL Fade4.png")),
                        p.image.load(resource_path("Files/Sprites/Enemy KO TL Fade5.png")),
                        p.image.load(resource_path("Files/Sprites/Enemy KO TL Fade6.png")))

        self.br_fade = (p.image.load(resource_path("Files/Sprites/Enemy KO BR Fade1.png")),
                        p.image.load(resource_path("Files/Sprites/Enemy KO BR Fade2.png")),
                        p.image.load(resource_path("Files/Sprites/Enemy KO BR Fade3.png")),
                        p.image.load(resource_path("Files/Sprites/Enemy KO BR Fade4.png")),
                        p.image.load(resource_path("Files/Sprites/Enemy KO BR Fade5.png")),
                        p.image.load(resource_path("Files/Sprites/Enemy KO BR Fade6.png")))

        self.bl_fade = (p.image.load(resource_path("Files/Sprites/Enemy KO BL Fade1.png")),
                        p.image.load(resource_path("Files/Sprites/Enemy KO BL Fade2.png")),
                        p.image.load(resource_path("Files/Sprites/Enemy KO BL Fade3.png")),
                        p.image.load(resource_path("Files/Sprites/Enemy KO BL Fade4.png")),
                        p.image.load(resource_path("Files/Sprites/Enemy KO BL Fade5.png")),
                        p.image.load(resource_path("Files/Sprites/Enemy KO BL Fade6.png")))

    def draw(self, win):
        if not self.fade:
            self.move()

            if self.d > 0:
                if self.d == 1:
                    if 0 < self.corner <= 50:
                        win.blit(self.go_right[0], (self.x, self.y))

                    else:
                        win.blit(self.go_right[1], (self.x, self.y))

                else:
                    if 0 < self.corner <= 50:
                        win.blit(self.go_up[0], (self.x, self.y))

                    else:
                        win.blit(self.go_up[1], (self.x, self.y))

            else:
                if self.d == -1:
                    if 0 < self.corner <= 50:
                        win.blit(self.go_left[0], (self.x, self.y))

                    else:
                        win.blit(self.go_left[1], (self.x, self.y))

                else:
                    if 0 < self.corner <= 50:
                        win.blit(self.go_down[0], (self.x, self.y))

                    else:
                        win.blit(self.go_down[1], (self.x, self.y))

        else:
            if self.d > 0:
                if self.d == 1:
                    if 0 < self.corner <= 50:
                        if (self.frame + 1) < 24:
                            win.blit(self.tr_fade[self.frame // 4], (self.x, self.y))

                            self.frame +=1

                    else:
                        if (self.frame + 1) < 24:
                            win.blit(self.br_fade[self.frame // 4], (self.x, self.y))

                            self.frame +=1

                else:
                    if 0 < self.corner <= 50:
                        if (self.frame + 1) < 24:
                            win.blit(self.tr_fade[self.frame // 4], (self.x, self.y))

                            self.frame +=1

                    else:
                        if (self.frame + 1) < 24:
                            win.blit(self.tl_fade[self.frame // 4], (self.x, self.y))

                            self.frame +=1

            else:
                if self.d == -1:
                    if 0 < self.corner <= 50:
                        if (self.frame + 1) < 24:
                            win.blit(self.tl_fade[self.frame // 4], (self.x, self.y))

                            self.frame +=1

                    else:
                        if (self.frame + 1) < 24:
                            win.blit(self.bl_fade[self.frame // 4], (self.x, self.y))

                            self.frame +=1

                else:
                    if 0 < self.corner <= 50:
                        if (self.frame + 1) < 24:
                            win.blit(self.br_fade[self.frame // 4], (self.x, self.y))

                            self.frame +=1

                    else:
                        if (self.frame + 1) < 24:
                            win.blit(self.bl_fade[self.frame // 4], (self.x, self.y))

                            self.frame +=1

    def move(self):
        if self.d > 0:
            if self.d == 1:
                if 0 < self.corner <= 50:
                    if self.x >= 700 and (self.y + self.h) <= 0:
                        self.destroy = True

                    else:
                        if self.x < 700:
                            self.x += self.vel + 2

                        if (self.y + self.h) > 0:
                            self.y -= self.vel + 2

                else:
                    if self.x >= 700 and self.y >= 700:
                        self.destroy = True

                    else:
                        if self.x < 700:
                            self.x += self.vel + 2

                        if self.y < 700:
                            self.y += self.vel + 2

            else:
                if 0 < self.corner <= 50:
                    if self.x >= 700 and (self.y + self.h) <= 0:
                        self.destory = True

                    else:
                        if self.x < 700:
                            self.x += self.vel + 2

                        if (self.y + self.h) > 0:
                            self.y -= self.vel + 2

                else:
                    if (self.x + self.w) <= 0 and (self.y + self.h) <= 0:
                        self.destroy = True

                    else:
                        if (self.x + self.w) > 0:
                            self.x -= self.vel + 2

                        if (self.y + self.h) > 0:
                            self.y -= self.vel + 2

        else:
            if self.d == -1:
                if 0 < self.corner <= 50:
                    if (self.x + self.w) <= 0 and (self.y + self.h) <= 0:
                        self.destroy = True

                    else:
                        if (self.x + self.w) > 0:
                            self.x -= self.vel + 2

                        if (self.y + self.h) > 0:
                            self.y -= self.vel + 2

                else:
                    if (self.x + self.w) <= 0 and self.y >= 700:
                        self.destroy = True

                    else:
                        if (self.x + self.w) > 0:
                            self.x -= self.vel + 2

                        if self.y < 700:
                            self.y += self.vel + 2

            else:
                if 0 < self.corner <= 50:
                    if self.x >= 700 and self.y >= 700:
                        self.destroy = True

                    else:
                        if self.x < 700:
                            self.x += self.vel + 2

                        if self.y < 700:
                            self.y += self.vel + 2

                else:
                    if (self.x + self.w) <= 0 and self.y >= 700:
                        self.destroy = True

                    else:
                        if (self.x + self.w) > 0:
                            self.x -= self.vel + 2

                        if self.y < 700:
                            self.y += self.vel + 2

    def pos(self):
        if self.d > 0:
            if self.d == 1:
                self.x = int((700 / 2) + (60 / 32))
                self.y = int((700 / 2) - (self.h / 2))

            else:
                self.x = int((700 / 2) - (self.w / 2))
                self.y = int((700 / 2) - ((80 / 32) + self.h))

        else:
            if self.d == -1:
                self.x = int((700 / 2) - ((60 / 32) + self.w))
                self.y = self.y = int((700 / 2) - (self.h / 2))

            else:
                self.x = int((700 / 2) - (self.w / 2))
                self.y = int((700 / 2) + (80 / 32))


class pause(object):
    def __init__(self):
        self.title = p.image.load(resource_path("Files/Sprites/Pause.png"))
        self.activate = False
        self.count = 0

    def draw(self, win):
        win.blit(self.title, (0, 0))

class menu(object):
    def __init__(self):
        self.title = p.image.load(resource_path("Files/Sprites/Title.png"))
        self.activate = True
        self.score = 0
        self.music = False
        self.t = 0
        self.c = 1
        self.speed = 0.5
        self.ae = True

    def draw(self, win):
        win.blit(self.title, (0, 0))
        if not self.music and sound:
            p.mixer.music.play(-1)
            self.music = True

    def reset(self):
        self.t = 0
        self.c = 1
        self.speed = 0.5

class instr(object):
    def __init__(self):
        self.title = p.image.load(resource_path("Files/Sprites/instructions.png"))
        self.activate = False
        self.count = 0

    def draw(self, win):
        win.blit(self.title, (0, 0))

class gg(object):
    def __init__(self):
        self.title = p.image.load(resource_path("Files/Sprites/game over.png"))
        self.activate = False
        self.music = False
        self.count = 0

    def draw(self, win):
        win.blit(self.title, (0,0))
        self.count = 1
        if not self.music and sound:
            gover.play()
            self.music = True

class hs(object):
    def __init__(self):
        self.high = 0
        self.counter = 0

    def read(self):
        file.seek(0, 0)
        self.high = file.read()

        if not len(str(self.high)):
            self.high = 0

    def incr(self):
        file.seek(0,0)
        file.write(f"{m.score}")
        self.counter = 1

"""---------------------------------------------------------FUNCTIONS----------------------------------------------------------"""
def update():
    win.blit(bg, (0, 0))

    if m.activate:
        gameover.music = False
        gameover.count = 0
        gover.stop()
        m.draw(win)
        hscore = font.render(f"HIGH SCORE:{highscore.high}", (0, 0, 0), size = 30)
        win.blit(hscore[0], (180, 80))
        if highscore.counter:
            highscore.counter = 0

    elif ins.activate:
        ins.draw(win)

    elif pa.activate:
        pa.draw(win)

    elif gameover.activate:
        hero.reset()
        m.ae = True

        if not highscore.counter:
            if int(m.score) > int(highscore.high):
                highscore.incr()
            oc()
            highscore.read()

        m.reset()
        score = font.render(f"SCORE:{m.score}", (0, 0, 0), size = 40)
        win.blit(score[0], (200, 410))
        gameover.draw(win)
        for e in enemies:
            e.clear()

        for de in denemies:
            de.clear()

    else:
        if gameover.count:
            m.score = 0
            gameover.count = 0

        if highscore.counter:
            highscore.counter = 0

        if int(m.score) <= int(highscore.high):
            score = font.render(f"SCORE:{m.score}", (0, 0, 0), size = 20)
            hscore = font.render(f"HIGH SCORE:{highscore.high}", (0, 0, 0), size = 20)

        else:
            score = font.render(f"SCORE:{m.score}", (0, 0, 0), size = 20)
            hscore = font.render(f"HIGH SCORE:{m.score}", (0, 0, 0), size = 20)

        win.blit(score[0], (10, 40))
        win.blit(hscore[0], (10, 10))

        hero.draw(win)

        for den in denemies:
            for de in den:
                de.draw(win)

                if de.destroy:
                    den.pop(0)

        for en in enemies:
            for e in en:
                e.draw(win)

    p.display.update()

def add_enemy():
    r = randint(0, 100)

    if 0 < r <= 25:
        di = 1
        enemies_fromRight.append(enemy(di))

    elif 25 < r <= 50:
        di = 2
        enemies_fromUp.append(enemy(di))

    elif 50 < r <= 75:
        di = -1
        enemies_fromLeft.append(enemy(di))

    elif 75 < r <= 100:
        di = -2
        enemies_fromDown.append(enemy(di))

def end():
    for en in enemies:
        for e in en:
            if e.d > 0:
                if e.d == 1:
                    if e.x <= e.limit:
                        if not hero.hitc:
                            for en in enemies:
                                for e in en:
                                    if not e.fade:
                                        m.ae = False
                                        e.frame = 0
                                        e.fade = True

                            for den in denemies:
                                for de in den:
                                    if not de.fade:
                                        de.frame = 0
                                        de.fade = True

                            hero.hit = True
                            if sound:
                                die.play()
                            m.music = False
                            p.mixer.music.pause()

                        elif not hero.hit:
                            gameover.activate = True

                else:
                    if (e.y + e.h) >= e.limit:
                        if not hero.hitc:
                            for en in enemies:
                                for e in en:
                                    if not e.fade:
                                        m.ae = False
                                        e.frame = 0
                                        e.fade = True

                            for den in denemies:
                                for de in den:
                                    if not de.fade:
                                        de.frame = 0
                                        de.fade = True

                            hero.hit = True
                            if sound:
                                die.play()
                            m.music = False
                            p.mixer.music.pause()

                        elif not hero.hit:
                            gameover.activate = True

            else:
                if e.d == (-1):
                    if (e.x + e.w) >= e.limit:
                        if not hero.hitc:
                            for en in enemies:
                                for e in en:
                                    if not e.fade:
                                        m.ae = False
                                        e.frame = 0
                                        e.fade = True

                            for den in denemies:
                                for de in den:
                                    if not de.fade:
                                        de.frame = 0
                                        de.fade = True

                            hero.hit = True
                            if sound:
                                die.play()
                            m.music = False
                            p.mixer.music.pause()

                        elif not hero.hit:
                            gameover.activate = True

                else:
                    if e.y <= e.limit:
                        if not hero.hitc:
                            for en in enemies:
                                for e in en:
                                    if not e.fade:
                                        m.ae = False
                                        e.frame = 0
                                        e.fade = True

                            for den in denemies:
                                for de in den:
                                    if not de.fade:
                                        de.frame = 0
                                        de.fade = True

                            hero.hit = True
                            if sound:
                                die.play()
                            m.music = False
                            p.mixer.music.pause()

                        elif not hero.hit:
                            gameover.activate = True

def oc():
    global file
    file.close()
    file = open(resource_path("hs.txt"), "r+")

"""---------------------------------------------------------MAIN-LOOP----------------------------------------------------------"""
hero = character()
pa = pause()
m = menu()
ins = instr()
gameover = gg()
highscore = hs()

while run:
    clock.tick(24)

    keys = p.key.get_pressed()

    for event in p.event.get():
        if event.type == p.QUIT:
            run = False

        if keys[p.K_s]:
            if sound:
                sound = False
                p.mixer.music.pause()
                gover.stop()

            else:
                sound = True
                if gameover.activate:
                    gover.play()

                else:
                    p.mixer.music.play(-1)

        if not m.activate:
            if keys[p.K_ESCAPE] and not gameover.activate:
                if not pa.count:
                    pa.activate = True
                    pa.count = 1

                elif pa.count:
                    pa.activate = False
                    pa.count = 0

            elif keys[p.K_q] and pa.activate:
                m.activate = True
                pa.activate = False

            elif keys[p.K_i] and ins.activate:
                ins.activate = False
                m.activate = True
                ins.count = 0

            elif gameover.activate and keys[p.K_RETURN]:
                gameover.activate = False
                gameover.music = False
                gover.stop()
                if sound:
                    p.mixer.music.play(-1)

            elif gameover.activate and keys[p.K_q]:
                gameover.activate = False
                m.activate = True

            else:
                if keys[p.K_LEFT] and not hero.hit:
                    hero.frame = 0
                    hero.l = True
                    hero.u = False
                    hero.d = False
                    hero.r = False
                    hero.hit_left = True

                    if len(enemies_fromLeft):
                        h = enemies_fromLeft[0].hit_l()

                        if h:
                            cor = randint(0, 100)
                            enemies_fromLeft.pop(0)
                            denemies_fromLeft.append(denemy(-1, cor))

                            m.score += 1

                        elif sound:
                            miss.play()

                    elif sound:
                        miss.play()

                if keys[p.K_RIGHT] and not hero.hit:
                    hero.frame = 0
                    hero.l = False
                    hero.u = False
                    hero.d = False
                    hero.r = True
                    hero.hit_right = True

                    if len(enemies_fromRight):
                        h = enemies_fromRight[0].hit_r()

                        if h:
                            cor = randint(0, 100)
                            enemies_fromRight.pop(0)
                            denemies_fromRight.append(denemy(1, cor))
                            m.score += 1

                        elif sound:
                            miss.play()

                    elif sound:
                        miss.play()

                if keys[p.K_UP] and not hero.hit:
                    hero.frame = 0
                    hero.l = False
                    hero.u = True
                    hero.d = False
                    hero.r = False
                    hero.hit_up = True

                    if len(enemies_fromUp):
                        h = enemies_fromUp[0].hit_u()

                        if h:
                            cor = randint(0, 100)
                            enemies_fromUp.pop(0)
                            denemies_fromUp.append(denemy(2, cor))

                            m.score += 1

                        elif sound:
                            miss.play()

                    elif sound:
                        miss.play()

                if keys[p.K_DOWN] and not hero.hit:
                    hero.frame = 0
                    hero.l = False
                    hero.u = False
                    hero.d = True
                    hero.r = False
                    hero.hit_down = True

                    if len(enemies_fromDown):
                        h = enemies_fromDown[0].hit_d()

                        if h:
                            cor = randint(0, 100)
                            enemies_fromDown.pop(0)
                            denemies_fromDown.append(denemy(-2, cor))

                            m.score += 1

                        elif sound:
                            miss.play()

                    elif sound:
                        miss.play()

        else:
            highscore.read()
            oc()
            hero.r = True
            hero.l = False
            hero.u = False
            hero.d = False
            delay = 1000
            m.c = 1
            m.speed = 0.5
            m.t = 0
            m.score = 0

            for e in enemies:
                e.clear()

            if keys[p.K_RETURN]:
                m.activate = False

            elif keys[p.K_i]:
                if not ins.count:
                    m.activate = False
                    ins.activate = True
                    ins.count = 1

            elif keys[p.K_q]:
                run = False



    if (not pa.activate) and (not m.activate) and (not gameover.activate) and (not ins.activate):
        m.c += m.speed ** (1 / 3)
        m.speed += 0.0001

        add = False

        if m.t == 0:
            if m.ae:
                add_enemy()

            m.t = 10 ** (-100)

        elif m.t < delay:
            m.t += (1 / 2) * m.c

        else:
            m.t = 0

    update()

    end()

else:
    file.close()
    p.quit()