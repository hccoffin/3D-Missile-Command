from __future__ import print_function,division
from visual import *
import math

class Target(object):
    def __init__(self, x, y, z, radius):
        #initializes target
        self.position = vector(x, y, z)
        self.radius = radius
        self.launchPoints = self.findTargetLaunchPoints()
        self.colors = dict()
        green = (.114, .914, .714)
        blue = (0, .69, 100)
        yellow = (1, 1, 0)
        orange = (1, .439, .263)
        self.colors[self.launchPoints[0]] = orange
        self.colors[self.launchPoints[1]] = orange
        self.colors[self.launchPoints[2]] = blue
        self.colors[self.launchPoints[3]] = blue
        self.colors[self.launchPoints[4]] = yellow
        self.colors[self.launchPoints[5]] = yellow
        self.colors[self.launchPoints[6]] = green
        self.colors[self.launchPoints[7]] = green
        #draws earth
        self.draw()

    def findTargetLaunchPoints(self):
        # gets the target points (8 evenly distributed points)
        points = []
        for theta in [0, math.pi/2, math.pi, math.pi*3/2]:
            for phi in [.9553, 2.186]:
                x = math.sin(phi)*math.sin(theta)*self.radius
                y = math.cos(phi)*self.radius
                z = math.sin(phi)*math.cos(theta)*self.radius
                points += [vector(x, y, z)]
        return points

    def launchPointColor(point):
        return self.colors[point]

    def checkCollision(missile):
        #checks if missle collides with earth
        missilePos = missile.position
        collisionRadius = self.radius + missile.radius
        distance = (misslePos-self.position).mag
        return distance < collisionRadius

    def draw(self):
        #draws target or earth
        sphere(pos=tuple(self.position), radius=self.radius,
               material=materials.earth)
        #puts the launch points silos
        for p in range(len(self.launchPoints)):
            point = self.launchPoints[p]
            c = self.colors[point]
            cone(pos = tuple(point), radius = self.radius/10,
                 axis = tuple(point/10), color = c)