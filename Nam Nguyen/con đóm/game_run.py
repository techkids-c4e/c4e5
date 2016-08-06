import pygame
import time
import random
from pygame.locals import *
import pygame, sys, eztext
#khoi tao tat ca ca'c module duoc import tu pygame
pygame.init()

white = (255, 255, 255)
gray = (185, 185, 185)
black = ( 0, 0, 0)
red = (155, 0, 0)
green = ( 0, 155, 0)
blue = ( 0, 0, 155)
yellow = (155, 155, 0)

display_width = 800  #ngang
display_height = 600    #doc

#set width and height
gameDisplay = pygame.display.set_mode((display_width,display_height))

#dat title cua cua so la My game
pygame.display.set_caption("Ran")

#cap nhat man hinh va tiep tuc vong lap tiep theo
pygame.display.update()

icon = pygame.image.load('D:\game\IMG_4055.JPG')
pygame.display.set_icon(icon)

img = pygame.image.load('D:\game\iii.png') #anh dau ran
appleimg = pygame.image.load('D:\game\images_8.jpeg') #anh tao nho
bigappleimg = pygame.image.load('bigApple.jpg')

clock = pygame.time.Clock()

AppleThickness = 30
block_size = 20
FPS = 30

direction = "right"

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        gameDisplay.fill(white)
        message_to_screen("paused",black,-100,size = "large")
        message_to_screen("Press C to continue or Q to quit",black,25)
        pygame.display.update()
        clock.tick(5)
        
                


def score(score):
    text = smallfont.render("Score: "+ str(score), True, black)
    gameDisplay.blit(text,[0,0])

def randAppleGen():
    randAppleX = round(random.randrange(0, display_width-AppleThickness))#/20.0)*20.0
    randAppleY = round(random.randrange(0, display_height-AppleThickness))#/20.0)*20.0

    return randAppleX, randAppleY

def Tao_to(): 
    Tao_toX = round(random.randrange(0, display_width-AppleThickness*3))#/20.0)*20.0
    Tao_toY = round(random.randrange(0, display_height-AppleThickness*3))#/20.0)*20.0
    return Tao_toX, Tao_toY
def game_intro():
    intro = True
    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        
        message_to_screen("Welcome to Slither",
                          yellow,
                          -100,
                          "large")
        message_to_screen("The objective of the game is to eat red apples",
                          black,
                          -30)
        message_to_screen("The more apples you eat, the longer you get",
                          black,
                          10)
        message_to_screen("If you run into yourself, or the edges, you die!",
                          black,
                          50)

        message_to_screen("Moi Ban Nhap Ten: ",
                          black,
                          90)
        message_to_screen("Press C to play or Q to quit.",
                          black,
                          180)
        pygame.display.update()
        clock.tick(15)
        
def snake(block_size, snakelist):

    if direction == "right":
        head = pygame.transform.rotate(img, 270)
    if direction == "left":
        head = pygame.transform.rotate(img, 90)
    if direction == "up":
        head = img
    if direction == "down":
        head = pygame.transform.rotate(img, 180)
    
    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))

    
    for XnY in snakelist[:-1]:  
         pygame.draw.rect(gameDisplay, blue, [XnY[0],XnY[1],block_size,block_size])#vi tri cua môi(400,300) width and height cua môi(20,20)

def text_objects(text,color,size):
    if size =="small":
        textSurface = smallfont.render(text, True, color)
    elif size =="medium":
        textSurface = medfont.render(text, True, color)
    elif size =="large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()
    


def message_to_screen(msg,color, y_displace = 0, size = "small"):
    textSurf, textRect = text_objects(msg,color, size)
    textRect.center = (display_width / 2), (display_height/2) + y_displace
    gameDisplay.blit(textSurf, textRect)

def gameLoop():
    global snakeScore
    snakeScore = 0
    global direction
    direction = 'right'
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2
    
    lead_x_change = 10
    lead_y_change = 0

    block_speed = 15
    
    snakeList = []
    snakeLength = 1
    
    randAppleX, randAppleY = randAppleGen()
    Tao_toX,Tao_toY= Tao_to()
    
    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(green)
            message_to_screen("Game over",
                              red,
                              -50,
                              size = "large")
            message_to_screen("Press C to play again or Q to quit",
                              black,
                              50,
                              size = "medium")
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = False
                        
                        gameExit = True
                        
                    if event.key == pygame.K_c:
                        gameLoop()

                        


        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_speed
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_speed
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_speed
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_speed
                    lead_x_change = 0

                elif event.key == pygame.K_p:
                    pause()

        if lead_x >= display_width:
            lead_x=0
        elif lead_x < 0:
            lead_x=800
        elif lead_y >= display_height:
            lead_y=0
        elif lead_y < 0:
            lead_y=600


                    
        lead_x += lead_x_change
        lead_y += lead_y_change     

        gameDisplay.fill(white)#màu nen

        
        gameDisplay.blit(appleimg, (randAppleX, randAppleY))
        gameDisplay.blit(bigappleimg, (Tao_toX, Tao_toY))
        
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True #ran cham vao ng la thua
 
        snake(block_size, snakeList)
        score(snakeScore)
        
        pygame.display.update()

        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:
            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:
                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1
                snakeScore += 1
            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1
                snakeScore += 1

        if lead_x > Tao_toX and lead_x < Tao_toX + AppleThickness*3 or lead_x + block_size > Tao_toX and lead_x + block_size < Tao_toX + AppleThickness*3:
            if lead_y > Tao_toY and lead_y < Tao_toY + AppleThickness*3:
                Tao_toX, Tao_toY = Tao_to()
                snakeLength += 1
                snakeScore += 5
            elif lead_y + block_size > Tao_toY and lead_y + block_size< Tao_toY + AppleThickness*3:
                Tao_toX, Tao_toY = Tao_to()
                snakeLength += 1
                snakeScore += 5
                

        
        clock.tick(FPS)# speed chay cua snake

    pygame.quit()
    quit()

game_intro()   
gameLoop()
