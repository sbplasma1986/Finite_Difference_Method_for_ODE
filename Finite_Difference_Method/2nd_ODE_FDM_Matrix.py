# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 11:42:47 2022

@author: Suresh BASNET
"""

# Solve the ordinary differential equation (Poisson's equation) using FDM
# d^2\phi/dx^2=-rho; phi(x_min) = 0 and phi(x_max) = 0,rh0=n0*q/epsilon_not

import numpy as np
import matplotlib.pyplot as plt


x_min = -10
x_max = 10
nx = 500
x = np.linspace(x_min,x_max,nx)

n0 = 1e16   # Plasma density
epsilon_not = 8.8542e-12
q = 1.6e-19
rho = n0*q/epsilon_not
dx = (x_max-x_min)/nx
#==================Making left-hand side matrix
ML=np.zeros((nx,nx))
ML[0,0]=1                           # Element of 1st row 1st column.
ML[nx-1,nx-1]=1

for k in range(1,nx-1):
    ML[k,k-1]=1
    ML[k,k]=-2
    ML[k,k+1]=1   
#print(ML)
#===================Making right-hand side matrix    
MR=np.zeros(nx)
MR[0:nx]=-rho*dx**2
#=================Boundary values
MR[-1]=0
MR[0]=0;

#print(MR)

#====================Solving the linear equations
phi = np.linalg.solve(ML,MR)

#=====================Calculate the maximum value of phi to normalize.
phi0 = max(phi)

plt.rcParams.update({'font.family':'Times New Roman'})

# Plot the graph
plt.plot(x, phi/phi0, color='r', linestyle='-.', linewidth = 2.0)    

plt.ylabel('Potential, $\phi / \phi_{0}$',fontsize=16,color = "black") 

plt.xlabel('Distance, $\it{x}$ ( m )',fontsize=16,color = "blue")           
plt.title('Solving ODE Using FDM Inverse Matrix Technique',
          fontsize=14, color = "red")

plt.xlim(-10, 10)           # Control the x max and min values in the plot
plt.ylim(0,1.0)             # Control the y max and min values in the plot
plt.xticks(fontsize=14)     # Fontsize of xticks
plt.yticks(fontsize=14) 

plt.minorticks_on()
plt.tick_params(which='major', length=6)
plt.tick_params(which='minor', length=3)
plt.savefig('Graph.jpeg', dpi=300,bbox_inches='tight') 
plt.show



