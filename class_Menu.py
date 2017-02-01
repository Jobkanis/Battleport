import pygame
import class_Game
import time
#import class_Game
import sqlite3
from tkinter import *
import database


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
soundfx_on = [pygame.image.load('but/soundfx_on_but.png') , pygame.image.load('but/soundfx_on_but_over.png')]
soundfx_off = [pygame.image.load('but/soundfx_off_but.png') , pygame.image.load('but/soundfx_off_but_over.png')]
backgroundmusic_on = [pygame.image.load('but/backgroundmusic_on_but.png') , pygame.image.load('but/backgroundmusic_on_but_over.png')]
backgroundmusic_off = [pygame.image.load('but/backgroundmusic_off_but.png') , pygame.image.load('but/backgroundmusic_off_but_over.png')]

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
        self.Playing = False
        self.Played = False
        self.Database = database.Database()

        #colours
        self.darkblue = (15,15,23)
        self.white = (255,255,255)
        
        self.HelpCheckPoint = False
        self.Cooldown = 0
        self.font = pygame.font.SysFont('Calibri', 20)
        self.headfont = pygame.font.SysFont('Calibri', 35)

        self.player1 = ''
        self.player2 = ''

        self.soundfx = True
        self.backgroundmusic = True

        pygame.mixer.music.load("sound/background_music.wav")

        if self.backgroundmusic:
            pygame.mixer.music.play(-1)
    
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
                if event == 'backgroundmusic off':
                        self.backgroundmusic = False
                        pygame.mixer.music.stop()
                elif event == 'backgroundmusic on':
                        self.backgroundmusic = True
                        pygame.mixer.music.play(-1)
                elif event == 'soundfx off':
                        self.soundfx = False
                elif event == 'soundfx on':
                        self.soundfx = True
                elif self.Clicked > 0:
                    self.Clicked = 0
                    self.loop = False
                    if event == 'choose players' and self.Playing == False:
                        self.Playing = True
                        self.Pick_Players()

                    self.menu_start(event)


        else:
            self.Display.blit(button[0],(x,y))

    def NextHelpButton(self, currenthelp, button, x, y, width, height, event= None):
    
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

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

        #highscore
        connection = sqlite3.connect('battleport.db')
        c = connection.cursor()

        c.execute("SELECT * FROM players ORDER BY wins DESC, losses ASC")
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

            if count >= 12:
                break

            count += 1
            y_pos += 20

        but_x = self.Width * 0.65
        but_y = self.Height * 0.3

        self.button(newgame_but, but_x, but_y, 268, 68, 'pickplayer')
        but_y += 100

        self.CurrentHelp = 0
        self.button(help_but, but_x, but_y, 268, 68, 'help')
        self.TimeOut = 0
        but_y += 100

        self.button(options_but, but_x, but_y, 268, 68, 'options')
        but_y += 100

        self.button(exit_but, but_x, but_y, 268, 68, 'exit')

    def show_choose_players (self):
        x_pos = (self.Width * 0.5) - 134
        y_pos = self.Height * 0.6
        self.button(startturn_but, x_pos, y_pos, 268, 68, 'start game')
        
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

    def show_nextturn (self):

        but_x = (self.Width*0.5) - 134
        but_y = (self.Height*0.65)

        self.button(startturn_but, but_x, but_y, 268, 68, 'main menu')

    def Pick_Players(self):
        if self.Played == False:
            self.Played = True
            self.Display.fill(self.darkblue)
            self.show_backgroundship()
            self.show_logo ()
            self.Display.blit(self.headfont.render("Please insert the name of Player 1 in the opened textbox", True, self.white, (700, 100)),(self.Width * 0.5 - 375 , self.Height * 0.5 - 50))
            self.menu_display_refresh()
            checkpoint = False
            while checkpoint == False:
                checkpoint = True
                p1 = InputBox(self.Game, 'Player 1')
                if p1.player1 == "":
                    checkpoint = False

        
            self.Display.fill(self.darkblue)
            self.show_backgroundship()
            self.show_logo ()
            self.Display.blit(self.headfont.render("Please insert the name of Player 2 in the opened textbox", True, self.white, (700, 100)),(self.Width * 0.5 - 375 , self.Height * 0.5 - 50))
            self.menu_display_refresh()
            checkpoint = False
            while checkpoint == False:
                checkpoint = True
                p2 = InputBox(self.Game, 'Player 2')
                if p2.player2 == "" or p2.player2 == p1.player1:
                    checkpoint = False
    

            self.player1 = p1.player1
            self.player2 = p2.player2

            self.Display.fill(self.darkblue)
            self.show_backgroundship()
            self.show_logo ()
            self.Display.blit(self.headfont.render("Starting game | Player 1: " + self.player1 + " | Player2: " + self.player2, True, self.white, (700, 100)),(self.Width * 0.5 - 350 , self.Height * 0.5 - 50))
            self.menu_display_refresh()
            time.sleep(3)
            self.Game.Sound_enabled = self.soundfx
            self.Game.Music_enabled = self.backgroundmusic
            winner = self.Game.setupgame(self.player1, self.player2)
            if winner.Name == self.player1:
                print(self.player1 + " wins!")
                self.Game.Database.player_win(self.player1)
                self.Game.Database.player_lose(self.player2)
            elif winner.Name == self.player2:
                print(self.player2 + " wins!")
                self.Game.Database.player_win(self.player2)
                self.Game.Database.player_lose(self.player1)

            self.loop = False

    def show_options (self):

        x_pos = (self.Width * 0.5) - 134
        y_pos = self.Height * 0.4

        if self.backgroundmusic:
            self.button(backgroundmusic_on, x_pos, y_pos, 268, 68, 'backgroundmusic off')
        elif not self.backgroundmusic:
            self.button(backgroundmusic_off, x_pos, y_pos, 268, 68, 'backgroundmusic on')

        y_pos += 130

        if self.soundfx:
            self.button(soundfx_on, x_pos, y_pos, 268, 68, 'soundfx off')
        elif not self.soundfx:
            self.button(soundfx_off, x_pos, y_pos, 268, 68, 'soundfx on')

        y_pos += 130

        self.button(back_but, x_pos, y_pos, 268, 68, 'main menu')
        
    ##########################################

    ################  FUNCTIONS  ################

    def menu_start (self, name):

        self.loop = True

        while self.loop:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.loop = False
                    self.exit()

            self.Display.fill(self.darkblue)
        
            self.show_backgroundship()
            self.show_logo()

            self.show(name)
            if self.loop == True:
                self.menu_display_refresh()
            
    def show(self, name):

        if name == 'main menu':

            self.show_main()

        elif name == 'exit':

            self.loop = False
            self.exit()

        elif name == 'help':
            self.show_help(1)

        elif name == 'pickplayer':
            self.loop = False
            self.Pick_Players()

        elif name == 'options':
            self.show_options()
                        
    def addText(self, text, x, y, width, height):
        self.Display.blit(self.font.render(text, True, self.white, (width, height)),(x,y))

    def menu_display_refresh (self):
        pygame.display.flip()
        self.Cooldown += 1
        self.Clock.tick(15)

    def exit (self):
        pygame.quit()
        quit()

class InputBox:
    def __init__ (self, game, player):
        self.master = Tk()
        self.master.title('Enter your name')

        self.Game = game

        self.player = player

        self.player1 = ''
        self.player2 = ''

        self.mybutton = Button(self.master, text = 'Enter', command = self.get_name)
        self.mybutton.grid(row = 1, column = 0)

        self.usertext = StringVar()
        self.usertext.set(player)
        self.myentry = Entry(self.master, textvariable = self.usertext)
        self.myentry.grid(row = 0, column = 0)
        self.counter = 0

        self.master.mainloop()

    def get_name (self):

        name = self.usertext.get()
        self.Game.Database.data_entry(name)

        if self.player == 'Player 1':
            self.player1 = name # This will be player 1

        elif self.player == 'Player 2':
            self.player2 = name # This will be player 2

        self.close_window()

    def close_window (self):
        self.master.destroy()
