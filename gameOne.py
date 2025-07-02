"""A stupid bullet hell game by Calstar9000 using Pokemon Sprites
Credit to my friend Sage for the sprite
"""

# import pygame
# from sprites import *


def initGameOne():
    import pygame
    from sprites import sprite, textSprite, spriteList, textSpriteList, screenWidth, screenHeight, time, math, initScreen, getScreen, screen

    if screen == None:
        screen = initScreen()

    spriteList.empty()
    textSpriteList.empty()

    # Game Label
    pygame.display.set_caption("Game One")

    # BG Image
    # bgImage = pygame.image.load('')

    # player sprite init
    ps = sprite(
        'util/playerSprite.png',
        50, 
        0, 
        200, 
        200, 
        'playerSprite', 
        15
    )
    psSpeedMult = 1
    psIFrames = 0
    psProtectUses = 0
    psProtectUsesMax = 0
    psCoins = 0

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
    try:
        protectSound = pygame.mixer.Sound(r'util\explosion.wav')
        protectSound.set_volume(0.1)
    except:
        try:
            pygame.mixer.init()
            protectSound = pygame.mixer.Sound(r'util\explosion.wav')
            protectSound.set_volume(0.1)
        except:
            print('Weird error with music thats not the mixer????')

    # Text init
    psLabel = textSprite("Yo, its ps, and im here to fight ya cuz you're in my house", 0, 0)

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

        # player sprite movment
        if keys[pygame.K_UP]:
            ps.applyForce(0, -5 * psSpeedMult)
        if keys[pygame.K_DOWN]:
            ps.applyForce(0, 5 * psSpeedMult)
        if keys[pygame.K_LEFT]:
            ps.applyForce(-5 * psSpeedMult, 0)
        if keys[pygame.K_RIGHT]:
            ps.applyForce(5 * psSpeedMult, 0)
    
        # Protect
        if keys[pygame.K_SPACE] and not protecting:
            # print('protecting start: ', protecting)
            if psProtectUses > 0:
                psLabel.relabel('No Protect Uses')
                psProtectUses -= 1
                protectSprite.setVisible(True)
                protecting = True
                protectSound.play(0)

        
        if protecting:
            if protectingItr < 75:
                protectingItr += 1
                protectSprite.resize(protectingItr * 1.3 + 283, protectingItr * 1.3 + 283)
                protectSprite.setPos(ps.rect.centerx, ps.rect.centery)
                protectSprite.update()
            else:
                protectingItr = 0
                protecting = False
                protectSprite.setPos(-400, -400)
        else: 
            protectSprite.resize(0, 0)
            protectSprite.setVisible(False)
        #Bounding 
        if abs(ps.xVel) > 25:
            ps.xVel *= 0.8
        if abs(ps.yVel) > 25:
            ps.yVel *= 0.8

        # Label movment
        psLabel.setPos(ps.rect.right, ps.rect.top)

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
                    ps.rect.centery-i.rect.centery, 
                    ps.rect.centerx-i.rect.centerx
                ) * mod
                i.applyForce(math.cos(angleTo) * enemySpeed, math.sin(angleTo) * enemySpeed)
                if ps.hitsSprite(i) and not psIFrames > 0:
                    ps.hp -= 1.5 ** level
                    psIFrames = 100
                    psLabel.relabel('HP: ' + str(ps.hp) + '/' + str(ps.maxHp))
                    i.kill()
                if protectSprite.hitsSprite(i):
                    i.applyForce(-math.cos(angleTo) * 100, -math.sin(angleTo) * 100)
        if psIFrames > 0:
            if round(currentTime * 2) / 2 == round(prevSec * 2) / 2 + 0.5:
                ps.faded = not ps.faded
        else:
            ps.faded = False
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
            psCoins += ps.hp
            realSpeedMult = psSpeedMult
            psSpeedMult = 1
            ps.setPos(screenWidth / 2, (screenHeight / 4) * 3)
            ps.xVel = 0
            ps.yVel = 0
            shopMode = True    

        # During shop updates
        if shopMode:
            for i in shopTextSprites:
                i.setVisible(True)
                i.setPos(((screenWidth / 4) - 40) * (shopTextSprites.sprites().index(i) + 1), ((screenHeight / 2) + 80))
            exitLabel.setPos(exitLabel.rect.left, exitButton.rect.top - exitLabel.rect.height)

            hitSprite = ''
            for i in shopSprites:
                if ps.hitsSprite(i):
                    ps.setPos(ps.rect.centerx, ps.rect.centery + 150)
                    hitSprite = i
                    # print (i.name)
            if hitSprite != '':
                match hitSprite.name:
                    case 'healthUpgrade':
                        if healthUpgradeCost <= psCoins:
                            psCoins -= healthUpgradeCost
                            psLabel.relabel(('Bought Health Upgrade for ' + str(healthUpgradeCost)))
                            healthUpgradeCost = round(healthUpgradeCost * 1.5)
                            healthLabel.relabel('Hit to gain health upgrade, Cost:' + str(healthUpgradeCost))
                            ps.maxHp += 1
                        else:
                            psLabel.relabel('ERR: Too expensive')
                    case 'speedUpgrade':
                        if speedUpgradeCost <= psCoins:
                            psLabel.relabel(('Bought Speed Upgrade for ' +  str(speedUpgradeCost)))
                            psCoins -= speedUpgradeCost
                            speedUpgradeCost = round(speedUpgradeCost * 1.5)
                            speedLabel.relabel('Hit to gain speed upgrade, Cost:' + str(speedUpgradeCost))
                            realSpeedMult += speedUpgradeCost/20
                        else:
                            psLabel.relabel('ERR: Too expensive')
                    case 'protectUse':
                        if protectUsesCost <= psCoins:
                            psLabel.relabel(('Bought Protect Use for ' + str(protectUsesCost)))
                            psCoins -= protectUsesCost
                            protectUsesCost = round(protectUsesCost * 1.5)
                            protectLabel.relabel('Hit to gain protect uses, Cost:' + str(protectUsesCost))
                            psProtectUsesMax += 1
                        else:
                            psLabel.relabel('ERR: Too expensive')
                    case 'exit':
                        for i in shopSprites:
                            i.setVisible(False)
                        for i in shopTextSprites:
                            i.setVisible(False)
                        ps.hp = ps.maxHp
                        psProtectUses = psProtectUsesMax
                        shopMode = False
                        runEnemies = True
                        psSpeedMult = realSpeedMult
                        startSec = time.gmtime(time.time()).tm_sec
                        level += 1
                        enemySpeed = 1 + (0.5 * level)
        if ps.hp <= 0:
            ps.hp = 0.1
            ps.setPos(screenWidth / 2, (screenHeight / 4) * 3)
            runEnemies = False
            for i in enemies:
                i.kill()
            restartLabel.setVisible(True)
            gameEnd = True
        
        if gameEnd:
            if ps.hitsSprite(restartLabel):
                enemySpeed = 1
                ps.maxHp = 15
                ps.hp = ps.maxHp
                psSpeedMult = 1
                psIFrames = 0
                psProtectUses = 0
                psProtectUsesMax = 0
                psCoins = 0
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
        
        coinsLabel.relabel('Coins: ' + str(psCoins))
        coinsLabel.rect.topright = (screenWidth, 0)
        psIFrames -= 1
        if not gameEnd:
            enemySpeed += 0.001
    screen = None
    pygame.quit()

if __name__ == "__main__":
    initGameOne()