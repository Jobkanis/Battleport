import pygame
#import class_Game



################  IMAGES  ################

#Logo
logoimg = pygame.image.load('img/logo.png')

#Background ship
backgroundshipimg = pygame.image.load('img/background_ship.png')

#Columns
column_normalimg = [pygame.image.load('grid/column.png') , pygame.image.load('grid/column_over.png')]

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


##########################################


class Visual:

    def __init__ (self, game, gameDisplay, clock, width, height):

        self.Game = game
        self.Display = gameDisplay
        self.Clock = clock
        self.Width = width
        self.Height = height
        self.Size = (width, height)

        self.loop = False

        self.move_boat = False
        self.p1_boat_1_x = 0
        self.p1_boat_1_y = 0


        #Colors
        self.darkblue = (15,15,23)
    
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



    ################  THE GAME  ################

    def show_game (self):

        ### SHOW GRID  ###

        pos_y = (self.Height * 0.5) - 250

        for grid_y in range (0,20):

            pos_x = (self.Width * 0.5) - 250

            for grid_x in range (0,20):

                self.column(column_normalimg, pos_x, pos_y, 25, 25, grid_x, grid_y )

                pos_x += 25

            pos_y += 25

        ##################

        if self.move_boat == True:

            x_pos = self.Width * 0.8
            y_pos = self.Height * 0.2

            self.button(rightarrow_but, x_pos + 34, y_pos - 34, 68, 68, 'right')
            self.button(leftarrow_but, x_pos - 102, y_pos - 34, 68, 68, 'left')
            self.button(uparrow_but, x_pos - 34, y_pos - 102, 68, 68, 'up')
            self.button(downarrow_but, x_pos - 34, y_pos + 34, 68, 68, 'down')
            self.button(x_but, x_pos + 130, y_pos - 102, 68, 68, 'cancel move')

        p1_boat_1 = self.place_boat(boat_red_size_2, self.p1_boat_1_x, self.p1_boat_1_y, 2, 'p1 boat 1')


    def show_nextturn (self):

        but_x = (self.Width*0.5) - 134
        but_y = (self.Height*0.65)

        self.button(startturn_but, but_x, but_y, 268, 68, 'next turn')

    ##########################################

    ################  FUNCTIONS  ################

    def run (self, name):

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

            self.display_refresh()


    def show(self, name):

        if name == 'game':

            self.show_game()

        elif name == 'next turn':

            self.show_nextturn()



    def display_refresh (self):

        pygame.display.flip()
        self.Clock.tick(15)


    def exit (self):

       pygame.quit()
       quit()


    def button (self, button, x, y, width, height, event=None):

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if (x + width) > mouse[0] > x and (y + height) > mouse[1] > y:
            
            self.Display.blit(button[1],(x,y))

            if click[0] == 1 and event != None:


                if event == 'right':

                    if self.p1_boat_1_x >= 19:

                        pass

                    else:

                        self.p1_boat_1_x += 1

                elif event == 'left':

                    if self.p1_boat_1_x <= 0:

                        pass
                    
                    else:

                        self.p1_boat_1_x -= 1


                elif event == 'down':

                    if self.p1_boat_1_y >= 18:

                        pass

                    else:

                        self.p1_boat_1_y += 1

                elif event == 'up':

                    if self.p1_boat_1_y <= 0:

                        pass

                    else:

                        self.p1_boat_1_y -= 1

                else:

                    if event == 'cancel move':

                        self.move_boat = False


        else:

           self.Display.blit(button[0],(x,y))


    def column (self, column, x, y, width, height, event_1=None, event_2=None):


        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if (x + width) > mouse[0] > x and (y + height) > mouse[1] > y:
            
            self.Display.blit(column[1],(x,y))

            if click[0] == 1 and event_1 != None and event_2 != None:
                
                pass


        else:
           self.Display.blit(column[0],(x,y))


    def boat (self, boat_name, x, y, width, height, event=None):

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if (x + width) > mouse[0] > x and (y + height) > mouse[1] > y:
            
            self.Display.blit(boat_name[1],(x,y))

            if click[0] == 1 and event != None:

                self.move_boat = True

        else:
           self.Display.blit(boat_name[0],(x,y))


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


    def place_boat(self, boat_img, x, y, size, event):

        x_pos = self.grid_position_x(x)
        y_pos = self.grid_position_y(y)

        if size == 2:

            self.boat(boat_img, x_pos, y_pos, 25, 50, event)

        elif size == 3:

            self.boat(boat_img, x_pos, y_pos, 25, 75, event)

        elif size == 4:

            self.boat(boat_img, x_pos, y_pos, 25, 100, event)