from graphics import *
import math
import pygame
win=GraphWin("Collisions",1300,900)
win.setBackground(color_rgb(0,0,0))



m1=1
m2=100
speed=0.1

k=(m2/m1)**(1/2)
tan_theta_line=1.0/k
bottom=850
xstart=50
l2=500



def lines():
    line1=Line(Point(xstart,bottom),Point(1200+xstart,bottom))
    line2=Line(Point(xstart,bottom),Point(xstart+k*l2,bottom-l2))
    line1.setFill(color_rgb(255,0,0))
    line2.setFill(color_rgb(255,0,0))
    line1.draw(win)
    line2.draw(win)



class bullet:
    collisions=0
    def __init__(self,r,init_x_cor,init_y_cor,sp):
        self.r=r
        self.x=float(init_x_cor)
        self.y=float(init_y_cor)
        self.v=float(sp)
        self.theta=math.pi
    def collision(self):
        k1=self.x+self.v*(math.cos(self.theta))
        k2=self.y-self.v*(math.sin(self.theta))
        if(self.y>bottom):
            self.theta=2*math.pi-self.theta
            bullet.collisions+=1
        self.cols.setText("Collisions = "+ str(self.collisions))
        if self.x+self.y*k<xstart+k*bottom:
            bullet.collisions+=1
            self.theta=2*math.atan(tan_theta_line)-self.theta
            while self.x+self.y*k<xstart+k*bottom:
                self.move()
            self.cols.setText("Collisions = "+ str(self.collisions))
            


    def move(self):
        self.x+=self.v*(math.cos(self.theta))
        self.y-=self.v*(math.sin(self.theta))
        self.cir.move(self.v*(math.cos(self.theta)),-self.v*(math.sin(self.theta)))
        # print(self.theta)
    def draw(self,screen):
        pt=Point(self.x,self.y)
        self.cir=Circle(pt,self.r)
        self.cir.setFill(color_rgb(0,255,255))
        self.cir.draw(win)
        self.cols=Text(Point(100,120),"Collisions = "+ str(self.collisions))
        self.cols.setTextColor('white')
        self.cols.setSize(20)
        self.cols.draw(win)

b=bullet(5,1200,bottom-500/k,speed)
b.draw(win)
lines()
while True:
    b.collision()
    b.move()