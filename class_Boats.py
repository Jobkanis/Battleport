import random
import math
import time
import copy
import pygame

import class_Player
import class_Positions
import class_Game

class Boat:
    def __init__(self, game, player, kind):
        ####################################################
        self.Game = game

        #For educational purposes
        self.Players = self.Game.Players
        self.EmptyPlayer=self.Game.EmptyPlayer
        self.Player1 = self.Game.Player1
        self.Player2 = self.Game.Player2

        self.Positions = self.Game.Positions
        self.EmptyPosition = self.Game.EmptyPosition

        self.EmptyBoat = self.Game.EmptyBoat
        ###################################################

        self.Player = player
        self.Kind = kind
        self.Name = "empty"
        self.Health = -1
        self.MovementRange = 0
        self.X_AttackRange = 0
        self.Y_AttackRange = 0
        self.DefensiveRange = 0

        if self.Player == self.EmptyPlayer: 
            LocalBoatName = -1
        elif self.Player == self.Player1:
            LocalBoatName = 0
        elif self.Player == self.Player2:
            LocalBoatName = 1
        else:
            LocalBoatName = -2


        #BoatKinds = ["size2", "size31", "size32", "size4"]
        if LocalBoatName == 0 or LocalBoatName == 1:    
            if kind == "size2":
                self.Name = ["Furgo Saltire", "Santa Bettina"][LocalBoatName]
                self.Health = 2
                self.MovementRange = 3
                self.X_AttackRange = 2
                self.Y_AttackRange = 2
                self.DefensiveRange = 3
            if kind == "size31":
                self.Name = ["Silver whisper", "Sea Spirit"][LocalBoatName]
                self.Health = 3
                self.MovementRange = 2
                self.X_AttackRange = 3
                self.Y_AttackRange = 3
                self.DefensiveRange = 4
            if kind == "size32":
                self.Name = ["Windsurf", "Intensity"][LocalBoatName]
                self.Health = 3
                self.MovementRange = 2
                self.X_AttackRange = 3
                self.Y_AttackRange = 3
                self.DefensiveRange = 4
            if kind == "size4":
                self.Name = ["Merapi", "Amadea"][LocalBoatName]
                self.Health = 4
                self.MovementRange = 1
                self.X_AttackRange = 4
                self.Y_AttackRange = 4
                self.DefensiveRange = 5          
        
        self.Perks = "none"
        self.DefensiveStance = False

        self.X = -1
        self.Y = -1
        if self.Player != self.EmptyPlayer:
            BoatPosition = self.PlaceBoats() #returns position class
            if BoatPosition in self.Game.Positions: #makes sure the position exists: fixes error in creating empty class"
                self.X = BoatPosition.X
                self.Y = BoatPosition.Y

    def PlaceBoats(self):
        print("Pick Boat Position: yet to be implemented!")
        x = random.randint(0,19) #int(input("Player: " + self.Player.Name + "| Boat: " + self.Name + "| Insert X Postion (0-19): "))
        y = random.randint(0,19) #int(input("Player: " + self.Player.Name + "| Boat: " + self.Name + "| Insert Y Postion (0-19): "))
        print("Player: " + self.Player.Name + "| Boat: " + self.Name + "| Coordinates: " + str(x) + " , " + str(y))
        LocalPosition = self.Game.GetPosition(x,y)
        return LocalPosition