from __future__ import print_function,division
from visual import *

class scoreScreen(object):
    def __init__(self):
        #generates a new window for radar
        self.width=300
        self.height=300
        self.sceneCenter=(0,0,0)
        self.background=(0,0,0)

        self.scoreScene=display(title="Score Screen",width=self.width,
                               height=self.height,center=self.sceneCenter,
                               background=self.background,x=800,y=50,
                               autoscale = False,
                               userZoom = False,
                               userSpin = False)
        
        self.scoreScene.forward = vector(0, 0, -1)
        label(pos=(0,8,0), text='Score Screen', box=True,height = 20)
        self.missilesHit = 0
        self.missilesHitEarth = 0
        textHit = "Score:%d" % (self.missilesHit)
        self.wehit = label(pos=(0,3,0), text=textHit, box=False,height=20)
        textHitBy = "Hits Taken:%d" % (self.missilesHitEarth)
        self.hitby = label(pos=(0,0,0), text= textHitBy, box=False, height=20)

    def timerFired(self):
        textHit = "Score:%d" % (self.missilesHit)
        self.wehit.text = textHit 
        textHitBy = "Hits Taken:%d" % (self.missilesHitEarth)
        self.hitby.text = textHitBy

