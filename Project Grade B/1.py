# import pygame library
import pygame
from pygame.math import Vector2 as vector
from sys import exit

import sys

# สร้างหน้าจอเกม
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Sweet Teacher")     # ชื่อเกมตรงมุม
        self.screen_w = 1280 ; self.screen_h = 720
        self.screen = pygame.display.set_mode((self.screen_w,self.screen_h))

        # frame rate
        self.clock = pygame.time.Clock()

        #สี
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN= (0, 255, 0)
        self.BLUE = (0, 0, 255)

        # ความเร็วการเคลื่อนที่ของวัตถุ
        self.speed = 5
        custom_font = pygame.font.Font("Asset/tahoma/tahoma.ttf", 40)
        self.message_text = custom_font.render(u"สวัสดีอาจารย์นน", True, self.RED)

        # โหลดรูปภาพตัวละคร
        self.character = pygame.image.load("Asset/Picture/3.png")
        # ตั้งค่าคุณสมบัติรูปตัวละคร
        self.character_rect = self.character.get_rect()
        print(self.character_rect)
        self.character_rect.centerx = self.screen_w//2
        self.character_rect.centery = self.screen_h//2

        # โหลดรูปกล่องสีดำ
        self.block_black = pygame.image.load("Asset/Picture/2.png")

        # ตั้งค่าคุณสมบัติรูปกล่องสีดำ
        self.block_black_rect = self.block_black.get_rect()
        self.block_black_rect.center = (self.screen_w//2, self.screen_h//2-200)

        self.screen.fill(self.WHITE)
    def run(self):
        while True:
            for event in pygame.event.get():        # วนซ้ำลูบผ่านเหตุการณ์(ตัวแปร event) ที่เกิดขึ้นในโปรแกรม
                if event.type == pygame.QUIT:       # เมื่อกด x มุมขวาบนเกมจะปิด
                    pygame.quit()
                    sys.exit()
            
                # mouse
                #if event.type == pygame.MOUSEBUTTONDOWN:
                #    mouse_x = event.pos[0]
                #    mouse_y = event.pos[1]
                #    print(mouse_x, mouse_y)
                #    self.character_rect.centerx = mouse_x
                #    self.character_rect.centery = mouse_y
            # การชน
            if self.character_rect.colliderect(self.block_black_rect):
                print("Hit")
            # keyboard
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w] and self.character_rect.top > 0:
                self.character_rect.centery -= self.speed
            if keys[pygame.K_s] and self.character_rect.bottom < self.screen_h:
                self.character_rect.centery += self.speed
            if keys[pygame.K_a] and self.character_rect.left > 0:
                self.character_rect.centerx -= self.speed
            if keys[pygame.K_d] and self.character_rect.right < self.screen_w:
                self.character_rect.centerx += self.speed
            
            # แสดงภาพ
            self.screen.fill(self.WHITE)
            self.screen.blit(self.message_text,(80, 100))
            self.screen.blit(self.block_black,self.block_black_rect)
            self.screen.blit(self.character,self.character_rect)

            # แสดงขอบเขตการชน
            pygame.draw.rect(self.screen, self.GREEN, self.character_rect, 1)

            pygame.display.update()                 # อัพเดทจอแสดงผล
            self.clock.tick(60)                     # Frame rate

# เริ่มเกม
game = Game()
game.run()