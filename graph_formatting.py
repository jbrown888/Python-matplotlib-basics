# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 11:07:00 2021

@author: Joanna Brown, Github : jbrown888

Basics of Matplotlib Graph formatting settings

By no means is this a definitive guide, or the best way of doing things, and it's definitely not complete. But hopefully it gives some basic ideas for formatting, and serves as a starting point for plotting.

Extra tips: stackoverflow and the matplotlib and numpy websites are your friends!
90% of the time your question has already been asked by somebody else on stack overflow, and the documentation for the python websites is actually quite good.

https://matplotlib.org/
https://numpy.org/

"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm #colormap library
from scipy.stats import norm

#%% axes  - the OOP way to make plots

fig, ax = plt.subplots() # creates a figure (fig) and axes (ax) object. 
"""
By creating objects, you can access and alter the properties more easily than if you use plt.plot(...), but it is a little difficult to wrap your head around at first. 
It saves massive amounts of time, as you can create default settings for these objects, and apply functions to them.
You can do this because Python is an object oriented programming language, and has objects and classes - this is the fun bit! You can even create your own classes.


Aside: confusingly, the axes object is not actually the axes of the graph - it's kind of a canvas on which you add stuff like plot lines and the x and y axis.
"""


def standard_axes_settings(ax):
        """
        A function to apply standard settings to a graph for label sizes, gridlines, frame etc.
        
        input argument ax is an axes object of matplotlib
        
        """
        ax.set_frame_on # adds frame around plot
        ax.grid(b=True, which = 'major', axis = 'both', c = 'grey', ls='--', lw = 1) #adds major grid lines
        # ax.grid(b=True, which='minor', axis='both', c='darkgrey', ls = '--', linewidth =2) # adds minor grid lines
        ax.tick_params(axis = 'both', which = 'major', direction ='in', labelsize = 22) # adds major ticks (the little marks on axes like on a ruler) 
        ax.tick_params(axis ='both', which = 'minor', direction ='in') # adds minor ticks
        ax.xaxis.label.set_size(28) # sets size of axis labels (the numbers on the axis)
        ax.yaxis.label.set_size(28)
        # ax.minorticks_on() # turns on minor ticks
        ax.yaxis.get_offset_text().set_fontsize(20) # sets fontsize of the axis label i.e. the "Time [s]" bit
        ax.xaxis.get_offset_text().set_fontsize(20)
        ax.ticklabel_format(axis = 'x', style = 'sci', scilimits = (-3,3), useOffset = True) # formats the numbering of the axes if you have really big or really small numbers - if >1e3 or <1e-3, will use scientific notation automatically
        ax.ticklabel_format(axis = 'y', style = 'sci', scilimits = (-3,3), useOffset=True)

# these settings can be copy and pasted out of the function and applied individually to each graph - but putting it in a function like this saves you having to rewrite it all everytime you make a new graph

standard_axes_settings(ax) # applies formatting to the graph (axes object)

red = 'indianred' # a nice red
blue = 'royalblue' # a nice blue



plot_arguments = {'marker':'o', #marker style
                  'lw':3, #line width
                  'ms':10, #marker size
                  'ls':'--', #line style
                  'c': 'k', #line color
                  'mew':2, #marker edge width
                  'mec': 'red', #marker edge color
                  'mfc':'None',#marker face color
                  } # this is a dictionary of arguments to set the style of the line/points you draw

plot_arguments_y = {'marker':'x', #marker style
                  'lw':3, #line width
                  'ms':7, #marker size
                  'ls':':', #line style - none gives no line
                  'c': 'darkslategray', #line color
                  'mew':2, #marker edge width
                  'mec': 'blue', #marker edge color
                  'mfc':'blue',#marker face color
                  } # same thing but for the y data, to distinguish from the x data

#Create some data
def example_function(t):
    return (t-6.5)**2

t = np.linspace(0, 4*np.pi, 25) # generates evenly distributed points
y = 30*np.sin(t)
x = example_function(t)

ax.plot(t, x, **plot_arguments, label = 'x data') # plot x data
ax.plot(t, y, **plot_arguments_y, label = 'y data') # plot y data

"""
the **plot_arguments adds all the items in the dictionary plot_arguments into the plot as if you had written them directly as ax.plot(t, x, lw = 3, marker = 'o',... etc). Just makes the code a little bit neater
"""

# Set x and y axis labels
ax.set_xlabel('Time [s]')
ax.set_ylabel('Dependent Variable')



### LEGENDS ###
"""
There are a few ways of creating legends. Uncomment one to use it. Notice both produce the same result!
"""


# Method A
"""
Since I labelled my data when I plotted it (label = 'x data' etc in the ax.plot() line), I can simply call legend directly and Python will automatically create the legend with the correct key. Nice! 
"""
leg = ax.legend(fontsize = 26, loc='best', markerfirst = True, frameon = True) # creates a legend for the axes object ax that I created earlier


# Method B
"""
If displaying lots of data on one plot, it may be more useful to customise the legend and create your own entries
"""

# handles = [mpl.lines.Line2D([], [], **plot_arguments), mpl.lines.Line2D([], [], **plot_arguments_y)] # creates the symbols for the legend
# labels = ['x data', 'y data'] #labels for legend
# leg = ax.legend(handles, labels, fontsize = 26, loc='best', markerfirst = True, frameon = True) # creates custom legend



#general formatting of legend for either method
leg.get_frame().set_edgecolor('k')
leg.get_frame().set_facecolor('w')

plt.show()


#%% COLOR RANGE EXAMPLE
fig, ax = plt.subplots()
standard_axes_settings(ax)

t = np.linspace(-5, 5, 100)
mean = 0.0
Z = np.linspace(0.5, 5, 6) # values for standard deviation (sigma)

cs = [cm.magma(i/len(Z), 1) for i in range(len(Z))] # creates list of colours according to the colour map magma, evenly distributed over the range of Z. Colour maps available at https://matplotlib.org/stable/tutorials/colors/colormaps.html

# here for the labels I use f-string formatting. This was new with Python 3 and I much prefer it the Python 2 method. Google  

for i, stddev in enumerate(Z): # iterate over the different values of standard deviation
    x = norm.pdf(t, loc = mean, scale = stddev)
    ax.plot(t, x, marker = 'None', ls = '-', lw = 2.5, color = cs[i], label = fr'$\sigma$ = {stddev:.1f}')
    
    
ax.set_xlabel(r'Distance [$\mu$m]')
ax.set_ylabel('Intensity')

leg = ax.legend(fontsize = 26, loc='best', markerfirst = True, frameon = True) # creates a legend for the axes object ax that I created earlier

leg.get_frame().set_edgecolor('k')
leg.get_frame().set_facecolor('w')


#%% 4 plots together
t = np.linspace(-5, 5, 100)
x = np.cos(t)
y = np.sin(t)
z = t**3
v = t*t
q = 3*t**4 -t**3 +2

fig, AXES = plt.subplots(1, 2, sharex = False, sharey = False, num =3) # create 2 subplots - allows shared axes like this
fig.frameon = False
[AXL, AXR] = AXES # left and right subplot
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(223)
ax3 = fig.add_subplot(222)
ax4 = fig.add_subplot(224)
axes = [ax1, ax2, ax3, ax4]
fig.subplots_adjust(wspace =0.3, hspace=0.3) # adjust spacing

for AX in AXES:
    AX.spines['top'].set_color('None') # remove visible frame from the the left and right underlying subplots
    AX.spines['bottom'].set_color('None')
    AX.spines['left'].set_color('None')
    AX.spines['right'].set_color('None')
    AX.set_facecolor('None')
    # AX.set_xticklabels([])
    # AX.set_yticklabels([])
    AX.tick_params(labelcolor='None', top='off', bottom='off', left='off', right='off')
    
for ax in axes: #format the 4 axe
    standard_axes_settings(ax)

axes[2].plot(t, x, '-', label='x(t)',linestyle= '-', color = red)
axes[2].plot(t, y, '-', label='y(t)',linestyle= '-', color = blue)
# axes[2].set_xlabel('t [s]')
axes[2].set_ylabel('Position [m]')

axes[3].plot(t, z, '-', label='z(t)', linestyle= '-', color = 'purple')
axes[3].set_xlabel('t [s]')
axes[3].set_ylabel(r'$z$ [${ms}^{-1}$]')

axes[1].plot(t, v, '-', label=r'$v$(t)',linestyle= '-', color = 'orange')
axes[1].set_xlabel('t [s]')
axes[1].set_ylabel(r'$v$ [${ms}^{-1}$]')

axes[0].plot(t, q, '-', label=r'$v$(t)',linestyle= '-', color = 'k')
# axes[0].set_xlabel('t [s]')
axes[0].set_ylabel(r'$q$ [${s}^{-1}$]')

handles = [mpl.lines.Line2D([0], [0], ls = '-', color = red), mpl.lines.Line2D([0], [0], ls = '-', color = blue)]
leg1 = axes[2].legend(handles = handles, labels = ['x', 'y'], fontsize = 20, loc='best', markerfirst = False, frameon = True)
leg1.get_frame().set_edgecolor('k')
leg1.get_frame().set_facecolor('w')

#add annotating text
bbox_props = dict(boxstyle = "square,pad=0.2", fc = "w", ec ="k", lw = 1)
axes[0].text(-1, 1.25e3, 'Some useful text', fontsize = 24, bbox = bbox_props)

plt.show()

#%% f-string and latex

#These expressions won't work printing in e.g. spyder console, but will work in jupyter notebooks or in matplotlib.
#Using LaTeX with strings:
print(r'$\theta$')

theta = 35.4282711
#Using LaTeX and f-string formatting
print(fr'$\theta$ = {theta:.2f}')

#Using f-string and latex together but you need {} in Latex:
print(fr'$\Delta_{{\mu}}$ = {np.pi:.2f}')
