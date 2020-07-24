from kaggle_environments import make
from kaggle_environments.envs.halite.helpers import *
import os

local_dir = os.getcwd()
env = make("halite", configuration={"episodeSteps": 400}, debug=True)
env.run([local_dir + "/tutorial_agent.py", "/random_agent.py", "random", "random"])
g
f = open('/home/databox/Pictures/board.html', 'w')
f.write(env.render(mode="html", width=800, height=600))
f.close()
