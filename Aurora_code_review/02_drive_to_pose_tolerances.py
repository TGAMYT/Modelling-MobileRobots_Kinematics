"""Advanced: ``drive_to_pose`` on TWO_WHEEL — goal pose, position/angle tolerances, then static plot.

``drive_to_pose`` chains rotate-then-drive segments until (x, y) and θ match the target.
It is *not* available for Ackermann (use explicit arcs in your own code).
"""

from __future__ import annotations #This allows you to cite types before they are actually defined

import math #Allows you use math functions
import os #This allows you to interact with the operating ystem, so we can use it to create and save files.
from pathlib import Path #Makes it easier to work with files with directories stated

import matplotlib.pyplot as plt #This library gives us access to plots to help visualize motion
from amr.kinematics.integration import wrap_pi #Somewhere hidden in the library(Spoiler: integration.py) is the function wrap_pi so we are impoting it.

import AuroraMR as amr #Importing the AuroraMR library as amr so we can use already made functions

os.environ.setdefault("MPLBACKEND", "Agg") #This sets the default display for matplotlib to "Agg", which is a backend that doesn't show any pop-ups. Not necessary for this code but it is useful in robotics as hardware does not have display

here = Path(__file__).resolve().parent #This saves the current directory as 'here'


def main() -> None:
    #This ensures the file doesn't get executed if imported into another project
    pose = amr.pose(-5, 6, math.pi/36)  #predefining the pose of the bot (see line 27).
    s = amr.MotionSession.create( #This creates an instance of the robot that can be later used to plot/visualize motion  
        pose, #The pose function defines the position (x,y) and orientation (theta) 
        amr.KinematicsModel.TWO_WHEEL, #this configures the robot to the already programmed attributes
        dt=0.015, #This represents the time step, how many times the computer would go through the code
        unicycle=amr.TwoWheelParams(max_linear_speed=1.0, max_angular_speed=1.2), #Here you can edit the already defined parameters of the robot
    )
    goal = amr.pose(1.2, 0.8, math.radians(40)) #This definessssssss a pose (position and orientation) for the robot to be used as an end goal 
    s.drive_to_pose( 
        #this is a code that, unlike s.forward or s.turn_left, does not take a series of steps to get to a position rather just moves from where it is to where it should be 
        goal, #the pose
        linear_speed=0.55, #speed of linear motion
        angular_speed=0.9, #speed of anular motion(turning)
        position_tol=0.07, #This gives us the smallest distance that the robot would consider as a goal with respect to the target position (x, y)
        angle_tol=0.08, #This gives us the smallest angle that the robot would consider as a goal with respect to the target orientation
    )
    err_xy = math.hypot(s.pose.x - goal.x, s.pose.y - goal.y) #This calculates the error between the actual final position and the goal position (the hypot function calculates the straight line distance between 2 points)
    err_th = abs(wrap_pi(s.pose.theta - goal.theta)) #This calculates the error between the actual final orientation and the goal orientation (the wrap_pi function ensures that the angle error is between -pi and pi) and the abs function makes sure the answer is positive
    print("Goal:", goal) #This prints the goal pose
    print("Final:", s.pose) #This prints the final position of the robot after running the command
    print(f"Position error: {err_xy:.4f} m   angle error: {err_th:.4f} rad") #Then we have the error previously calculated

    fig, ax = plt.subplots(figsize=(8, 8)) #Here we create the interface for visualization. figsize determnines the width adn height of the plot in inches.
    amr.plot_motion(s, ax=ax, show=True) #This creates a plot which visualizes the final position of the robot and the path it took to get there.
    ax.scatter([goal.x, pose.x], [goal.y, pose.y], c="grey", s=70, zorder=10 , label="goal (x, y)") #Creates a mini scatter plot that maps the initial position and the goal position with a grey dot and made to be over the robot (zorder).
    ax.legend(loc="lower right") #Defines position of the legend
    out = here / "adv_drive_to_pose.png" #This defines the name of a file to be ssaved in the current directory (cited at line 20)
    fig.savefig(out, dpi=150) #This saves the visualized image to the just created file with a resolution of 150 dots per inch (dpi)
    print("Wrote", out) #Prints "wrote" and the file location of the image


if __name__ == "__main__":
    #Here we call the main function and it executes all the code above.
    main()
