import random
from tkinter.font import BOLD
from turtle import width
from webbrowser import get
import pygame
pygame.init()

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

fps = pygame.time.Clock()

pygame.display.set_caption('Rock Paper Scissors')
DISPLAY = pygame.display.set_mode([1400, 700])

rock_image = pygame.image.load('images/rock.svg').convert_alpha()
paper_image = pygame.image.load('images/paper.svg').convert_alpha()
scissors_image = pygame.image.load('images/scissors.svg').convert_alpha()

pygame.font.init()
font = pygame.font.SysFont('Futura', 100)

win = font.render('You Win!', True, WHITE)
draw = font.render('Draw!', True, WHITE)
lose = font.render('You Lose!', True, WHITE)
select = font.render('Take your pick', True, WHITE)

text_rect_win = win.get_rect(center=(700, 100))
text_rect_draw = draw.get_rect(center=(700, 100))
text_rect_lose = lose.get_rect(center=(700, 100))
text_rect_select = select.get_rect(center=(700, 100))

class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft =  (x, y)
        self.clicked = False
        
    def draw(self):
        action = False
        
        position = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        DISPLAY.blit(self.image, (self.rect.x, self.rect.y))
        return action
        


rock_button = Button(100, 280, rock_image, 0.25)
paper_button = Button(270, 280, paper_image, 0.2)
scissors_button = Button(420, 280, scissors_image, 0.2)

computer_rock_button = Button(880, 280, rock_image, 0.25)
computer_paper_button = Button(1050, 280, paper_image, 0.2)
computer_scissors_button = Button(1200, 280, scissors_image, 0.2)

rock_clicked = False
paper_clicked = False
scissors_clicked = False

computer_rock_clicked = False
computer_paper_clicked = False
computer_scissors_clicked = False

pick = random.randrange(1, 4)


while True:
    DISPLAY.fill((21, 128, 209))
    
    if paper_clicked == False and scissors_clicked == False:
        if rock_button.draw():
            rock_clicked = True

           
    if rock_clicked == False and scissors_clicked == False:
        if paper_button.draw():
            paper_clicked = True
            
    
    if paper_clicked == False and rock_clicked == False:
        if scissors_button.draw():
            scissors_clicked = True
            
    if paper_clicked == False and rock_clicked == False and scissors_clicked == False:
        if computer_rock_button.draw():
            print('r')

        if computer_paper_button.draw():
            print('p')

        if computer_scissors_button.draw():
                print('s')
            
    if rock_clicked or paper_clicked or scissors_clicked == True:
        if pick == 1:
            computer_rock_clicked = True
            if computer_rock_button.draw():
                print('r')
            
                

        elif pick == 2:
            computer_paper_clicked = True
            if computer_paper_button.draw():
                print('p')
                
                
        elif pick == 3:
            computer_scissors_clicked = True
            if computer_scissors_button.draw():
                print('s')


    if rock_clicked and computer_rock_clicked == True:
        DISPLAY.blit(draw, text_rect_draw)
        
    if paper_clicked and computer_paper_clicked == True:
        DISPLAY.blit(draw, text_rect_draw)
        
    if scissors_clicked and computer_scissors_clicked == True:
        DISPLAY.blit(draw, text_rect_draw)

    if rock_clicked and computer_paper_clicked == True:
        DISPLAY.blit(lose, text_rect_lose)
    
    if rock_clicked and computer_scissors_clicked == True:
        DISPLAY.blit(win, text_rect_win)
    
    if paper_clicked and computer_rock_clicked == True:
        DISPLAY.blit(win, text_rect_win)
    
    if paper_clicked and computer_scissors_clicked == True:
        DISPLAY.blit(lose, text_rect_lose)
    
    if scissors_clicked and computer_rock_clicked == True:
        DISPLAY.blit(lose, text_rect_lose)
    
    if scissors_clicked and computer_paper_clicked == True:
        DISPLAY.blit(win, text_rect_win)
    

    if paper_clicked == False and rock_clicked == False and scissors_clicked == False:
        DISPLAY.blit(select, text_rect_select)
    
    
    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()