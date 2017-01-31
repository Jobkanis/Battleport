import pygame
import time
#import class_Game



################  IMAGES  ################

#Logo
logoimg = pygame.image.load('img/logo.png')

#Background ship
backgroundshipimg = pygame.image.load('img/background_ship.png')

#Tutorial
tutimg = [pygame.image.load('img/tutorial_place-ships.png'), pygame.image.load('img/tutorial_turn.png'), pygame.image.load('img/tutorial_move.png'), pygame.image.load('img/tutorial_attack.png')]

#place ships: 0. turn: 1, move: 2, attack: 3

#Columns
column_normalimg = [pygame.image.load('grid/column.png') , pygame.image.load('grid/column_over.png')]
column_choosable = [pygame.image.load('grid/column_choosable.png') , pygame.image.load('grid/column_choosable_over.png')]
column_boat_red = pygame.image.load('grid/column_boat_red.png')
column_boat_choosable_red = pygame.image.load('grid/column_choosable_boat_red.png')
column_boat_green = pygame.image.load('grid/column_boat_green.png')
column_boat_choosable_green = pygame.image.load('grid/column_choosable_boat_green.png')

#Boats
boat_red_size_2 = [pygame.image.load('boats/s2-p2-v2.png') , pygame.image.load('boats/s2-p2-v2_over.png')]
boat_green_size_2 = [pygame.image.load('boats/s2-p1-v1.png') , pygame.image.load('boats/s2-p1-v1_over.png')]

#Buttons
back_but = [pygame.image.load('but/back_button.png') , pygame.image.load('but/back_button_over.png')]
startturn_but = [pygame.image.load('but/startturn_button.png') , pygame.image.load('but/startturn_button_over.png')]
mainimenu_but = [pygame.image.load('but/mainmenu_button.png') , pygame.image.load('but/mainmenu_button_over.png')]
x_but = [pygame.image.load('but/X_button.png') , pygame.image.load('but/X_button_over.png')]
rightarrow_but = [pygame.image.load('but/rightarrow_button.png') , pygame.image.load('but/rightarrow_button_over.png')]
leftarrow_but = [pygame.image.load('but/leftarrow_button.png') , pygame.image.load('but/leftarrow_button_over.png')]
uparrow_but = [pygame.image.load('but/uparrow_button.png') , pygame.image.load('but/uparrow_button_over.png')]
downarrow_but = [pygame.image.load('but/downarrow_button.png') , pygame.image.load('but/downarrow_button_over.png')]
attack_but = [pygame.image.load('but/attack_button.png') , pygame.image.load('but/attack_button_over.png')]
move_but = [pygame.image.load('but/move_button.png') , pygame.image.load('but/move_button_over.png')]
cancel_but = [pygame.image.load('but/cancel_button.png') , pygame.image.load('but/cancel_button_over.png')]
endturn_but = [pygame.image.load('but/End_Turn.png')]
defensive_left = [pygame.image.load('but/Defensive_Left.png')]
defensive_right = [pygame.image.load('but/Defensive_Right.png')]
defensive_inactive = [pygame.image.load('but/Defensive_Inactive.png')]
continue_to_menu = [pygame.image.load('but/continue_to_menu_button.png')]
contine = [pygame.image.load('but/continue_button.png')]
help_button_small = [pygame.image.load('but/Help_ingame_button.png')]
##########################################

class Visual:

    def __init__ (self, game, gameDisplay, clock, width, height):

        self.Game = game
        self.Display = gameDisplay
        self.Clock = clock
        self.Width = width
        self.Height = height
        self.Size = (width, height)
        self.font = pygame.font.SysFont('Calibri', 20)
        self.headfont = pygame.font.SysFont('Calibri', 50)
        self.loop = False

        self.move_boat = False

        self.PositionPicked = self.Game.EmptyPosition
        self.ActionPicked = "none"
        self.MovementPicked = "none"
        self.CoordinatesClicked = (-1,-1)

        #Colors
        self.darkblue = (15,15,23)
        self.white = (255, 255, 255)
        self.Help = False

    def show_logo (self):

        pos_x = 15
        pos_y = 15
        pos = (pos_x,pos_y)
        self.Display.blit(logoimg,pos)

    def show_backgroundship (self):

        pos_x = (self.Width*0.5) - 360
        pos_y = (self.Height*0.5) - 177
        pos = (pos_x,pos_y)
        self.Display.blit(backgroundshipimg,pos)

    def show_tut(self):


        pos_x = (self.Width*0.5) - 400
        pos_y = (self.Height*0.5) - 177
        pos = (pos_x,pos_y)
        self.Display.blit(tutimg, pos)

    ##########################################

    ################  FUNCTIONS  ################

    def display_refresh (self):

        pygame.display.flip()
        self.Clock.tick(15)

    def exit (self):

       pygame.quit()
       quit()
#############################################################
    
    def helpopenbutton(self, x, y, width, height, event=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        self.Display.blit(help_button_small[0],(x , y))
        if (x + width) > mouse[0] > x and (y + height) > mouse[1] > y:
            if click[0] == 1 and event != None:
                self.showhelp(event)

    def ContinueToNextPlayerButton (self, button, x, y, width, height, event=None): 
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        self.Display.blit(button[0],(x,y))

        if (x + width) > mouse[0] > x and (y + height) > mouse[1] > y:
            if click[0] == 1 and event != None:
                self.ActionPicked = event    

    def Movementbutton (self, mouse, click, button, x, y, width, height, event=None): 
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        self.Display.blit(button[0],(x,y))
        if (x + width) > mouse[0] > x and (y + height) > mouse[1] > y:
            if click[0] == 1 and event != None:
                self.MovementPicked = event      

    def addRect(self, x, y, width, height, outline):
        self.rect = pygame.draw.rect(self.Display, self.white, (x, y, width, height), outline)

    def addText(self, text, x, y, width, height):
        self.Display.blit(self.font.render(text, True, self.white, (width, height)),(x+5,y+5))

    def addHead(self, text, x, y, width, height):
        self.Display.blit(self.headfont.render(text, True, self.white, (width, height)),(x+5,y+5))

    def MessageBox(self, text, x, y, width, height):
        self.addRect(x, y, width, height, 1)
        self.addText(text, x, y, width, height)

    def Playerstats(self, x, y, width, height, line1, line2, line3, line4, line5):
        self.addRect(x, y, width, height, 2)
        self.addText(line1, x, y + 5, width, height)
        self.addText(line2, x, y + 35, width, height)
        self.addText(line3, x, y + 60, width, height)
        self.addText(line4, x, y + 85, width, height)
        self.addText(line5, x, y + 110, width, height)

    def Getstringfromboat(self,Boat):
        string = str(Boat.Name) + " | Size: " + str(Boat.Size) + " | Health = " + str(Boat.Health) + "/" + str(Boat.MaxHealth)
        return string

    def GetPlayerStatsString(self, Player):
        line1 = " "; line2 = " "; line3 = " "; line4 = " "; line5 = " "
        boats = Player.Boats
        line1 = str(Player.Name) + "s stats:"
        if len(boats) > 0:
            localboat = boats[0]
            line2 = self.Getstringfromboat(boats[0])
        if len(Player.Boats) > 1:
            localboat = boats[1]
            line3 = self.Getstringfromboat(boats[1])
        if len(Player.Boats) > 2:
            localboat = boats[2]
            line4 = self.Getstringfromboat(boats[2])
        if len(Player.Boats) > 3:
            localboat = boats[3]
            line5 = self.Getstringfromboat(boats[3])
        return [line1, line2, line3, line4, line5]
            
    #all possiblegridcoordinates

    def NormalCoordininate (self, position, x, y):
            
            self.Display.blit(column_normalimg[0],(x,y))

    def ChoosableCoordinate (self, mouse, click, position, x, y, width, height, event_1=None, event_2=None):
        if (x + width) > mouse[0] > x and (y + height) > mouse[1] > y:
            
            self.Display.blit(column_choosable[1],(x,y))

            if click[0] == 1 and event_1 != None and event_2 != None:
                
                self.PositionPicked = position

        else:
            
            self.Display.blit(column_choosable[1],(x,y))

    def BoatCoordinate (self, position, x, y):

        if position.Boat.Player == self.Game.Player1:
            self.Display.blit(column_boat_red,(x,y))
        elif position.Boat.Player == self.Game.Player2:
            self.Display.blit(column_boat_green,(x,y))    

    def ChooseableboatCoordinate (self, mouse, click, position, x, y, width, height, event_1=None, event_2=None):

        if (x + width) > mouse[0] > x and (y + height) > mouse[1] > y:
            
            if position.Boat.Player == self.Game.Player1:
                self.Display.blit(column_boat_choosable_red,(x,y))
            elif position.Boat.Player == self.Game.Player2:
                self.Display.blit(column_boat_choosable_green,(x,y))    

            if click[0] == 1 and event_1 != None and event_2 != None:
                self.PositionPicked = position
        else:
            
            if position.Boat.Player == self.Game.Player1:
                self.Display.blit(column_boat_choosable_red,(x,y))
            elif position.Boat.Player == self.Game.Player2:
                self.Display.blit(column_boat_choosable_green,(x,y))  

####

    def EndTurnButton (self, button, x, y, width, height, event=None):
        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if (x + width) > mouse[0] > x and (y + height) > mouse[1] > y:

            if click[0] == 1 and event != None:
                self.PositionPicked = event
#choose action

    def ChooseActionButton (self, button, x, y, width, height, event=None):

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if (x + width) > mouse[0] > x and (y + height) > mouse[1] > y:

            if click[0] == 1 and event != None:
                self.ActionPicked = event
       # else:
            #self.Display.blit(button[0],(x,y))
            
#Draw the game

    def grid_position_x(self, n):

        x = (self.Width * 0.5) - 250

        for i in range (0 , n):

            x += 25

        return x

    def grid_position_y(self, n):

        y = (self.Height * 0.5) - 250

        for i in range (0, n):

            y += 25

        return y
         
    def draw_grid (self, Chooseablecoordinates, Chooseableboats):
        chooseableboatpositions = []

        for localchoosableboat in Chooseableboats:
            localboatcoordinates = localchoosableboat.GetLocalBoatsPositions(True, -1, -1, "inactive")
            chooseableboatpositions = chooseableboatpositions + localboatcoordinates

        AllBoatPositions = self.Game.GetAllBoatPositions([])

        ### SHOW GRID  ###

        pos_y = (self.Height * 0.5) - 250

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.Game.Player_Playing == self.Game.Player2:
            i = 0; j = 20; k = 1

        elif self.Game.Player_Playing == self.Game.Player1:
            i = 19; j = -1; k = -1

        for grid_y in range (i, j, k):

            pos_x = (self.Width * 0.5) - 250

            for grid_x in range (0, 20):
                
                LocalPositionClass = self.Game.GetPosition(grid_x, grid_y)


                if LocalPositionClass.Boat == self.Game.EmptyBoat:
                    if LocalPositionClass in Chooseablecoordinates:
                        #choosablecoordinate
                        self.ChoosableCoordinate(mouse, click, LocalPositionClass, pos_x, pos_y, 25, 25, grid_x, grid_y)

                    else:
                        #normalcoordinate
                        self.NormalCoordininate(LocalPositionClass, pos_x, pos_y)

                else:

                    if LocalPositionClass in chooseableboatpositions:
                        #choosablecoordinate
                        self.ChooseableboatCoordinate(mouse, click, LocalPositionClass, pos_x, pos_y, 25, 25, grid_x, grid_y)

                    else:
                        #choosablecoordinate
                        self.BoatCoordinate(LocalPositionClass, pos_x, pos_y)

                pos_x += 25

            pos_y += 25
        PositionClass = self.Game.GetPosition(pos_x , pos_y)
    
    def draw_game(self, MessageBox1Tekst, MessageBox2Tekst, help):
        self.show_backgroundship()
        self.show_logo()

        self.MessageBox(MessageBox1Tekst, ((self.Width * 0.5) - 350), self.Height * 0.5 - 325, 700, 25)

        self.MessageBox(MessageBox2Tekst, ((self.Width * 0.5) - 250), self.Height * 0.5 - 275, 500, 25)

        
        Player1Text = self.GetPlayerStatsString(self.Game.Player1)
        self.Playerstats(10, 170, 350, 200, Player1Text[0], Player1Text[1], Player1Text[2], Player1Text[3], Player1Text[4])
        
        Player2Text = self.GetPlayerStatsString(self.Game.Player2)
        self.Playerstats(10, 400, 350, 200, Player2Text[0], Player2Text[1], Player2Text[2], Player2Text[3], Player2Text[4])

        if help != -1:
            self.helpopenbutton(self.Width * 0.5 + 282, self.Height * 0.1 + 13 ,  68, 68, help)
            

#################### interactive funcitons ###############
    def drawscreen(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                self.exit()

        self.Display.fill(self.darkblue)
        self.draw_game("","", -1)
        self.draw_grid([], [])
        self.display_refresh()

    def selectcoordinate(self, Chooseablecoordinates, Chooseableboats, ShowEndTurnDisplay, MessageBox1Tekst, MessageBox2Tekst, help):
        self.PositionPicked = self.Game.EmptyPosition
        while self.PositionPicked == self.Game.EmptyPosition:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    self.exit()

            self.Display.fill(self.darkblue)
            
            self.draw_game(MessageBox1Tekst, MessageBox2Tekst, help)
            self.draw_grid(Chooseablecoordinates, Chooseableboats)

            x_pos = self.Width * 0.5
            y_pos = self.Height * 0.86
            x = x_pos - 134
            y = y_pos

            print(ShowEndTurnDisplay)
            if ShowEndTurnDisplay:
                self.Display.blit(endturn_but[0],(x,y))                
                self.EndTurnButton(endturn_but, x, y, 268, 68, 'end turn')

            self.display_refresh()

        return self.PositionPicked
    
    def chooseaction(self, Boat, AbleToMove, AbleToAttackBoats, PositionsToAttack, MessageBox1Tekst, MessageBox2Tekst):
        self.ActionPicked = "none"
        self.Display.fill(self.darkblue)
        self.draw_game(MessageBox1Tekst,MessageBox2Tekst, 1)
        self.draw_grid(PositionsToAttack, [])
        if AbleToMove == True:
            x = self.Width * 0.5 - 134
            y = self.Height * 0.86
            self.Display.blit(move_but[0],(x,y))
        if AbleToAttackBoats == True:
            x = self.Width * 0.5 - 422
            y = self.Height * 0.86
            self.Display.blit(attack_but[0],(x,y))

        x = self.Width * 0.5 + 154
        y = self.Height * 0.86
        self.Display.blit(cancel_but[0],(x,y))

        self.display_refresh()

        while self.ActionPicked == "none":
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    self.exit()
            x_pos = self.Width * 0.5 
            y_pos = self.Height * 0.86
            if AbleToMove == True:
                self.ChooseActionButton(move_but, x_pos- 134, y_pos, 268, 68, 'move')

            if AbleToAttackBoats == True:
                self.ChooseActionButton(attack_but, x_pos - 422, y_pos, 268, 68, 'attack')
            
            self.ChooseActionButton(cancel_but, x_pos + 154, y_pos, 268, 68, 'cancel')

            self.Clock.tick(15)
            self.helpopenbutton(self.Width * 0.5 + 282, self.Height * 0.1 + 13,  68, 68, 1)

        return self.ActionPicked

####

    def ChooseActionPhase1(self, BoatsAbleForAction, BoatsAbleToMove, BoatsAbleToAttack, MessageBox1Tekst, MessageBox2Tekst): #AvaiblePlayCards_No):      #returns boatclass for boataction, returns 'play cards' or 'end turn'  
        #place ships: 0. turn: 1, move: 2, attack: 3
        PositionPicked = self.selectcoordinate([], BoatsAbleForAction, True, MessageBox1Tekst, MessageBox2Tekst, 1)
        if PositionPicked == "end turn":
            return "end turn"
        else:
            return PositionPicked.Boat

    def ChooseBoatActionPhase2(self, Boat, AbleToMove, AbleToAttackBoats, PositionsToAttack, MessageBox1Tekst, MessageBox2Tekst): #returns 'attack when pressed attack, returns 'move' when pressed move, returns 'cancle' when cancled
        Action = self.chooseaction(Boat, AbleToMove, AbleToAttackBoats, PositionsToAttack, MessageBox1Tekst, MessageBox2Tekst) #"attack", "move", "cancle"
        return Action
    
    def GetAttackActionPhase3(self, Boat, PositionsAbleToAttack, BoatsAbleToAttack, MessageBox1Tekst, MessageBox2Tekst): #returns ["stance", "left"/"right"/"inactive"] or ["move", "left"/"right","forward","backward"] or ["stop", "stop]  
        BoatPicked = self.selectcoordinate([], BoatsAbleToAttack, False,  MessageBox1Tekst, MessageBox2Tekst, 3)
        boat = BoatPicked.Boat
        return boat

    def GetMovementActionPhase3(self, Boat, PossibleStanceActions, PossibleMovementActions, PositionsToAttack, MessageBox1Tekst, MessageBox2Tekst): #returns ["stance", "left"/"right"/"inactive"] or ["move", "left"/"right","forward","backward"] or ["stop", "stop]  
        self.MovementPicked = "none"

        while self.MovementPicked == "none":
            self.Help = False
            selectedboatpositions = Boat.GetLocalBoatsPositions(True, -1,-1,"inactive")

            MoveRight = False
            MoveLeft = False
            MoveForward = False
            MoveBackward = False
            for possiblemovement in PossibleMovementActions:
                if possiblemovement == "left":
                    MoveLeft = True
                elif possiblemovement == "right":
                    MoveRight = True
                elif possiblemovement == "forward":
                    MoveForward = True
                elif possiblemovement == "backward":
                    MoveBackward = True

            StanceLeft = False
            StanceRight = False
            StanceInactive = False
            for possiblestance in PossibleStanceActions:
                if possiblestance == "left":
                    StanceLeft = True
                elif possiblestance == "right":
                    StanceRight = True
                elif possiblestance == "inactive":
                    StanceInactive = True
        
            self.Display.fill(self.darkblue)
            self.draw_game(MessageBox1Tekst, MessageBox2Tekst, 2)
            self.draw_grid(PositionsToAttack, [])
            
            while self.MovementPicked == "none" and self.Help == False:
            
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
    
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        self.exit()
        
                x_pos = self.Width * 0.8
                y_pos = self.Height * 0.75

                if MoveRight == True:
                    self.Movementbutton(mouse, click, rightarrow_but, x_pos + 33, y_pos - 34, 68, 68, ["move", "right"])
                if MoveLeft == True:
                    self.Movementbutton(mouse, click, leftarrow_but, x_pos - 101, y_pos - 34, 68, 68, ["move", "left"])
                if MoveForward == True:
                    self.Movementbutton(mouse, click, uparrow_but, x_pos - 34, y_pos - 101, 68, 68, ["move", "forward"])
                if MoveBackward == True:
                    self.Movementbutton(mouse, click, downarrow_but, x_pos - 34, y_pos + 33, 68, 68, ["move", "backward"])
            
                self.Movementbutton(mouse, click, x_but, x_pos - 34, y_pos - 34, 68, 68, ["stop", "stop"])

                self.Movementbutton(mouse, click, x_but, x_pos - 34, y_pos - 34, 68, 68, ["stop", "stop"])

                x_pos = self.Width * 0.5 
                y_pos = self.Height * 0.86

                if StanceLeft == True:
                    self.Movementbutton(mouse, click, defensive_left, x_pos - 288, y_pos, 268, 68, ["stance", "left"])
                if StanceInactive == True:
                    self.Movementbutton(mouse, click, defensive_inactive, x_pos - 144, y_pos, 268, 68, ["stance", "inactive"])   
                if StanceRight == True:
                    self.Movementbutton(mouse, click, defensive_right, x_pos + 20, y_pos, 268, 68, ["stance", "right"])         

                self.helpopenbutton(self.Width * 0.5 + 282, self.Height * 0.1 + 13,  68, 68, 2)

                pygame.display.flip()
                self.Clock.tick(15)

        action = self.MovementPicked
        return action

    def DrawWinnerScreen(self):
        self.Display.fill(self.darkblue)
        self.show_backgroundship()
        self.show_logo()

        x_pos = self.Width * 0.5 
        y_pos = self.Height * 0.3
        self.addHead( "Congratulations! " + str(self.Game.Winner.Name) +  " won!", x_pos - 300, y_pos - 25, 600, 50)

        self.display_refresh()
        time.sleep(1)
        self.ActionPicked = "none"
        while self.ActionPicked == "none":
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    self.exit()



            self.Display.fill(self.darkblue)
            self.show_backgroundship()
            self.show_logo()

            

            x_pos = self.Width * 0.5 
            y_pos = self.Height * 0.3

            self.addHead( "Congratulations! " + str(self.Game.Winner.Name) +  " won!", x_pos - 300, y_pos - 25, 600, 50)

            x_pos = self.Width * 0.5 
            y_pos = self.Height * 0.7
            self.ContinueToNextPlayerButton (continue_to_menu, x_pos - 144, y_pos - 34, 268, 68, "pressed")
            

            self.display_refresh()

    def show_nextturn (self, player):
        
        
        self.Display.fill(self.darkblue)
        self.show_backgroundship()
        self.show_logo()

        x_pos = self.Width * 0.5 
        y_pos = self.Height * 0.3
        self.addHead("It is " + str(player.Name) +  "'s turn!", x_pos - 190, y_pos - 25, 380, 50)

        self.display_refresh()
        time.sleep(1)
        self.ActionPicked = "none"
        while self.ActionPicked == "none":
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    self.exit()



            self.Display.fill(self.darkblue)
            self.show_backgroundship()
            self.show_logo()

            

            x_pos = self.Width * 0.5 
            y_pos = self.Height * 0.3

            self.addHead("It is " + str(player.Name) +  "'s turn!", x_pos - 190, y_pos - 25, 380, 50)

            x_pos = self.Width * 0.5 
            y_pos = self.Height * 0.7
            self.ContinueToNextPlayerButton (contine, x_pos - 144, y_pos - 34, 268, 68, "pressed")
            

            self.display_refresh()
        self.drawscreen()
        time.sleep(0.5)

    def showhelp(self, helpscreen):
        self.Help = True
        self.ActionPicked = "none"
        while self.ActionPicked == "none":
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    self.exit()


            pos_x = (self.Width * 0.5) - 400
            pos_y = (self.Height * 0.5) - 300
            pos = (pos_x, pos_y)
            self.Display.blit(tutimg[helpscreen], pos)

            
            #draw the helpscreen
            x_pos = self.Width * 0.9
            y_pos = self.Height * 0.3
            self.ContinueToNextPlayerButton (x_but, x_pos - 34, y_pos - 34, 68, 68, "pressed")
            

            self.display_refresh()

        self.drawscreen()
        time.sleep(1)


    ####
