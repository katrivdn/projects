# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 14:33:06 2020

@author: Katri
"""

import matplotlib.pyplot as plt
import numpy as np

time = np.arange(0.,2,0.001); time[0:5]
a    = 1.  #amplitude
phi  = np.pi  #phase
freq = 2 #frequency

def f(t):
     y=a*np.sin(2*np.pi*freq*t+phi)
     return y
y_ori = []
for value in time:
    y_ori.append(f(value))    

plt.plot(time, y_ori, color = 'blue',linewidth=2, linestyle='-')  
plt.title("math.sin()")  
plt.xlabel("X")  
plt.ylabel("Y")  
plt.show()  

#%%
#now let us how many times we should sample to be able to reconstruct the signal
jet= plt.get_cmap('jet')
sampling = np.arange(2,50,5)[::-1]; sampling
colors    = iter(jet(np.linspace(0,1.5,len(sampling))))

for s in sampling:
    sample = np.linspace(start=0, stop=2, num=s*2)
    y = []
    for value in sample:
        y.append(f(value))
    plt.plot(sample, y, color = next(colors),linewidth=2, linestyle='-')
    plt.plot(time, y_ori, color = 'blue',linewidth=2, linestyle='--')  
    plt.title('Sampling frequency: {0} Hz'.format(s))
    plt.pause(2)
    plt.close()


#%%
## just for fun: now make different curves of different frequencies, amplitude and phase and guess what changed:
freq_list = np.array([0.5,2,10,20]) #frequency
colors    = iter(jet(np.linspace(0,1.5,10)))

def f(t,a,phi,freq):
     y=a*np.sin(2*np.pi*freq*t+phi)
     return y
# 1) change frequency each time
for frequency in freq_list:
    y = []
    for value in time:
        y.append(f(value,a,phi,frequency))    
    plt.plot(time, y, color = next(colors),linewidth=2, linestyle='-')
    
plt.title("math.sin()")  
plt.xlabel("X")  
plt.ylabel("Y")  
plt.show()  
#%%
#2) change amplitude
colors    = iter(jet(np.linspace(0,1.5,10)))
a_list    = np.arange(1,5,0.5) #amplitude
for amplitude in a_list:
    y = []
    for value in time:
        y.append(f(value,amplitude,phi,freq))    
    plt.plot(time, y, color = next(colors),linewidth=2, linestyle='-')
    
plt.title("math.sin()")  
plt.xlabel("X")  
plt.ylabel("Y")  
plt.show()  
#%%
#3) phase
colors    = iter(jet(np.linspace(0,1.5,10)))
phi_list  = np.arange(0,1+2*np.pi,np.pi/2)  #phase
for phi in phi_list:
    y = []
    for value in time:
        y.append(f(value,a,phi,freq))    
    plt.plot(time, y, color = next(colors),linewidth=2, linestyle='-')
    
plt.title(phi_list)  
plt.xlabel("X")  
plt.ylabel("Y")  
plt.show() 
