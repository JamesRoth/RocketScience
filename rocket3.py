#James Roth
#3/15/18
#rocket3.py - controlling a rocket

from ggrocket import Rocket, Planet
from math import sqrt, log, radians
from ggmath import InputButton, Timer

earth=Planet(planetmass=0)

RocketStarted=0
StartTime=None
BurnTime=0

me=25600
mp=395700
F1D=716000
N1D=9

Ftotal=F1D*N1D
tbrun=180

vmax=Ftotal*tburn/(me+mp)
print("Predicted final velocity (Newton's 2nd law), vmax:", vmax, "m/s")

def GetThrust():
    global BurnTime
    global RocketStarted
    if RocketStarted:
        BurnTime=rocket.shiptime - StartTime
        if BurnTime>=tburn:
            RocketStarted=0
            return 0
        else:
            return Ftotal
def StartRocket():
    global RocketStarted
    global StartTime
    if not RocketStarted:
        RocketStarted=1
        StartTime=rocket,shiptime
start=InputButton((10, 400), "START", StartRocket, positioning="physical", size=15)

rocket=Rocket(earth, thrust=GetThrust, mass=mp+me)
earth.run(rocket)
