# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 17:52:44 2020

illustrating the signal to noise ratio, and when averaging does or does not work.
@author: Katri
"""
import matplotlib.pyplot as plt
import numpy as np



# let us imagine that we have a signal at a frequency of 1 Hz, a phase of pi and an amplitude of 1
time = np.arange(0.,1,0.001); time[0:5]
freq = 1  #frequency
phi  = np.pi  #phase
a    = 1.  #amplitude

def f(t):
     y=a*np.sin(2*np.pi*freq*t+phi)
     return y
y_ori = []
for value in time:
    y_ori.append(f(value))    

#%% plot
plt.plot(time, y_ori, color = 'blue',linewidth=2, linestyle='-')  
plt.title("Waveform of a certain signal in the brain")  
plt.xlabel("X")  
plt.ylabel("Y")  
plt.show()  
#%% let us imagine we have this signal at some trials, but not in others such as:
time = np.arange(0.,10,0.001); time[0:5]
freq = 2  #frequency
phi  = np.pi  #phase
a    = 1.  #amplitude

def f(t):
     y=a*np.sin(2*np.pi*freq*t+phi)
     return y
y_ori = []
event = [2,4,6] ## say we give at these moment a certain stimuli
for value in time:
    if event[0]<value<event[0]+1 or event[1]<value<event[1]+1 or event[2]<value<event[2]+1:
        y_ori.append(f(value))   
    else:
        y_ori.append(0)

for markers in np.arange(0,10,1):
    plt.axvline(markers, linewidth=0.25, linestyle ='--')
plt.plot(time, y_ori, color = 'blue',linewidth=0.5, linestyle='-')  
plt.title("Waveform of the signal during all our trials")  
plt.xlabel("X")  
plt.ylabel("Y")  
plt.show()  

#%% now let us add some noise to all this
#1) random noise
random_noise = np.random.rand(len(time)); print(random_noise[0:5])
# we add this to our plot:
y_ori_rand = y_ori + random_noise ## note: this is additive noise; it has nothing to do with our measurement
plt.plot(time, y_ori_rand, color = 'blue',linewidth=0.5, linestyle='-')  
plt.title("Signal + random noise")  
plt.xlabel("X")  
plt.ylabel("Y")  
plt.show() 

#%%
#2) you can also add systematic noise: 
freq = 1.5
a = 2.4 # you can play with the amplitude and see how this affects the signal
phi = np.pi/4
systematic_noise = []
for t in time:
    systematic_noise.append(a*np.sin(2*np.pi*freq*t+phi))
y_ori_rand_sys = y_ori + random_noise + systematic_noise
plt.plot(time, y_ori_rand_sys, color = 'blue',linewidth=0.5, linestyle='-')  
plt.title("Signal + random noise + systematic noise")  
plt.xlabel("X")  
plt.ylabel("Y")  
plt.show()     

#%% you can also have noise that is linked to your measure:
multiplicative_noise = np.random.randn(len(time))*y_ori; multiplicative_noise[0:5]
y_ori_rand_sys_mul = y_ori + random_noise + systematic_noise + multiplicative_noise
plt.plot(time, y_ori_rand_sys_mul, color = 'blue',linewidth=0.5, linestyle='-')  
plt.title("Signal + random noise + systematic noise + multiplicative")  
plt.xlabel("X")  
plt.ylabel("Y")  
plt.show()   
#%% only multiplicative
y_ori_mul = y_ori+multiplicative_noise
plt.plot(time, y_ori_mul, color = 'blue',linewidth=0.5, linestyle='-')  
plt.title("Signal + multiplicative noise")  
plt.xlabel("X")  
plt.ylabel("Y")  
plt.show()   


#%% would averaging work here to recover our signal?
import pandas
data = pandas.DataFrame(y_ori_rand_sys, index = np.repeat(range(0,10),1000),columns=['y']);data [0:10] #index represents the trial number
time_series = np.zeros((int(len(time)/10),len(event))); time_series
i = 0
for n in event:
    time_series[:,i] = data['y'][data.index.all==n]
    i +=1
print('The first column indicates all y values at time {0}, the second at {1} and the third at {2}:'.format(event[0],event[1],event[2]))
print(time_series[0:5,:])

# now we can take the mean of each time point by 'squeezing' these three columns
average = np.mean(time_series, axis = 1); average
print(len(average))
#let us plot this and have a look at it:
plt.plot(np.arange(0,len(average)), average, color = 'blue',linewidth=0.5, linestyle='-')  
plt.title("Average waveform")  
plt.xlabel("X")  
plt.ylabel("Y")  
plt.show()   


