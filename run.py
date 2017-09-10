from __future__ import print_function,division
from visual import *
from Target import Target
from Radar import Radar
from Radar import radarMis
from splashScreen import splashScreen
from game import game
from missileObject import missileObject
import math,random,time

s = splashScreen()
s.run()

missileCommand=game()
missileCommand.run()

