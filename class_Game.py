import random
import math
import time
import copy
import pygame

import class_Player
import class_Boats
import class_Positions

class Game:
    def __init__(self):
        #creating classes

        ######### Empty Variables ###########
        self.Players = []
        self.Positions = []

        self.EmptyBoat = NotImplemented
        self.EmptyPosition = NotImplemented
        self.EmptyPlayer = NotImplemented
        self.Player1 = NotImplemented
        self.Player2 = NotImplemented

        ########## Empty Classes ##########
        self.EmptyPlayer = class_Player.Player(self, "empty")
        self.Players.append(self.EmptyPlayer)

        self.EmptyPosition = class_Positions.Position(self, -1, -1)
        self.Positions.append(self.EmptyPosition)
        

        self.EmptyBoat = class_Boats.Boat(self, self.EmptyPlayer, "empty")
        self.EmptyPlayer.Boats.append(self.EmptyBoat)

        ################ Players ###################
        self.CreatePositions() #Create all positions

        self.Player1 = class_Player.Player(self, "player1")
        self.Players.append(self.Player1)

        self.Player2 = class_Player.Player(self, "player2")
        self.Players.append(self.Player2)

        self.Player1.CreateBoats()
        self.Player2.CreateBoats()        

    def Play(self):
        self.Player_Playing = self.Player2        
        while self.Checkifwon() == self.EmptyPlayer:
            self.Player_Playing = self.NextPlayer()
            print("\nIt is " + self.Player_Playing.Name + " his turn")
            self.Player_Playing.PlayTurn()

############# USEABLE GAME FUNCTIONS #############
    def GetPosition(self, x, y):
        for Pos in self.Positions:
            if Pos.X == x and Pos.Y == y:
                return Pos
        return self.EmptyPosition

    def GetBoat(self, x, y):
        for LocalBoats in GetBoatPositions(self):
            if LocalBoats.X == x and LocalBoats.Y == y:
                return LocalBoats
        for LocalPlayers in self.Players:
            for boat in LocalPlayers.Boats:
                if boat.X == x and boat.Y == y:
                    return boat
        else: return self.EmptyBoat

############### SPECIFIC GAME FUNCTIONS ###################

    
    def Checkifwon(self):
        print("Check if player won: yet to be implemented: return won player else EmptyPlayer")
        return self.EmptyPlayer

    def NextPlayer(self):
        if self.Player_Playing == self.Player1:
            return self.Player2
        else:
            return self.Player1    
   
    def CreatePositions(self):
        print("Creating positions")
        for y in range (0,20):
            for x in range (0,20):
                LocalPosition = class_Positions.Position(self, x, y)
                self.Positions.append(LocalPosition)    

    def GetAllBoatPositions(self):
        BoatPositions = []
        BoatPositions += self.Player1.GetPlayerBoatPositions()
        BoatPositions += self.Player2.GetPlayerBoatPositions()
        return BoatPositions
