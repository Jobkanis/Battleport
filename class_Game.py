import random
import math
import time
import copy
import pygame

import class_Player
import class_Boats
import class_Positions
import class_Visual
import class_Menu
import database

class Game:
    def __init__(self, gameDisplay, clock, width, height):
        #creating classes
        self.Sound_enabled = True

        self.Players = []
        self.Positions = []

        self.EmptyBoat = NotImplemented
        self.EmptyPosition = NotImplemented
        self.EmptyPlayer = NotImplemented

        self.Player1 = NotImplemented
        self.Player2 = NotImplemented

        self.Visual = class_Visual.Visual(self, gameDisplay, clock, width, height)
        self.Database = database.Database()

    def setupgame(self, player1name, player2name):
        if self.Sound_enabled == True:
            pygame.mixer.music.load("sound/bgm_ingame.wav")
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)
        ######### Empty Variables ###########

        ########## Empty Classes ##########
        self.EmptyPlayer = class_Player.Player(self, "empty")
        self.Players.append(self.EmptyPlayer)

        self.EmptyPosition = class_Positions.Position(self, -1, -1)
        self.Positions.append(self.EmptyPosition)
        
        self.EmptyBoat = class_Boats.Boat(self, self.EmptyPlayer, "empty")
        self.EmptyPlayer.Boats.append(self.EmptyBoat)

        ################ Players ###################
        self.CreatePositions() #Create all positions

        self.att_sound = pygame.mixer.Sound('ship_att.wav')
        self.sink_sound = pygame.mixer.Sound('ship_dead.wav')
        self.goal_sound = pygame.mixer.Sound('ship_dead.wav')
        self.move_sound = pygame.mixer.Sound('ship_move.wav')
        self.ship_select_sound = pygame.mixer.Sound('ship_select.wav')
        self.game_won = pygame.mixer.Sound('game_won.wav')
        self.game_over = pygame.mixer.Sound('game_over.wav')

        self.Player1 = class_Player.Player(self, player1name)
        self.Players.append(self.Player1)

        self.Player2 = class_Player.Player(self, player2name)
        self.Players.append(self.Player2)

        self.Winner = self.EmptyPlayer

        self.Player_Playing = self.Player1
        self.Visual.show_nextturn(self.Player_Playing)
        self.Player1.CreateBoats()

        self.Player_Playing = self.Player2
        self.Visual.show_nextturn(self.Player_Playing)
        self.Player2.CreateBoats()      
        
        self.Play()  
        return self.Winner
        #sounds

    def Play(self):
        self.Player_Playing = self.Player2        
        while self.Winner == self.EmptyPlayer:
            self.Visual.drawscreen()
            time.sleep(1)
            self.Player_Playing = self.NextPlayer()
            self.Visual.show_nextturn(self.Player_Playing)

            self.Player_Playing.PlayTurn()
        self.Visual.drawscreen()
        time.sleep(1)
        if self.Sound_enabled:
            self.game_over.play()

        self.Visual.DrawWinnerScreen()
        

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

    def GetAllBoatPositions(self, exception): #exception is list
        BoatPositions = []
        BoatPositions += self.Player1.GetPlayerBoatPositions(exception) #exception
        BoatPositions += self.Player2.GetPlayerBoatPositions(exception) #exception
        return BoatPositions

    def ToughUpdateBoats(self):
        positions = self.Positions
        Player1Boats = self.Player1.Boats
        Player2Boats = self.Player2.Boats
        for localpositions in positions:
            localpositions.Boat = self.EmptyBoat
            for p1boats in Player1Boats:
                allboatpositions = p1boats.GetLocalBoatsPositions(True, -1, -1, "inactive")
                for p1allboats in allboatpositions:
                    if p1allboats.X == localpositions.X and p1allboats.Y == localpositions.Y:
                        localpositions.Boat = p1boats

            for p2boats in Player2Boats:
                allboatpositions = p2boats.GetLocalBoatsPositions(True, -1, -1, "inactive")
                for p2allboats in allboatpositions:
                    if p2allboats.X == localpositions.X and p2allboats.Y == localpositions.Y:
                        localpositions.Boat = p2boats
