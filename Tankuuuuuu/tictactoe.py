
import pygame
import time
from random import randint
pygame.init()
gameover = 0
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0, 0)
GREEN = (0, 255, 51)
YELLOW = (255, 255, 0)
DARK_BLUE = (0, 0, 100)
BLUE = (80, 80, 255)
ccc=[1,2]
aaaaa=0
'''створюємо вікно програми'''
back = (10,230,230)#колір фону (background)
mw = pygame.display.set_mode((500,500))#Вікно програми (main window)
mw.fill(back)
clock = pygame.time.Clock()

cherga = RED

'''клас прямокутник'''
class Area():
    def __init__(self, x=0, y=0, width =10, height = 10, color=cherga):
        self.rect = pygame.Rect(x, y, width, height)#прямокутник
        self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(mw,self.fill_color,self.rect)
   
    def outline(self, frame_color, thickness):#обведення існуючого прямокутника
        pygame.draw.rect(mw, frame_color,self.rect, thickness)


    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)




'''клас напис'''
class Label(Area):  
    def set_text(self, text, fsize =12, text_color=(0,0,0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text,True, text_color)

tab = Label(80, 20, 250, 50, WHITE) 
tab.fill()

tab.outline(BLUE,5)


restart = Label(320, 20, 90, 50, YELLOW)
restart.set_text("restart",20)

restart.fill()
restart.outline(BLUE,5)

mw.blit(restart.image, (restart.rect.x + 10,restart.rect.y + 12))



def wo():
    tab.set_text("перемогли нулики", 20)

    tab.fill()
    tab.outline(BLUE,5)

    mw.blit(tab.image, (tab.rect.x + 10,tab.rect.y + 5))
def wx():
    tab.set_text("перемогли хрестики", 20)
    tab.fill()
    tab.outline(BLUE,5)

    mw.blit(tab.image, (tab.rect.x + 10,tab.rect.y + 5))
cards = []
num_cards =3
t = [0,0,0,  0,0,0,  0,0,0]
x =100

for i in range(num_cards):
    new_card = Label(x,100,100,100, WHITE)
    new_card2 = Label(x,205,100,100, WHITE)
    new_card3 = Label(x,310,100,100, WHITE)

    #new_card.outline(BLUE,10)
    #new_card2.outline(BLUE,10)
    #new_card3.outline(BLUE,10)

    cards.append(new_card)
    cards.append(new_card2)
    cards.append(new_card3)

    x = x +105

for i in range(9):
    cards[i].fill()
    #cards[i].outline(BLUE,5)

while True:
    #на кожному тіку перевіряємо клік::
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            if restart.collidepoint(x,y):
                mw.fill(back)
                restart.set_text("restart", 20)
                #cherga = WHITE
                restart.fill()
                restart.outline(BLUE,5)
                mw.blit(restart.image, (restart.rect.x + 10,restart.rect.y+12))
                tab.fill()
                tab.outline(BLUE,5)


                x = 100
                t = [0,0,0,  0,0,0,  0,0,0]
                gameover = 0
                for i in range(num_cards):
                    new_card = Label(x,100,100,100, WHITE)
                    new_card2 = Label(x,205,100,100, WHITE)
                    new_card3 = Label(x,310,100,100, WHITE)

                    x +=105
                for i in range(9):
                    #pygame.draw.rect(mw,cards[i].fill_color,cards[i].rect)
                    cards[i].color(WHITE)
                    cards[i].fill()

                #cherga = RED
            for i in range(9):
                if cards[i].collidepoint(x,y) and gameover == 0:
                    if cherga == GREEN and t[i] == 0:
                        cards[i].color(GREEN)
                        cards[i].fill()
                        t[i]=2
                        cards[i].set_text("O", 80)
                        mw.blit(cards[i].image, (cards[i].rect.x+20, cards[i].rect.y))
                        cherga= RED
                    elif cherga == RED and t[i] ==0:
                        cards[i].color(RED)
                        cards[i].fill()
                        cards[i].set_text("X", 80)
                        mw.blit(cards[i].image, (cards[i].rect.x+25, cards[i].rect.y))
                        cherga = GREEN
                        t[i]=1
                    def peremoga():
                        for c in ccc:
                            global gameover
                            if t[0]==c and t[1]==c and t[2]==c:
                                if c == 1:
                                    wx()
                                elif c == 2:
                                    wo()
                                gameover=1
                            elif t[3]==c and t[4]==c and t[5]==c:
                                if c == 1:
                                    wx()
                                elif c == 2:
                                    wo()            
                                gameover=1
                            elif t[6]==c and t[7]==c and t[8]==c:#рядок
                                if c == 1:
                                    wx()
                                elif c == 2:
                                    wo()
                                gameover=1 
                            elif t[0]==c and t[3]==c and t[6]==c:
                                if c == 1:
                                    wx()
                                elif c == 2:
                                    wo()
                                gameover=1
                            elif t[1]==c and t[4]==c and t[7]==c:
                                if c == 1:
                                    wx()
                                elif c == 2:
                                    wo()
                                gameover=1
                            elif t[2]==c and t[5]==c and t[8]==c:  #стовбик 
                                if c == 1:
                                    wx()
                                elif c == 2:
                                    wo()        
                                gameover=1
                            elif t[0]==c and t[4]==c and t[8]==c:
                                if c == 1:
                                    wx()
                                elif c == 2:
                                    wo()           
                                gameover=1
                            elif t[2]==c and t[4]==c and t[6]==c: 
                                if c == 1:
                                    wx()
                                elif c == 2:
                                    wo()          
                                gameover=1
                            else:
                                if 0 not in t and gameover == 0:
                                    tab.set_text("Нічия", 20)
                                    tab.fill()
                                    mw.blit(tab.image, (tab.rect.x + 10,tab.rect.y + 10))
                                    tab.outline(BLUE,5)

                    peremoga()
                    #if 0 not in t:
                    #    tab.set_text("Нічия", 35)
                    #    tab.fill()
                    #    mw.blit(tab.image, (tab.rect.x + 5,tab.rect.y + 5))
    pygame.display.update()
    clock.tick(40) 