import pygame
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 600))
wall =pygame.draw.rect(screen,(255,0,0),pygame.Rect(0,10,100,1000))
wallx=100
bottomy=550
bottom =pygame.draw.rect(screen,(255,0,0),pygame.Rect(0,bottomy,800,50))
pygame.display.set_caption("Collision counter")
clock=pygame.time.Clock()

m1=1
m2=10000
speed=0.1
class block:
    collisions=0
    def __init__(self,l_x,l_y,init_x_cor,mass,init_v):
        self.l_x=float(l_x)
        self.l_y=float(l_y)
        self.rectangle=pygame.rect.Rect((float(init_x_cor),bottomy-l_y,l_x,l_y))
        self.x=float(init_x_cor)
        self.v=float(init_v)
        self.mass=mass
    def collision(self,b):
        k=(self.v)+0
        self.v=(2*b.mass*b.v+self.mass*self.v-b.mass*self.v)/(self.mass+b.mass)
        b.v=self.v+k-b.v
        block.collisions+=1
    def wall_collision(self):
        self.v=-self.v
        block.collisions+=1
    def move(self):
        self.x+=self.v
        self.rectangle.x+=self.v
    def draw(self,screen):
        r=pygame.rect.Rect(self.x,bottomy-self.l_y,self.l_x,self.l_y)
        pygame.draw.rect(screen,(255,255,0),r)
        
        
        font1=pygame.font.Font('freesansbold.ttf',int(self.font_size))
        mass=font1.render(str(self.mass),True,(0,255,0))
        screen.blit(mass,(self.x,bottomy-self.l_y-self.font_size))
        font2=pygame.font.Font('freesansbold.ttf',32)
        scor=font2.render("Collisions:" + str(block.collisions),True,(255,255,255))
        screen.blit(scor,(550,100))
    
block1=block(30,30,300,m1,0)
block2=block(100,100,500,m2,-speed)

# s1=pygame.draw.rect(screen,(255,255,0),pygame.Rect(block2.x,bottomy-block2.l_y,block2.l_x,block2.l_y))

# s2=pygame.draw.rect(screen,(255,255,0),pygame.Rect(block1.x,bottomy-block1.l_y,block1.l_x,block1.l_y))

# def draw_block(b,b1):
    # global s1
    # global s2
    # s1.move_ip(b.v,0)
    # s2.move_ip(b1.v,0)
    # pass
    

running =True
while running:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False
            
    if block1.x<100:
        block1.wall_collision()
    if block1.x+block1.l_x>block2.x:
        block1.collision(block2)
    block1.font_size=20
    block2.font_size=17
    block1.move()
    block2.move()
    screen.fill((0,0,0))
    block1.draw(screen)
    block2.draw(screen)
    # draw_block(block2)
    if block1.v>0 and block2.v>0 and block2.v>block1.v:
        font=pygame.font.Font('freesansbold.ttf',32)
        scor1=font.render("No more collisions",True,(255,255,255))
        scor2=font.render("possible",True,(255,255,255))
        screen.blit(scor1,(500,150))
        screen.blit(scor2,(590,180))
    wall =pygame.draw.rect(screen,(255,0,0),pygame.Rect(0,10,100,1000))
    bottom =pygame.draw.rect(screen,(255,0,0),pygame.Rect(0,bottomy,800,50))
    pygame.display.update()
    clock.tick(6000000)
    
