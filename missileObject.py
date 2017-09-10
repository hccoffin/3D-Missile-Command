from __future__ import print_function,division
from visual import *
import math,random

class explosion(object):
    def __init__(self,location,blastRadius,blastYield,secondary=False):
        self.over=False
        self.location=location
        self.blastRadius=blastRadius
        self.blastYield=blastYield
        self.secondary=secondary
        self.color=(1,1,0) if (not secondary) else (0,1,0)
        self.explosion=sphere(pos=self.location,
                              radius=self.blastRadius+0.0005,color=self.color)
    def timerFired(self):
        self.explosion.radius+=0.01
        self.explosion.opacity -= 0.01
        (r, g, b) = self.explosion.color
        g -= 0.01
        self.explosion.color = (r, g, b)
        if (self.explosion.radius>self.blastYield): #end explosion
            self.over=True
            self.explosion.visible=False
            del self.explosion

class missileObject(object):
    def __init__(self,launchLocation,velocity,blastYield,target=None,
                 blastRadius=0,counter=False):
        self.counter=counter
        self.destroyed=False
        self.radius=0.05
        self.targetThreshold=0.05
        self.despawnLength = 10
        self.color=color.red if not counter else color.green
        self.blastRadius=blastRadius
        self.blastYield=blastYield
        self.velocity=velocity
        self.launchLocation=launchLocation
        self.target=target
        self.missileBody=sphere(pos=tuple(launchLocation),
                                radius=self.radius,color=self.color,
                                make_trail = True)
        self.missileBody.trail_object.color=color.orange
        self.hitEarth = False
    @staticmethod
    def distance(point1,point2): #point1, point2 vectors
        return mag(point1-point2)
    def spawnMissiles(self):
        pass
    def timerFired(self,deltaT,targetRadius, collide = False,secondary=False):
        if collide or ((mag(vector(self.missileBody.pos))<targetRadius) or
            (mag(vector(self.missileBody.pos))>self.despawnLength) or
            (self.target!=None and
            (missileObject.distance(self.missileBody.pos,vector(self.target))
                                    <self.targetThreshold))):
            if (mag(vector(self.missileBody.pos))<targetRadius):
                self.hitEarth = True
            self.destroyed=True
            missileLocation=self.missileBody.pos
            blastRadius=0
            blastYield=self.blastYield
            self.missileBody.visible=False
            self.missileBody.trail_object.visible=False
            del self.missileBody.trail_object
            del self.missileBody
            return explosion(missileLocation,blastRadius,blastYield,secondary=secondary)
        self.missileBody.pos+=self.velocity*deltaT