
import pygame 
import time 

pygame.init() 
GREEN = (15, 255, 15) 
RED = (255, 5, 5) 
WHITE = (255, 255, 255)  # колір фону (background) 
BLACK = (0, 0, 0) 
GRAY = (20,20,20)
DARK_GREEN = (18,115,52)
mw = pygame.display.set_mode((1500, 750))
clock = pygame.time.Clock()

pygame.mixer.init()
#tank_shot = pygame.mixer.Sound("tank_shot.mp3") 
#tank_BOOM = pygame.mixer.Sound("tank_BOOM.mp3") 
 
class Area(): 
    def __init__(self, x=0, y=0, width=10, height=10, color_back=BLACK, border_width = 3, border_color = BLACK): #конструктор 
        self.rect = pygame.Rect(x, y, width, height) #прямокутник 
        self.fill_color = color_back 
        self.border_width = border_width 
        self.border_color = border_color 
    def color(self, new_color): 
        self.fill_color = new_color 
    def fill(self): 
        pygame.draw.rect(mw, self.fill_color, self.rect) 
    def outline(self): #обведення існуючого прямокутника 
        pygame.draw.rect(mw, self.border_color, self.rect, self.border_width)   
    def collidepoint(self, x, y): 
        return self.rect.collidepoint(x, y)     
 
 

class Button(Area): 
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)): 
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color) 
        #створюємо текст 
    def draw(self, shift_x=0, shift_y=0): 
        self.fill() 
        self.outline()         
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y)) 
   

class HitBox: 
    def __init__(self, x, y, width, height): 
        self.rect = pygame.Rect(x, y, width, height) 
 
    def colliderect(self, rect): 
        return self.rect.colliderect(rect) 
 
 
# клас для об'єктів-картинок 
class Picture(HitBox): 
    def __init__(self, filename, x, y, width, height): 
        super().__init__(x, y, width, height) 
        self.image = pygame.transform.scale(pygame.image.load(filename), (width, height)) 
 
    def draw(self): 
        mw.blit(self.image, (self.rect.x, self.rect.y)) 



class Wall(HitBox): 
    def __init__(self, color, x, y, width, height): 
        super().__init__(x, y, width, height) 
        self.color = color 
 
    def draw(self): 
        pygame.draw.rect(mw, self.color, self.rect) 

class Stina(HitBox): 
    def __init__(self, filename, x, y, width, height): 
        super().__init__(x, y, width, height) 
        self.image = pygame.transform.scale(pygame.image.load(filename), (width, height)) 
 
    def draw(self): 
        mw.blit(self.image, (self.rect.x, self.rect.y))
  
class Karta(Picture):
    def __init__(self, filename, x, y, width, height):
        super().__init__(filename, x, y, width, height)


first_karta = Karta()


walls = [ 
    Wall(BLACK, 0, 0, 1400, 50), 
    Wall(BLACK, 0, 700, 1450, 50), 
    Wall(BLACK, 0, 0, 50, 700), 
    Wall(BLACK, 1400, 0, 50, 700), 
    Wall(BLACK, 300, 50, 50, 250), 
    Wall(BLACK, -10, 250, 200, 50), 
    Wall(BLACK, 550, 50, 50, 250), 
    Wall(BLACK, 180, 450, 450, 50), 
    Wall(BLACK, 250, 600, 50, 150), 
    Wall(BLACK, 400, 450, 50, 150), 
    Wall(BLACK, 580, 600, 50, 100), 
    Wall(BLACK, 800, 250, 50, 350), 
    Wall(BLACK, 1100, 450, 50, 250), 
    Wall(BLACK, 1000, 250, 450, 50), 
    Wall(BLACK, 1270, 450, 150, 50), 
    Wall(BLACK, 0, 0, 1400, 50), 
    Wall(BLACK, 0, 600, 300, 300), 
    Wall(BLACK, 1100, 0, 300, 300),

    ]

Stinka = [ 
    Stina("Stina_lamat.png",190, 250, 55, 50), 
    Stina("Stina_lamat.png",245, 250, 55, 50), 
    Stina("Stina_lamat.png",500, 250, 50, 50), 
    Stina("Stina_lamat.png",450, 250, 50, 50), 
    Stina("Stina_lamat.png",405, 250, 50, 50),  
    Stina("Stina_lamat.png",350, 250, 55, 50), 
    Stina("Stina_lamat.png",50, 450, 55, 50), 
    Stina("Stina_lamat.png",105, 450, 50, 50), 
    Stina("Stina_lamat.png",150, 450, 50, 50), 
    Stina("Stina_lamat.png",250, 550, 50, 50), 
    Stina("Stina_lamat.png",250, 500, 50, 50), 
    Stina("Stina_lamat.png",400, 600, 50, 50), 
    Stina("Stina_lamat.png",400, 650, 50, 50), 
    Stina("Stina_lamat.png",580, 550, 50, 50), 
    Stina("Stina_lamat.png",580, 500, 50, 50), 
    Stina("Stina_lamat.png",750, 450, 50, 50), 
    Stina("Stina_lamat.png",625, 450, 50, 50), 
    Stina("Stina_lamat.png",675, 450, 50, 50), 
    Stina("Stina_lamat.png",700, 450, 50, 50), 
    Stina("Stina_lamat.png",850, 250, 50, 50), 
    Stina("Stina_lamat.png",900, 250, 50, 50), 
    Stina("Stina_lamat.png",950, 250, 50, 50), 
    Stina("Stina_lamat.png",800, 200, 50, 50), 
    Stina("Stina_lamat.png",800, 150, 50, 50), 
    Stina("Stina_lamat.png",800, 100, 50, 50), 
    Stina("Stina_lamat.png",800, 50, 50, 50), 
    Stina("Stina_lamat.png",800, 600, 50, 50), 
    Stina("Stina_lamat.png",800, 650, 50, 50), 
    Stina("Stina_lamat.png",600, 250, 50, 50), 
    Stina("Stina_lamat.png",650, 250, 50, 50), 
    Stina("Stina_lamat.png",700, 250, 50, 50), 
    Stina("Stina_lamat.png",750, 250, 50, 50), 
    Stina("Stina_lamat.png",1150, 450, 60, 50), 
    Stina("Stina_lamat.png",1210, 450, 60, 50), 
    Stina("Stina_lamat.png",1100, 400, 50, 50), 
    Stina("Stina_lamat.png",1100, 350, 50, 50), 
    Stina("Stina_lamat.png",1100, 300, 50, 50), 
    ]
    

 
# прапор закінчення гри 
game_over = False 

bam=False
 
while not game_over: 
 
    mouse_x = 0
    mouse_y = 0
    mouse_click = False
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_click = True
            mouse_x, mouse_y = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            if restart.collidepoint(x,y):

 
        mw.fill(WHITE) 




          
    
        # відмалювання стінок 
        #for wall in walls: 
        #    wall.draw() 

        #for stina in Stinka: 
        #    stina.draw()  

    # оновлення екрану 
    pygame.display.update() 
    clock.tick(40)