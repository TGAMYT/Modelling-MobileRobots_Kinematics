import AuroraMR as car
import math
import matplotlib.pyplot as plt
import os
p=car.pose(0,0,0)

session = car.MotionSession.create(car.pose(0,0,0), car.KinematicsModel.MECANUM, dt=0.2)
"""
session.strafe_right(14, 3)
#session.forward(7.0, 4.0)
session.turn_left(2*math.pi/12, 2)
session.forward(14.0, 4.0)
session.turn_left(2*math.pi/3, 2)
session.forward(3, 4)
session.turn_left(15*math.pi/180,3)
session.strafe_right(-2,4)
session.forward(4,4)
session.strafe_right(2,4)
session.turn_right(15*math.pi/180,3)
session.forward(4.0, 4.0)
session.turn_left(30*math.pi/180,3)
session.strafe_right(-10,4)
session._drive_to_pose_mecanum(p, 0.3, 0.7, 0.06, 0.06)
"""

session.strafe_right(14, 3)#Wierdly strafe by 14 does not give the same distance as forward by 14, not sure why but I will find out.
session.turn_left(math.pi/2, 2)
session.forward(14.0, 4.0)
fig, ax = plt.subplots(figsize=(8, 8))
#car.plot_motion(session, ax=ax, show=True) #Find out how this actually work
car.play_motion(session, interval_ms=40, log=True, repeat = False, log_every_n_frames=30, playback_speed=2)

savefile = os.path.join(os.path.dirname(__file__), "Aurora_Sign.png") 
fig.savefig(savefile, dpi=150)