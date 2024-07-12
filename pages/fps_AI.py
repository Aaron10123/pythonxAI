import pygame
import sys
import random

# 初始化pygame
pygame.init()

# 設定視窗大小
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("射擊遊戲")

# 設定顏色
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 設定玩家
player = pygame.Rect(400, 550, 50, 50)

# 設定敵人
enemies = []
for i in range(10):
    enemy = pygame.Rect(random.randint(0, 750), random.randint(0, 200), 50, 50)
    enemies.append(enemy)

# 設定分數
score = 0

# 遊戲主迴圈
while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5

    for enemy in enemies:
        enemy.y += 1
        if enemy.y > 600:
            enemy.y = 0
            enemy.x = random.randint(0, 750)
            score -= 1

        if player.colliderect(enemy):
            score += 1
            enemy.y = 0
            enemy.x = random.randint(0, 750)

        pygame.draw.rect(screen, RED, enemy)

    pygame.draw.rect(screen, RED, player)

    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, RED)
    screen.blit(text, (10, 10))

    pygame.display.flip()
