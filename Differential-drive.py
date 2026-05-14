import math
import AuroraMR as amr
import matplotlib.pyplot as plt

p=amr.pose(13,248,2*math.pi/5)
drive = amr.MotionSession.create(
    amr.pose(0, 0, 0),
    amr.KinematicsModel.DIFFERENTIAL,
    dt=0.12,
    differential=amr.DifferentialParams(track_width=0.4, wheel_radius=0.1, max_wheel_speed=2.0),
)
drive.forward_wheels(8,8.0)
drive.differential_drive_wheels(0.3, 1.2, duration=1.5)
drive.backward(5,2)

fig,ax=plt.subplots(figsize=(8,8))
amr.plot_motion(drive, ax=ax)
amr.play_motion(drive, interval_ms=30, log=True, repeat=False, log_every_n_frames=15, playback_speed=2)