from __future__ import print_function,division
from visual import *
import math

class radarMis(object):
    def __init__(self,radar, mislaunchLocation,misVelocity,target=None):

        radar.radarScene.select()
        self.destroyed=False
        self.radius=1
        worldToRadar = 15/6
        self.launchLocation = (-1 * mislaunchLocation[0] * worldToRadar,
                               math.fabs(mislaunchLocation[1] * worldToRadar),
                               -1 * mislaunchLocation[2] * worldToRadar)
        self.ySign = mislaunchLocation[1]/math.fabs(mislaunchLocation[1])
        self.location2D = (self.launchLocation[0], 0, self.launchLocation[2])
        self.velocity =(-1 * misVelocity[0]*(worldToRadar),
                        misVelocity[1]*(worldToRadar),
                        -1 * misVelocity[2]*(worldToRadar))
        self.color = color.red
        self.despawn = 20
        self.radarMisBody=sphere(pos=tuple(self.launchLocation),
                                radius=self.radius,color=self.color)
        if self.ySign < 0: c = (1,1,1)
        else: c = color.black 
        self.line = cylinder(pos=tuple(self.location2D), 
                             axis = (0, self.launchLocation[1], 0), radius = .1,
                             color = c)

    def timerFired(self, deltaT):
        self.radarMisBody.pos.x += self.velocity[0]*deltaT
        self.radarMisBody.pos.y += -1 * math.fabs(self.velocity[1]*deltaT)
        self.radarMisBody.pos.z += self.velocity[2]*deltaT
        self.location2D = (self.radarMisBody.pos.x, 0, self.radarMisBody.pos.z)
        self.line.pos = self.location2D
        self.line.axis = (0, self.radarMisBody.pos.y, 0)
        if (mag(vector(self.radarMisBody.pos))<15/6):
            self.destroyed=True
            self.radarMisBody.visible=False
            self.line.visible = False
            del self.radarMisBody
            del self.line
            return False
        return True



class Radar(object):
    def __init__(self):
        #generates a new window for radar
        self.width=300
        self.height=300
        self.sceneCenter=(0,0,0)
        self.background=(0,0,0)

        self.radarScene=display(title="Radar",width=self.width,
                               height=self.height,center=self.sceneCenter,
                               background=self.background,x=800,y=400,
                               autoscale = False, 
                               userZoom = False,
                               userSpin = False,
                               range = (18,10,18))

        self.radarScene.select()
        # adds lights to scene
        self.radarScene.lights = (distant_light(direction = ( 0, 1,  0), color = color.gray(.4)),
                                  distant_light(direction = ( 0, 1, -1), color = color.gray(.2)),
                                  distant_light(direction = ( 0, 1,  1), color = color.gray(.2)),
                                  distant_light(direction = (-1, 1,  0), color = color.gray(.2)),
                                  distant_light(direction = ( 1, 1,  0), color = color.gray(.2)),)
        # sets default perspective
        self.radarScene.forward = vector(0, -1, -3)
        self.radarScene.userZoom = False
        self.radarScene.userSpin = False
        #draws the cylinder for radar
        cylinder(pos=(0,0,0), axis=(0,-2,0),
                 radius=15, color = (.18, .49, .196))
        planeSurface = (self.radarScene.forward[0]/100, 0, self.radarScene.forward[2]/100)
        self.plane = cylinder(pos = (0,0,0), axis = planeSurface
                              , radius = 100, color = color.white, opacity = .5)
        #draws the rods for navigation
        green = (.114, .914, .714)
        blue = (0, .69, 100)
        yellow = (1, 1, 0)
        orange = (1, .439, .263)
        cylinder(pos=(0,-.85,0),axis=(14.5,0,0),radius=1, color = green)
        cylinder(pos=(0,-.85,0),axis=(0,0,14.5),radius=1, color = yellow)
        cylinder(pos=(0,-.85,0),axis=(-14.5,0,0),radius=1, color = blue)
        cylinder(pos=(0,-.85,0),axis=(0,0,-14.5),radius=1, color = orange)

        #gets the intial camera view
        self.camRadius = 20
        self.camTheta = 0
        camX = math.sin(self.camTheta) * self.camRadius
        camZ = math.cos(self.camTheta) * self.camRadius
        self.radarScene.forward = vector(camX, -10, camZ)

        #for the test code
        self.gameOver = False

        #radar missles
        self.radarMisList = []

    def generateRadarMis(missle):
        pass

    def updateMis(self, target, missileList):
        #updates and draws missles
        self.radarScene.select()
        (targetX, targetY, targetZ) = target.position
        maxSpawnDistance = 15
        for missile in missileList:
            
            (miX,miY,miZ) = missile.missileBody.pos
            
            modelX = (miX - targetX) * (1/maxSpawnDistance) * 15
            modelZ = (miZ - targetZ) * (1/maxSpawnDistance) * 15
            
            #sphere(pos=(modelX,modelZ,0), radius = 3, color = color.red)
 
    def updateCam(self,dCamTheta):
        self.camTheta += dCamTheta
        camX = math.sin(self.camTheta) * self.camRadius
        camZ = math.cos(self.camTheta) * self.camRadius
        self.radarScene.forward = vector(camX, -10, camZ)
        planeSurface = (self.radarScene.forward[0]/100, 0, self.radarScene.forward[2]/100)
        self.plane.axis = planeSurface

    def test(self):
        while not self.gameOver:
            if self.radarScene.kb.keys!=0:
                key=self.radarScene.kb.getkey()
                if key=='esc':
                    print("Game over")
                    self.gameOver=True
                elif key == "right":
                    
                    self.camTheta += .2
                elif key == "left":
                    
                    self.camTheta -= .2

            camX = math.sin(self.camTheta) * self.camRadius
            camZ = math.cos(self.camTheta) * self.camRadius
            self.radarScene.forward = vector(camX, -10, camZ)

            rate(100)
        exit()

