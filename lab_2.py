import random

import pygame

pygame.init()

window = pygame.display.set_mode((1366, 768))
pygame.display.set_caption("My Game")

font = pygame.font.SysFont('Arial', 18, bold=True)

walkRightNinja = [pygame.image.load('Ninja/Run__000.png'),
                  pygame.image.load('Ninja/Run__001.png'),
                  pygame.image.load('Ninja/Run__002.png'),
                  pygame.image.load('Ninja/Run__003.png'),
                  pygame.image.load('Ninja/Run__004.png'),
                  pygame.image.load('Ninja/Run__005.png'),
                  pygame.image.load('Ninja/Run__006.png'),
                  pygame.image.load('Ninja/Run__007.png'),
                  pygame.image.load('Ninja/Run__008.png'),
                  pygame.image.load('Ninja/Run__009.png')]

walkRightCop = [pygame.image.load('Cop/Run__000.png'),
                pygame.image.load('Cop/Run__001.png'),
                pygame.image.load('Cop/Run__002.png'),
                pygame.image.load('Cop/Run__003.png'),
                pygame.image.load('Cop/Run__004.png'),
                pygame.image.load('Cop/Run__005.png'),
                pygame.image.load('Cop/Run__006.png'),
                pygame.image.load('Cop/Run__007.png'),
                pygame.image.load('Cop/Run__008.png'),
                pygame.image.load('Cop/Run__009.png')]

playerStandCop = pygame.image.load('Cop/Idle__000.png')
playerStandNinja = pygame.image.load('Ninja/Idle__000.png')
Ninja_Dead = pygame.image.load('Ninja/Dead__000.png')
Cop_Dead = pygame.image.load('Cop/Dead__000.png')
bg = pygame.image.load('Img/beaches.jpg')
win = pygame.image.load('Img/win5.png')
lose = pygame.image.load('Img/lose.png')
slow = pygame.image.load('Img/Slow.png')
slow = pygame.transform.scale(slow, (85, 45))
pinguin = pygame.image.load('Img/pingvin.png')
pinguin = pygame.transform.scale(pinguin, (30, 50))
crabs = pygame.image.load('Img/crab-icon.png')
crabs = pygame.transform.scale(crabs, (40, 40))
clock = pygame.time.Clock()


class Pregradi_Crab(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = random.randint(1200, 1366)
        self.y = 600
        self.widht = 51
        self.height = 51
        self.speed_Pregradi = 5.0

        self.image = pygame.image.load('Img/crab-icon.png')
        self.image = pygame.transform.scale(self.image, (self.widht, self.height))
        self.rect = self.image.get_rect()


class Pregradi_Pingvin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = random.randint(1200, 1366)
        self.y = 600
        self.widht = 50
        self.height = 70
        self.speed_Pregradi = 5.0

        self.image = pygame.image.load('Img/pingvin.png')
        self.image = pygame.transform.scale(self.image, (self.widht, self.height))
        self.rect = self.image.get_rect()
        self.run_away = False


x_Ninja = 450
x_Cop = 50
y_Ninja = 600
y_Cop = 600
widht = 72
height = 136
speed_Ninja = 1
speed_Cop = 1.5

isJump_Сop = False
jumpCount_Cop = 10
isJump_Ninja = False
jumpCount_Ninja = 10

right_Cop = False
right_Ninja = True
left_Pingvin = True

animCount_Cop = 0
animCount_Ninjs = 0

mas_pregrad_crab = []
mas_pregrad_pingvin = []

counter_for_Cop = 0
counter_for_Ninja = 0
counter_for_Crab = 0
counter_for_Pingvin = 0

you_win = False
you_lose = False


def drawWindow():
    global animCount_Cop, animCount_Ninjs, counter_for_Crab, counter_for_Pingvin, counter_for_Cop, \
        counter_for_Ninja, speed_Cop, speed_Ninja, right_Cop, right_Ninja, left_Pingvin, x_Ninja, y_Ninja, \
        x_Cop, y_Cop, isJump_Ninja, jumpCount_Ninja, widht, you_win, you_lose
    window.blit(bg, (0, 0))

    counter_for_Crab += 1
    counter_for_Pingvin += 1

    if counter_for_Crab == 90:
        crab = Pregradi_Crab()
        mas_pregrad_crab.append(crab)
        counter_for_Crab = 0

    if counter_for_Pingvin == 115:
        pingvin = Pregradi_Pingvin()
        mas_pregrad_pingvin.append(pingvin)
        counter_for_Pingvin = 0

    for pregrada_crab in mas_pregrad_crab:
        window.blit(pregrada_crab.image, (pregrada_crab.x, pregrada_crab.y + 80))
        pregrada_crab.x -= pregrada_crab.speed_Pregradi
        if pregrada_crab.x < 10 or pregrada_crab.x > 1366:
            mas_pregrad_crab.pop(mas_pregrad_crab.index(pregrada_crab))

        if (x_Cop + 15) // 10 == pregrada_crab.x // 10 and y_Cop // 10 == pregrada_crab.y // 10:
            counter_for_Cop = 100
            speed_Cop = 0
            window.blit(playerStandCop, (x_Cop, y_Cop))

        if counter_for_Cop <= 100:
            counter_for_Cop -= 1

        if counter_for_Cop == 0:
            speed_Cop = 1.5

        if counter_for_Cop >= 0 and counter_for_Cop <= 100:
            window.blit(slow, (x_Cop, y_Cop - 50))

    # print(x_Cop, x_Cop // 2)
    for pregrada_pingvin in mas_pregrad_pingvin:
        window.blit(pregrada_pingvin.image, (pregrada_pingvin.x, pregrada_pingvin.y + 60))

        if pregrada_pingvin.x < 10 or pregrada_pingvin.x > 1366:
            mas_pregrad_pingvin.pop(mas_pregrad_pingvin.index(pregrada_pingvin))

        if x_Cop // 10 == pregrada_pingvin.x // 10 and y_Cop // 10 == pregrada_pingvin.y // 10:
            pregrada_pingvin.run_away = True

        if not pregrada_pingvin.run_away:
            pregrada_pingvin.x -= pregrada_pingvin.speed_Pregradi
            if pregrada_pingvin.x // 10 == (x_Ninja) // 10:
                if pregrada_pingvin.y // 10 == y_Ninja // 10:
                    speed_Ninja = 0.5
                    counter_for_Ninja = 100

        else:
            pregrada_pingvin.x += pregrada_pingvin.speed_Pregradi
            # if pregrada_pingvin.x // 10 == (x_Ninja - 102) // 10:
            #     if pregrada_pingvin.y // 10 == y_Ninja // 10:
            #         speed_Ninja = 0.5
            #         counter_for_Ninja = 100

        # if ((x_Ninja)//2  == (pregrada_pingvin.x )//2) and (y_Ninja//2  == pregrada_pingvin.y//2 ):
        #     if pregrada_pingvin.x > x_Ninja and pregrada_pingvin.x < x_Ninja + 10:

        # if (pregrada_pingvin.x + 10) // 10 == x_Ninja // 10:
        #     if pregrada_pingvin.y == y_Ninja:
        #         speed_Ninja = 0.5
        #         counter_for_Ninja = 100

        if counter_for_Ninja <= 100:
            counter_for_Ninja -= 1

        if counter_for_Ninja == 0:
            speed_Ninja = 1

        if 0 <= counter_for_Ninja <= 100:
            window.blit(slow, (x_Ninja, y_Ninja - 50))

        # def rand():
        x = random.randint(0, 100)
        if not isJump_Ninja:
            if not pregrada_pingvin.run_away:
                if pregrada_pingvin.x // 10 == (x_Ninja + 15) // 10:
                    if pregrada_pingvin.y // 10 == y_Ninja // 10:
                        x = random.randint(0, 100)
                        if x >= 0 and x <= 75:
                            isJump_Ninja = True
                        else:
                            isJump_Ninja = False
            else:
                if pregrada_pingvin.x // 10 == (x_Ninja - 5) // 10:
                    if pregrada_pingvin.y // 10 == y_Ninja // 10:
                        x = random.randint(0, 100)
                        if x >= 0 and x <= 75:
                            isJump_Ninja = True
                        else:
                            isJump_Ninja = False
            # if (x_Ninja) // 10 == pregrada_pingvin.x // 10:
            # if pregrada_pingvin.x > x_Ninja and pregrada_pingvin.x < x_Ninja + 10:
            #     if pregrada_pingvin.y == y_Ninja:

            # if pregrada_pingvin.x > x_Ninja:
            # if 0 <= (pregrada_pingvin.x - x_Ninja + 36) < 10:

            # if (pregrada_pingvin.x) // 10 == (x_Ninja + 15) // 10:
            #     if pregrada_pingvin.y //10 == y_Ninja//10:
            #         if x >= 0 and x <= 75:
            #             isJump_Ninja = True
            #         else:
            #             isJump_Ninja = False

            # elif pregrada_pingvin.x < x_Ninja:
            #     if (pregrada_pingvin.x) // 10 == (x_Ninja-36) // 10:
            #         print(4)
            #         if pregrada_pingvin.y == y_Ninja:
            #             print(5)
            #             if x >= 0 and x <= 50:
            #                 isJump_Ninja = True
            #             else:
            #                 isJump_Ninja = False
        else:
            if jumpCount_Ninja >= -10:
                if jumpCount_Ninja < 0:
                    x_Ninja += speed_Ninja
                    y_Ninja += (jumpCount_Ninja ** 2) / 2
                else:
                    y_Ninja -= (jumpCount_Ninja ** 2) / 2
                jumpCount_Ninja -= 1
            else:
                isJump_Ninja = False
                jumpCount_Ninja = 10

    if animCount_Cop + 1 >= 50:
        animCount_Cop = 0

    if right_Cop:
        window.blit(walkRightCop[animCount_Cop // 5], (x_Cop, y_Cop))
        animCount_Cop += 1
    else:
        if not you_lose:
            window.blit(playerStandCop, (x_Cop, y_Cop))
        else:
            window.blit(Cop_Dead, (x_Cop, y_Cop))

    if right_Ninja:
        window.blit(walkRightNinja[animCount_Ninjs // 5], (x_Ninja, y_Ninja))
        animCount_Ninjs += 1
    else:
        if not you_win:
            window.blit(playerStandNinja, (x_Ninja, y_Ninja))
        else:
            window.blit(Ninja_Dead, (x_Ninja, y_Ninja))

    if x_Cop // 10 == x_Ninja // 10:
        you_win = True

    if (x_Ninja + widht) >= 1366:
        you_lose = True

    if you_win:
        window.blit(win, ((1366 / 2 - 200), (768 / 2 - 200)))
        pregrada_crab.speed_Pregradi = 0
        pregrada_pingvin.speed_Pregradi = 0

    if you_lose:
        window.blit(lose, ((1366 / 2 - 250), (768 / 2 - 200)))
        pregrada_crab.speed_Pregradi = 0
        pregrada_pingvin.speed_Pregradi = 0

    tip1 = font.render('Penguin slows down the Ninja', 1, (255, 255, 255))
    window.blit(pinguin, (1050, 10))
    window.blit(tip1, (1100, 10))
    tip2 = font.render('Crab slows down the Cowboy', 1, (255, 255, 255))
    window.blit(crabs, (1050, 55))
    window.blit(tip2, (1100, 65))
    tip3 = font.render('You can throw a penguin', 1, (255, 255, 255))
    window.blit(tip3, (1100, 35))

    pygame.display.update()


run = True
while run:

    clock.tick(50)

    x_Ninja += speed_Ninja
    animCount_Ninjs += 1
    if animCount_Ninjs + 1 >= 50:
        animCount_Ninjs = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x_Cop > 5:
        x_Cop -= speed_Cop
    elif keys[pygame.K_RIGHT] and x_Cop < 1366 - widht - 5:
        x_Cop += speed_Cop
        right_Cop = True
    else:
        right_Cop = False
        animCount_Cop = 0

    if not (isJump_Сop):
        if keys[pygame.K_UP]:
            isJump_Сop = True
    else:
        if jumpCount_Cop >= -10:
            if jumpCount_Cop < 0:
                x_Cop += speed_Cop
                y_Cop += (jumpCount_Cop ** 2) / 2
            else:
                y_Cop -= (jumpCount_Cop ** 2) / 2
            jumpCount_Cop -= 1
        else:
            isJump_Сop = False
            jumpCount_Cop = 10

    if you_win or you_lose:
        speed_Ninja = 0
        speed_Cop = 0
        counter_for_Crab = 0
        counter_for_Crab -= 1
        counter_for_Pingvin = 0
        counter_for_Pingvin -= 1
        right_Ninja = False
        right_Cop = False

    drawWindow()

pygame.quit()
