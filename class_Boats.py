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
        Players = self.Game.Players
        EmptyPlayer= self.Game.EmptyPlayer
        Player1 = self.Game.Player1
        Player2 = self.Game.Player2

        Positions = self.Game.Positions
        EmptyPosition = self.Game.EmptyPosition

        EmptyBoat = self.Game.EmptyBoat
        ###################################################

        self.Player = player
        self.Kind = kind
        self.Name = "empty"
        self.Health = -1
        self.Size = 1
        self.MovementRange = 0
        self.X_AttackRange = 0
        self.Y_AttackRange = 0
        self.DefensiveRange = 0

        self.Perks = "none"
        #differentStance = ["inactive", "left", "right"]
        self.DefensiveStance = "inactive"

        self.X = -1
        self.Y = -1

        if self.Player == EmptyPlayer: 
            LocalBoatName = -1
        elif self.Player == Player1:
            LocalBoatName = 0
        elif self.Player == Player2:
            LocalBoatName = 1
        else:
            LocalBoatName = -2


        #BoatKinds = ["size2", "size31", "size32", "size4"]
        if LocalBoatName == 0 or LocalBoatName == 1:    
            if kind == "size2":
                self.Name = ["Furgo Saltire", "Santa Bettina"][LocalBoatName]
                self.Health = 2
                self.Size = 2
                self.MovementRange = 3
                self.X_AttackRange = 2
                self.Y_AttackRange = 2
                self.DefensiveRange = 3
            if kind == "size31":
                self.Name = ["Silver whisper", "Sea Spirit"][LocalBoatName]
                self.Health = 3
                self.Size = 3
                self.MovementRange = 2
                self.X_AttackRange = 3
                self.Y_AttackRange = 3
                self.DefensiveRange = 4
            if kind == "size32":
                self.Name = ["Windsurf", "Intensity"][LocalBoatName]
                self.Health = 3
                self.Size = 3
                self.MovementRange = 2
                self.X_AttackRange = 3
                self.Y_AttackRange = 3
                self.DefensiveRange = 4
            if kind == "size4":
                self.Name = ["Merapi", "Amadea"][LocalBoatName]
                self.Health = 4
                self.Size = 4
                self.MovementRange = 1
                self.X_AttackRange = 4
                self.Y_AttackRange = 4
                self.DefensiveRange = 5          
        
        if self.Player != EmptyPlayer:
            BoatPosition = self.PickBoatPosition() #returns position class
            if BoatPosition in self.Game.Positions: #makes sure the position exists: fixes error in creating empty class"
                self.X = BoatPosition.X
                self.Y = BoatPosition.Y
                BoatPosition.Boat = self
                TakenPositions = self.GetLocalBoatsPositions(True, -1, -1, "inactive")
                for LocalPosition in TakenPositions:
                    LocalPosition.Boat = self

############# POSITION CHANGE #############
    def ChangeBoatPosition(self, plus, yplus):
        if self.CheckIfPositionTaken(self.X + xplus, self.Y + yplus, self.DefensiveStance) == True:
            self.ResetBoatPositions()
            self.X += xplus
            self.Y += yplus
            self.UpdateBoatPositions()
            print("PositionChange succes!")
        else:
            print("Error: changing position not possible!")

    def ChangeBoatStance(self, FutureStance):
        if self.CheckIfPositionTaken(self.X, self.Y, FutureStance) == True:
            self.ResetBoatPositions()
            self.DefensiveStance = FutureStance
            self.UpdateBoatPositions()
            print("stance is changed!")
        else:
            print("Error: changing stance not possible!")

    def ResetBoatPositions(self):
        CurrentPositions = self.GetLocalBoatsPositions(True, -1,-1,"inactive")
        for Cpos in CurrentPositions:
            localpos = self.Game.GetPosition(Cpos.X, Cpos.Y)
            localpos.Boat = self.Game.EmptyBoat
                    
    def UpdateBoatPositions(self):
        CurrentPositions = self.GetLocalBoatsPositions(True, -1,-1,"inactive")
        for Cpos in CurrentPositions:
            localpos = self.Game.GetPosition(Cpos.X, Cpos.Y)
            localpos.Boat = self
        print("updated")
############# STANCE ######################

    def GetPossibleDefensiveStance(self):
        PossileLeftStance = self.CheckIfPositionTaken(self.X, self.Y, "left")
        PossibleRightStance = self.CheckIfPositionTaken(self.X, self.Y, "right")
        PossibleInactiveStance = self.CheckIfPositionTaken(self.X, self.Y, "right")
        
        PossibleActions = []
        
        if self.DefensiveStance == "inactive":
            if PossileLeftStance == True:
                PossibleActions.append("left")
            if PossibleRightStance == True:
                PossibleActions.append("right")
        elif self.DefensiveStance == "left" or self.DefensiveStance == "right":
            if PossibleInactiveStance == True:
                PossibleActions.append("inactive")

        return PossibleActions

############# PICK BOAT ###################

    def PickBoatPosition(self):

        Player1 = self.Game.Player1
        Player2 = self.Game.Player2
        Emptyplayer = self.Game.EmptyPlayer

        check = False

        while check == False:
            #### PICKING POSITION TO PLACE BOAT: YET TO BE IMPLEMENTED ####


            if self.Player == Player1:
                x = random.randint(1,19) #int(input("Player: " + self.Player.Name + "| Boat: " + self.Name + "| Insert X Postion (0-19): "))
                y = random.randint(0,4) #int(input("Player: " + self.Player.Name + "| Boat: " + self.Name + "| Insert Y Postion (0-19): "))
            elif self.Player == Player2:
                x = random.randint(1,19) #int(input("Player: " + self.Player.Name + "| Boat: " + self.Name + "| Insert X Postion (0-19): "))
                y = random.randint(15,19) #int(input("Player: " + self.Player.Name + "| Boat: " + self.Name + "| Insert Y Postion (0-19): ")) 
            else:
                x = -1; x = -1 #definately triggers the loop
            

            ###############################################################

            check = self.CheckIfPositionTaken( x, y, "inactive")
            
            if check == False:
                print("Boat could not be placed on coordinates: " + str(x) + " , " + str(y))
            else:
                print("Player: " + self.Player.Name + "| Boat: " + self.Name + "| Coordinates: " + str(x) + " , " + str(y))
        

        #when finally a good coordinate: return the position
        return self.Game.GetPosition(x,y) 

    def CheckIfStancePossible(self):
            PossileLeftStance = CheckIfPositionTaken(self, False, self.X, self.Y, "left")
            PossibleRightStance = CheckIfPositionTaken(self, self.X, self.Y, "right")
            PossibleInactiveStance = CheckIfPositionTaken(self, self.X, self.Y, "inactive")
            PossibleActions = []
        
            if self.DefensiveStance == "inactive":
                if PossibleLeftStance == True:
                    PossibleActions.append("left")
                if PossibleRightStance == True:
                    PossibleActions.append("left")
            elif self.DefensiveStance == "left" or self.DefensiveStance == "right":
                if PossibleInactiveStance == True:
                    PossibleActions.append("inactive")

            return PossibleActions

############## POSITION CHECKS ############
    def CheckIfPositionTaken(self, x, y, defensivestance):

        TakenSpots = self.Game.GetAllBoatPositions()
        FutureBoatCoordinates = self.GetLocalBoatsPositions(False, x, y, defensivestance)

        for FutureBoatCoordinate in FutureBoatCoordinates:
            for Takenspot in TakenSpots:
                if Takenspot.X == FutureBoatCoordinate.X and Takenspot.Y == FutureBoatCoordinate.Y:
                    return False
            if FutureBoatCoordinate == self.Game.EmptyPosition:
                 return False
        return True

    def GetLocalBoatsPositions(self, UseCurrentPosition, x, y, defensivestance):  #when usecurrentposition == True: x and y don't matter  
        if UseCurrentPosition == True:
            X = self.X
            Y = self.Y
            LocalDefensiveStance = self.DefensiveStance
        else:
            X = x
            Y = y
            LocalDefensiveStance = defensivestance

        BoatPositions = []
        for i in range(0, self.Size):
            if LocalDefensiveStance == "inactive":
                if self.Player == self.Game.Player1:
                    BoatPositions.append(self.Game.GetPosition(X, Y - i))
                elif self.Player == self.Game.Player2:
                    BoatPositions.append(self.Game.GetPosition(X, Y + i))
            elif LocalDefensiveStance == "right":
                BoatPositions.append(self.Game.GetPosition(X + i, Y))
            elif LocalDefensiveStance == "left":
                BoatPositions.append(self.Game.GetPosition(X - i, Y))
        return BoatPositions
    