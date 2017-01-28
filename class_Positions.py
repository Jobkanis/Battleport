import random
import math
import time
import copy
import pygame

import class_Player
import class_Boats
import class_Game

class Position:
    def __init__(self, gameclass, x, y):
        ####################################################
        #For educational purposes
        self.Game = gameclass
        Players = self.Game.Players
        EmptyPlayer= self.Game.EmptyPlayer
        Player1 = self.Game.Player1
        Player2 = self.Game.Player2

        Positions = self.Game.Positions
        EmptyPosition = self.Game.EmptyPosition

        EmptyBoat = self.Game.EmptyBoat

        ###################################################

        self.ContainsBomb = True 
        self.BombActivated = False
  
        self.X = x 
        self.Y = y 
        self.Boat = EmptyBoat

    def __str__(self):
        return " (" + str(self.X) + " , " + str(self.Y) + ")"