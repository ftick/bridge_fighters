'''
Created on:   05/04/2014
Last edited:  02/05/2015

@authors: Toph and Basil

Thanks to "cvsnb", or Craig Hargove for Asuka and Jin sprites
Link: http://cvsnb.deviantart.com/

TODO:
    [ ] Finish documentation
    [ ] Update variable names
'''

import pygame, sys

def controls():
    default = raw_input('The Defaults are:\nP1 Left =   a\nP1 Right =  d\nP1 Jump =   w\nP1 Crouch = s\nP1 Punch =  v\nP1 Kick =   b\n \nP2 Left =  k\nP2 Right = ;\nP2 Up =    o\nP2 Down =  l\nP2 Punch = ]\nP2 Kick =  BckSlsh\n \nWould you like to change them?\n>> ')
    default = default.lower()

    if 'y' in default:
        values()
    elif 'n' in default:
        p1_key_left = ord('a')
        p1_key_right = ord('d')
        p1_key_up = ord('w')
        p1_key_down = ord('s')
        p1_key_punch = ord('v')
        p1_key_kick = ord('b')
    
        p2_key_left = ord('k')
        p2_key_right = ord(';')
        p2_key_up = ord('o')
        p2_key_down = ord('l')
        p2_key_punch = ord(']')
        p2_key_kick = ord('\\')
        
        music = ord('m')
        restart = ord('r')
        
        player1_controls = [p1_key_left, p1_key_right, p1_key_up, p1_key_down, p1_key_punch, p1_key_kick]
        player2_controls = [p2_key_left, p2_key_right, p2_key_up, p2_key_down, p2_key_punch, p2_key_kick]
        controls = [player1_controls, player2_controls, music, restart]
        return controls

def values():
    print '\nControl Configuration\n'
    
    p1_key_left = ord(raw_input('Player 1 left\n>> '))
    p1_key_right = ord(raw_input('Player 1 right\n>> '))
    p1_key_up = ord(raw_input('Player 1 up\n>> '))
    p1_key_down = ord(raw_input('Player 1 crouch\n>> '))
    p1_key_punch = ord(raw_input('Player 1 punch\n>> '))
    p1_key_kick = ord(raw_input('Player 1 kick\n>> '))
    
    p2_key_left = ord(raw_input('Player 2 left\n>> '))
    p2_key_right = ord(raw_input('Player 2 right\n>> '))
    p2_key_up = ord(raw_input('Player 2 up\n>> '))
    p2_key_down = ord(raw_input('Player 2 crouch\n>> '))
    p2_key_punch = ord(raw_input('Player 2 punch\n>> '))
    p2_key_kick = ord(raw_input('Player 2 kick\n>> '))
    
    print 'P1 Left:  ' + chr(p1_key_left) + '\nP1 Right: ' + chr(p1_key_right) + '\nP1 Up:    ' + chr(p1_key_up) + '\nP1 Down:  ' + chr(p1_key_down) + '\nP1 Punch: ' + chr(p1_key_punch) + '\nP1 Kick:  ' + chr(p1_key_kick)
    print
    print 'P2 Left:  ' + chr(p2_key_left) + '\nP2 Right: ' + chr(p2_key_right) + '\nP2 Up:    ' + chr(p2_key_up) + '\nP2 Down:  ' + chr(p2_key_down) + '\nP2 Punch: ' + chr(p2_key_punch) + '\nP2 Kick:  ' + chr(p2_key_kick)
    print
    
    confirm = raw_input('Is this correct?\n>> ').lower()
    if confirm == 'n' or confirm == 'no':
        values()
    if confirm == 'y' or confirm == 'yes':
        player1_controls = [p1_key_left, p1_key_right, p1_key_up, p1_key_down, p1_key_punch, p1_key_kick]
        player2_controls = [p2_key_left, p2_key_right, p2_key_up, p2_key_down, p2_key_punch, p2_key_kick]
        controls = [player1_controls, player2_controls]
        return controls
    else:
        values()

pygame.init()
pygame.mixer.init()

# Get controls
controls = controls()

player1_controls = controls[0]
player2_controls = controls[1]

# Assign movement controls
p1l = player1_controls[0]
p1r = player1_controls[1]
p1u = player1_controls[2]
p1d = player1_controls[3]

p2l = player2_controls[0]
p2r = player2_controls[1]
p2u = player2_controls[2]
p2d = player2_controls[3]

# Assign combat controls
p1p = player1_controls[4]
p1k = player1_controls[5]

p2p = player2_controls[4]
p2k = player2_controls[5]

# Assign other stuffs
music = controls[2]
restart = controls[3]

start1 = pygame.image.load('Graphics/Start Screen1.jpg')
start2 = pygame.image.load('Graphics/Start Screen2.jpg')

start1 = pygame.transform.scale(start1, (1280, 700))
start2 = pygame.transform.scale(start2, (1280, 700))

loc1 = pygame.Rect(0, 0, 1, 1)

clock = pygame.time.Clock()

def win(winner):
    screen = pygame.display.set_mode([1280,700])
    z = 0
    if winner == 1:
        while z < 29:
            img = pygame.image.load('Graphics/Player 1 Wins/Player 1 Wins'+str(z)+'.jpg')
            img = pygame.transform.scale(img, (1280, 700))
            screen.blit(img, pygame.Rect(0, 0, 1, 1))
            z += 1
    if winner == 2:
        while z < 29:
            img = pygame.image.load('Graphics/Player 2 Wins/Player 2 Wins'+str(z)+'.jpg')
            img = pygame.transform.scale(img, (1280, 700))
            screen.blit(img, pygame.Rect(0, 0, 1, 1))
            z += 1

def start():
    
    screen = pygame.display.set_mode([1280,700])
    
    pygame.display.set_caption("Bridge Fighter")
    done = False
    
    while not done:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True
                
            screen.blit(start1, loc1)
            
            pygame.display.flip()

            screen.blit(start2, loc1)
            
            clock.tick(4)
            
            pygame.display.flip()

def shatter():
    
    screen = pygame.display.set_mode([1280,700])
    
    pygame.display.set_caption("Bridge Fighter")
    
    done = False
    frameCount = 0
    
    while not done:
            
        frame = pygame.image.load('Graphics/Title Screen Shatter/Title Screen Shatter_000'+str(frameCount)+'.jpg')
        frame = pygame.transform.scale(frame, (1280, 700))
            
        screen.blit(frame,loc1)
            
        pygame.display.flip()
        
        frameCount += 1
        if frameCount > 74:
            done = True

def instructions():
    
    backImg = pygame.image.load('Graphics/Background_Pause.jpg')
    backImg = pygame.transform.scale(backImg, (1280, 700))
    back = pygame.Rect(0, 0, 700, 1280)
    
    blankImg = pygame.image.load('Graphics/Instructions/Instructions_Template.png')
    blankImg = pygame.transform.scale(blankImg, (426,500))
    blank = pygame.Rect(427,87,500,426)
    
    size = [1280, 700]
    screen = pygame.display.set_mode(size)
    
    pygame.display.set_caption("Bridge Fighter")
    
    page = 1
    
    while page <= 8:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                page += 1
        
        screen.blit(backImg, back)
        screen.blit(blankImg, blank)
        
        if page == 9:
            break
        
        txtImg = pygame.image.load('Graphics/Instructions/page-'+str(page)+'.gif')
        txtImg = pygame.transform.scale(txtImg, (426,500))
        
        screen.blit(txtImg,blank)
        
        pygame.display.flip()

def count():

    backImg = pygame.image.load('Graphics/Background_Pause.jpg')
    backImg = pygame.transform.scale(backImg, (1280, 700))
    back = pygame.Rect(0, 0, 700, 1280)
    
    blank = pygame.Rect(427,87, 500,426)

    size = [1280, 700]
    screen = pygame.display.set_mode(size)
    
    pygame.display.set_caption("Bridge Fighter")
        
    count = 4

    while count > 0:
        
        screen.blit(backImg, back)
        
        clock.tick(1)
        
        count -= 1
        
        if count == 0:
            break
        
        numImg = pygame.image.load('Graphics/Countdown/num-'+str(count)+'.gif')
        numImg = pygame.transform.scale(numImg, (426,500))
        
        screen.blit(numImg,blank)
        
        pygame.display.flip()
        
        clock.tick(1)

def play():

    # Movement Variables
    
    moveLeft = False
    moveRight = False
    moveUp = False
    moveDown = True
    knockLeft = False
    knockRight = False
    tapLeft = False
    tapRight = False
    downLeft = False
    downRight = False
    fallDown = False
    jump = True
    punch = False
    kick = False
    crouching = False
    moving = (moveLeft or moveRight or moveUp or moveDown)
    stun = (tapLeft or tapRight or knockLeft or knockRight or downLeft or downRight or fallDown)
    
    move2Left = False
    move2Right = False
    move2Up = False
    move2Down = True
    knock2Left = False
    knock2Right = False
    tap2Left = False
    tap2Right = False
    down2Left = False
    down2Right = False
    fall2Down = False
    jump2 = True
    punch2 = False
    kick2 = False
    crouching2 = False
    moving2 = (move2Left or move2Right or move2Up or move2Down)
    stun2 = (tap2Left or tap2Right or knock2Left or knock2Right or down2Left or down2Right or fall2Down)
    
    # Animation Counters
        
    crouchCount = 0
    idleCount = 0
    jumpCount = 18
    walkCount = 0
    punchCount = 0
    kickCount = 0
    deathCount = 0
    
    crouch2Count = 0
    idle2Count = 0
    jump2Count = 18
    walk2Count = 0
    punch2Count = 0
    kick2Count = 0
    death2Count = 0

    # Misc. Images
    
    back = pygame.Rect(0, 0, 700, 1280)
    backImage = pygame.image.load('Graphics/Background.jpg')
    backStretched = pygame.transform.scale(backImage, (1280, 700))
    
    rail = pygame.Rect(0, 600, 1280, 150)
    railImage = pygame.image.load('Graphics/Railing Transparent.png')
    railStretched = pygame.transform.scale(railImage, (1280, 150))
    
    # Images / Rects
    
    pHei = 180
    pWid  = 80
    p1 = 100
    p2 = 100
    
    player = pygame.Rect(560-pWid, 700-pHei, pWid, pHei)
    playerImage = pygame.image.load('Graphics/Cvs Asuka Idle Stance Right/tmp-2.gif')
    playerStretchedImage = pygame.transform.scale(playerImage, (pWid, pHei))
    
    p1BoxVul = player
    
    basic = pygame.Rect((player.left+10,player.bottom-10),(pWid-20,10))
    gone = pygame.Rect((0,0),(1,1))
    p1BoxAtt = basic
    
    player2 = pygame.Rect(720+pWid, 700-pHei, pWid, pHei)
    player2Image = pygame.image.load('Graphics/Cvs Jin Idle Stance/tmp-1.gif')
    player2StretchedImage = pygame.transform.scale(player2Image, (pWid, pHei))
    
    p2BoxVul = player2
    
    basic2 = pygame.Rect((player2.left+10,player2.bottom-10),(pWid-20,10))
    gone2 = pygame.Rect((10,0),(1,1))
    p2BoxAtt = basic2

    board = pygame.image.load('Graphics/Health Bar/Health Bar 90.gif')
        
    boardBox = pygame.Rect((10,10),(1,1))
        
    board2 = pygame.image.load('Graphics/Health Bar/Health Bar 90.gif')
    
    board2Box = pygame.Rect((870,10),(1,1))
    
    # Audio
    
    pygame.mixer.music.load('song.mp3')
    pygame.mixer.music.play(-1, 5.0)
    pygame.mixer.music.set_volume(0.4)
    musicPlaying = True
    
    a_punch = pygame.mixer.Sound("Audio/Asuka_Punch.wav")
    a_kick = pygame.mixer.Sound("Audio/Asuka_Kick.wav")
    a_jump = pygame.mixer.Sound("Audio/Asuka_Jump.wav")
    a_punch.set_volume(0.1)
    a_kick.set_volume(0.1)
    a_jump.set_volume(0.1)
    
    j_punch = pygame.mixer.Sound("Audio/Jin_Punch.wav")
    j_kick = pygame.mixer.Sound("Audio/Jin_Kick.wav")
    j_jump = pygame.mixer.Sound("Audio/Jin_Jump.wav")
    j_punch.set_volume(0.1)
    j_kick.set_volume(0.1)
    j_jump.set_volume(0.1)
    
    screen = pygame.display.set_mode([1280,700])
    screen.blit(backStretched,back)
    
    # Misc.
    
    pygame.display.set_caption("Bridge Fighter")

    while True:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
                break
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mixer.music.pause()
                loop = 1
                screen = pygame.display.set_mode([1280,700])
                while loop == 1:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit(0)
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            pygame.mixer.music.unpause()
                            loop = 0
                                
                    pygame.display.flip()
                    
                    backImg = pygame.image.load('Graphics/Background_Pause.jpg')
                    backImg = pygame.transform.scale(backImg, (1280, 700))
                    screen.blit(backImg,back)

                    if p1 > 0:
                        screen.blit(board,boardBox)
                    if p2 > 0:
                        screen.blit(board2,board2Box)
                    
                    screen.blit(playerStretchedImage, player)
                    screen.blit(player2StretchedImage, player2)
                        
                    screen.blit(railStretched,rail)
                        
                    pause1 = pygame.Rect((640-60,240),(40,100))
                    pause2 = pygame.Rect((640+20,240),(40,100))

                    pygame.draw.rect(screen, (255,255,255), pause1)
                    pygame.draw.rect(screen, (255,255,255), pause2)
                                
                    if loop == 0:
                        break
                    else:
                        continue
                    
                    pygame.display.flip()
                    
            if event.type == pygame.KEYDOWN:
                
                if event.key == p1u:               # If p1 tries to move up
                    if p1 > 0 and not(jump):
                        a_jump.play()
                        moveUp, jump = True, True
                        moveDown, fallDown = False, False
                
                elif event.key == p1p:
                    if p1 > 0 and not(moveUp or crouching):
                        punch = True
                        crouching = False
                
                elif event.key == p1k:
                    if p1 > 0 and not(moveUp or crouching):
                        kick = True
                        crouching = False
                                    
                if event.key == p2u:               # If p2 tries to move up
                    if p2 > 0 and not(jump2):
                        j_jump.play()
                        move2Up, jump2 = True, True
                        move2Down, fall2Down = False, False
                
                elif event.key == p2p:
                    if p2 > 0 and not(move2Up or crouching2):
                        punch2 = True
                        crouching2 = False
                
                elif event.key == p2k:
                    if p2 > 0 and not(move2Up or crouching2):
                        kick2 = True
                        crouching2 = False
                        
                elif event.key == restart:
                    pygame.mixer.music.stop()
                    play()
                
                elif event.key == music:
                    if musicPlaying:
                        pygame.mixer.music.stop()
                    else:
                        pygame.mixer.music.play(-1,5.0)
                    musicPlaying = not musicPlaying

            if event.type == pygame.KEYUP:         # Disable horizontal movement
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if p1 > 0:                        # If p1 lets go of a key
                    if jump:
                        pass
                    else:
                        if event.key == p1l:
                            moveLeft = False
                            moveRight = False
                        if event.key == p1r:
                            moveRight = False
                            moveLeft = False
                if p2 > 0:                        # If p2 lets go of a key
                    if jump2:
                        pass
                    else:
                        if event.key == p2l:
                            move2Left = False
                            move2Right = False
                        if event.key == p2r:
                            move2Right = False
                            move2Left = False
                            
        if p1 > 0:
            if p1 > 90:
                p1 = 90
                dmg1 = 0
        
        if p2 > 0:
            if p2 > 90:
                p2 = 90
                dmg2 = 0
        
        if p1 < 0:
            p1 = 0
            
        if p2 < 0:
            p2 = 0
        
        screen.blit(backStretched,back)
            
        # Display Health Bars
        
        if p1 >= 0:
            board = pygame.image.load('Graphics/Health Bar/Health Bar '+ str(p1) + '.gif')
            board = pygame.transform.scale(board, (400, 100))
        
        boardBox = pygame.Rect((10,10),(1,1))
        
        if p2 >= 0:        
            board2 = pygame.image.load('Graphics/Health Bar/Health Bar '+ str(p2) + '.gif')
            board2 = pygame.transform.flip(board2,1,0)
            board2 = pygame.transform.scale(board2, (400, 100))
        
        board2Box = pygame.Rect((870,10),(1,1))
        
        screen.blit(board,boardBox)
        screen.blit(board2,board2Box)
        
        # Handle movement requests
        
        keys = pygame.key.get_pressed()
        
        if p1 > 0:
            if keys[p1d]:
                crouching = True
                moveRight = False
                moveLeft = False
            else:
                crouching = False
            if not(crouching):
                if keys[p1l]:
                    if player.top > pHei:
                        if punch or kick:
                            pass
                        else:
                            moveLeft = True
                            moveRight = False
                    else:
                        moveRight = False
                        moveLeft = True
                elif keys[p1r]:
                    if player.top > pHei:
                        if punch or kick:
                            pass
                        else:
                            moveRight = True
                            moveLeft = False
                    else:
                        moveLeft = False
                        moveRight = True
        else:
            if player.bottom < 700:
                moveDown = True

        if p2 > 0:
            if keys[p2d]:
                crouching2 = True
                move2Right = False
                move2Left = False
            else:
                crouching2 = False
            if not(crouching2):
                if keys[p2l]:
                    if player2.top > pHei:
                        if punch2 or kick2:
                            pass
                        else:
                            move2Left = True
                            move2Right = False
                    else:
                        move2Right = False
                        move2Left = True
                elif keys[p2r]:
                    if player2.top > pHei:
                        if punch2 or kick2:
                            pass
                        else:
                            move2Right = True
                            move2Left = False
                    else:
                        move2Left = False
                        move2Right = True
        else:
            if player2.bottom < 700:
                move2Down = True
        
        # Move Characters according to requests made
        
        if p1 > 0:
            if moveDown and player.bottom < 700:
                player.top += 23
            if fallDown and player.bottom < 700:
                tapRight, tapLeft, knockLeft, knockRight = False, False, False, False
                player.top += 23
            if player.bottom >= 700:
                player.bottom = 700
                jump = False
                moveDown, fallDown = False, False
            if moveUp and player.top > 0 and not(punch or kick):
                if player.top < 200:
                    moveUp = False
                    moveDown = True
                else:
                    player.top -= 25
            if moveLeft and not(punch or kick):
                if player.left > 0:
                    player.left -= 10
                else:
                    moveLeft = False
                    moveRight = True
            if moveRight and not(punch or kick):
                if player.right < 1280:
                    player.left += 10
                else:
                    moveRight = False
                    moveLeft = True
            if knockLeft:
                if player.top < 490:
                    knockLeft, tapLeft = False, False
                    fallDown = True
                else:
                    player.top -= 5
                    player.left -= 20
            if knockRight:
                if player.top < 490:
                    knockRight, tapRight = False, False
                    fallDown = True
                else:
                    player.top -= 5
                    player.left += 20
            if tapLeft:
                if player.top < 490:
                    knockLeft, tapLeft = False, False
                    fallDown = True
                else:
                    player.top -= 15
                    player.left -= 20
            if tapRight:
                if player.top < 490:
                    knockRight, tapRight = False, False
                    fallDown = True
                else:
                    player.top -= 15
                    player.left += 20
        else:
            if deathCount < 10:
                moveUp = True
            else:
                moveDown = True
            if moveUp:
                player.top -= 23
            if moveDown and player.bottom < 825:
                player.top += 23
            else:
                player.bottom = 825
                moveDown = False
                    
        if p2 > 0:
            if move2Down and player2.bottom < 700:
                player2.top += 23
            if fall2Down and player2.bottom < 700:
                tap2Right, tap2Left = False, False
                player2.top += 23
            if player2.bottom >= 700:
                player2.bottom = 700
                jump2 = False
                move2Down = False
                fall2Down = False
            if move2Up and player2.top > 0 and not(punch2 or kick2):
                if player2.top < 240:
                    move2Up = False
                    move2Down = True
                else:
                    player2.top -= 23
            if move2Left and not(punch2 or kick2):
                if player2.left > 0:
                    player2.left -= 10
                else:
                    move2Left = False
                    move2Right = True
            if move2Right:
                if not(punch2 or kick2):
                    if player2.right < 1280:
                        player2.left += 10
                    else:
                        move2Right = False
                        move2Left = True
            if knock2Left:
                if player2.top < 490:
                    knock2Left, tap2Left = False, False
                    down2Right = True
                else:
                    tap2Left, tap2Right = False, False
                    if player2.left > 0:
                        player2.top -= 15
                        player2.left -= 20
                    else:
                        player2.top += 15
                        player2.left += 20
                        knock2Left = False
                        fall2Down = True
            if knock2Right:
                if player2.top < 490:
                    knock2Right, tap2Right = False, False
                    down2Right = True
                else:
                    tap2Left, tap2Right = False, False
                    if player2.right < 1280:
                        player2.top -= 15
                        player2.left += 20
                    else:
                        player2.top += 15
                        player2.left -= 20
                        knock2Right = False
                        fall2Down = True
            if down2Left:
                if player2.bottom < 700:
                    player2.top += 15
                    player2.left -= 20
                else:
                    down2Left = False
            if down2Right:
                if player2.bottom < 700:
                    player2.top += 15
                    player2.left += 20
                else:
                    down2Right = False
            if tap2Left:
                if player2.top < 490:
                    tap2Left = False
                    fall2Down = True
                else:
                    knock2Left, knock2Right = False, False
                    if player2.left > 0:
                        player2.top -= 10
                        player2.left -= 5
                    else:
                        player2.top += 10
                        player2.left += 5
                        tap2Left = False
                        fall2Down = True
            if tap2Right:
                if player2.top < 490:
                    tap2Right = False
                    fall2Down = True
                else:
                    knock2Left, knock2Right = False, False
                    if player2.right < 1280:
                        player2.top -= 10
                        player2.left += 5
                    else:
                        player2.top += 10
                        player2.left -= 5
                        tap2Right = False
                        fall2Down = True
        else:
            if move2Down and player2.bottom < 700:
                player2.top += 23
            else:
                player2.bottom = 700
                move2Down = False
                
        # Animate sprites
        
        if p1 > 0:
            if (player.left+player.right)/2 > (player2.right+player2.left)/2:        # P1 face right, P2 face left
                if player.bottom >= 700:
                    if jumpCount > 20 and jumpCount < 28:
                        jumpCount += 1
                        playerImage = pygame.image.load('Graphics/Cvs Asuka Jump Right/tmp-'+ str(jumpCount/2) + '.gif')
                        playerImage = pygame.transform.flip(playerImage,1,0)
                    else:
                        jumpCount = 3
                    if not(moveLeft or moveRight or punch or kick):
                        if not(crouching):
                            crouchCount = 0
                            playerImage = pygame.image.load('Graphics/Cvs Asuka Idle Stance Right/tmp-'+ str(idleCount/5) + '.gif')
                            playerImage = pygame.transform.flip(playerImage,1,0)
                            if idleCount != 36*5:
                                idleCount += 1
                            else:
                                idleCount = 0
                        else:
                            playerImage = pygame.image.load('Graphics/Cvs Asuka Crouch Right/tmp-'+ str(crouchCount) + '.gif')
                            playerImage = pygame.transform.flip(playerImage,1,0)
                            if crouchCount < 2:
                                crouchCount += 1
                    else:
                        if punch:
                            crouchCount = 0
                            walkCount = 0
                            playerImage = pygame.image.load('Graphics/Cvs Asuka Punch Right/tmp-'+ str(punchCount) + '.gif')
                            playerImage = pygame.transform.flip(playerImage,1,0)
                            if punchCount < 5:
                                punchCount += 1
                            else:
                                punchCount = 0
                                punch = False
                        elif kick:
                            crouchCount = 0
                            walkCount = 0
                            playerImage = pygame.image.load('Graphics/Cvs Asuka Kick Right/tmp-'+ str(kickCount/2) + '.gif')
                            playerImage = pygame.transform.flip(playerImage,1,0)
                            if kickCount < 6*2:
                                kickCount += 1
                            else:
                                kickCount = 0
                                kick = False
                        elif moveRight:
                            crouchCount = 0
                            playerImage = pygame.image.load('Graphics/Cvs Asuka Walking Back Right/tmp-'+ str(walkCount) + '.gif')
                            playerImage = pygame.transform.flip(playerImage,1,0)
                            if walkCount < 10:
                                walkCount += 1
                            else:
                                walkCount = 0
                        elif moveLeft:
                            crouchCount = 0
                            if walkCount == 10:
                                walkCount = 9
                            playerImage = pygame.image.load('Graphics/Cvs Asuka Walking Right/tmp-'+ str(walkCount) + '.gif')
                            playerImage = pygame.transform.flip(playerImage,1,0)
                            if walkCount < 9:
                                walkCount += 1
                            else:
                                walkCount = 0
                else:
                    if moveUp:
                        playerImage = pygame.image.load('Graphics/Cvs Asuka Jump Right/tmp-'+ str(jumpCount/2) + '.gif')
                        playerImage = pygame.transform.flip(playerImage,1,0)
                        if jumpCount < 8:
                            jumpCount += 1
                        elif jumpCount > 8:
                            jumpCount = 2
                    elif moveDown:
                        playerImage = pygame.image.load('Graphics/Cvs Asuka Jump Right/tmp-'+ str(jumpCount/2) + '.gif')
                        playerImage = pygame.transform.flip(playerImage,1,0)
                        if jumpCount < 21:
                            jumpCount += 1
                    else:
                        playerImage = pygame.image.load('Graphics/Cvs Asuka Punch Right/tmp-4.gif')
                        playerImage = pygame.transform.flip(playerImage,1,0)
                    
            else:      # P1 face left, P2 face right
                if player.bottom >= 700:
                    if jumpCount > 20 and jumpCount < 28:
                        playerImage = pygame.image.load('Graphics/Cvs Asuka Jump Right/tmp-'+ str(jumpCount/2) + '.gif')
                        playerImage = pygame.transform.flip(playerImage,1,0)
                        jumpCount += 1
                    else:
                        jumpCount = 3
                    if not(moveLeft or moveRight or punch or kick):
                        if not(crouching):
                            crouchCount = 0
                            playerImage = pygame.image.load('Graphics/Cvs Asuka Idle Stance Right/tmp-'+ str(idleCount/5) + '.gif')
                            if idleCount != 36*5:
                                idleCount += 1
                            else:
                                idleCount = 0
                        else:
                            playerImage = pygame.image.load('Graphics/Cvs Asuka Crouch Right/tmp-'+ str(crouchCount) + '.gif')
                            if crouchCount < 2:
                                crouchCount += 1
                    else:
                        if punch:
                            crouchCount = 0
                            walkCount = 0
                            playerImage = pygame.image.load('Graphics/Cvs Asuka Punch Right/tmp-'+ str(punchCount) + '.gif')
                            if punchCount < 5:
                                punchCount += 1
                            else:
                                punchCount = 0
                                punch = False
                        elif kick:
                            crouchCount = 0
                            walkCount = 0
                            playerImage = pygame.image.load('Graphics/Cvs Asuka Kick Right/tmp-'+ str(kickCount/2) + '.gif')
                            if kickCount < 6*2:
                                kickCount += 1
                            else:
                                kickCount = 0
                                kick = False
                        elif moveLeft:
                            crouchCount = 0
                            playerImage = pygame.image.load('Graphics/Cvs Asuka Walking Back Right/tmp-'+ str(walkCount) + '.gif')
                            if walkCount < 10:
                                walkCount += 1
                            else:
                                walkCount = 0
                        elif moveRight:
                            crouchCount = 0
                            if walkCount == 10:
                                walkCount = 9
                            playerImage = pygame.image.load('Graphics/Cvs Asuka Walking Right/tmp-'+ str(walkCount) + '.gif')
                            if walkCount < 9:
                                walkCount += 1
                            else:
                                walkCount = 0
                else:
                    if moveUp:
                        playerImage = pygame.image.load('Graphics/Cvs Asuka Jump Right/tmp-'+ str(jumpCount/2) + '.gif')
                        if jumpCount < 8:
                            jumpCount += 1
                        elif jumpCount > 8:
                            jumpCount = 2
                    elif moveDown:
                        playerImage = pygame.image.load('Graphics/Cvs Asuka Jump Right/tmp-'+ str(jumpCount/2) + '.gif')
                        if jumpCount < 21:
                            jumpCount += 1
                    else:
                        playerImage = pygame.image.load('Graphics/Cvs Asuka Punch Right/tmp-4.gif')
        else:
            playerImage = pygame.image.load('Graphics/Cvs Asuka Death/tmp-'+str(deathCount/2)+'.gif')
            if ((player.left+player.right)/2 > (player2.right+player2.left)/2) and deathCount < 18:
                playerImage = pygame.transform.flip(playerImage,1,0)
            if deathCount < 18:
                deathCount += 1
            if deathCount == 18:
                win(2)
            
        if p2 > 0:
            if (player.left+player.right)/2 < (player2.right+player2.left)/2:        # P1 face left, P2 face right
                if player2.bottom >= 700:
                    if jump2Count > 15 and jump2Count < 20:
                        jump2Count += 1
                        player2Image = pygame.image.load('Graphics/Cvs Jin Jump/tmp-'+ str(jump2Count/2) + '.gif')
                        player2Image = pygame.transform.flip(player2Image,1,0)
                    else:
                        jump2Count = 2
                    if not(move2Left or move2Right or punch2 or kick2):
                        if not(crouching2):
                            crouch2Count = 0
                            player2Image = pygame.image.load('Graphics/Cvs Jin Idle Stance/tmp-'+ str(idle2Count/5) + '.gif')
                            player2Image = pygame.transform.flip(player2Image,1,0)
                            if idle2Count != 6*5:
                                idle2Count += 1
                            else:
                                idle2Count = 0
                        else:
                            player2Image = pygame.image.load('Graphics/Cvs Jin Crouch/tmp-'+ str(crouch2Count) + '.gif')
                            player2Image = pygame.transform.flip(player2Image,1,0)
                            if crouch2Count < 2:
                                crouch2Count += 1
                    else:
                        if punch2:
                            crouch2Count = 0
                            walk2Count = 0
                            player2Image = pygame.image.load('Graphics/Cvs Jin Punch/tmp-'+ str(punch2Count/2) + '.gif')
                            player2Image = pygame.transform.flip(player2Image,1,0)
                            if punch2Count < 10:
                                punch2Count += 1
                            else:
                                punch2Count = 0
                                punch2 = False
                        elif kick2:
                            crouch2Count = 0
                            walk2Count = 0
                            player2Image = pygame.image.load('Graphics/Cvs Jin Kick/tmp-'+ str(kick2Count/2) + '.gif')
                            player2Image = pygame.transform.flip(player2Image,1,0)
                            if kick2Count < 6*2:
                                kick2Count += 1
                            else:
                                kick2Count = 0
                        # This '2'  |   was typed by Ian's little brother Martin Bantoto
                        #           v
                                kick2 = False
                        elif move2Right:
                            crouch2Count = 0
                            player2Image = pygame.image.load('Graphics/Cvs Jin Walking Back/tmp-'+ str(walk2Count) + '.gif')
                            player2Image = pygame.transform.flip(player2Image,1,0)
                            if walk2Count < 10:
                                walk2Count += 1
                            else:
                                walk2Count = 0
                        elif move2Left:
                            crouch2Count = 0
                            if walk2Count == 10:
                                walk2Count = 9
                            player2Image = pygame.image.load('Graphics/Cvs Jin Walking/tmp-'+ str(walk2Count) + '.gif')
                            player2Image = pygame.transform.flip(player2Image,1,0)
                            if walk2Count < 9:
                                walk2Count += 1
                            else:
                                walk2Count = 0
                else:
                    if move2Up:
                        player2Image = pygame.image.load('Graphics/Cvs Jin Jump/tmp-'+ str(jump2Count/2) + '.gif')
                        player2Image = pygame.transform.flip(player2Image,1,0)
                        if jump2Count < 11:
                            jump2Count += 1
                        elif jump2Count > 11:
                            jump2Count = 2
                    elif move2Down:
                        player2Image = pygame.image.load('Graphics/Cvs Jin Jump/tmp-'+ str(jump2Count/2) + '.gif')
                        player2Image = pygame.transform.flip(player2Image,1,0)
                        if jump2Count < 15:
                            jump2Count += 1
                    else:
                        player2Image = pygame.image.load('Graphics/Cvs Jin Jump/tmp-1.gif')
                        player2Image = pygame.transform.flip(player2Image,1,0)
                    
            else:      # P1 face right, P2 face left
                if player2.bottom >= 700:
                    if jump2Count > 15 and jump2Count < 20:
                        player2Image = pygame.image.load('Graphics/Cvs Jin Jump/tmp-'+ str(jump2Count/2) + '.gif')
                        player2Image = pygame.transform.flip(player2Image,1,0)
                        jump2Count += 1
                    else:
                        jump2Count = 2
                    if not(move2Left or move2Right or punch2 or kick2):
                        if not(crouching2):
                            crouch2Count = 0
                            player2Image = pygame.image.load('Graphics/Cvs Jin Idle Stance/tmp-'+ str(idle2Count/5) + '.gif')
                            if idle2Count != 6*5:
                                idle2Count += 1
                            else:
                                idle2Count = 0
                        else:
                            player2Image = pygame.image.load('Graphics/Cvs Jin Crouch/tmp-'+ str(crouch2Count) + '.gif')
                            if crouch2Count < 2:
                                crouch2Count += 1
                    else:
                        if punch2:
                            crouch2Count = 0
                            walk2Count = 0
                            player2Image = pygame.image.load('Graphics/Cvs Jin Punch/tmp-'+ str(punch2Count/2) + '.gif')
                            if punch2Count < 10:
                                punch2Count += 1
                            else:
                                punch2Count = 0
                                punch2 = False
                        elif kick2:
                            crouch2Count = 0
                            walk2Count = 0
                            player2Image = pygame.image.load('Graphics/Cvs Jin Kick/tmp-'+ str(kick2Count/2) + '.gif')
                            if kick2Count < 6*2:
                                kick2Count += 1
                            else:
                                kick2Count = 0
                                kick2 = False
                        elif move2Left:
                            crouch2Count = 0
                            player2Image = pygame.image.load('Graphics/Cvs Jin Walking Back/tmp-'+ str(walk2Count) + '.gif')
                            if walk2Count < 10:
                                walk2Count += 1
                            else:
                                walk2Count = 0
                        elif move2Right:
                            crouch2Count = 0
                            if walk2Count == 10:
                                walk2Count = 9
                            player2Image = pygame.image.load('Graphics/Cvs Jin Walking/tmp-'+ str(walk2Count) + '.gif')
                            if walk2Count < 9:
                                walk2Count += 1
                            else:
                                walk2Count = 0
                else:
                    if move2Up:
                        player2Image = pygame.image.load('Graphics/Cvs Jin Jump/tmp-'+ str(jump2Count/2) + '.gif')
                        if jump2Count < 11:
                            jump2Count += 1
                        elif jump2Count > 11:
                            jump2Count = 2
                    elif move2Down:
                        player2Image = pygame.image.load('Graphics/Cvs Jin Jump/tmp-'+ str(jump2Count/2) + '.gif')
                        if jump2Count < 15:
                            jump2Count += 1
                    else:
                        player2Image = pygame.image.load('Graphics/Cvs Jin Jump/tmp-1.gif')
        else:
            if death2Count < 13:
                death2Count += 1
            player2Image = pygame.image.load('Graphics/Cvs Jin Death/tmp-'+str(death2Count)+'.gif')
            if ((player2.left+player.right)/2 > (player.right+player.left)/2) and death2Count < 13:
                player2Image = player2Image.transform.flip(player2Image,1,0)
            if death2Count == 13:
                win(1)
            
        # Draw player characters
        
        if p1 > 0:
            if moveUp or moveDown or punch:
                playerStretchedImage = pygame.transform.scale(playerImage, (pWid+15, pHei+20))
            elif kick:
                playerStretchedImage = pygame.transform.scale(playerImage, (pWid+40, pHei+20))
            elif jump:
                playerStretchedImage = pygame.transform.scale(playerImage, (pWid+15, pHei+20))
            else:
                playerStretchedImage = pygame.transform.scale(playerImage, (pWid, pHei))
        else:
            playerStretchedImage = pygame.transform.scale(playerImage, (pHei, pWid))
        
        if p2 > 0:
            if move2Up or move2Down or punch2 or crouching2:
                player2StretchedImage = pygame.transform.scale(player2Image, (pWid+15, pHei+20))
            elif kick2:
                player2StretchedImage = pygame.transform.scale(player2Image, (pWid+45, pHei+20))
            elif jump2:
                player2StretchedImage = pygame.transform.scale(player2Image, (pWid+15, pHei+20))
            else:
                player2StretchedImage = pygame.transform.scale(player2Image, (pWid, pHei))
        else:
            player2StretchedImage = pygame.transform.scale(player2Image, (pHei, pHei))
            
        # Adjust Vulnerable Hitboxes
        
        if p1 > 0:
            if player.bottom == 700:
                if crouching:
                    if crouchCount == 2:
                        p1BoxVul = pygame.Rect((player.left,player.top+(pHei/3)),(pWid,(2*pHei)/3))
                    elif crouchCount == 1:
                        p1BoxVul = pygame.Rect((player.left,player.top+(pHei/6)),(pWid,(5*pHei)/6))
                    else:
                        pass
                elif punch:
                    if punchCount < 2:
                        p1BoxVul = pygame.Rect((player.left+(pWid/3),player.top),((2*pWid)/3,pHei))
                    else:
                        p1BoxVul = pygame.Rect((player.left+(pWid/4),player.top),((5*pWid)/7,pHei))
                elif kick:
                    if kickCount < 5 and kickCount > 0:
                        if p1BoxVul.right < p2BoxVul.right:
                            p1BoxVul = pygame.Rect((player.left-(pWid/8)+30,player.top),((5*pWid)/6-30,pHei))
                        else:
                            p1BoxVul = pygame.Rect((player.left+((3*pWid)/4)+20,player.top),((5*pWid)/6-20,pHei))
                else:
                    if (p1BoxVul.right+p1BoxVul.left) < (p2BoxVul.left+p2BoxVul.right):
                        p1BoxVul = pygame.Rect((player.left-(pWid/8)+10,player.top),((5*pWid)/6-10,pHei))
                    elif (p2BoxVul.right+p2BoxVul.left) < (p1BoxVul.left+p1BoxVul.right):
                        p1BoxVul = pygame.Rect((player.left+(pWid/3),player.top),((5*pWid)/6-20,pHei))
            else:
                p1BoxVul = player
        else:
            p1BoxVul = basic
        
        if p2 > 0:
            if player2.bottom == 700:
                if crouching2:
                    if (p1BoxVul.left+p1BoxVul.right)/2 < (p2BoxVul.left+p2BoxVul.right)/2:
                        if crouch2Count == 2:
                            p2BoxVul = pygame.Rect((player2.left+20,player2.top+(pHei/3)),(pWid,(2*pHei)/3))
                        elif crouch2Count == 1:
                            p2BoxVul = pygame.Rect((player2.left+20,player2.top+(pHei/6)),(pWid,(5*pHei)/6))
                        else:
                            pass
                    else:
                        if crouch2Count == 2:
                            p2BoxVul = pygame.Rect((player2.left,player2.top+(pHei/3)),(pWid,(2*pHei)/3))
                        elif crouch2Count == 1:
                            p2BoxVul = pygame.Rect((player2.left,player2.top+(pHei/6)),(pWid,(5*pHei)/6))
                        else:
                            pass
                elif punch2:
                    if (p1BoxVul.left+p1BoxVul.right)/2 < (p2BoxVul.left+p2BoxVul.right)/2:
                        if punch2Count < 4:
                            p2BoxVul = pygame.Rect((player2.left+(pWid/2),player2.top),((2*pWid)/3,pHei))
                        else:
                            p2BoxVul = pygame.Rect((player2.left+(pWid/3),player2.top),((5*pWid)/7,pHei))
                    else:
                        if punch2Count < 4:
                            p2BoxVul = pygame.Rect((player2.left+(pWid/2)-30,player2.top),((2*pWid)/3,pHei))
                        else:
                            p2BoxVul = pygame.Rect((player2.left+(pWid/3)-10,player2.top),((5*pWid)/7,pHei))
                elif kick2:
                    if kick2Count < 5 and kick2Count > 0:
                        if p1BoxVul.right < p2BoxVul.right:
                            p2BoxVul = pygame.Rect((player2.left+((3*pWid)/4)-10,player2.top),((5*pWid)/6-20,pHei))
                        else:
                            p2BoxVul = pygame.Rect((player2.left-(pWid/8)+20,player2.top),((5*pWid)/6-30,pHei))
                else:
                    if (p1BoxVul.right+p1BoxVul.left) < (p2BoxVul.left+p2BoxVul.right):
                        p2BoxVul = pygame.Rect((player2.left+(pWid/3),player2.top),((5*pWid)/6-20,pHei))
                    else:
                        p2BoxVul = pygame.Rect((player2.left-(pWid/8)+10,player2.top),((5*pWid)/6-10,pHei))
            else:
                p2BoxVul = player2
        else:
            p2BoxVul = basic2
                
        # Adjust Attack Hitboxes
        
        basic = pygame.Rect((player.left,player.bottom-10),(pWid,10))
        basic2 = pygame.Rect((player2.left,player2.bottom-10),(pWid,10))
        
        if player.bottom == 700:
            if punch:
                if (p1BoxVul.right+p1BoxVul.left) < (p2BoxVul.left+p2BoxVul.right):
                    p1BoxAtt = pygame.Rect((player.right,player.top),(20,10))
                else:
                    p1BoxAtt = pygame.Rect((player.left-20,player.top),(20,10))
            elif kick:
                if (p1BoxVul.right+p1BoxVul.left)/2 < (p2BoxVul.left+p2BoxVul.right)/2:
                    if kickCount == 2 or kickCount == 3:
                        if kick2:
                            p1BoxAtt = gone
                        else:
                            p1BoxAtt = pygame.Rect((player.left+110,player.bottom-80),((9*(basic.left-basic.right))/10,80))
                    else:
                        if kick2:
                            p1BoxAtt = gone
                        else:
                            p1BoxAtt = pygame.Rect((player.left+90,player.bottom-80),((basic.left-basic.right)/2,80))
                else:
                    if kickCount == 2 or kickCount == 3:
                        if kick2:
                            p1BoxAtt = gone
                        else:
                            p1BoxAtt = pygame.Rect((player.left+70,player.bottom-80),((9*(basic.left-basic.right))/10,80))
                    else:
                        p1BoxAtt = pygame.Rect((player.left+80,player.bottom-80),((basic.left-basic.right)/2,80))
            else:
                p1BoxAtt = gone
        else:
            if (tapLeft or tapRight or knockLeft or knockRight or downLeft or downRight or fallDown):
                p1BoxAtt = gone
            else:
                p1BoxAtt = basic
        
        if player2.bottom == 700:
            if punch2:
                if (p2BoxVul.right+p2BoxVul.left) < (p1BoxVul.left+p1BoxVul.right):
                    if 0 < punch2Count < 6 or punch2Count > 11:
                        p2BoxAtt = gone2
                    else:
                        p2BoxAtt = pygame.Rect((player2.right,player2.top),(20,10))
                else:
                    if 0 < punch2Count < 6 or punch2Count > 11:
                        p2BoxAtt = gone2
                    else:
                        p2BoxAtt = pygame.Rect((player2.left-10,player2.top),(20,10))
            elif kick2:
                if (p2BoxVul.right+p2BoxVul.left)/2 < (p1BoxVul.left+p1BoxVul.right)/2:
                    if kick2Count == 2 or kick2Count == 3:
                        p2BoxAtt = pygame.Rect((player2.left+120,player2.bottom-80),((9*(basic2.left-basic2.right))/10,80))
                    else:
                        p2BoxAtt = pygame.Rect((player2.left+90,player2.bottom-80),((basic2.left-basic2.right)/2,80))
                else:
                    if kick2Count == 2 or kick2Count == 3:
                        p2BoxAtt = pygame.Rect((player2.left+70,player2.bottom-80),((9*(basic2.left-basic2.right))/10,80))
                    else:
                        p2BoxAtt = pygame.Rect((player2.left+80,player2.bottom-80),((basic2.left-basic2.right)/2,80))
            else:
                p2BoxAtt = gone2
        else:
            if (tap2Left or tap2Right or knock2Left or knock2Right or down2Left or down2Right or fall2Down):
                p2BoxAtt = gone2
            else:
                p2BoxAtt = basic2
        
        if p1 > 0:
            pygame.draw.rect(screen, (0,50,0), p1BoxVul)
            pygame.draw.rect(screen, (50,0,0), p1BoxAtt)
        if p2 > 0:
            pygame.draw.rect(screen, (0,50,0), p2BoxVul)
            pygame.draw.rect(screen, (50,0,0), p2BoxAtt)
        
        screen.blit(playerStretchedImage, player)
        screen.blit(player2StretchedImage, player2)
            
        # Take Damage / Knock back
        
        if p2 > 0:
            if not(kick or punch or moveUp or moveDown or stun):
                if p1BoxAtt.colliderect(p2BoxVul) and not(p1BoxAtt.colliderect(p2BoxAtt)):
                    dmg2 = 5
            else:
                if kick:
                    if p1BoxAtt.colliderect(p2BoxVul) or p2BoxVul.colliderect(p1BoxAtt):
                        a_kick.play()
                        if (p1BoxVul.right+p1BoxVul.left)/2 < (p2BoxVul.right+p2BoxVul.left)/2:
                            if not(knock2Right):
                                move2Down, fall2Down = False, False
                                if not(move2Up):
                                    knock2Right = True
                        else:
                            if not(knock2Left):
                                move2Down, fall2Down = False, False
                                if not(move2Up):
                                    knock2Left = True
                        dmg2 += 10
                    if dmg2 >= 10:
                        dmg2 = 10
                elif punch:
                    if p1BoxAtt.colliderect(p2BoxVul) or p2BoxVul.colliderect(p1BoxAtt):
                        a_punch.play()
                        if (p1BoxVul.right+p1BoxVul.left)/2 < (p2BoxVul.right+p2BoxVul.left)/2:
                            if not(tap2Right):
                                move2Down, fall2Down = False, False
                                if not(move2Up):
                                    tap2Right = True
                        else:
                            if not(tap2Left):
                                move2Down, fall2Down = False, False
                                if not(move2Up):
                                    tap2Left = True
                        dmg2 += 5
                    if dmg2 >= 5:
                        dmg2 = 5

        if not(kick or punch or moveUp or move2Down):
            if p2 > dmg2:
                p2 -= dmg2
            else:
                p2 -= p2
            dmg2 = 0
        
        if p1 > 0:
            if not(kick2 or punch2 or move2Up):
                if p2BoxAtt.colliderect(p1BoxVul) and not(p2BoxAtt.colliderect(p1BoxAtt)):
                    j_punch.play()
                    dmg1 = 5
            else:
                if kick2:
                    if p2BoxAtt.colliderect(p1BoxVul) or p1BoxVul.colliderect(p2BoxAtt):
                        j_kick.play()
                        if (p1BoxVul.left+p1BoxVul.right)/2 < (p2BoxVul.left+p2BoxVul.right)/2:
                            if not(knockLeft):
                                moveDown, fallDown = False, False
                                if not(moveUp):
                                    knockLeft = True
                            else:
                                pass
                        else:
                            if not(knockRight):
                                moveDown, fallDown = False, False
                                if not(moveUp):
                                    knockRight = True
                            else:
                                pass
                        dmg1 += 15
                    if dmg1 >= 15:
                        dmg1 = 15
                elif punch2:
                    if p2BoxAtt.colliderect(p1BoxVul) or p1BoxVul.colliderect(p2BoxAtt):
                        j_punch.play()
                        if (p1BoxVul.left+p1BoxVul.right)/2 < (p2BoxVul.left+p2BoxVul.right)/2:
                            if not(tapLeft):
                                moveDown, fallDown = False, False
                                if not(moveUp):
                                    tapLeft = True
                            else:
                                pass
                        else:
                            if not(tapRight):
                                moveDown, fallDown = False, False
                                if not(moveUp):
                                    tapRight = True
                            else:
                                pass
                        dmg1 += 25
                    if dmg1 >= 25:
                        dmg1 = 25
                    
        if not(kick2 or punch2 or moveDown or move2Up):
            if p1 > dmg1:
                p1 -= dmg1
            else:
                p1 -= p2
            dmg1 = 0

        # Draw Railing
            
        screen.blit(railStretched,rail)
        
        # Update display
        
        pygame.display.flip()
        
        clock.tick(30)
        
start()
shatter()
instructions()
count()
play()
