import pygame
import time


pygame.init()
pygame.mixer.init()

s=pygame.mixer.Sound("C:\Users\u1\Documents\github\Hero-1\Gothic-hero\Justin-Bieber-Sorry-PURPOSE-The-Movement.mp3")
pygame.mixer.Sound.play(s)
#s.set_volume(200)
c = raw_input()
print 'sound played'