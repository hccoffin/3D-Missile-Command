from __future__ import print_function,division
from visual import *

class splashScreen(object):
    def __init__(self):
        #generates a new window for radar
        self.width=800
        self.height=800
        self.sceneCenter=(0,0,0)
        self.background=(0,0,0)

        self.splashScene=display(title="3D Missle Command",width=self.width,
                               height=self.height,center=self.sceneCenter,
                               background=self.background,x=270,y=30, 
                               userZoom = False,
                               userSpin = False,
                               autoscale = False)
        self.splashScene.forward = vector(0, 0, -1)
        self.splashScene.lights = (distant_light(direction = ( 1, 0,  0), color = color.gray(.4)),
                                 distant_light(direction = (-1, 0,  0), color = color.gray(.5)),
                                 distant_light(direction = ( 0, 0,  1), color = color.gray(.6)),
                                 distant_light(direction = ( 0, 0, -1), color = color.gray(.7)),
                                 )
        self.splashScene.range = (5,5,5)
        self.splashScene.select()
        text(pos=(0,2,0),
            text='Missile\nCommand\n3D',
            align='center', depth=-0.3, color=color.green, height = 1)
        text(pos=(0,-3,0),
            text='Inspired by the 1980 Atari Missile Command\nInsert Token To Start',
            align='center', depth=.1, color=color.blue, height = 0.2)
        self.splashOver = False

        #gets the camera view
        self.camRadius = 5
        self.camTheta = math.pi * 3/4
        camX = math.sin(self.camTheta) * self.camRadius
        camZ = math.cos(self.camTheta) * self.camRadius
        self.splashScene.forward = vector(camX, -1, camZ)
        self.dir = 1

    def timerFired(self):
        self.camTheta += .005 * self.dir
        if self.camTheta >= 3/2 * math.pi - math.pi/4:
            self.dir = -1
        elif self.camTheta <= math.pi/2 + math.pi/4:
            self.dir = 1
        camX = math.sin(self.camTheta) * self.camRadius
        camZ = math.cos(self.camTheta) * self.camRadius
        self.splashScene.forward = vector(camX, -1, camZ)

    def run(self):
        self.splashScene.select()
        while not self.splashOver:
            #mouse events
            if self.splashScene.mouse.events!=0:
                print("Click!")
                self.splashOver = True
            if self.splashScene.kb.keys!=0:
                self.splashOver = True
                
            #timer fired
            self.timerFired()

            rate(100)
        self.splashScene.delete()
        
