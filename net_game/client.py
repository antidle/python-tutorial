#!/usr/bin/env python
#coding: utf-8
import pygame
from pygame.locals import *
import os
import sys
# Echo client program
import socket
    

HOST = 'localhost'    # The remote host
PORT = 50000              # The same port as used by the server
VERSION = '  0'
ID_SIZE = 1
PLAYERS = 2

SCR_RECT = Rect(0, 0, 640, 480)

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCR_RECT.size)
    #    pygame.display.set_caption(u"Invader 02 ミサイルの発射")
    pygame.display.set_caption(u"Invader 02 missile")
    # サウンドのロード
    Shot.shot_sound = load_sound("shot.wav")
    # スプライトグループを作成して登録
    all = pygame.sprite.RenderUpdates()
    # スプライトの画像を登録
    Player.image = load_image("player.png")
    Shot.image = load_image("shot.png")
    # 自機を作成
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(VERSION)
    my_id = int(s.recv(ID_SIZE))
    print "my_id: ", my_id
    player = Player(0) # bottom
    enemy = Player(1) # top
    all.add(player)

    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        screen.fill((0, 0, 0))
        all.update()
        all.draw(screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN: 
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        #        # 押されているキーをチェック
        #        pressed_keys = pygame.key.get_pressed()
                # 押されているキーに応じてプレイヤーを移動
#                elif event.key == K_LEFT:
#                    player.move_left()
#                elif event.key == K_RIGHT:
#                    player.move_right()
#                # ミサイルの発射
#                elif event.key == K_SPACE:
#                    shot = player.shot()
#                    if shot != None:
#                        all.add(shot)
        print 'befoer send'                
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            s.sendall('l')
        elif pressed_keys[K_RIGHT]:
            s.sendall('r')
        elif pressed_keys[K_SPACE]:
            s.sendall('s')
        else:
            s.sendall('e')
        print 'sent'
            
        data = str(s.recv(2))
#        data = ''
#        s.recv_into(data, 2)
#        data = str(data)
        if len(data) < 2:
            print 'error'
            sys.exit
        print 'recv', data;
        
#        if my_id == 0:
#            my_action = data[0]
#            enemy_action = data[1]
#        if my_id == 1:
#            my_action = data[1]
#            enemy_action = data[0]
#
#        if my_action == 'l':
#            player.move_left()
#        elif my_action == 'r':
#            player.move_right()
#        elif my_action == 's':
#            # ミサイルの発射
#            shot = player.shot()
#            if shot != None:
#                all.add(shot)
#
#        if enemy_action == 'l':
#            enemy.move_left()
#        elif enemy_action == 'r':
#            enemy.move_right()
#        elif enemy_action == 's':
#            # ミサイルの発射
#            shot = enemy.shot()
#            if shot != None:
#                all.add(shot)
        print 'loop end'

class Player(pygame.sprite.Sprite):
    """自機"""
    speed = 5  # 移動速度
    reload_time = 15  # リロード時間
    def __init__(self, position):
        # imageとcontainersはmain()でセット
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
        self.position = position
        if position == 0:
            self.rect.bottom = SCR_RECT.bottom  # プレイヤーが画面の一番下
        else:
            self.rect.bottom = SCR_RECT.top  # プレイヤーが画面の一番下
        self.reload_timer = 0
    def update(self):
        pass
    def move_left(self):
        self.rect.move_ip(-self.speed, 0)
        self.rect.clamp_ip(SCR_RECT)
    def move_right(self):
        self.rect.move_ip(self.speed, 0)
        self.rect.clamp_ip(SCR_RECT)

    def shot(self):
        # リロード時間が0になるまで再発射できない
        if self.reload_timer > 0:
            # リロード中
            self.reload_timer -= 1
            return None
        else:
            # 発射！！！
            if self.position == 0:
                shot = Shot(self.rect.center, -9)  # 作成すると同時にallに追加される
            if self.position == 1:
                shot = Shot(self.rect.center, 9)  # 作成すると同時にallに追加される
            self.reload_timer = self.reload_time
            return shot

class Shot(pygame.sprite.Sprite):
    """プレイヤーが発射するミサイル"""
    def __init__(self, pos, speed = -9):
        # imageとcontainersはmain()でセット
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
        self.rect.center = pos  # 中心座標をposに
        self.speed = speed
        Shot.shot_sound.play()
    def update(self):
        self.rect.move_ip(0, self.speed)  # 上へ移動
        if self.rect.top < 0:  # 上端に達したら除去
            self.kill()

def load_image(filename, colorkey=None):
    """画像をロードして画像と矩形を返す"""
    filename = os.path.join("data", filename)
    try:
        image = pygame.image.load(filename)
    except pygame.error, message:
        print "Cannot load image:", filename
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image

def load_sound(filename):
    filename = os.path.join("data", filename)
    return pygame.mixer.Sound(filename)

if __name__ == "__main__":
    main()
