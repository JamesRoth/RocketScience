#James Roth
#3/14/18
#escapeVelocity.py - escape velocity for planets

from ggrocket import Rocket, Planet
from math import radians, sqrt

# Constants related to earth and physics
Re=6.371E6
Me=5.972E24
G=6.674E-11

#Claculating escape velocity 
Ve=sqrt(2*Me*G/Re)
print("Redicted escape velocity is", Ve, "m/s")

earth=Planet()
rocket=Rocket(earth, heading=radians(90), directiond=90, velocity=Ve)
earth.run(rocket)
