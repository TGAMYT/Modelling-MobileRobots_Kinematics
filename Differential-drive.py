import math
import AuroraMR as amr
import matplotlib.pyplot as plt

p=amr.pose(13,248,2*math.pi/5)
drive = amr.MotionSession.create(
    p,
    amr.KinematicsModel.DIFFERENTIAL,
    dt=0.2,
    differential=amr.DifferentialParams(track_width=0.4, max_wheel_speed=2.0),
)
#drive.forward(8,8.0)
drive.differential_drive_wheels(2,50,10)
drive.backward(5,2)

fig,ax=plt.subplots(figsize=(8,8))
amr.plot_motion(drive, ax=ax)
amr.play_motion(drive, interval_ms=30, log=True, repeat=False, log_every_n_frames=15, playback_speed=2)