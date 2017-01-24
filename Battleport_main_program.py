#running game
import random
import math
import time
import copy
import pygame

#PlayerNames = ["empty", "player1", "player2"]
#BoatKinds = ["size2", "size31", "size32", "size4"]
#Perks = ["none"]

import class_Player
import class_Boats
import class_Positions
import class_Game

NewGame = class_Game.Game()
CurrentGame = NewGame
CurrentGame.Play()