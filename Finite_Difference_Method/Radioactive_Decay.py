# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 13:02:16 2022

@author: Suresh BASNET
"""
#====Radioactive Decay equation dN/dt = -N*Ld and its analytical solution is
#======= N = N0*exp(-t*Ld); where N0 = 1e5, Mean life time Tm = 4.4711e9

import numpy as np
import matplotlib.pyplot as plt

#=====================Physcial parameters
N0 = 1e5                # Initial concentration
Tm = 4.4711e9           # Mean life time 
Ld = 1/Tm               # Decay constant
tmin = 0                # Initial time or miniumum value of Decay time 
tmax = Tm               # Final time or maximum value of Decay time.
nt = 50000
dt = (tmax-tmin)/nt     # Time interval between two consecutive time points

#=========================For analytical solution
t = np.linspace(tmin,tmax,nt)
N_a = N0*np.exp(-t*Ld)

#==================For numerical solution using FDM
N_s=np.zeros(nt)        # Making array for numerical solution  (N_s) 
t_s=np.zeros(nt)        # Making array for time t_s

#========================Initial conditions
N_s[0] = N0
t_s[0] = tmin
#========================Making for loop
for i in range (1,nt):
    N_s[i] = N_s[i-1]*(1-Ld*dt)
    t_s[i] = t_s[i-1]+dt

#===============================Plot the graphs for N_s and N_a    
plt.figure(figsize = (8, 5)) 
  
plt.plot(t_s/1e9,N_s/N0,color='red',linestyle='-', linewidth = 2.0,
         label='Num. soln')

plt.plot(t/1e9,N_a/N0,color='blue',linestyle=':', linewidth = 2.0,
         label='Anal. soln')  

plt.rcParams.update({'font.family':'Times New Roman'})

plt.legend()

plt.legend(loc='upper right',prop = {'size': 12})

plt.xlabel('Time, $t / 10^{9}$ ( sec )', fontsize=16, color='red')

plt.ylabel('Radioactive concentration, $N / N_{0}$', fontsize=16,color='black')

plt.xlim(0,5)

plt.ylim(0.3,1.0)

plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

plt.title('Radioactive Decay Equation using FDM', fontsize=14, color='blue')

#=============Add minor ticks on the plot
plt.minorticks_on()

plt.tick_params(which='major', length=7)

plt.tick_params(which='minor', length=4)


plt.savefig('radioactivity.jpeg',dpi=300,bbox_inches='tight')

plt.show 
