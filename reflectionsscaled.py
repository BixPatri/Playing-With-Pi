from graphics import *
import math
win=GraphWin("Collisions",1300,900)
win.setBackground(color_rgb(0,0,0))


# pt=Point(1200,800)
# cir=Circle(pt,4)
# cir.setFill(color_rgb(0,255,255))
# cir.draw(win)
m1=1
m2=10000
speed=0.01

k=(m2/m1)**(1/2)
tan_theta_line=1.0/k
bottom=850
xstart=50
l2=500



def lines():
    line1=Line(Point(xstart,bottom),Point(1200+xstart,bottom))
    line2=Line(Point(xstart,bottom),Point(xstart+k*l2,(bottom-l2-bottom)*k+bottom))
    line1.setFill(color_rgb(255,0,0))
    line2.setFill(color_rgb(255,0,0))
    line1.draw(win)
    line2.draw(win)



class particle:
    collisions=0
    def __init__(self,r,init_x_cor,init_y_cor,sp):
        self.r=r
        self.x=float(init_x_cor)
        self.y=float(init_y_cor)
        self.v=float(sp)
        self.theta=math.pi
        # self.prev=False
    def collision(self):
        # print("hi")
        k1=self.x+self.v*(math.cos(self.theta))
        k2=self.y-self.v*(math.sin(self.theta))
        if(self.y>bottom):
            # self.prev=True
            self.theta=2*math.pi-self.theta
            particle.collisions+=1
            self.cols.setText("Collisions = "+ str(self.collisions))
            
            
            # lines()
        if self.x+self.y*k<xstart+k*bottom:
            particle.collisions+=1
            # if(math.sin(self.theta)<.00000001):
            #     self.theta+=2*math.atan(tan_theta_line)
            # else:
            self.theta=2*math.atan(tan_theta_line)-self.theta
            self.cols.setText("Collisions = "+ str(self.collisions))
            
            while self.x+self.y*k<xstart+k*bottom:
                self.move()

    def move(self):
        self.x+=self.v*(math.cos(self.theta))
        self.y-=self.v*(math.sin(self.theta))
        self.cir.move(self.v*(math.cos(self.theta)),-k*self.v*(math.sin(self.theta)))
        # print(self.theta)
    def draw(self,screen):
        pt=Point(self.x,k*(self.y-bottom)+bottom)
        self.cir=Circle(pt,self.r)
        self.cir.setFill(color_rgb(0,255,255))
        self.cir.draw(screen)
        
        self.cols=Text(Point(100,120),"Collisions = "+ str(self.collisions))
        self.cols.setTextColor('white')
        self.cols.setSize(20)
        self.cols.draw(win)
        
        # lines()
# clock=pygame.time.Clock()
b=particle(4,1200,bottom-400/k,speed)
b.draw(win)
lines()
while True:
    b.collision()
    b.move()
    