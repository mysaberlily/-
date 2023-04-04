import pygame
import time

pygame.init()

# 颜色定义
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# 窗口大小
display_width = 800
display_height = 600

# 游戏窗口初始化
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('贪吃蛇')

# 时钟对象
clock = pygame.time.Clock()

# 字体对象
font = pygame.font.SysFont(None, 25)


def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width / 4, display_height / 4])


def gameLoop():
    gameExit = False
    gameOver = False

    # 蛇头位置
    lead_x = display_width / 2
    lead_y = display_height / 2

    # 蛇的速度
    lead_x_change = 0
    lead_y_change = 0

    # 初始化食物位置
    randAppleX = round(random.randrange(0, display_width - 10) / 10.0) * 10.0
    randAppleY = round(random.randrange(0, display_height - 10) / 10.0) * 10.0

    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("游戏结束，按 Q 退出，按 C 重新开始", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -10
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = 10
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -10
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = 10
                    lead_x_change = 0

        # 当蛇的位置大于窗口大小时，游戏结束
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True

        # 更新蛇头位置
        lead_x += lead_x_change
        lead_y += lead_y_change

        # 填充背景颜色
        gameDisplay.fill(white)

        # 画出食物和蛇
        pygame.draw.rect(gameDisplay, blue, [randAppleX, randAppleY, 10, 10])
        pygame.draw.rect(gameDisplay, green, [lead_x, lead_y, 10, 10])

        pygame.display.update()

        # 如果蛇头和食物碰撞，则重新定义食物的位置
        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX = round(random.randrange(0, display_width - 10) / 10.0) * 10.0
            randAppleY = round(random.randrange(0, display_height - 10) / 10.0) * 10.0

        # 定义游戏帧率
        clock.tick(30)

    # 退出 Pygame 库，清理窗口
    pygame.quit()
    quit()

# 启动游戏
gameLoop()
