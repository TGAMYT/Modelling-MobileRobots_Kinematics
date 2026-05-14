#This is a well documented code showing a robot moving on a 2d interface using ___ configuration.
import math #this makes us able to use math functions 
import AuroraMR as bot #This is the library that helps us use the mobile robot's functions.
import os #This is used to save the image of the motion that we are going to plot using matplotlib



p=bot.pose(5,1,0) # So this is the bot's pose the x position, y position and heading ie angle of orientation.
q=bot.Pose(x=4, y=25, theta= math.pi/18) #this is the class that stores the values from the function above


#Using Motion Session; this just gives a plot of the motion that is going to be undergone by the bot and saves the image sha 
movement = bot.MotionSession.create(bot.pose(0,0,0), bot.KinematicsModel.TWO_WHEEL, dt=0.2)

movement.forward(2.0, 0.8) #the amount of movement and the speed of movement is specified respectively
movement.turn_left(45*math.pi/180, 0.8) #The angle of movement and speed are specified respectively
movement.forward(.8,0.6)
movement.turn_right(90*math.pi/180, 0.8)
movement.forward(.8,0.6)

#print(f'This is the number of poses {movement.poses}')
#So this just does backend work and provides the numerical details of the motion

#Introducing figures and plotting using matplotlib now allows us to visualize it tho it is static, it is still valid

import matplotlib.pyplot as plt
#os.environ.setdefault("MPLBACKEND", "Agg") Not sure what this does yet I believe it just disables you to view anypop ups and makes everything run just in backend but future David will check that out
fig, ax = plt.subplots(figsize=(8, 8))
bot.plot_motion(movement, ax=ax, show = True)


#The next 2 files save your static image to a document in this directory
savefile = os.path.join(os.path.dirname(__file__), "motion_mecanum_demo.png") 
fig.savefig(savefile, dpi=150)
plt.show()

bot.play_motion(movement, interval_ms=30, repeat = True, log= True)