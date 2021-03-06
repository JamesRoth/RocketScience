#James Roth
#3/15/18
#rocket3.py - controlling a rocket

from ggrocket import Rocket, Planet
from math import radians, sqrt, log
from ggmath import InputButton, Timer, Slider

earth = Planet(viewscale=0.0001)  # no gravity to simplify things - not anymore!

RocketStarted = False
StartTime = None    # to keep track of when burn started
BurnTime = 0        # keep track of how much time the burn has lasted

# Falcon F9R specifications
me = 25600          # Empty mass
mp =  395700        # Propellent mass
F1D = 716000        # Single engine thrust (Newtons)
N1D = 9             # Number of rocket engines

Ftotal = F1D * N1D  # Total thrust (Newtons)
tburn = 180         # Burn time (seconds)

# Predict the final velocity using Tsiolkovsky's Rocket Equation
vmaxre = Ftotal*tburn/mp*log((me+mp)/me)
print("Predicted final velocity (Rocket Equation), vmax: ", vmaxre, " m/s")


# Create a function for determining the rocket thrust
def GetThrust():
    global BurnTime
    global RocketStarted
    if RocketStarted:
        # get the burn time: seconds since start
        BurnTime = rocket.shiptime - StartTime
        # is it time to stop the rocket?
        if BurnTime >= tburn:
            # stop the rocket and report zero thrust
            RocketStarted = False
            return 0
        else:
            # still burning, report full thrust
            return Ftotal
    else:
        return 0

# Function for starting the rocket thrust (called by the START "button")
def StartRocket():
    global RocketStarted


    global StartTime
    if not RocketStarted:
        RocketStarted = True
        # Note the starting time
        StartTime = rocket.shiptime

# Function for calculating the total rocket mass, based on burn time and total
# propellent mass.
def GetMass():
    global RocketStarted
    if RocketStarted:
        # calculate empty mass plus a fraction of the propellent mass based on time
        return me + mp*(tburn-BurnTime)/tburn
    else:
        # not started: just return the full pre-launch rocket mass
        return me + mp


# Create a button for starting the simulation
# Physical positioning at 10,400 pixels, calls the StartRocket function
start = InputButton((10,400), "START", StartRocket, positioning="physical", size=15)

tz = Slider((10,450), 0, 5, 0, positioning="physical", leftkey="a", rightkey="d")

#Create and "run" the rocket
rocket = Rocket(earth, thrust=GetThrust, mass=GetMass, timezoom=tz)
earth.run(rocket)
