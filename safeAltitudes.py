#James Roth
#3/14/18
#safeAltitudes.py - safe velocity for low earth orbits

from ggrocket import Rocket, Planet

earth=Planet()
rocket=Rocket(earth)
earth.run(rocket)
