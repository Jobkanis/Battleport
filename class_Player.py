import random
import math
import time
import copy
import pygame

import class_Boats
import class_Positions
import class_Game

class Player:

    def __init__(self, gameclass, playername):
        ####################################################
        #For educational purposes
        self.Game = gameclass
        Players = self.Game.Players
        EmptyPlayer= self.Game.EmptyPlayer
        Player1 = self.Game.Player1
        Player2 = self.Game.Player2

        Positions = self.Game.Positions
        EmptyPosition = self.Game.EmptyPosition

        EmptyBoat = self.Game.EmptyPosition
        ###################################################

        self.Name = playername
        self.Cards = []
        self.Boats = []

################### CALLABLE ########################

    def PlayTurn(self):
##########################Creating possibleaction value #########################
############for keeping track what the user did and can still do#################

        AvaibleBoatsToMove = []
        for LocalBoat in self.Boats:
            AvaibleBoatsToMove.append(LocalBoat.Name)

        AvaibleAttacks_No = 2

        AvaibleBoatsToAttack = []
        for LocalBoat in self.Boats:
            AvaibleBoatsToAttack.append(LocalBoat.Name)

        AvaiblePlayCards_No = 2

        #Taking a card
        if len(self.Cards) < 7:
            print("Takecard: yet to be implemented")


        #The actual possible moves the player can do (loop)
        LocalDone = False
        while LocalDone == False:
            if len(AvaibleBoatsToMove) > 0 or  AvaibleAttacks_No > 0 or AvaiblePlayCards_No > 0:
                
                self.CreateSea() #VISUAL

                LocalDone = self.Ask_End_Turn() #Check if player wants to end turn
                
                if LocalDone == False: # player does not want to stop his turn

                    #Actions: LocalAction = chosen action by user: returns "play cards", "attack", "move boat"
                
                    #CHOOSE ACTION TO DO
                    LocalAction = self.ChooseAction(AvaiblePlayCards_No, AvaibleAttacks_No, AvaibleBoatsToMove)
                    
############################### DOING ACTION #############################

                    if LocalAction == "play cards":

                        AvaiblePlayCards_No -= 1
                        self.PlayCards()

                    if LocalAction == "attack":

                        LocalBoatToAttack = self.ChooseBoat(AvaibleBoatsToAttack) #returns boat name
                        AvaibleBoatsToAttack.remove(LocalBoatToAttack)
                        LocalBoatToAttack = self.GetBoatFromName(LocalBoatToAttack)

                        AvaibleAttacks_No -= 1
                        

                        self.Attack()

                    if LocalAction == "move boat":

                        #CHOOSE BOAT TO MOVE

                        LocalBoatToMoveName = self.ChooseBoat(AvaibleBoatsToMove)

                        AvaibleBoatsToMove.remove(LocalBoatToMoveName)

                        LocalBoatToMove = self.GetBoatFromName(LocalBoatToMoveName)

                        self.MoveBoat(LocalBoatToMove)

            else:
                LocalDone = True

    def CreateBoats(self):
        self.Boats = []
        self.Boats.append(class_Boats.Boat(self.Game, self, "size2"))
        self.Boats.append(class_Boats.Boat(self.Game, self, "size31"))
        self.Boats.append(class_Boats.Boat(self.Game, self, "size32"))
        self.Boats.append(class_Boats.Boat(self.Game, self, "size4"))

##################  ACTIONS #########################

    def PlayCards(self):
        print("Choose a card to play: yet to be implemented")
        print("Play the card: yet to be implemented")

    def Attack(self):
        print("Check if ship in range: yet to be implemented")
        print("Chooseboat: yet to be implemented")
        print("Attackboat: yet to be implemented")

    def MoveBoat(self, BoatToMove):

        #CHOOSE MOVE ACTION TO DO

        AvaibleMovements = BoatToMove.MovementRange
        LocalDone = False

        while AvaibleMovements > 0 and LocalDone == False:
            PossibleStanceActions = BoatToMove.GetPossibleDefensiveStance()
            PossibleMovementActions = BoatToMove.GetPossibleMovement()

            print("You have " + str(AvaibleMovements) + " movements left.")

            self.CreateSea() #visual!

            InputText = "Possible actions("
            if len(PossibleStanceActions) > 0:
                InputText += "stance "
            if len(PossibleMovementActions) >0:
                InputText += "move " 
            InputText += "stop "
            InputText += "): "

            LocalInput = input(InputText)

            if len(PossibleStanceActions) > 0 and LocalInput == "stance":
                AvaibleMovements -= 1
                self.ChangeStance(BoatToMove, PossibleStanceActions)
                PossibleStanceActions = []

            if len(PossibleMovementActions) > 0 and LocalInput == "move":
                AvaibleMovements -= 1
                self.ChangePositionBoat(BoatToMove, PossibleMovementActions)
                PossibleMovementActions = []

            if LocalInput == "stop":
                print("Stopped moving boat")
                LocalDone = True

            if BoatToMove.X == False: #end reached
                print("Check if goal is reached: yet to be implemented")
                print("Take special card: yet to be implemented")
                print("Play the special card: yet to be implemented")
                LocalDone = True

################### Action functions ##########################

    def ChooseBoat(self, AvaibleBoats):
        print("Choosing a boat: yet to be implemented")
        return AvaibleBoats[0]

    def ChangeStance(self, boat, PossibleStance):
        if len(PossibleStance) > 0:

            PossibleStanceInactive = False
            PossibleStanceLeft = False
            PossibleStanceRight = False

            for LocalPossibleStance in PossibleStance:
                if LocalPossibleStance == "inactive":
                    PossibleStanceInactive = True
                elif LocalPossibleStance == "left":
                    PossibleStanceLeft = True
                elif LocalPossibleStance == "right":
                    PossibleStanceRight = True

        ############## GET INPUT AND POSSIBLESTANCE ######################
            InputText = "Change stance too: "

            if PossibleStanceInactive == True:
                InputText += "inactive "

            if PossibleStanceLeft == True:
                InputText += "left "

            if PossibleStanceRight == True:
                InputText += "right "

            LocalInput = input(InputText) #making player choose
    
       ###################################################################

            if PossibleStanceInactive == True and LocalInput == "inactive":
                boat.ChangeBoatStance("inactive")
            elif PossibleStanceLeft == True and LocalInput == "left":
                boat.ChangeBoatStance("left")
            elif PossibleStanceRight == True and LocalInput == "right":
                boat.ChangeBoatStance("right")

    def ChangePositionBoat(self, boat, possiblemovement):
        print("Move boat: yet to be implemented")
  
        PossibleForward = False
        PossibleBackward = False
        PossileLeft = False
        PossibleRight = False

        for LocalMovement in possiblemovement:
            if LocalMovement == "forward":
                PossibleForward = True
            elif LocalMovement == "backward":
                PossibleBackward = True
            elif LocalMovement == "left":
                PossileLeft = True
            elif LocalMovement == "right":
                PossibleRight = True

    ############## GET INPUT AND POSSIBLESTANCE ######################
        InputText = "Move boat: "

        if PossibleForward == True:
            InputText += "forward "

        if PossibleBackward == True:
            InputText += "backward "

        if PossileLeft == True:
            InputText += "left "
        if PossibleRight == True:
            InputText += "right "


        LocalInput = input(InputText) #making player choose
    
    ###################################################################

        if PossibleForward == True and LocalInput == "forward":
            boat.ChangeBoatPosition("forward")
        elif PossibleBackward == True and LocalInput == "backward":
            boat.ChangeBoatPosition("backward")
        elif PossileLeft == True and LocalInput == "left":
            boat.ChangeBoatPosition("left")
        elif PossibleRight == True and LocalInput == "right":
            boat.ChangeBoatPosition("right")

################### PickAction functions ##########################

    def Ask_End_Turn(self):
        LocalInput = input("End turn? (yes/no): ")
        if LocalInput == "yes":
            return True
        else: 
            return False
    
    def ChooseAction(self, AvaiblePlayCards_No, AvaibleAttacks_No, AvaibleBoatsToMove):
        #adding possible actions to list
        PossibleActions = []

        if AvaiblePlayCards_No > 0:
            PossibleActions.append("play cards("+ str(AvaiblePlayCards_No) + ")")

        if  AvaibleAttacks_No > 0:
            PossibleActions.append("attack(" + str(AvaibleAttacks_No) + ")")

        if len(AvaibleBoatsToMove) > 0:
            PossibleActions.append("move boat(" + str(len(AvaibleBoatsToMove)) + ")")


        #creating string of possible actions
        SelectActionText = ""
        for LocalPossibleAction in PossibleActions:
            SelectActionText += " | " + LocalPossibleAction
        
        SelectActionText = "Possible actions: " + SelectActionText +  "\n"


        #letting user pick an action
        LocalImput = input(SelectActionText)
        LocalAction = ""

        if LocalImput == "play cards" and AvaiblePlayCards_No > 0:
            LocalAction = "play cards"
            
        if LocalImput == "attack" and AvaibleAttacks_No > 0:
            LocalAction = "attack"

        if  LocalImput == "move boat" and len(AvaibleBoatsToMove) > 0:
            LocalAction = "move boat"
        
        return LocalAction   #returns "play cards", "attack", "move boat"

################### OTHER FUNCTIONS #######################

    def GetPlayerBoatPositions(self, exception):
        BoatPositions = []
        for PlayerBoats in self.Boats:
            for ExceptionBoats in exception:
                if PlayerBoats.Name != ExceptionBoats.Name:
                    BoatPositions += PlayerBoats.GetLocalBoatsPositions(True, -1, -1, "inactive")
        return BoatPositions

    def GetBoatFromName(self,BoatName):
        Boats = self.Boats
        for LocalBoat in Boats:
            if LocalBoat.Name == BoatName:
                return LocalBoat

###################### VISUAL ##############################

    def CreateSea(self):
        if self == self.Game.Player1:
            Y1 = 19; Y2 = -1; Y3 = -1
        elif self == self.Game.Player2:
            Y1 = 0; Y2 = 20; Y3 = 1

        print("Create visual sea: yet to be implemented!")
        print (" " + "--" * 20 + " ")

        for y in range(Y1, Y2, Y3):
            PrintLine = str(y) + "|"
            for x in range(0,20):
                for positions in self.Game.Positions:
                    if positions.X == x and positions.Y == y:
                        LocalBoat = positions.Boat
                        if LocalBoat.Player == self.Game.EmptyPlayer:
                            PrintLine += "  "
                        elif LocalBoat.Player == self.Game.Player1:
                            PrintLine += " 1"
                        elif LocalBoat.Player == self.Game.Player2:
                            PrintLine += " 2"
            print(PrintLine + "|")
        print (" " + "--" * 20 + " ")
