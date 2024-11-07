import pygame as pg # pg ย่อมาจาก pygame
import sys
from os import path
# import file
from sprites import *
from settings import *
from tilemap import *

# ------------------------------------ สร้าง class Game ขึ้น ------------------------------------
class Game:
    # ------------------------------- default constructor -------------------------------
    def __init__(self):

        # เริ่มต้น pygame
        pg.init()

        # หน้าต่างแสดงผลให้มีขนาด = WIDTH, HEIGHT
        self.scr_display = pg.display.set_mode((WIDTH, HEIGHT))
        
        # ตั้งค่าชื่อของหน้าต่างเกม ซึ่งจะแสดงที่แถบด้านบนของหน้าต่าง
        pg.display.set_caption("Sweet teacher")

        # ใช้สำหรับควบคุมความเร็วในการอัปเดตและการแสดงผลของเกม
        self.clock = pg.time.Clock()

        # ใช้สำหรับการตั้งค่าการทำซ้ำของการกดปุ่มคีย์บอร์ด เมื่อผู้ใช้กดปุ่มค้างไว้
        # โปรแกรมจะรับรู้ว่าปุ่มถูกกดซ้ำตามช่วงเวลาที่กำหนด
        pg.key.set_repeat(200, 200) # (เวลารอตรวจจับกดปุ่มซ้ำหลังจากกดปุ่มค้างไว้, ตรวจจับว่ากดซ้ำเรื่อยๆในอีก...ตราบใดที่ยังกด)

        self.load_data()
    # -----------------------------------------------------------------------------------

    # Exit
    def quit(self):
        pg.quit()
        sys.exit()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, "img")
        map_folder = path.join(game_folder, "maps")
        self.map = Tiledmap(path.join(map_folder, "level1.tmx"))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()
    # method วาดตารางกริด
    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.scr_display, LIGHTGREY, (x,0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.scr_display, LIGHTGREY, (0,y), (WIDTH, y))

    # method แสดงผล
    def draw(self):
        # self.scr_display.fill("DARKGREY")
        self.scr_display.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        self.draw_grid()
        for sprite in self.all_sprites:
            self.scr_display.blit(sprite.image, self.camera.apply(sprite))
        pg.display.flip()

    # method อัพเดทตำแหน่งของสไปร์ท
    def update(self):
        self.all_sprites.update()
        self.camera.update(self.player)

    # method อีเวนท์ต่างๆ
    def events(self):

        # กดกาที่แถบด้านบนของหน้าต่างเพื่อออกเกม
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit() # เรียกใช้งาน method ออกเกม

            # เมื่อกดปุ่มอะไรบางอย่างจะเริ่มทำงาน
            if event.type == pg.KEYDOWN:

                if event.key == pg.K_ESCAPE:    # กด Esc เพื่อออกเกม
                    self.quit()                 # เรียกใช้งาน method ออกเกม

    # --------------------- สร้าง method run สำหรับรันเกม  ---------------------
    def run(self):
        
        # ตราบใดที่ self.playing = True เกมก็จะยังทำงาน
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()
    # ----------------------------------------------------------------------

    def new(self):
        # initialize all variables and do all the setup for a new game

        # สร้างกลุ่มของสไปร์ททั้งหมด จะเก็บวัตถุที่เป็นสไปร์ททั้งหมดที่เราต้องการ
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()

        #for row, tiles in enumerate(self.map.data):
        #    for col, tile in enumerate(tiles):
        #        if tile == "1":
        #            Wall(self, col, row)
        #        if tile == "P": # ตำแหน่งเกิดผู้เล่น
        #            self.player = Player(self, col, row)
        for tile_object in self.map.tmxdata.objects:
            if tile_object.name == 'players':
                self.player = Player(self, tile_object.x, tile_object.y)
            if tile_object.name == 'wall':
                Obstacle(self, tile_object.x, tile_object.y,
                         tile_object.width, tile_object.height)
        self.player = Player(self, 5, 5)
        self.camera = Camera(self.map.width, self.map.height)
# -----------------------------------------------------------------------------------------------

# ------------------ ส่วนของการรันเกม ------------------
# เช็คว่าชื่อโมดูลปัจจุบัน (__name__) มีค่าเป็น '__main__' หรือไม่
# ถ้าใช่ แสดงว่าไฟล์นี้ถูกเรียกใช้โดยตรง
if __name__ == '__main__':
    game = Game()   # สร้าง object game จาก class Game
    game.new()
    game.run()
# ----------------------------------------------------