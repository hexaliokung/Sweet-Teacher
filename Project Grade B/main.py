import pygame
pygame.init()

# ตัวแปร
X = 50
Y = 50
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SPEED = 3

# สี
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# font
custom_font = pygame.font.Font("Asset/tahoma/tahoma.ttf", 40)
message_text = custom_font.render(u"สวัสดีอาจารย์นน", True, RED)

# ขนาดของหน้าจอ
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# โหลดรูปภาพตัวละคร
CHARACTER = pygame.image.load("Asset/Picture/3.png")
# ตั้งค่าคุณสมบัติรูปตัวละคร
CHARACTER_RECT = CHARACTER.get_rect()
print(CHARACTER_RECT)
CHARACTER_RECT.centerx = SCREEN_WIDTH//2
CHARACTER_RECT.centery = SCREEN_HEIGHT//2

# โหลดรูปกล่องสีดำ
BLOCK_BLACK = pygame.image.load("Asset/Picture/2.png")
# ตั้งค่าคุณสมบัติรูปกล่องสีดำ
BLOCK_BLACK_RECT = BLOCK_BLACK.get_rect()
BLOCK_BLACK_RECT.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2-200)


# ชื่อเกม
pygame.display.set_caption("Sweet Teacher")

# เกมรัน
RUNNING = True
while RUNNING:
    # Frame rate
    CLOCK = pygame.time.Clock()
    for EVENT in pygame.event.get():
        if EVENT.type == pygame.QUIT:
            RUNNING = False
    pygame.draw.rect(SCREEN, (255,0,0), (X,Y, 60, 40))
    
    # Keyboard
    KEYS = pygame.key.get_pressed()
    if (KEYS[pygame.K_w] or KEYS[pygame.K_UP]) and CHARACTER_RECT.top > 0:
        CHARACTER_RECT.centery -= SPEED
    if (KEYS[pygame.K_s] or KEYS[pygame.K_DOWN]) and CHARACTER_RECT.bottom < SCREEN_HEIGHT:
        CHARACTER_RECT.centery += SPEED
    if (KEYS[pygame.K_a] or KEYS[pygame.K_LEFT]) and CHARACTER_RECT.left > 0:
        CHARACTER_RECT.centerx -= SPEED
    if (KEYS[pygame.K_d] or KEYS[pygame.K_RIGHT]) and CHARACTER_RECT.right < SCREEN_WIDTH:
        CHARACTER_RECT.centerx += SPEED
    
    # แสดงภาพ
    SCREEN.fill(WHITE)
    SCREEN.blit(message_text,(80, 100))
    SCREEN.blit(BLOCK_BLACK,BLOCK_BLACK_RECT)
    SCREEN.blit(CHARACTER,CHARACTER_RECT)

    # การชน
    if CHARACTER_RECT.colliderect(BLOCK_BLACK_RECT):
        print("Hit")
    pygame.display.update()
    CLOCK.tick(60)

# ปิดเกม
pygame.quit()