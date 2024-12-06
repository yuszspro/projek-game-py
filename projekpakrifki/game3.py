import pygame
import random
import sys

# Inisialisasi Pygame
pygame.init()

# Dimensi layar
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Pesawat Tempur")

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Kecepatan frame
FPS = 60
clock = pygame.time.Clock()

# Font untuk skor
font = pygame.font.SysFont("Arial", 24)

# Gambar pesawat dan peluru
player_image = pygame.Surface((50, 40))
player_image.fill(GREEN)
bullet_image = pygame.Surface((10, 20))
bullet_image.fill(RED)
enemy_image = pygame.Surface((50, 40))
enemy_image.fill(BLUE)

# Kelas pemain
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 50)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()  # Ambil input di dalam metode
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed


    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        bullets.add(bullet)
        all_sprites.add(bullet)

# Kelas peluru
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = bullet_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = -7

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()

# Kelas musuh
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speed = random.randint(2, 5)

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed


    def reset_position(self):
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speed = random.randint(2, 5)

# Grup sprite
player = Player()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Tambahkan musuh ke grup
for _ in range(8):
    enemy = Enemy()
    enemies.add(enemy)
    all_sprites.add(enemy)

# Skor
score = 0

# Loop utama
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    # Input
    keys = pygame.key.get_pressed()
    player.update(keys)

    # Update objek
    all_sprites.update()

    # Tabrakan peluru dengan musuh
    hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
    for hit in hits:
        score += 10  # Tambahkan skor
        new_enemy = Enemy()
        enemies.add(new_enemy)
        all_sprites.add(new_enemy)

    # Gambar semua sprite
    all_sprites.draw(screen)

    # Tampilkan skor
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update layar
    pygame.display.flip()

# Keluar dari game
pygame.quit()
sys.exit()
