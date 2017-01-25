import pygame
import class_Menu
pygame.init()


################  BACKGROUND MUSIC  ################
pygame.mixer.music.load("sound/rockit.wav")
pygame.mixer.music.play(-1)


################  COLORS  ################
darkblue = (15,15,23)


################  SCREENSIZE  ################
width = 1280
height = 720
size = (width,height)


################  GAME DISPLAY  ################
gameDisplay = pygame.display.set_mode(size)
pygame.display.set_caption('Battleport')
clock = pygame.time.Clock()


################  START MENU  ################
Menu = class_Menu.Menu()

Menu.menu_start('main menu')


