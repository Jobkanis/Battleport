import pygame
import class_Game
import time
#import class_Game
import sqlite3


################  IMAGES  ################

#Logo
logoimg = pygame.image.load('img/logo.png')

#Background ship
backgroundshipimg = pygame.image.load('img/background_ship.png')

#Top 10 content box
top10img = pygame.image.load('img/top10.png')

#Help content boxes
helpimg = [pygame.image.load('img/help_1.png') , pygame.image.load('img/help_2.png') , pygame.image.load('img/help_3.png') , pygame.image.load('img/help_4.png')]

#Buttons
newgame_but = [pygame.image.load('but/newgame_button.png') , pygame.image.load('but/newgame_button_over.png')]
help_but = [pygame.image.load('but/help_button.png') , pygame.image.load('but/help_button_over.png')]
options_but = [pygame.image.load('but/options_button.png') , pygame.image.load('but/options_button_over.png')]
chooseplayers_but = [pygame.image.load('but/chooseplayers_button.png') , pygame.image.load('but/chooseplayers_button_over.png')]
addnewplayer_but = [pygame.image.load('but/addnewplayer_button.png') , pygame.image.load('but/addnewplayer_button_over.png')]
exit_but = [pygame.image.load('but/exit_button.png') , pygame.image.load('but/exit_button_over.png')]
back_but = [pygame.image.load('but/back_button.png') , pygame.image.load('but/back_button_over.png')]
startturn_but = [pygame.image.load('but/startturn_button.png') , pygame.image.load('but/startturn_button_over.png')]
nextpage_but = [pygame.image.load('but/nextpage_button.png') , pygame.image.load('but/nextpage_button_over.png')]
mainimenu_but = [pygame.image.load('but/mainmenu_button.png') , pygame.image.load('but/mainmenu_button_over.png')]
x_but = [pygame.image.load('but/X_button.png') , pygame.image.load('but/X_button_over.png')]

##########################################


class Menu:

    def __init__ (self, game, gameDisplay, clock, width, height):
        self.Display = gameDisplay
        self.Clock = clock
        self.Width = width
        self.Height = height
        self.Size = (width, height)
        self.CurrentHelp = 0
        self.loop = True
        self.Game = game
        self.Clicked = 0
        
        #colours
        self.darkblue = (15,15,23)
        self.white = (255,255,255)
        
        self.HelpCheckPoint = False
        self.Cooldown = 0
        self.font = pygame.font.SysFont('Calibri', 20)
    
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

    def show_top10 (self):

        pos_x = self.Width*0.1
        pos_y = self.Height*0.3
        pos = (pos_x,pos_y)
        self.Display.blit(top10img,pos)

    def button (self, button, x, y, width, height, event=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if (x + width) > mouse[0] > x and (y + height) > mouse[1] > y:
            self.Display.blit(button[1],(x,y))
            if click[0] == 1 and event != None:
                self.Clicked = self.Clicked + 1
                if self.Clicked > 0:
                    self.Clicked = 0
                    self.loop = False
                    self.menu_start(event)


        else:
            self.Display.blit(button[0],(x,y))

    def NextHelpButton(self, currenthelp, button, x, y, width, height, event= None):
    
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        print(self.CurrentHelp)
        
        if (x + width) > mouse[0] > x and (y + height) > mouse[1] > y:

            self.Display.blit(button[1],(x,y))

            if click[0] == 1 and event != None and self.CurrentHelp == currenthelp and self.HelpCheckPoint == False:
                    self.HelpCheckPoint = True
                    self.Loop = False
                    self.Cooldown = 0
                    time.sleep(0.3)
                    self.CurrentHelp = currenthelp + 1
                    self.show_help(self.CurrentHelp)

        self.Display.blit(button[0],(x,y))

    ################  MENU'S  ################

    def show_main (self):

        self.show_top10()
        
        connection = sqlite3.connect('battleport.db')
        c = connection.cursor()

        c.execute("SELECT * FROM players ORDER BY wins DESC")
        count = 1
        y_pos = (self.Height * 0.3) + 75

        for row in c.fetchall():
            x_pos = (self.Width * 0.1) + 10

            self.addText(str(count) + '. ' + row[0], x_pos, y_pos, 100, 20)
            x_pos += 200

            self.addText(str(int(row[1])), x_pos, y_pos, 100, 20)
            x_pos += 50

            self.addText(str(int(row[2])), x_pos, y_pos, 100, 20)
            x_pos += 50

            if row[1] != 0 and row[2] != 0:
                ratio = int(row[1]) / int(row[2])
                self.addText(str(ratio), x_pos, y_pos, 100, 20)
            elif row[1] != 0 and row[2] == 0:
                self.addText(str(row[1]), x_pos, y_pos, 100, 20)
            else:
                self.addText('0', x_pos, y_pos, 100, 20)

            if count >= 10:
                break

            count += 1
            y_pos += 20

        but_x = self.Width * 0.65
        but_y = self.Height * 0.35

        self.button(newgame_but, but_x, but_y, 268, 68, 'new game')
        but_y += 100

        self.CurrentHelp = 0
        self.button(help_but, but_x, but_y, 268, 68, 'help')
        self.TimeOut = 0
        but_y += 100

        self.button(exit_but, but_x, but_y, 268, 68, 'exit')

    def show_new_game (self):
        self.Game.Play()
        self.exit()
        """
        but_x = (self.Width * 0.5) - 134
        but_y = self.Height * 0.3

        self.button(chooseplayers_but, but_x, but_y, 268, 68, 'next turn')
        but_y += 130

        self.button(addnewplayer_but, but_x, but_y, 268, 68, 'main menu')
        but_y += 130

        self.button(back_but, but_x, but_y, 268, 68, 'main menu')
        """   #starts game
        
    def show_help (self, c_help):
        self.HelpCheckPoint = False
        self.loop = True
        self.CurrentHelp = c_help

        while self.loop:

            currenthelp = self.CurrentHelp
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.loop = False
                    self.exit()

            pos_x = (self.Width * 0.5) - 400
            pos_y = (self.Height * 0.5) - 300
            pos = (pos_x, pos_y)


            but_x = (self.Width * 0.5) - 134
            but_y = self.Height * 0.8
            self.Display.fill(self.darkblue)
            self.show_backgroundship()
            self.show_logo()
            if self.CurrentHelp <= len(helpimg):
                self.Display.blit(helpimg[self.CurrentHelp - 1],pos)
            if self.CurrentHelp < len(helpimg):
                self.NextHelpButton(currenthelp, nextpage_but, but_x, but_y, 268, 68, "NextHelp")
            but_y = 20
            but_x = self.Width - 88

            self.button(x_but, but_x, but_y, 268, 68, 'main menu')

            self.menu_display_refresh()


    def GetNextHelpButton(self, event):
        pass

    def show_nextturn (self):

        but_x = (self.Width*0.5) - 134
        but_y = (self.Height*0.65)

        self.button(startturn_but, but_x, but_y, 268, 68, 'main menu')

    ##########################################

    ################  FUNCTIONS  ################

    def menu_start (self, name):

        self.loop = True

        while self.loop:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.loop = False

            self.Display.fill(self.darkblue)
        
            self.show_backgroundship()
            self.show_logo()

            self.show(name)

            self.menu_display_refresh()
            
    def show(self, name):

        if name == 'main menu':

            self.show_main()

        elif name == 'new game':

            self.show_new_game()

        elif name == 'exit':

            self.loop = False
            self.exit()

        elif name == 'help':
            self.show_help(1)
            
    def addText(self, text, x, y, width, height):
        self.Display.blit(self.font.render(text, True, self.white, (width, height)),(x,y))

    def menu_display_refresh (self):
        pygame.display.flip()
        self.Cooldown += 1
        self.Clock.tick(15)

    def exit (self):
        pygame.quit()
        quit()
