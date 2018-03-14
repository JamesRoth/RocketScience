#James Roth
#3/14/18
#escapeVelocity.py - escape velocity for planets

earth=Planet()
from ggrocket import Rocket, Planet
from math import radians, sqrt
from ggmath import Slider

# Constants related to earth and physics
Re=6.371E6
Me=5.972E24
G=6.674E-11

#Claculating escape velocity 
Ve=sqrt(2*Me*G/Re)
print("Predicted escape velocity is", Ve, "m/s")
#Add a slider to control timezoom
tz=Slider((10,400),0,5,0,positioning="pyhsical")

rocket=Rocket(earth, heading=radians(90), directiond=90, velocity=Ve, timezoom=tz)
earth.run(rocket)
