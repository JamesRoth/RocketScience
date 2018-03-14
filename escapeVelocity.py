#James Roth
#3/14/18
#escapeVelocity.py - escape velocity for planets

from ggrocket import Rocket, Planet
from math import radians

earth=Planet()
rocket=Rocket(earth, heading=radians(90), directiond=90, velocity=10)
earth.run(rocket)