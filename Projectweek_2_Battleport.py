import random
import math
import time
import copy
import pygame

PlayerNames = ["empty", "player1", "player2"]

Boats = []

Positions = []

Perks = ["none"]

################### CLASSES ########################

class Player:
    def __init__(self, playername):
        self.Name = playername
        self.Cards = []
        self.Boats = []
        self.Points = 0

EmptyPlayer = Player("empty")
Player1 = Player("player1")
Player2 = Player("player2")


class Boat:
    def __init__(self, x, y, player):
        self.Player = player        
        
        self.Size = 4 #2-4
        self.X = x
        self.Y = y
        self.DefensiveStance = False

        self.AttackRange = x
        self.MovementRange = x
        self.Health = x
        
        self.DefensiveStance = False

        self.Perks = "none"
            #healthmultiplier = 0.5
        

        #defence
        def Health(self, Health):
            self.Health += Health

        #attack
        def Damaged(self, damage):
            reflects = checkifreflect()
            if reflects == False:
                self.Health -= damage # * healthmultiplier
        
        #Movement
        def Move(self, MoveX, MoveY):
            self.X += MoveX
            self.Y += MoveY 
        def Stance(self):
            DefensiveStance = not DefensiveStance

EmptyBoat = Boat(-1,-1, EmptyPlayer)     
Boats.append(EmptyBoat)

class Position:
    def __init__(self, player, x, y):
        self.ContainsBomb = True 
        self.BombActivated = False
        
        self.X = x 
        self.Y = y 
        self.Boat = EmptyBoat

    def BoatOnBomb(self):
        print("Boat is on bomb")
EmptyPosition = Position(EmptyPlayer, -1, -1)
Positions.append(EmptyPosition)

###################### GET ITEMS FROM LIST ################

def GetPosition(x,y):
    for Pos in Positions:
        if Position.X == x and Position.Y == y:
            return Pos
    return EmptyPosition

def GetBoat(x, y):
    for boat in Boats:
        if boat.x == x and boat.y == y:
            return boat
    else: return EmptyBoat

################ VISUAL PART ####################
def createsea():
    print("Create visual sea: yet to be implemented\n\n")
    for y in range(19, -1, -1):
        PrintLine = ""
        for x in range(0,20):
            LocalPosition = GetPosition(x,y)
            LocalBoat = GetBoat(x,y)
            if LocalBoat.Player == EmptyPlayer:
                line += " "
            elif LocalBoat.Player == Player1:
                line += "1"
            elif LocalBoat.Player == Player2:
                line += "2"
        PrintLine(line)
   
def createstats():
    print("Create visual stats: yet to be implemented")             

################# SET UP GAME ################

def creategame():
    #players: globals so not necesarry
    #maybe add reseting their stats
    

    Player1.Boats = [EmptyBoat, EmptyBoat]
    Player2.Boats = [EmptyBoat, EmptyBoat]

    #positions
    print("Creating positions")
    for y in range (0,20):
        for x in range (0,20):
            LocalPosition = Position(EmptyPlayer, x, y)
            Positions.append(LocalPosition)\
    
    #createboats
    print("Createboats: yet to be implemented")

################## ACTIONS #####################

#actions: play card, attack, move 
def attack():
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
def Attack(player):
    print("Attack: yet to be implemented")

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

Player_Playing = Player2
creategame()

while checkifwon() == EmptyPlayer:
    Player_Playing = nextplayer(Player_Playing)
    print("\nIt is " + Player_Playing.Name + " his turn")
    turn(Player_Playing)