import pygame
pygame.init()

pygame.mixer.music.load("sound/backgroundmusic.wav")
pygame.mixer.music.play(-1)

#Colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkgrey = (15,15,23)

#Screensize
width = 1280
height = 720
size = (width,height)

#Game Display
gameDisplay = pygame.display.set_mode(size)
pygame.display.set_caption('Battleport')
clock = pygame.time.Clock()




#############################  IMAGES  ###############################

#Logo image
logoimg = pygame.image.load('img/logo.png')

#Background ship
backgroundship = pygame.image.load('img/background_ship.png')

#Buttons images
newgame_but = [pygame.image.load('but/newgame_button.png') , pygame.image.load('but/newgame_button_over.png')]
help_but = [pygame.image.load('but/help_button.png') , pygame.image.load('but/help_button_over.png')]
options_but = [pygame.image.load('but/options_button.png') , pygame.image.load('but/options_button_over.png')]
chooseplayers_but = [pygame.image.load('but/chooseplayers_button.png') , pygame.image.load('but/chooseplayers_button_over.png')]
addnewplayer_but = [pygame.image.load('but/addnewplayer_button.png') , pygame.image.load('but/addnewplayer_button_over.png')]
exit_but = [pygame.image.load('but/exit_button.png') , pygame.image.load('but/exit_button_over.png')]
back_but = [pygame.image.load('but/back_button.png') , pygame.image.load('but/back_button_over.png')]

#Top 10 content box
top10img = pygame.image.load('img/top10.png')




######################################  FUNCTIONS  #######################################

#Display logo
def logo():
    #logo_x = width*0.02
    #logo_y = height*0.04
    logo_x = 15
    logo_y = 15
    logo_pos = (logo_x,logo_y)
    gameDisplay.blit(logoimg,logo_pos)

#Display background ship
def background_ship():
    ship_x = (width*0.5) - 360
    ship_y = (height*0.5) - 177
    ship_pos = (ship_x,ship_y)
    gameDisplay.blit(backgroundship,ship_pos)

#Display buttons and functions
def button(button,x,y,width,height,event=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+width > mouse[0] > x and y+height > mouse[1] > y:
        gameDisplay.blit(button[1],(x,y))
        if click[0] == 1 and event != None:
            if event == 'newgame':
                newgame()
            elif event == 'help':
                help()
            elif event == 'options':
                options()
            elif event == 'chooseplayers':
                chooseplayers()
            elif event == 'addnewplayer':
                addnewplayer()
            elif event == 'exit':
                pygame.quit()
                quit()
            elif event == 'back':
                main_menu()
    else:
        gameDisplay.blit(button[0],(x,y))

#Display top 10
def top10():
    x_pos = width*0.1
    y_pos = height*0.3
    pos = (x_pos,y_pos)
    gameDisplay.blit(top10img,pos)





###############################  MENU LOOPS  ###############################

#New Game loop
def newgame():
    newgame = True

    while newgame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(darkgrey)
        background_ship()
        logo()

        but_x = (width*0.5) - 134 #Buttons X position
        but_y = height * 0.3 #Buttons Y start position

        button(chooseplayers_but,but_x,but_y,268,68,'chooseplayers')
        but_y += 130
        
        button(addnewplayer_but,but_x,but_y,268,68,'addnewplayers')
        but_y += 130

        button(back_but,but_x,but_y,268,68,'back')
        but_y += 130

        pygame.display.flip()
        clock.tick(15)


#Help loop
def help():
    pass

#Options loop
def options():
    pass

#Choose players loop
def chooseplayers():
    pass

#Add new player loop
def addnewplayer():
    pass




##########################  MAIN MENU  ##########################

def main_menu():
    main = True

    while main:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(darkgrey)
        background_ship()
        logo()
        top10()

        but_x = width*0.65 # Buttons X position
        but_y = height*0.25 # Buttons Y start position

        button(newgame_but,but_x,but_y,268,68,'newgame')
        but_y += 100

        button(help_but,but_x,but_y,268,68,'help')
        but_y += 100

        button(options_but,but_x,but_y,268,68,'options')
        but_y += 100

        button(exit_but,but_x,but_y,268,68,'exit')
        but_y += 100

        pygame.display.flip()
        clock.tick(15)





##################################  GAME LOOP  ######################################
   
#Game loop
def game_loop():
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    
        gameDisplay.fill(white)
        pygame.display.flip()
        clock.tick(30)

main_menu()
pygame.quit()
quit()