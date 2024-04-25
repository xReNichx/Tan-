
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
tank_shot = pygame.mixer.Sound("tank_shot.mp3") 
tank_BOOM = pygame.mixer.Sound("tank_BOOM.mp3") 
 
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

 
class Bullet(Picture): 
    def __init__(self, filename, x, y, size, angel): 
        super().__init__(filename, x, y, size, size)   #клас пуля 
        # self.speed_bul_x = 10 
        # self.speed_bul_y = 10 
        self.angel = angel
    def move(self): 
        if self.angel==0:
            self.rect.y-=10
        if self.angel==90:
            self.rect.x-=10
        if self.angel==180:
            self.rect.y+=10
        if self.angel==270:
            self.rect.x+=10
        

  #      
 
bullets = [] 
 
 
class Tank(Picture): 
    def __init__(self, name, filename, x, y, size, forward_key, back_key, left_key, right_key, fire_key, speed_fire, xhp, yhp, pyx,vog): 
        super().__init__(filename, x, y, size, size)
        self.name=name
        self.vog=vog
        self.pyx=pyx 
        self.obj_angel = 0 
        self.forward_key = forward_key 
        self.back_key = back_key 
        self.left_key = left_key 
        self.right_key = right_key 
        self.fire_key = fire_key 
        self.size = size 
        self.xhp = xhp
        self.yhp = yhp
        self.d = 0 
        self.a = 0 
        self.s = 0 
        self.w = 0 
        self.hp = 100 #hp tank
        self.speed_fire = speed_fire 
        self.time_next_fire = time.time() + self.speed_fire
    def rotate_by(self, angle): 
        self.obj_angel += angle 
        self.image = pygame.transform.rotate(self.image, angle) 
 
    def set_angel(self, angel): 
        self.rotate_by(angel - self.obj_angel) 
 
 
    def move(self): 
        keys = pygame.key.get_pressed() 
 
        if keys[self.forward_key]: 
            self.set_angel(0) 
            self.w +=0.08
            self.rect.y -= self.w 
        elif keys[self.back_key]: 
            self.set_angel(180) 
            self.s +=0.08 
            self.rect.y += self.s 
        elif keys[self.left_key]: 
            self.set_angel(90) 
            self.a +=0.08 
            self.rect.x -= self.a 
        elif keys[self.right_key]: 
            self.set_angel(270) 
            self.d +=0.08 
            tank.rect.x += self.d 
 
        if not keys[self.forward_key]: 
            if self.w > 0: 
                self.w -=0.2 
                tank.rect.y -= self.w 
            else: 
                self.w = 0 
        if not keys[self.back_key]: 
            if self.s > 0: 
                self.s -=0.2 
                tank.rect.y += self.s 
            else: 
                self.s = 0 
        if not keys[self.right_key]: 
            if self.d > 0: 
                self.d -=0.2 
                tank.rect.x += self.d 
            else: 
                self.d = 0 
        if not keys[self.left_key]: 
            if self.a > 0: 
                self.a -=0.2 
                tank.rect.x -= self.a 
            else: 
                self.a = 0

    def fire(self): 
        if time.time()<self.time_next_fire:
            return
        
        keys = pygame.key.get_pressed() 
        if keys[self.fire_key]:
            tank_shot.play() 
            if self.obj_angel == 270: 
                bul = Bullet("bullet.png", self.rect.x + self.size , self.rect.y + (self.size/2)-5, 10, self.obj_angel) 
                bullets.append(bul) 
                
             
 
            if self.obj_angel == 90: 
                bul = Bullet("bullet.png",  self.rect.x -10, self.rect.y + (self.size/2)-5, 10, self.obj_angel) 
                bullets.append(bul) 
                
  
                #bul.rect.x-5 
            if self.obj_angel == 0: 
                bul = Bullet("bullet.png", self.rect.x + (self.size/2)-5 , self.rect.y -10, 10, self.obj_angel) 
                bullets.append(bul)

                
 
            if self.obj_angel == 180: 
                bul = Bullet("bullet.png", self.rect.x + (self.size/2)-5. , self.rect.y + self.size, 10, self.obj_angel) 
                bullets.append(bul) 

            self.time_next_fire = time.time() + self.speed_fire
    def hpdraw(self):
        text_lose = pygame.font.SysFont('verdana', 15).render("Dead", True, WHITE)
        mw.blit(text_lose, (self.xhp-5, self.yhp))
        red_polosa_hp = HitBox(self.xhp-35,self.yhp, 100, 20)
        green_polosa_hp = HitBox(self.xhp-35,self.yhp, self.hp, 20)
        pygame.draw.rect(mw, RED, red_polosa_hp.rect)
        pygame.draw.rect(mw, GREEN, green_polosa_hp.rect) 
        pygame.draw.rect(mw, GRAY, red_polosa_hp.rect, 3)
        text = pygame.font.SysFont('verdana', 15).render(f"{self.hp}", True, BLACK)
        mw.blit(text, (self.xhp, self.yhp))
    def ypr(self):
        text = pygame.font.SysFont('verdana', 15).render(f"{self.pyx}", True, WHITE)
        mw.blit(text, (self.xhp, self.yhp+20))
        text = pygame.font.SysFont('verdana', 15).render(f"{self.vog}", True, WHITE)
        mw.blit(text, (self.xhp, self.yhp+40))


walls = []
Stinka = []
tanks = []

def initialization():
    global walls, Stinka, tanks
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
    
    tanks = [ 
        Tank("player 1",'tank.png', 1300, 550, 50, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_m, 1, 1150, 45, "up, down, ringt, left - рух p2","m-вогонь"), 
        Tank("player 2",'tank.png', 100, 100, 50, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_f, 1, 100, 650,  "w, s, d, a, f - рух p1","f-вогонь")   
    ]

initialization()



btn_restart = Button(750, 450, 140 , 75,DARK_GREEN,3,RED )
btn_restart.set_text("RESTART", 20)

btn_exit = Button(750, 550, 140 , 75,DARK_GREEN,3,RED )
btn_exit.set_text("EXIT", 20)
 
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
 
    if tanks[0].hp == 0 or tanks[1].hp == 0:
        if bam == False:
            tank_BOOM.play()
            bam=True
        font = pygame.font.SysFont('verdana', 45)

        if tanks[0].hp == 0 and tanks[1].hp == 0:
            mw.fill(GREEN)
            text = font.render("Нічія", True, BLACK)                   
        elif tanks[0].hp == 0:
            mw.fill(GREEN)
            text = font.render(f"{tanks[1].name} WIN", True, BLACK)     
        elif tanks[1].hp == 0:
            mw.fill(GREEN)
            text = font.render(f"{tanks[0].name} WIN", True, BLACK)
        
        mw.blit(text, (650,350))
        
        btn_restart.draw(20,15) 
        btn_exit.draw(20,15)

        if mouse_click == True:
            if btn_restart.collidepoint(mouse_x, mouse_y):
                initialization()
            if btn_exit.collidepoint(mouse_x, mouse_y):
                game_over = True

    else:
        # рух усіх танків 
        for tank in tanks: 
            # зберігаємо попередні координати поточного танку 
            original_x = tank.rect.x 
            original_y = tank.rect.y 
    
            # переміщуємо танк 
            tank.move() 
            tank.fire() 
            # перевіряжмо чи він стикнувся зі стінками 
            for wall in walls: 
                # якщо стикнувся, то повернути такн на попередню позицію 
                if tank.colliderect(wall.rect): 
                    tank.rect.x = original_x 
                    tank.rect.y = original_y 
            for stina in Stinka: 
            # якщо стикнувся, то повернути такн на попередню позицію 
                if tank.colliderect(stina.rect): 
                    tank.rect.x = original_x 
                    tank.rect.y = original_y
            # перевіряємо чи стикунвся танк з іншим танком 
            for another_tank in tanks: 
                if tank == another_tank: 
                    continue 
                if tank.colliderect(another_tank.rect): 
                    tank.rect.x = original_x 
                    tank.rect.y = original_y 


    
        # відмалювання заднього фону 
        mw.fill(WHITE) 
        for bul in bullets: 
            bul.move() 
                
        # відмалювання усіх танків 
        for tank in tanks: 
            tank.draw() 
            for bul in bullets:
                if bul.colliderect(tank.rect):
                    tank.hp-=20
                    bullets.remove(bul) 
          
    
        # відмалювання стінок 
        for wall in walls: 
            wall.draw() 
            for bul in bullets:  
                if bul.colliderect(wall.rect):
                    bullets.remove(bul)
        for stina in Stinka:  
            for bul in bullets:    
                if bul.colliderect(stina.rect):  
                    bullets.remove(bul)  
                    Stinka.remove(stina)

        for stina in Stinka: 
            stina.draw()  

        for tank in tanks: 
            tank.hpdraw()
            tank.ypr()

        for bul in bullets: 
            bul.draw() 
        

         


    # оновлення екрану 
    pygame.display.update() 
    clock.tick(40)