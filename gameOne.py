"""A stupid bullet hell game by Calstar9000 using Pokemon Sprites
Credit to my friend Sage for the Ceruledge sprite
"""

import pygame
from sprites import *


def initGameOne():

    screen = pygame.display.set_mode((screenWidth, screenHeight))

    # Game Label
    pygame.display.set_caption("Game One")

    # BG Image
    # bgImage = pygame.image.load('')

    # Ceruledge init
    ceru = sprite(
        r'util\ceruledge.png', 
        50, 
        0, 
        200, 
        200, 
        'ceru', 
        15
    )
    ceruSpeedMult = 1
    ceruIFrames = 0
    ceruProtectUses = 0
    ceruProtectUsesMax = 0
    ceruCoins = 0

    # Protect setup
    protectSprite = sprite(
        r'util\protect.png', 
        50, 
        50, 
        50, 
        50, 
        'protect'
    )
    protectSprite.setVisible(False)
    protecting = False
    protectingItr = 0
    spriteList.add(protectSprite)
    protectSound = pygame.mixer.Sound(r'util\explosion.wav')
    protectSound.set_volume(0.1)

    # Text init
    ceruLabel = textSprite("Yo, its ceru, and im here to fight ya cuz you're in my house", 0, 0)

    # Enemy setup
    enemies = pygame.sprite.Group()
    enemySpeed = 1

    # Shop Setup
    shopSprites = pygame.sprite.Group()
    shopTextSprites = pygame.sprite.Group()
    healthUpgrade = sprite(
        r'util\healthUpgrade.png', 
        ((screenWidth / 4) - 40), 
        ((screenHeight / 2) - 40), 
        80, 
        80,
        'healthUpgrade'
    )
    speedUpgrade = sprite(
        r'util\speedUpgrade.png', 
        (((screenWidth / 4) * 2) - 20), 
        ((screenHeight / 2) - 20), 
        80, 
        80,
        'speedUpgrade'
    )
    protectUses = sprite(
        r'util\protect.png', 
        (((screenWidth / 4) * 3) - 20), 
        ((screenHeight / 2) - 20), 
        80, 
        80,
        'protectUse'
    )
    exitButton = sprite(
        r'util\exit.png',
        screenWidth-(screenWidth / 15),
        screenHeight-(screenWidth / 15),
        (screenWidth / 15), 
        (screenWidth / 15),
        'exit'
    )
    healthLabel = textSprite(
        'Hit to upgrade health, Cost:2',
        ((screenWidth / 4) - 40), 
        ((screenHeight / 2) - 80)
    )
    speedLabel = textSprite(
        'Hit to upgrade speed, Cost:2',
        (((screenWidth / 4) * 2) - 40), 
        ((screenHeight / 2) - 80)
    )
    protectLabel = textSprite(
        'Hit to gain protect uses, Cost:4',
        (((screenWidth / 4) * 3) - 40), 
        ((screenHeight / 2) - 80)
    )
    exitLabel = textSprite(
        'Exit',
        screenWidth-(screenWidth / 15),
        screenHeight-(screenWidth / 15)
    )
    coinsLabel = textSprite(
        'Coins: 0',
        screenWidth,
        0
    )
    restartLabel = textSprite(
        'YOU DIED. Run into to restart',
        screenWidth / 2,
        screenHeight / 2
    )
    shopSprites.add(healthUpgrade, speedUpgrade, protectUses, exitButton)
    shopTextSprites.add(healthLabel, speedLabel, protectLabel, exitLabel)
    for i in shopSprites:
        i.setVisible(False)
    for i in shopTextSprites:
        i.setVisible(False)
    restartLabel.setVisible(False)
    healthUpgradeCost = 2
    speedUpgradeCost = 2
    protectUsesCost = 4
    shopMode = False
    gameEnd = False

    # Loop setup
    exit = False
    clock = pygame.time.Clock()
    shadowBalls = 0
    cont = True
    prevSec = time.time()
    startSec = time.gmtime(time.time()).tm_sec
    runEnemies = True
    level = 0

    # Loop
    while not exit:
        # Get key list
        keys = pygame.key.get_pressed()

        # Exit funcs
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit = True
            elif i.type == pygame.WINDOWMINIMIZED:
                cont = False
                while not cont:
                    for j in pygame.event.get():
                        if j.type == pygame.MOUSEMOTION:
                            cont = True
        
        if keys[pygame.K_ESCAPE]:
            exit = True

        # Ceruledge movment
        if keys[pygame.K_UP]:
            ceru.applyForce(0, -5 * ceruSpeedMult)
        if keys[pygame.K_DOWN]:
            ceru.applyForce(0, 5 * ceruSpeedMult)
        if keys[pygame.K_LEFT]:
            ceru.applyForce(-5 * ceruSpeedMult, 0)
        if keys[pygame.K_RIGHT]:
            ceru.applyForce(5 * ceruSpeedMult, 0)
    
        # Protect
        if keys[pygame.K_SPACE] and not protecting:
            ceruProtectUses -= 1
            # protectSprite.setPos(ceru.rect.centerx, ceru.rect.centery)
            protectSprite.setVisible(True)
            protecting = True
            protectSound.play(0)
            # print('protecting start: ', protecting)
            if ceruProtectUses > 0:
                ceruLabel.relabel('No Protect Uses')
        
        if protecting:
            # print('protecting: ', protecting, ', ', protectingItr, ', ', protectSprite.rect.width, ', ', protectSprite.rect.center, ', ', ceru.rect.center)
            if protectingItr < 75:
                protectingItr += 1
                protectSprite.resize(protectingItr * 1.3 + 283, protectingItr * 1.3 + 283)
                protectSprite.setPos(ceru.rect.centerx, ceru.rect.centery)
                protectSprite.update()
            else:
                protectingItr = 0
                protecting = False
                protectSprite.setPos(-400, -400)
        else: 
            protectSprite.resize(0, 0)
            protectSprite.setVisible(False)
        #Bounding 
        if abs(ceru.xVel) > 25:
            ceru.xVel *= 0.8
        if abs(ceru.yVel) > 25:
            ceru.yVel *= 0.8

        # Label movment
        ceruLabel.setPos(ceru.rect.right, ceru.rect.top)

        # Sprite and screen updates
        spriteList.update()
        screen.fill((50, 50, 50))
        spriteList.draw(screen)
        # screen.blit(protectSprite.image, protectSprite.rect.topleft)
        pygame.display.flip()
        for i in spriteList:
            i.tick()
        clock.tick(60)
        currentTime = time.time()
        # Enemy movment
        if runEnemies:
            if time.gmtime(currentTime).tm_sec % 10 == 1 and shadowBalls < 5:
                if shadowBalls < 5:
                    if (round(currentTime * 100) % (20 / (level + 1))) == 1:
                        obj = sprite(
                            r'util\shadowBallSprite.png', 
                            ((screenWidth / 2) - 20), 
                            ((screenHeight / 2) - 20), 
                            40, 
                            40,
                            'shadowBall'
                        )
                        enemies.add(obj)
                        shadowBalls += 1
            if time.gmtime(currentTime).tm_sec % 10 == 0:
                shadowBalls = 0
            for i in enemies:
                mod = 1 + (enemies.sprites().index(i) / 20)
                angleTo = math.atan2(
                    ceru.rect.centery-i.rect.centery, 
                    ceru.rect.centerx-i.rect.centerx
                ) * mod
                i.applyForce(math.cos(angleTo) * enemySpeed, math.sin(angleTo) * enemySpeed)
                if ceru.hitsSprite(i) and not ceruIFrames > 0:
                    ceru.hp -= 1.5 ** level
                    ceruIFrames = 100
                    ceruLabel.relabel('HP: ' + str(ceru.hp) + '/' + str(ceru.maxHp))
                    i.kill()
                if protectSprite.hitsSprite(i):
                    i.applyForce(-math.cos(angleTo) * 100, -math.sin(angleTo) * 100)
        if ceruIFrames > 0:
            if round(currentTime * 2) / 2 == round(prevSec * 2) / 2 + 0.5:
                ceru.faded = not ceru.faded
        else:
            ceru.faded = False
        if round(currentTime * 2) / 2 == round(prevSec * 2) / 2 + 0.5:
            prevSec = currentTime
        
        # Shop start
        if (time.gmtime(time.time()).tm_sec) == (startSec + 40) % 60 and not shopMode:
            runEnemies = False
            for i in shopSprites:
                i.setVisible(True)
            for i in shopTextSprites:
                i.setVisible(True)
                i.setPos(((screenWidth / 4) - 40) * (shopTextSprites.sprites().index(i) + 1), ((screenHeight / 2) + 80))
            exitLabel.setPos(exitLabel.rect.left, exitButton.rect.top - exitLabel.rect.height)
            for i in enemies:
                i.kill()
            ceruCoins += ceru.hp
            realSpeedMult = ceruSpeedMult
            ceruSpeedMult = 1
            ceru.setPos(screenWidth / 2, (screenHeight / 4) * 3)
            ceru.xVel = 0
            ceru.yVel = 0
            shopMode = True    

        # During shop updates
        if shopMode:
            for i in shopTextSprites:
                i.setVisible(True)
                i.setPos(((screenWidth / 4) - 40) * (shopTextSprites.sprites().index(i) + 1), ((screenHeight / 2) + 80))
            exitLabel.setPos(exitLabel.rect.left, exitButton.rect.top - exitLabel.rect.height)

            hitSprite = ''
            for i in shopSprites:
                if ceru.hitsSprite(i):
                    ceru.setPos(ceru.rect.centerx, ceru.rect.centery + 150)
                    hitSprite = i
                    # print (i.name)
            if hitSprite != '':
                match hitSprite.name:
                    case 'healthUpgrade':
                        if healthUpgradeCost <= ceruCoins:
                            ceruCoins -= healthUpgradeCost
                            ceruLabel.relabel(('Bought Health Upgrade for ' + str(healthUpgradeCost)))
                            healthUpgradeCost = round(healthUpgradeCost * 1.5)
                            healthLabel.relabel('Hit to gain health upgrade, Cost:' + str(healthUpgradeCost))
                            ceru.maxHp += 1
                        else:
                            ceruLabel.relabel('ERR: Too expensive')
                    case 'speedUpgrade':
                        if speedUpgradeCost <= ceruCoins:
                            ceruLabel.relabel(('Bought Speed Upgrade for ' +  str(speedUpgradeCost)))
                            ceruCoins -= speedUpgradeCost
                            speedUpgradeCost = round(speedUpgradeCost * 1.5)
                            speedLabel.relabel('Hit to gain speed upgrade, Cost:' + str(speedUpgradeCost))
                            realSpeedMult += speedUpgradeCost/20
                        else:
                            ceruLabel.relabel('ERR: Too expensive')
                    case 'protectUse':
                        if protectUsesCost <= ceruCoins:
                            ceruLabel.relabel(('Bought Protect Use for ' + str(protectUsesCost)))
                            ceruCoins -= protectUsesCost
                            protectUsesCost = round(protectUsesCost * 1.5)
                            protectLabel.relabel('Hit to gain protect uses, Cost:' + str(protectUsesCost))
                            ceruProtectUsesMax += 1
                        else:
                            ceruLabel.relabel('ERR: Too expensive')
                    case 'exit':
                        for i in shopSprites:
                            i.setVisible(False)
                        for i in shopTextSprites:
                            i.setVisible(False)
                        ceru.hp = ceru.maxHp
                        ceruProtectUses = ceruProtectUsesMax
                        shopMode = False
                        runEnemies = True
                        ceruSpeedMult = realSpeedMult
                        startSec = time.gmtime(time.time()).tm_sec
                        level += 1
                        enemySpeed = 1 + (0.5 * level)
        if ceru.hp <= 0:
            ceru.hp = 0.1
            ceru.setPos(screenWidth / 2, (screenHeight / 4) * 3)
            runEnemies = False
            for i in enemies:
                i.kill()
            restartLabel.setVisible(True)
            gameEnd = True
        
        if gameEnd:
            if ceru.hitsSprite(restartLabel):
                enemySpeed = 1
                ceru.maxHp = 15
                ceru.hp = ceru.maxHp
                ceruSpeedMult = 1
                ceruIFrames = 0
                ceruProtectUses = 0
                ceruProtectUsesMax = 0
                ceruCoins = 0
                healthUpgradeCost = 2
                speedUpgradeCost = 2
                protectUsesCost = 4
                shopMode = False
                gameEnd = False
                shadowBalls = 0
                cont = True
                prevSec = time.time()
                startSec = time.gmtime(time.time()).tm_sec
                runEnemies = True
                level = 0
                restartLabel.setVisible(False)
        
        coinsLabel.relabel('Coins: ' + str(ceruCoins))
        coinsLabel.rect.topright = (screenWidth, 0)
        ceruIFrames -= 1
        enemySpeed += 0.001
    pygame.quit()

initGameOne()