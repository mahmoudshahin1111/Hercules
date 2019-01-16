import pygame
from spritesheet import *
from pygame.mixer import *
import random

'''
actions:idel-walk-run-attack
moving:start position - end position


'''
class HellHound:
    def __init__(self,x,y):
        hellHoundIdelSheet=SpriteSheet(r'hell-hound\hell-hound-idle.png')
        hellHoundWalkSheet=SpriteSheet(r'hell-hound\hell-hound-walk.png')
        hellHoundJumplSheet=SpriteSheet(r'hell-hound\hell-hound-jump.png')
        hellHoundRunSheet=SpriteSheet(r'hell-hound\hell-hound-run.png')
        
        self.startPosition=[x,y]
        self.endPostion=[x,y]
        self.currentPosition=[x,y]
        self.idel=True
        self.left=False
        self.right=False
        self.run=False
        self.width=55
        self.height=30
        self.idelImages=[
                hellHoundIdelSheet.get_image(14,8,45,30),
                hellHoundIdelSheet.get_image(77,8,45,30),
                hellHoundIdelSheet.get_image(138,8,45,30),
                hellHoundIdelSheet.get_image(203,8,45,30),
                hellHoundIdelSheet.get_image(266,8,45,30),
                hellHoundIdelSheet.get_image(330,8,45,30),
        ]
        self.moveImages=[
                hellHoundWalkSheet.get_image(12,5,55,30),
                hellHoundWalkSheet.get_image(76,5,55,30),
                hellHoundWalkSheet.get_image(136,5,55,30),
                hellHoundWalkSheet.get_image(268,5,55,30),
                hellHoundWalkSheet.get_image(331,5,55,30),
                hellHoundWalkSheet.get_image(395,5,55,30),
                hellHoundWalkSheet.get_image(460,5,55,30),
                hellHoundWalkSheet.get_image(522,5,55,30),
                hellHoundWalkSheet.get_image(580,5,55,30),
                hellHoundWalkSheet.get_image(650,5,55,30),
                hellHoundWalkSheet.get_image(715,5,55,30),
        ]
        self.runImages=[
                hellHoundRunSheet.get_image(10,0,50,30),
                hellHoundRunSheet.get_image(80,0,50,30),
                hellHoundRunSheet.get_image(150,0,50,30),
                hellHoundRunSheet.get_image(210,0,50,30),
                hellHoundRunSheet.get_image(280,0,50,30),
        ]
        self.imageIndex=0
        self.flipped=False
        self.rangeAttack=100
        self.objectCatched=False
        self.maxDelay=10
        self.isDead=False
        self.Health=60
        self.attackSound=[]
        '''
            pygame.mixer.Sound(r'\monster\monster-1.wav'),
            pygame.mixer.Sound(r'\monster\monster-2.wav'),
            pygame.mixer.Sound(r'\monster\monster-3.wav'),
            pygame.mixer.Sound(r'\monster\monster-4.wav'),
            pygame.mixer.Sound(r'\monster\monster-5.wav'),
            pygame.mixer.Sound(r'\monster\monster-6.wav'),
            pygame.mixer.Sound(r'\monster\monster-7.wav'),
            pygame.mixer.Sound(r'\monster\monster-8.wav'),
            pygame.mixer.Sound(r'\monster\monster-9.wav'),
            pygame.mixer.Sound(r'\monster\monster-10.wav'),
            pygame.mixer.Sound(r'\monster\monster-11.wav'),
            pygame.mixer.Sound(r'\monster\monster-12.wav'),
        ]'''
    def Draw(self,screen,delay):
        tempImageList=[]
        if self.left:
            if self.run:
                tempImageList=self.runImages
            else:
                tempImageList=self.moveImages
            self.flipped=False
        elif self.right:
            if self.run:
                tempImageList=self.runImages
            else:
                tempImageList=self.moveImages
            self.flipped=True
        else:
            self.idel=True
            tempImageList=self.idelImages
            
        if self.imageIndex>=len(tempImageList)-1:
            self.imageIndex=0
        screen.blit(pygame.transform.flip(tempImageList[self.imageIndex],self.flipped,False),self.currentPosition)
        if delay%self.maxDelay==0:
            self.imageIndex+=1
            
    def CheckRedRange(self,heroPosition):
        hX=heroPosition[0]
        hY=heroPosition[1]
        hleft=heroPosition[0]
        hright=heroPosition[0]+25#hero width
        left=self.currentPosition[0]
        right=self.currentPosition[0]+self.width
        xRange=[self.currentPosition[0]-self.rangeAttack,self.currentPosition[0]+self.rangeAttack]
        yRange=[self.currentPosition[1],self.currentPosition[1]-self.height]
        if (hX<xRange[1] and hX>xRange[0]) and (hY<yRange[0] and hY>yRange[1]):
            self.run=True
            if ((right<hright and right>hleft) or (left<hright and left>hleft)):
                if hY<yRange[0] and hY>yRange[1]:
                    return True
            self.endPostion=heroPosition
        else:
            self.run=False
            self.endPostion=[self.startPosition[0],self.startPosition[1]]
        return False
    def playAttackSound(self):
        for sf in self.attackSound:
            sf.play()
    def Move(self):
        xChange=0
        byX=1
        if self.run:
            byX*=3
        currentX=self.currentPosition[0]
        endX=self.endPostion[0]
        self.right=False
        self.left=False
        if currentX != endX:
            if currentX<endX:
                xChange=byX
                self.right=True
            elif currentX>endX:
                xChange=-byX
                self.left=True
        else:
            xChange=0
            return False
        self.currentPosition[0]+=xChange
        return True
        
    def Update(self,heroPosition,delay):
        if self.isDead:
            print 'Dog is dead'
            return
        goToStartPosition=False
        
        hX=heroPosition[0]
        hY=heroPosition[1]
        currentX=self.currentPosition[0]
        currentY=self.currentPosition[1]
        
        self.objectCatched=self.CheckRedRange(heroPosition)
        if self.objectCatched:
            self.right=False
            self.left=False
        else:
            if delay%self.maxDelay==0:
                moved=self.Move()
                
    def isCatchObject(self):
        return self.objectCatched
    def isHit(self):
        if self.Health>=0:
            self.Health-=50
        else:
            self.isDead=True
        

        
        
    