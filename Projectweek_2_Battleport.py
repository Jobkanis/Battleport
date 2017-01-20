import random
import math
import time
import copy
import pygame

#PlayerNames = ["empty", "player1", "player2"]
#BoatKinds = ["size2", "size31", "size32", "size4"]
#Perks = ["none"]

Players = []

Positions = []

################### CLASSES ########################
class Player:
    def __init__(self, playername):
        self.Name = playername
        self.Cards = []
        self.Boats = []
        self.Points = 0

    def CreateBoats(self):
        self.Boats = []
        self.Boats.append(Boat(self, "size2"))
        self.Boats.append(Boat(self, "size31"))
        self.Boats.append(Boat(self, "size32"))
        self.Boats.append(Boat(self, "size4"))

class Boat:
    def __init__(self, player, kind):
        self.Player = player
        self.Kind = kind
        self.Name = "empty"

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
        if self.Player != EmptyPlayer:
            BoatPosition = self.PlaceBoats() #returns position class
            if BoatPosition in Positions: #makes sure the position exists: fixes error in creating empty class"
                self.X = BoatPosition.X
                self.Y = BoatPosition.Y

    def PlaceBoats(self):
        print("Pick Boat Position: yet to be implemented!")
        x = int(input("Player: " + self.Player.Name + "| Boat: " + self.Name + "| Insert X Postion (0-19): "))
        y = int(input("Player: " + self.Player.Name + "| Boat: " + self.Name + "| Insert Y Postion (0-19): "))
        LocalPosition = GetPosition(x,y)
        return LocalPosition

    #defence
    def IncreaseHealth(self, Health):
        self.Health += Health

    #attack
    def DealDamage(self, damage):
        reflects = checkifreflect()
        if reflects == False:
            self.Health -= damage # * healthmultiplier
        
    #Movement
    def Move(self, MoveX, MoveY):
        self.X += MoveX
        self.Y += MoveY 
    def Stance(self):
        DefensiveStance = not DefensiveStance

class Position:
    def __init__(self, x, y):
        self.ContainsBomb = True 
        self.BombActivated = False
        
        self.X = x 
        self.Y = y 
        self.Boat = EmptyBoat

    def CreatePositions(self):
        if self == EmptyPosition:
            print("Creating positions")
            for y in range (0,20):
                for x in range (0,20):
                    LocalPosition = Position(x, y)
                    Positions.append(LocalPosition)
        else:
            print("Not legal action: trying to create unnecessary positions")

    def BoatOnBomb(self):
        print("Boat is on bomb")

###################### GET ITEMS FROM LIST ################

def GetPosition(x,y):
    for Pos in Positions:
        if Pos.X == x and Pos.Y == y:
            return Pos
    return EmptyPosition

def GetBoat(x, y):
    for LocalPlayers in Players:
        for boat in LocalPlayers.Boats:
            if boat.X == x and boat.Y == y:
                return boat
    else: return EmptyBoat

################ VISUAL PART ####################
def createsea():
    print("Create visual sea: yet to be implemented!")
    print (" " + "--" * 20 + " ")
    for y in range(19, -1, -1):
        PrintLine = "|"
        for x in range(0,20):
            LocalPosition = GetPosition(x,y)
            LocalBoat = GetBoat(x,y)
            if LocalBoat.Player == EmptyPlayer:
                PrintLine += "  "
            elif LocalBoat.Player == Player1:
                PrintLine += " 1"
            elif LocalBoat.Player == Player2:
                PrintLine += " 2"
        print(PrintLine + "|")
    print (" " + "--" * 20 + " ")
   
def createHUD():
    print("Create visual stats: yet to be implemented")             

################# SET UP GAME ################

def creategame():
    #players: globals so not necesarry
    #maybe add reseting their stats
    
    #Creating positions
    EmptyPosition.CreatePositions()

    #Creating boats 
    Player1.CreateBoats()
    Player2.CreateBoats()
    EmptyPlayer.Boats.append(EmptyBoat)

################## ACTIONS #####################

#actions: play card, attack, move 
def Attack(player):
    print("Check if ship in range: yet to be implemented")
    print("Chooseboat: yet to be implemented")
    print("Attackboat: yet to be implemented")

def move():
    print("Chooseboat: yet to be implemented")
    AvailbleMovements = Boats.Movements
    Done = False
    while AvaibleMovements > 0 and Done == False:
        Input = input("Stance or Move?")
        if Input == "stance":
            print("Change stance mode: yet to be implemented")
            AvaibleMovements -= 1
        if Input == "move":
            print("Choose boat direction: yet to be implemented")
            print("Moveboat: yet to be implemented")
            AvaibleMovements -= 1
        if Position == Doel:
            print("Check if goal is reached: yet to be implemented")
            print("Take special card: yet to be implemented")
            print("Play the special card: yet to be implemented")

def playcard():
    print("Choose a card to play: yet to be implemented")
    print("Play the card: yet to be implemented")
    
################# PLAYER ACTIONS #######################

def ChooseBoatToMove(AvaibleBoatsToMove):
    return AvaibleBoatsToMove[0] #return boat out of AvaibleBoatsToMove

def MoveBoat(BoatToMove):
    print("Move boat: yet to be implemented")

def PlayCards(player):
    print("Play cards: yet to be implemnted")

def GetAction(player):
    PlayerBoats = player.Boats
    AvaibleBoatsToMove = copy.deepcopy(PlayerBoats)

    AvaibleAttacks_No = 2

    AvaibleBoatsToAttack = copy.deepcopy(PlayerBoats)
    AvaiblePlayCards_No = 2

    if len(player.Cards) < 7:
        print("Takecard: yet to be implemented")

    LocalDone = False
    while LocalDone == False:
        if len(AvaibleBoatsToMove) > 0 or  AvaibleAttacks_No > 0 or AvaiblePlayCards_No > 0:
            #check if skip turn:
            createsea()
            EndTurn = input("End turn? (yes/no): ")
            if EndTurn == "yes":
                LocalDone = True
            else: 
                LocalDone = False

            #Actions

            PossibleActions = []
            if LocalDone == False:

                #Selecting action
                SelectActionText = ""
                if AvaiblePlayCards_No > 0:
                    PossibleActions.append("play cards("+ str(AvaiblePlayCards_No) + ")")

                if  AvaibleAttacks_No > 0:
                    PossibleActions.append("attack(" + str(AvaibleAttacks_No) + ")")

                if len(AvaibleBoatsToMove) > 0:
                    PossibleActions.append("move boat(" + str(len(AvaibleBoatsToMove)) + ")")

                SelectActionText = ""
                for possibleactions in PossibleActions:
                    SelectActionText += " | " + possibleactions
                SelectActionText = "Possible actions: " + SelectActionText +  "\n"

                LocalAction = input(SelectActionText)

                #Doing Action
                if LocalAction == "play cards" and AvaiblePlayCards_No > 0:
                    AvaiblePlayCards_No -= 1
                    PlayCards(player)

                if LocalAction == "attack" and AvaibleAttacks_No > 0:
                    AvaibleAttacks_No -= 1
                    Attack(player)

                if LocalAction == "move boat" and len(AvaibleBoatsToMove) > 0:
                    BoatToMove = ChooseBoatToMove(AvaibleBoatsToMove)
                    AvaibleBoatsToMove.remove(BoatToMove)
                    MoveBoat(BoatToMove)
        else:
            LocalDone = True

################## PLAYER TURNS ####################
def turn(player):
    GetAction(player)
        

    print(player.Name + " his turn ended")

def nextplayer(player):
    if player == Player1:
        return Player2
    else:
        return Player1 

def checkifwon():
    print("Check if player won: yet to be implemented: return won player else EmptyPlayer")
    return EmptyPlayer

#######################################

#creating classes
EmptyBoat = NotImplemented
EmptyPosition = NotImplemented
EmptyPlayer = Player("empty")

Players.append(EmptyPlayer)
EmptyPosition = Position(-1, -1)
EmptyBoat = Boat(EmptyPlayer, "empty")
Positions.append(EmptyPosition)

Player1 = Player("player1")
Players.append(Player1)

Player2 = Player("player2")
Players.append(Player2)

#starting the game
Player_Playing = Player2
creategame()

while checkifwon() == EmptyPlayer:
    Player_Playing = nextplayer(Player_Playing)
    print("\nIt is " + Player_Playing.Name + " his turn")
    turn(Player_Playing)