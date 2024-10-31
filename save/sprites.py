import pygame as pg
from settings import *
vec = pg.math.Vector2

# ----------------------------- Player Class -----------------------------
class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        # กำหนดกลุ่มสไปร์ทที่ผู้เล่นจะถูกเพิ่มเข้าไป
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)  # เพิ่มตัว Player เข้ากลุ่มสไปร์ท
        self.game = game  # เก็บข้อมูลอ้างอิงถึงอ็อบเจกต์เกมหลัก
        self.image = game.player_img
        self.rect = self.image.get_rect()  # สร้างสี่เหลี่ยมล้อมรอบพื้นผิว
        self.vel = vec(0, 0)
        self.pos = vec(x, y) * TILESIZE

    def get_keys(self):
        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vel.x = -PLAYER_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vel.x = PLAYER_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vel.y = -PLAYER_SPEED
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vel.y = PLAYER_SPEED
        if self.vel.x != 0 and self.vel.y != 0:
            self.vel *= 0.7071

    def move(self, dx=0, dy=0):
        # ฟังก์ชันเคลื่อนที่ตามค่าที่ส่งเข้ามา ถ้าไม่ชนกับกำแพง
        if not self.collide_with_walls(dx, dy):
            self.x += dx
            self.y += dy

    def collide_with_walls(self, dir):
        if dir == "x":
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel.x > 0:
                    self.pos.x = hits[0].rect.left - self.rect.width
                if self.vel.x <0:
                    self.pos.x = hits[0].rect.right
                self.vel.x = 0
                self.rect.x = self.pos.x

        if dir == "y":
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel.y > 0:
                    self.pos.y = hits[0].rect.top - self.rect.height
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom
                self.vel.y = 0
                self.rect.y = self.pos.y

    def update(self):
        self.get_keys()
        self.pos += self.vel * self.game.dt
        # อัปเดตตำแหน่งของผู้เล่นในกริดไปยังตำแหน่งจริงในพิกเซล
        self.rect.x = self.pos.x
        self.collide_with_walls("x")
        self.rect.y = self.pos.y
        self.collide_with_walls("y")

# ------------------------------------------------------------------------

# ------------------------------ Wall Class ------------------------------
class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):

        # กำหนดกลุ่มสไปร์ทที่กำแพงจะถูกเพิ่มเข้าไป (ทั้ง all_sprites และ walls)
        self.groups = game.all_sprites, game.walls

        pg.sprite.Sprite.__init__(self, self.groups)    # เพิ่มตัว Wall เข้ากลุ่มสไปร์ท

        self.game = game    # เก็บข้อมูลอ้างอิงถึงอ็อบเจกต์เกมหลัก

        self.image = pg.Surface((TILESIZE, TILESIZE))   # สร้างพื้นผิวสี่เหลี่ยมขนาด 32 * 32 สำหรับกำแพง
        self.image.fill(GREEN)                          # และเติมสีเขียวให้กับพื้นผิวของกำแพง

        self.rect = self.image.get_rect()   # สร้างสี่เหลี่ยมล้อมรอบพื้นผิวเพื่อใช้งานหลายอย่างเช่น การตรวจจับการชนของวัตถุ

        self.x = x  # ตำแหน่ง X ของกำแพงในกริด
        self.y = y  # ตำแหน่ง Y ของกำแพงในกริด

        # อัปเดตตำแหน่งกำแพงในพิกเซลโดยคูณตำแหน่งในกริดด้วยขนาด TILESIZE
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
# ------------------------------------------------------------------------