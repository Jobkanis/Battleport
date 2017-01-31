import random
import math
import time
import copy
import pygame

import class_Player
import class_Positions
import class_Game

class Boat:

    def __init__(self, gameclass, player, kind):
        ###################################################
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

        self.Player = player
        self.Kind = kind
        self.Name = "empty"
        self.Health = -1
        self.MaxHealth = -1
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
                self.Health = 1 #2
                self.MaxHealth = 2
                self.Size = 2
                self.MovementRange = 50# 3
                self.X_AttackRange = 2
                self.Y_AttackRange = 2
                self.DefensiveRange = 3
            if kind == "size31":
                self.Name = ["Silver whisper", "Sea Spirit"][LocalBoatName]
                self.Health = 1 #3
                self.MaxHealth = 3
                self.Size = 3
                self.MovementRange = 50#2
                self.X_AttackRange = 3
                self.Y_AttackRange = 3
                self.DefensiveRange = 4
            if kind == "size32":
                self.Name = ["Windsurf", "Intensity"][LocalBoatName]
                self.Health = 1# 3
                self.MaxHealth = 3
                self.Size = 3
                self.MovementRange = 50# 2
                self.X_AttackRange = 3
                self.Y_AttackRange = 3
                self.DefensiveRange = 4
            if kind == "size4":
                self.Name = ["Merapi", "Amadea"][LocalBoatName]
                self.Health = 1#4
                self.MaxHealth = 4
                self.Size = 4
                self.MovementRange = 50#1
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

    def ChangeBoatPosition(self, PositionToMove, AvaibleMovements):
        xplus = 0
        yplus = 0

        NextPosition = self.GetXandYchangeoutofpositionChange(PositionToMove)
        xplus = NextPosition[0]
        yplus = NextPosition[1]

        if self.CheckIfPositionTaken(self.X + xplus, self.Y + yplus, self.DefensiveStance) == True:
            self.ResetBoatPositions()
            self.X += xplus
            self.Y += yplus
            self.UpdateBoatPositions()
            print("PositionChange succes!")
        else:
            print("Error: changing position not possible!")

        #checkifonendofmap
        if self.Player == self.Game.Player1:
            goal = 19
            spawn = 0
            NextPlus = 1
        elif self.Player == self.Game.Player2:
            goal = 0
            spawn = 19
            NextPlus = -1
        else:
            goal = -1
            spawn = -1
            NextPlus = -1

        if self.Y == goal:
            #end reached
            print(self.Health)
            if self.Health < self.MaxHealth:
                self.Health += 1
                #update visual!!!!
            print(self.Health)

            NextY = spawn + (self.Size - 1) * NextPlus
            succes = False

            xplus = 0
            multiplier = 0
            var = False
            plus = 1

            while succes == False:

                xplus = xplus + multiplier * plus

                if self.CheckIfPositionTaken(self.X + xplus, NextY, self.DefensiveStance) == True:
                    self.ResetBoatPositions()
                    self.Y = NextY
                    self.X = self.X + xplus
                    self.UpdateBoatPositions()
                    succes = True
                    print("PositionChange succes!")
                    return 0

                else:
                    if var: plus = 1
                    else: plus = -1
                    var = not var
                    multiplier += 1 

                print (xplus)

                if xplus < -22:
                    print("placement error: removing boat")
                    self.DealDamage(1000)
                    return 0

        return AvaibleMovements

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

    def GetXandYchangeoutofpositionChange(self, PositionToMove): #returns [xplus, yplus]
        xplus = 0
        yplus = 0

        if  PositionToMove == "left":
            xplus += -1
        elif PositionToMove == "right":    
            xplus += 1

        elif self.Player == self.Game.Player1:
            if PositionToMove == "forward":
                yplus += 1
            elif PositionToMove == "backward":
                yplus += -1

        elif self.Player == self.Game.Player2:
            if PositionToMove == "forward":
                yplus -= 1
            elif PositionToMove == "backward":
                yplus -= -1        
        return [xplus, yplus]

############# STANCE ######################

    def GetPossibleDefensiveStance(self):

        PossileLeftStance = self.CheckIfPositionTaken(self.X, self.Y, "left")
        PossibleRightStance = self.CheckIfPositionTaken(self.X, self.Y, "right")
        PossibleInactiveStance = self.CheckIfPositionTaken(self.X, self.Y, "inactive")
        
        PossibleActions = []
        
        if self.DefensiveStance == "inactive":

            if PossileLeftStance == True:
                PossibleActions.append("left")
            if PossibleRightStance == True:
                PossibleActions.append("right")

        elif self.DefensiveStance == "left" or self.DefensiveStance == "right":
            if PossibleInactiveStance == True:
                PossibleActions.append("inactive")

        return PossibleActions #returns list of possible stance ("left", "right", "inactive")

    def GetPossibleMovement(self):  #returns list of possible movement actions ("left", "right", "forward", "backward")
        PossibleActions = []
        if self.DefensiveStance == "inactive":
            
            LocalPosition = self.GetXandYchangeoutofpositionChange("left")
            PossileLeft = self.CheckIfPositionTaken(self.X + LocalPosition[0], self.Y + LocalPosition[1], self.DefensiveStance)

            LocalPosition = self.GetXandYchangeoutofpositionChange("right")
            PossibleRight = self.CheckIfPositionTaken(self.X + LocalPosition[0], self.Y + LocalPosition[1], self.DefensiveStance)

            LocalPosition = self.GetXandYchangeoutofpositionChange("forward")
            PossibleForward = self.CheckIfPositionTaken(self.X + LocalPosition[0], self.Y + LocalPosition[1], self.DefensiveStance)

            LocalPosition = self.GetXandYchangeoutofpositionChange("backward")
            PossibleBackward = self.CheckIfPositionTaken(self.X + LocalPosition[0], self.Y + LocalPosition[1], self.DefensiveStance)
            
            if PossileLeft == True:
                PossibleActions.append("left")    
            if PossibleRight == True:
                PossibleActions.append("right")
            if PossibleForward == True:
                PossibleActions.append("forward")
            if PossibleBackward == True:
                PossibleActions.append("backward")
            
        return PossibleActions

############# PICK BOAT ###################

    def PickBoatPosition(self):

        Player1 = self.Game.Player1
        Player2 = self.Game.Player2
        Emptyplayer = self.Game.EmptyPlayer

        check = False

        while check == False:
            #### PICKING POSITION TO PLACE BOAT: YET TO BE IMPLEMENTED ####
            allowedpositions = []
            if self.Player == Player1:
                y = 0 + self.Size - 1
            elif self.Player == Player2:
                y = 19 - self.Size + 1
            else: 
                return(self.Game.GetPosition(-1,-1))

            for x in range(0,20):
                check = self.CheckIfPositionTaken(x,y, "inactive")
                if check == True:
                    localposition = self.Game.GetPosition(x,y)
                    allowedpositions.append(localposition)

            MessageBox1Tekst = " " * 41 + "Select a place to place your boat"
            MessageBox2Tekst = "Boat to place: " + str(self.Name) + " | Size: " + str(self.Size) +  "| Health: " + str(self.Health)
            length = len(MessageBox2Tekst)
            spacenum = 72 - length
            halfspacenum = int(spacenum / 2)
            MessageBox2Tekst = " " * halfspacenum + MessageBox2Tekst
            coordinate = self.Game.Visual.selectcoordinate(allowedpositions, [], False, MessageBox1Tekst, MessageBox2Tekst)
            return coordinate


############ GET ATTACKED #################
    def DealDamage(self, damageamount):

        self.Health -= damageamount

        if self.Health <= 0:
            LocalPositions = self.GetLocalBoatsPositions(True, -1, -1, 'inactive')
            for localpos in LocalPositions:
                localpos.Boat = self.Game.EmptyBoat
            self.Player.DeleteBoat(self)

############## POSITION CHECKS ############

    def GetPositionsInreachToAttack(self):
        ownpositions = self.GetLocalBoatsPositions(True, -1,-1,"inactive")

        attackpositions = []

        if self.DefensiveStance == "inactive":
            for pos in ownpositions:
                y = pos.Y
                x = pos.X
                
                PlusLeft = False
                PlusRight = False
                #yrange
                for Range in range(1, self.Y_AttackRange + 1):
                    if self.Player == self.Game.Player1:
                        localpos1 = self.Game.GetPosition(x, y - Range)
                        localpos2 = self.Game.GetPosition(x, y + Range)

                    elif self.Player == self.Game.Player2:
                        localpos1 = self.Game.GetPosition(x, y + Range)
                        localpos2 = self.Game.GetPosition(x, y - Range) #somehow adds all coordinates where from boat (size - 1 + range)
                
                    if localpos1 != self.Game.EmptyPosition and localpos1.Boat != self and PlusLeft == False:
                        attackpositions.append(localpos1)
                        if localpos1.Boat != self.Game.EmptyBoat:
                            PlusLeft = True

                    if localpos2 != self.Game.EmptyPosition and localpos2.Boat != self and PlusRight == False:
                        attackpositions.append(localpos2)
                        if localpos2.Boat != self.Game.EmptyBoat:
                            PlusRight = True

                #xrange
                PlusUp = False
                PlusDown = False
                for i in range(1, self.X_AttackRange + 1):
                    localpos3 = self.Game.GetPosition(x - i, y)
                    localpos4 = self.Game.GetPosition(x + i, y)
                    
                    if localpos3 != self.Game.EmptyPosition and localpos3.Boat != self and PlusUp == False:
                        attackpositions.append(localpos3)
                        if localpos3.Boat != self.Game.EmptyBoat:
                            PlusUp = True

                    if localpos4 != self.Game.EmptyPosition and localpos4.Boat != self and PlusDown == False:
                        attackpositions.append(localpos4)
                        if localpos4.Boat != self.Game.EmptyBoat:
                            PlusDown = True

        else:

            for pos in ownpositions:

                y = pos.Y
                x = pos.X

                PlusLeft2 = False
                PlusRight2 = False

                for i in range(1, self.DefensiveRange + 1):
                    
                    localpos1 = self.Game.GetPosition(x, y+i)
                    localpos2 = self.Game.GetPosition(x, y-i)

                    if localpos1 != self.Game.EmptyPosition and localpos1.Boat != self and PlusLeft2 == False:
                        attackpositions.append(localpos1)    
                        if localpos1.Boat != self.Game.EmptyBoat:
                            PlusLeft2 = True

                    if localpos2 != self.Game.EmptyPosition and localpos2.Boat != self and PlusRight2 == False:
                        attackpositions.append(localpos2)
                        if localpos2.Boat != self.Game.EmptyBoat:
                            PlusRight2 = True

        return(attackpositions)

    def GetBoatsInReachToAttack(self):

        PositionsInReach = self.GetPositionsInreachToAttack()

        if self.Player == self.Game.Player2:
            opponent = self.Game.Player1
        elif self.Player == self.Game.Player1:
            opponent = self.Game.Player2
        print(opponent.Name)

        BoatPositionsOfOpponent = opponent.GetPlayerBoatPositions([])
    
        BoatsInReach = []
        for pos in PositionsInReach:
            if pos in BoatPositionsOfOpponent:
                if pos.Boat not in BoatsInReach:
                    BoatsInReach.append(pos.Boat)     

        return BoatsInReach

#########################################################################
    def CheckIfPositionTaken(self, x, y, defensivestance):


        Exception = []
        Exception.append(self)

        TakenSpots = self.Game.GetAllBoatPositions(Exception)
        FutureBoatCoordinates = self.GetLocalBoatsPositions(False, x, y, defensivestance)

        for FutureBoatCoordinate in FutureBoatCoordinates:
            for Takenspot in TakenSpots:
                if (Takenspot.X, Takenspot.Y) == (FutureBoatCoordinate.X, FutureBoatCoordinate.Y):                        #make sure it is not the standard one
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