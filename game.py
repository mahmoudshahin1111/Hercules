from pygame import *
from constants import *
from spritesheet import *
import random
from HellHound import HellHound
from pygame.mixer import *
import time



pygame.font.init()
#window
screen=pygame.display.set_mode([640,480])

#hero
heroIdelSheet=SpriteSheet(r'Gothic-hero\gothic-hero-idle.png')
heroMoveSheet=SpriteSheet(r'Gothic-hero\gothic-hero-run.png')
heroJumpSheet=SpriteSheet(r'Gothic-hero\gothic-hero-jump.png')
heroAttackSheet=SpriteSheet(r'Gothic-hero\gothic-hero-attack.png')

heroWidth=50
heroHeight=45
#load animating images
heroIdelImgs=[
    heroIdelSheet.get_image(5,11,30,45),
    heroIdelSheet.get_image(45,11,30,45),
    heroIdelSheet.get_image(80,11,30,45),
    heroIdelSheet.get_image(120,11,30,45),
    ]
heroMovImgs=[
    heroMoveSheet.get_image(8,5,50,45),
    heroMoveSheet.get_image(78,5,50,45),
    heroMoveSheet.get_image(140,5,50,45),
    heroMoveSheet.get_image(210,5,50,45),
    heroMoveSheet.get_image(280,5,50,45),
    heroMoveSheet.get_image(340,5,50,45),
    heroMoveSheet.get_image(400,5,50,45),
    heroMoveSheet.get_image(475,5,50,45),
    heroMoveSheet.get_image(535,5,50,45),
    heroMoveSheet.get_image(610,5,50,45),
    heroMoveSheet.get_image(675,5,50,45),
    heroMoveSheet.get_image(735,5,50,45),
    ]
heroJumpImgs=[
    heroJumpSheet.get_image(70,25,55,45),
    heroJumpSheet.get_image(135,15,55,45),
    heroJumpSheet.get_image(190,5,55,45),
    heroJumpSheet.get_image(250,0,55,55),
    ]
heroAttackImgs=[
    heroAttackSheet.get_image(30,8,30,45),
    heroAttackSheet.get_image(115,10,45,45),
    heroAttackSheet.get_image(205,10,80,45),
    heroAttackSheet.get_image(305,10,70,45),
    heroAttackSheet.get_image(410,10,45,45),
    heroAttackSheet.get_image(510,10,45,45),
    ]
#attackSound=

#delay images
idelIndex=0
heroIdel=True
movIndex=0
heroMov=False
jumpIndex=0
heroJump=False
attackIndex=0
heroAttack=False
flipped=False
delay=0

#player actions
left=False
right=False
jump=False
fall=True
attack=False


#moving params
heroPos=[100,300]
MovSpeed=1
change_x=0
change_y=0
jumpSpeed=3
jumpCount=0
maxJump=40
attackCount=0
maxAttack=50
heroHealth=300
onFloor=False



#map
background=pygame.transform.scale(pygame.image.load(r'Map\old-dark-castle-interior-background.png'),(640,480))
castelSheet=SpriteSheet(r'Map\old-dark-castle-interior-tileset.png')
#meteric
floorWidth=32
floorHeight=22
floor=[
    #down floor
    [castelSheet.get_image(608,154,floorWidth,floorHeight),(0,400)],
    [castelSheet.get_image(608,154,floorWidth,floorHeight),(35,400)],
    [castelSheet.get_image(608,154,floorWidth,floorHeight),(70,400)],
    [castelSheet.get_image(608,154,floorWidth,floorHeight),(105,400)],
    [castelSheet.get_image(608,154,floorWidth,floorHeight),(140,400)],
    [castelSheet.get_image(608,154,floorWidth,floorHeight),(175,400)],
    [castelSheet.get_image(608,154,floorWidth,floorHeight),(210,400)],
    [castelSheet.get_image(608,154,floorWidth,floorHeight),(245,400)],
    [castelSheet.get_image(608,154,floorWidth,floorHeight),(280,400)],
    [castelSheet.get_image(608,154,floorWidth,floorHeight),(315,400)],
    [castelSheet.get_image(608,154,floorWidth,floorHeight),(350,400)],
    [castelSheet.get_image(608,154,floorWidth,floorHeight),(385,400)],
    [castelSheet.get_image(608,154,floorWidth,floorHeight),(420,400)],
    [castelSheet.get_image(608,154,floorWidth,floorHeight),(455,400)],
    [castelSheet.get_image(608,154,floorWidth,floorHeight),(490,400)],
    [castelSheet.get_image(608,154,floorWidth,floorHeight),(525,400)],
    [castelSheet.get_image(608,154,floorWidth,floorHeight),(560,400)],
    [castelSheet.get_image(608,154,floorWidth,floorHeight),(595,400)],
    [castelSheet.get_image(608,154,floorWidth,floorHeight),(630,400)],

    #upper floor

    [castelSheet.get_image(608,154,floorWidth,floorHeight),(350,210)],
    [castelSheet.get_image(608,154,floorWidth,floorHeight),(385,210)],
    [castelSheet.get_image(608,154,floorWidth,floorHeight),(420,210)],

    [castelSheet.get_image(608,154,floorWidth,floorHeight),(560,300)],
    [castelSheet.get_image(608,154,floorWidth,floorHeight),(595,300)],
    [castelSheet.get_image(608,154,floorWidth,floorHeight),(630,300)],
    ]

pygame.draw.rect(screen,(40,40,0),(0,0,100,30))
font = pygame.font.SysFont('iomanoid.ttf',14,True,True)
#enemys


# 0 idel - 1 attack - 2 move

hellHounds=[
    HellHound(300,380),
    HellHound(200,380),
    HellHound(100,380),
    ]
hellHoundImageDelay=0
maxHells=10
run = True


while run:
#MAP
    screen.blit(background,(0,0))
    screen.blits(floor)
    screen.blit(font.render("Health : ",False,(100,90,10)),(0,0))
    pygame.draw.rect(screen,(255,0,0),(0,20,300,10))
    pygame.draw.rect(screen,(0,255,0),(0,20,heroHealth,10))
    if heroHealth<=0:

        break
    for f in floor:
        fTop=f[1][1]+10
        fbottom=f[1][1]+floorHeight
        fLeft=f[1][0]
        fRight=f[1][0]+floorWidth
        heroBottom=heroPos[1]+heroHeight
        heroLeft=heroPos[0]+22
        heroRight=heroPos[0]+heroWidth
        if heroBottom<=fbottom and heroBottom>=fTop:
            if heroRight>=fLeft and heroLeft<=fRight:
                onFloor=True
                break
        onFloor=False
        fall=True
#enemys

    hellHoundImageDelay+=1
    for hellHound in hellHounds:
        if not hellHound.isDead:
            hellHound.Update(heroPos,hellHoundImageDelay)
            hellHound.Draw(screen,hellHoundImageDelay)
            if hellHound.isCatchObject():
                #hellHound.playAttackSound()
                if delay%100==0:
                    heroHealth-=20
                    print 'ooh it is hit me'
        else:
            hellHounds.remove(hellHound)
    if len(hellHounds) < maxHells:
        if delay%1000==0:
            r=random.randint(0, 20)
            if r==11:
                di=random.randint(0,2)
                if di==1:
                    h=HellHound(620,380)
                else:
                    h=HellHound(-20,380)
                h.startPosition=[random.randint(100,500),380]
                hellHounds.append(h)


#hero
    delay+=1
    if heroIdel:
        if flipped:
            heroImgFliped=pygame.transform.flip(heroIdelImgs[idelIndex],True,False)
            screen.blit(heroImgFliped,heroPos)
        else:
            screen.blit(heroIdelImgs[idelIndex],heroPos)
        if delay%15==0:
            if idelIndex==3:
                idelIndex=0
                delay=0
            else:
                idelIndex+=1

    elif heroMov:
        if flipped:
            heroImgFliped=pygame.transform.flip(heroMovImgs[movIndex],True,False)
            screen.blit(heroImgFliped,heroPos)
        else:
            screen.blit(heroMovImgs[movIndex],heroPos)
        if delay%6==0:
            if movIndex==11:
                movIndex=0
                delay=0
            else:
                movIndex+=1

    elif heroJump:
        if flipped:
            heroImgFliped=pygame.transform.flip(heroJumpImgs[jumpIndex],True,False)
            screen.blit(heroImgFliped,heroPos)
        else:
            screen.blit(heroJumpImgs[jumpIndex],heroPos)
        if delay%20==0:
            if jumpIndex==3:
                jumpIndex=0
                delay=0
            else:
                jumpIndex+=1

    elif heroAttack:
        if flipped:
            heroImgFliped=pygame.transform.flip(heroAttackImgs[attackIndex],True,False)
            screen.blit(heroImgFliped,heroPos)
        else:
            screen.blit(heroAttackImgs[attackIndex],heroPos)
        if delay%10==0:
            if attackIndex==5:
                attackIndex=0
                delay=0
            else:
                attackIndex+=1


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_a:
                left=True
            elif event.key==pygame.K_d:
                right=True
            if event.key==pygame.K_SPACE:
                if onFloor:
                    jump=True

        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_a:
                left=False
            if event.key==pygame.K_d:
                right=False
            if event.key==pygame.K_e:
                attack=True
#do movements
    if left:
        change_x = -MovSpeed
    elif right:
        change_x = +MovSpeed
    else:
        change_x=0

    if jump:
        if jumpCount<=maxJump:
            change_y =-jumpSpeed
        else:
            fall=True
            jump=False
            onFloor=False
            jumpCount=0
        jumpCount+=1

    elif fall:
        if onFloor:
            fall=False
            change_y=0
        else:
            change_y=jumpSpeed

    if attack:
        if attackCount<=maxAttack:
            attackCount+=1
        else:
            attack=False
            #attackSound.play()
            for hellHound in hellHounds:
                if hellHound.isCatchObject():
                    hellHound.isHit()
                    print 'I hit you'
            attackCount=0




#idel hero when no action
    if left==False and right==False and jump==False and attack==False and fall==False:
        heroJump=False
        heroMov=False
        heroAttack=False
        heroIdel=True
    else:
        if left:
            flipped=True
            heroMov=True
            heroAttack=False
            heroIdel=False
        elif right:
            flipped=False
            heroMov=True
            heroAttack=False
            heroIdel=False
        if jump:
            heroIdel=False
            heroMov=False
            heroAttack=False
            heroJump=True
        elif fall:
            heroIdel=False
            heroAttack=False
            jumpIndex=3
            heroJump=True
            heroMov=False
        elif attack:
            heroAttack=True
            heroIdel=False
            heroJump=False
            heroMov=False

    heroPos[0] += change_x
    heroPos[1] += change_y


    pygame.display.flip()
font = pygame.font.Font('iomanoid.ttf',50)
other=  pygame.font.Font('iomanoid.ttf',30)
sign=pygame.font.Font('iomanoid.ttf',20)
while 1:
    st_gameover="Game Over"
    i=130
    pygame.draw.rect(screen,(0,0,0),(0,0,640,480))
    for c in st_gameover:
        if delay%30==0:
            screen.blit(font.render(c,True,(255,255,255)),(i,200))
            screen.blit(other.render('if you want play again restart game.',True,(255,255,255)),(10,250))
            screen.blit(other.render('Thank You ..',True,(255,255,255)),(340,300))
            screen.blit(sign.render('By Mahmoud Shahin',True,(255,255,255)),(420,420))
            pygame.display.flip()
            time.sleep(0.2)
            i+=50
    delay+=1
        #time.sleep(1)
