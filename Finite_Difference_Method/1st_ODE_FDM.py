# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 17:54:34 2022

@author: Suresh BASNET
"""

#=========Solving 1st differential equation using FDM
#====dy/dx=sin(ax), x=[0,10] and initial condition y(x=0)=0.5
#==== Its analytical solution is y(x)=-cos(ax)/a+ 1/2+1/a


import numpy as np
import matplotlib.pyplot as plt

#===================
a = 5        # Value of constant
x_max = 10   # Maximum value of x.
x_min = 0    # Minimum value of x.
nx = 500     # Number of grid points.

dx = (x_max-x_min)/nx  # DIstance between two consecutive grid points.
#x = np.linspace(x_min,x_max,nx) # Making array of x-cordinate.

x = np.zeros(nx) # Creating the array for the x cordiante. 
y = np.zeros(nx) # Creating the solution array for the numerical soln.

y_a=np.zeros(nx) # Creating the solution array for the analytical soln.

#================ Initial conditions
y[0]=1/2
x[0]=0
y_a[0]=1/2
#======================FDM
for i in range (1,nx):
    y[i] = y[i-1]+dx*np.sin(a*x[i-1])
    x[i] = x[i-1] + dx
    y_a[i] = -np.cos(a*x[i])/a + 1/2+1/a
    
    
plt.figure(figsize = (8, 5))    
plt.plot(x,y,color='red',linestyle='-.', linewidth = 2.0,
         label='Num. soln')
plt.plot(x,y_a,color='blue',linestyle=':', linewidth = 2.0,
         label='Anal. soln')

plt.rcParams.update({'font.family':'Times New Roman'})
plt.legend()
plt.legend(loc='upper left',prop = {'size': 12})

plt.xlabel('$x$-value', fontsize=16,color='red')
plt.ylabel('$y$-value', fontsize=16,color='black')
plt.xlim(0,10)
plt.ylim(0.5,1.0)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.title('FDM for 1st ODE', fontsize=14, color='blue')
#=============Add minor ticks on the plot
plt.minorticks_on()
plt.tick_params(which='major', length=6)
plt.tick_params(which='minor', length=3)


plt.savefig('1st_ODE.jpeg',dpi=300,bbox_inches='tight')
plt.show    

