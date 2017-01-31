#running game
import random
import math
import time
import copy
import pygame

#PlayerNames = ["empty", "player1", "player2"]
#BoatKinds = ["size2", "size31", "size32", "size4"]
#Perks = ["none"]

#import class_Player
#import class_Boats
#import class_Positions
#import class_Game
import class_Menu
import class_Visual
import class_Game
import class_Player
import class_Boats

pygame.init()

#start menu  (remove """)

################  BACKGROUND MUSIC  ################
pygame.mixer.music.load("sound/background_music.wav")
pygame.mixer.music.play(-1)


################  SCREENSIZE  ################
width = 1280
height = 720
size = (width,height)

################  GAME DISPLAY  ################
gameDisplay = pygame.display.set_mode(size)
pygame.display.set_caption('Battleport')
clock = pygame.time.Clock()

################  START MENU  ################
NewGame = class_Game.Game(gameDisplay, clock, width, height)
Menu = class_Menu.Menu(NewGame, gameDisplay, clock, width, height)
Menu.menu_start('main menu')


#start game (remove """)

################ START GAME ###################






