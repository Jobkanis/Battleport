import pygame
pygame.init()

class Menu():
   
    def __init__(self):
            #import class_Button

            #pygame.mixer.music.load("sound/backgroundmusic.wav")
            pygame.mixer.music.load("sound/rockit.wav")
            pygame.mixer.music.play(-1)

            #Colors
            self.white = (255,255,255)
            self.black = (0,0,0)
            self.red = (255,0,0)
            self.green = (0,255,0)
            self.blue = (0,0,255)
            self.darkgrey = (15,15,23)

            #Screensize
            self.width = 1280
            self.height = 720
            self.size = (self.width,self.height)

            #Game Display
            self.gameDisplay = pygame.display.set_mode(self.size)
            pygame.display.set_caption('Battleport')
            self.clock = pygame.time.Clock()


            self.mouse = pygame.mouse.get_pos()
            self.click = pygame.mouse.get_pressed()

        #############################  IMAGES  ###############################

            #Logo image
            self.logoimg = pygame.image.load('img/logo.png')

            #Background ship
            self.backgroundship = pygame.image.load('img/background_ship.png')

            #Buttons images
            self.newgame_but = [pygame.image.load('but/newgame_button.png') , pygame.image.load('but/newgame_button_over.png')]
            self.help_but = [pygame.image.load('but/help_button.png') , pygame.image.load('but/help_button_over.png')]
            self.options_but = [pygame.image.load('but/options_button.png') , pygame.image.load('but/options_button_over.png')]
            self.chooseplayers_but = [pygame.image.load('but/chooseplayers_button.png') , pygame.image.load('but/chooseplayers_button_over.png')]
            self.addnewplayer_but = [pygame.image.load('but/addnewplayer_button.png') , pygame.image.load('but/addnewplayer_button_over.png')]
            self.exit_but = [pygame.image.load('but/exit_button.png') , pygame.image.load('but/exit_button_over.png')]
            self.back_but = [pygame.image.load('but/back_button.png') , pygame.image.load('but/back_button_over.png')]
            self.startturn_but = [pygame.image.load('but/startturn_button.png') , pygame.image.load('but/startturn_button_over.png')]

            #Top 10 content box
            self.top10img = pygame.image.load('img/top10.png')

    ######################################  FUNCTIONS  #######################################

    #Display logo
    def logo(self):
        #logo_x = width*0.02
        #logo_y = height*0.04
        logo_x = 15
        logo_y = 15
        logo_pos = (logo_x,logo_y)
        self.gameDisplay.blit(self.logoimg, logo_pos)

    #Display background ship
    def background_ship(self):
        ship_x = (self.width*0.5) - 360
        ship_y = (self.height*0.5) - 177
        ship_pos = (ship_x, ship_y)
        self.gameDisplay.blit(self.backgroundship, ship_pos)

    #Display buttons and functions
    def button(self, button, x, y, width, height, event=None):
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()
        if x + width > self.mouse[0] > x and y+ height > self.mouse[1] > y:
            
            self.gameDisplay.blit(button[1],(x,y))

            if self.click[0] == 1 and event != None:
                if event == 'newgame':
                    self.newgame()
                elif event == 'help':
                    self.nextturn()
                elif event == 'options':
                    self.options()
                elif event == 'chooseplayers':
                    self.chooseplayers()
                elif event == 'addnewplayer':
                    self.addnewplayer()
                elif event == 'exit':
                    pygame.quit()
                    quit()
                elif event == 'back':
                    self.Activate()
                elif event == 'startturn':
                    self.Activate()
        else:
           self.gameDisplay.blit(button[0],(x,y))

    #Display top 10
    def top10(self):
        x_pos = self.width*0.1
        y_pos = self.height*0.3
        pos = (x_pos,y_pos)
        self.gameDisplay.blit(self.top10img,pos)

    ###############################  MENU LOOPS  ###############################

    #New Game loop
    def newgame(self):
        new_game = True

        while new_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.gameDisplay.fill(self.darkgrey)
            self.background_ship()
            self.logo()

            but_x = (self.width*0.5) - 134 #Buttons X position
            but_y = self.height * 0.3 #Buttons Y start position
            self.button(self.chooseplayers_but,but_x,but_y,268,68,'chooseplayers')
            but_y += 130
        
            self.button(self.addnewplayer_but,but_x,but_y,268,68,'addnewplayers')
            but_y += 130

            self.button(self.back_but,but_x,but_y,268,68,'back')
            but_y += 130

            pygame.display.flip()
            self.clock.tick(15)

    #Help loop
    def help(self):
        pass

    #Options loop
    def options(self):
        pass

    #Choose players loop
    def chooseplayers(self):
        pass

    #Add new player loop
    def addnewplayer(self):
        pass

    #Tussenscherm
    def nextturn(self):
        ready = False
        while not ready:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.gameDisplay.fill(self.darkgrey)
            self.background_ship()
            self.logo()

            but_x = (self.width*0.5) - 134
            but_y = (self.height*0.65)

            self.button(self.startturn_but,but_x,but_y,268,68,'startturn')

            pygame.display.flip()
            self.clock.tick(15)


    ##########################  MAIN MENU  ##########################

    def Activate(self):
        main = True

        while main:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.gameDisplay.fill(self.darkgrey)
            self.background_ship()
            self.logo()
            self.top10()
            
            but_x = self.width*0.65 # Buttons X position

            but_y = self.height*0.25 # Buttons Y start position
            self.button(self.newgame_but, but_x, but_y, 268, 68, 'newgame')

            but_y += 100
            self.button(self.help_but,but_x,but_y,268,68,'help')

            but_y += 100
            self.button(self.options_but,but_x,but_y,268,68,'options')

            but_y += 100
            self.button(self.exit_but,but_x,but_y,268,68,'exit')

            pygame.display.flip()

            self.clock.tick(15)

    ##################################  GAME LOOP  ######################################
   
    #Game loop
    def game_loop():
        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
    
            self.gameDisplay.fill(self.white)
            pygame.display.flip()
            self.clock.tick(30)

menu = Menu()
menu.Activate() 
pygame.quit()
quit()