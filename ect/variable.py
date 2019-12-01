
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as aninmation
from IPython.display import HTML
from matplotlib import style
fig, ax = plt.subplots()
ax.set_xlim((0,2))
ax.set_ylim((-2,2))
ax.grid(True)
line, = ax.plot([],[],lw =2)
def init():
    line.set_data([],[])
    return (line,)
def animtat(t):
    x = np.linspace(0,2,1000)
    y = np.sin(2*np.pi*(x-0.01*t))
    line.set_data(x,y)
    return(line,)
ani = animation.FuncAnimation(fig,animate,init_func = init,frames = 100,interval= 30,blit=True)
HTML(ani.to_html5_video())