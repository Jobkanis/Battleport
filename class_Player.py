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
        Visual = self.Game.Visual
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

    def PlayTurn(self):
        #Creating possibleaction value
        #for keeping track what the user did and can still do

        AvaibleBoatsToMove = []
        for LocalBoat in self.Boats:
            AvaibleBoatsToMove.append(LocalBoat.Name)

        AvaibleAttacks_No = 2
        AvaibleBoatsToAttack = []

        for LocalBoat in self.Boats:
            AvaibleBoatsToAttack.append(LocalBoat.Name)

        #AvaiblePlayCards_No = 2

        #Taking a card
        if len(self.Cards) < 7:
            print("Takecard: yet to be implemented")

        #The actual possible moves the player can do (loop)
        LocalDone = False

        while LocalDone == False:

            Actions = ["boataction", "play cards", "end turn"]
            

            ################# GETTING EASY TRUE/FALSE STATEMENTS ###############################
            # ATTACK AND MOVE

            BoatsAbleToAttack = self.GetBoatsAbleToAttack(AvaibleBoatsToAttack) #return list of boats able to attack - boat classes!
            AbleToAttack = False
            if AvaibleAttacks_No > 0:
                if len(BoatsAbleToAttack) > 0:
                    AbleToAttack = True
                
            BoatsAbleToMove = self.GetBoatsAbleToMove(AvaibleBoatsToMove) #return list of boats able to move - boat classes!
            AbleToMove = False
            if len(BoatsAbleToMove) > 0:
                AbleToMove = True

            # BOAT SELECT

            BoatsAbleForAction = []
            BoatsAbleForAction += BoatsAbleToMove 
            for LocalBoatsAbleToAttack in BoatsAbleToAttack:
                if LocalBoatsAbleToAttack not in BoatsAbleForAction:
                    BoatsAbleForAction.append(LocalBoatsAbleToAttack)

            AbleToBoatAction = False
            if len(BoatsAbleForAction) >0 :
                AbleToBoatAction = True    
   
            # PLAY CARDS

            #AbleToPlayCards = False

            #if AvaiblePlayCards_No > 0:
             #   AbleToPlayCards = True



            ######## PHASE 1: PICKING A BOAT FOR ACTION OR CHOOSING CARD PLAY #######
            if AbleToBoatAction == True: #or AbleToPlayCards == True:

                #PossibleActions = ["end turn"]
                #if AbleToBoatActoin == True:
                #    PossibleActions.append("boataction")
                #if AbleToPlayCards == True:
                #    PossibleActions.append("play cards")
                
                ActionPhase1 = self.Game.Visual.ChooseActionPhase1(BoatsAbleForAction, BoatsAbleToMove, BoatsAbleToAttack) #AvaiblePlayCards_No) #returns boatclass for boataction, returns 'play cards' or 'end turn'
                print("Action 1 chosen")

                if ActionPhase1 in BoatsAbleToAttack or ActionPhase1 in BoatsAbleToMove:  #returned a boat to move
                    ############# PHASE 2: PICKING A BOAT ACTION #########################
                    LocalBoat = ActionPhase1

                    PositionsToAttack = LocalBoat.GetPositionsInreachToAttack()
                    BoatsToAttack = LocalBoat.GetBoatsInReachToAttack()

                    AbleToMove = False
                    if LocalBoat.Name in AvaibleBoatsToMove:
                        BoatsPossibleMovement = LocalBoat.GetPossibleMovement()
                        if len(BoatsPossibleMovement) > 0:
                            AbleToMove = True
                        BoatsPossibleStance = LocalBoat.GetPossibleDefensiveStance()
                        if len(BoatsPossibleStance) > 0:
                            AbleToMove = True
                    
                    AbleToAttackBoats = False
                    if AvaibleAttacks_No > 0:
                        if LocalBoat.Name in AvaibleBoatsToAttack:
                            if len(BoatsToAttack) > 0:
                                AbleToAttackBoats = True
                    
                    CheckPoint = False
                    while CheckPoint == False:
                        print("Choose boat action")

                        BoatAction = self.Game.Visual.ChooseBoatActionPhase2(LocalBoat, AbleToMove, AbleToAttackBoats, PositionsToAttack) #returns 'attack when pressed attack, returns 'move' when pressed move, returns 'cancel' when cancled

                        print("action chosen")
                        if BoatAction == "attack":
                            ######################### PHASE 3: ATTACKING A BOAT #####################################
                            AvaibleAttacks_No -= 1
                            AvaibleBoatsToAttack.remove(LocalBoat.Name)
                            self.Attack(LocalBoat)
                            CheckPoint = True
                    
                        elif BoatAction == "move":
                            ######################### PHASE 3: MOVING A BOAT #####################################
                            print("move " +  LocalBoat.Name)
                            AvaibleBoatsToMove.remove(LocalBoat.Name)
                            self.MoveBoat(LocalBoat)
                            CheckPoint = True

                        elif BoatAction == "cancel":
                            #move back to phase 1
                            CheckPoint = True
                    
                #elif ActionPhase1 == "play cards":      #returned "Play cards"\ 
                    ####### PHASE 2 ##############
                #    print("Play cards")
                  #  AvaiblePlayCards_No

                elif ActionPhase1 == "end turn":        #returned "end turn"
                    # END TURN
                    LocalDone = True       
            else:
                #TURN DONE
                LocalDone = True

    def CreateBoats(self):
        self.Boats = []
        self.Boats.append(class_Boats.Boat(self.Game, self, "size2"))
        self.Boats.append(class_Boats.Boat(self.Game, self, "size31"))
        self.Boats.append(class_Boats.Boat(self.Game, self, "size32"))
        self.Boats.append(class_Boats.Boat(self.Game, self, "size4"))

##################  ACTIONS (Phase 3) #########################

    #def PlayCards(self):
    #    print("Choose a card to play: yet to be implemented")
    #    print("Play the card: yet to be implemented")

    def Attack(self, Boat):
        BoatPositionsAbleToAttack = Boat.GetPositionsInreachToAttack()
        BoatsAbleToAttack = Boat.GetBoatsInReachToAttack()

        BoatToAttack = self.Game.Visual.GetAttackActionPhase3(Boat, BoatPositionsAbleToAttack, BoatsAbleToAttack)
        BoatToAttack.DealDamage(1)

    def MoveBoat(self, Boat):
        #CHOOSE MOVE ACTION TO DO
        self.Game.Visual.drawscreen()
        time.sleep(0.5)
        AvaibleMovements = Boat.MovementRange
        LocalDone = False

        while AvaibleMovements > 0 and LocalDone == False:
            print(AvaibleMovements)
            Action = ""
            MovementAction = ""

            PossibleStanceActions = Boat.GetPossibleDefensiveStance()
            PossibleMovementActions = Boat.GetPossibleMovement()
            PositionsToAttack = Boat.GetPositionsInreachToAttack()
            print(PossibleStanceActions)

            MovementAction = self.Game.Visual.GetMovementActionPhase3(Boat, PossibleStanceActions, PossibleMovementActions, PositionsToAttack)  #returns ["stance", "left"/"right"/"inactive"]        or         ["move", "left"/"right","forward","backward"]       or        ["stop", "stop]

            if MovementAction[0] == "stance":
                Action = MovementAction[1]
                AvaibleMovements -= 1
                Boat.ChangeBoatStance(Action)
                self.Game.Visual.drawscreen()            
                time.sleep(0.5)

            if MovementAction[0] == "move":
                Action = MovementAction[1]
                AvaibleMovements -= 1
                Boat.ChangeBoatPosition(Action)
                self.Game.Visual.drawscreen()
                time.sleep(0.5)

            if MovementAction[0] == "stop":
                print("Stopped moving boat")
                LocalDone = True

            #yet to be implemented: end reached

################### OTHER FUNCTIONS #######################

    def GetBoatsAbleToAttack(self, AvaibleBoatsToAttack): #return list of boats able to attack
        BoatsAbleToAttack = []
        for boatname in AvaibleBoatsToAttack:
            boatclass = self.GetBoatFromName(boatname)

            LocalBoatsToAttack = boatclass.GetBoatsInReachToAttack()
            if len(LocalBoatsToAttack) > 0:
                BoatsAbleToAttack.append(boatclass)

        return BoatsAbleToAttack

    def GetBoatsAbleToMove(self, AvaibleBoatsToMove): #return list of boats able to move
        Boats = AvaibleBoatsToMove
        BoatsAbleToMove = []

        for LocalBoatName in Boats:

            LocalBoatClass = self.GetBoatFromName(LocalBoatName)

            BoatAbleToMove = False

            LocalPossibleStance = LocalBoatClass.GetPossibleDefensiveStance()
            if len(LocalPossibleStance) > 0:
                BoatAbleToMove = True

            LocalPossibleMovement = LocalBoatClass.GetPossibleMovement()
            if len(LocalPossibleMovement) > 0:
                BoatAbleToMove = True

            if BoatAbleToMove == True:
                BoatsAbleToMove.append(LocalBoatClass)

        return BoatsAbleToMove

    def GetPlayerBoatPositions(self, exception):
        BoatPositions = []
        for PlayerBoats in self.Boats:
            if PlayerBoats not in exception:
                BoatPositions += PlayerBoats.GetLocalBoatsPositions(True, -1, -1, "inactive")
        return BoatPositions

    def GetBoatFromName(self,BoatName):
        Boats = self.Boats
        for LocalBoat in Boats:
            if LocalBoat.Name == BoatName:
                return LocalBoat

    def DeleteBoat(self, Boat):
        if Boat in self.Boats:
            self.Boats.remove(Boat)
        del Boat
            