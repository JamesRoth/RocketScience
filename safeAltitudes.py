#James Roth
#3/14/18
#safeAltitudes.py - safe velocity for low earth orbits

from ggrocket import Rocket, Planet

earth=Planet(viewscale=0.00005)
rocket=Rocket(earth, altitude=200000, velocity=7900, timezoom=0.1)
earth.run(rocket)
