# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 12:11:21 2020

Going through chaper 11 cohen's book: 'The discrete fourier Transform, the FFT, and the Convolution Theorem
@author: Katri
"""
#import functions
import numpy as np
import matplotlib.pyplot as plt
#%% 11.1 making waves
def wave_making(t): #with a being the amplitude, f the frequency, t the time point and theta the phase
    return a*np.sin(2*np.pi*f*t+theta)

# eg. a wave of an amplitude of 2, a frequency of 10 and theta of 0
def wave (a, f , theta, sf, duration): 
    time  = np.arange(0,duration,1/sf)
    y = []
    for t in time:
        y.append(wave_making(t))
    return time,y
a = 2
f = 10
theta    = 0
duration = 1
sf       = 10
plt.figure(1)
y = wave (a, f , theta, sf, duration)
plt.plot(y[0],y[1])
plt.title('simple waveform')
# adding different sinewaves gives something more complicated than the initial sinewave
time = np.arange(0,20,1/sf)
complex_wave = []
duration = 1
sf = 25
# sine wave 1:
a = 3;f=2;theta=np.pi
sine1 = wave (a, f , theta, sf, duration)
# sine wave 2:
a = 6;f=10;theta=0
sine2 = wave (a, f , theta, sf, duration)
# sine wave 3:
a = 1;f=1;theta=np.pi
sine3 = wave (a, f , theta, sf, duration)
# sine wave 4:
a = 4;f=6;theta=2*np.pi
sine4 = wave (a, f , theta, sf, duration)
# we sum all these waves:
complex_wave = np.sum(np.array((sine1[1], sine2[1],sine3[1],sine4[1])),0)
plt.figure(2)
plt.plot(sine1[0],complex_wave)
plt.title('complex waveform')
#%% 11.2 Finding Waves in EEG data with the FT
# with EEG data we do not have the constituent waves making up our signal
## example of an EEG dataset:
import os
import mne
sample_data_folder = mne.datasets.sample.data_path()
sample_data_raw_file = os.path.join(sample_data_folder, 'MEG', 'sample',
                                    'sample_audvis_filt-0-40_raw.fif')
raw = mne.io.read_raw_fif(sample_data_raw_file)
orig_raw = raw.copy()
plt.figure(3)
plt.plot(orig_raw['EEG 031'][1],orig_raw['EEG 031'][0][0],linewidth=0.2)
plt.ylabel('Voltage')
plt.xlabel('time in ms')
plt.title('example of a (raw) EEG signal')

#%% 11.3 The discrete Time Fourier Transform
## the idea behind the discrete fourier transform is: create a sine wave and compute the dot product between
## that sinewave with sinewaves for each at different frequencies.
# For instance:
N = 10
data = np.random.randn(N)
fourier = np.zeros(data.shape)
time    = np.arange(0,N)/N
# fourier transform
for fj in range(1,N): 
    # create a complex sinewave
    sine_wave = np.exp(-1j*2*np.pi*(fj-1)*time)
    # compute dot product between sine wave and data
    print('result of dot product for {}: {}'.format(fj,np.dot(sine_wave,data)))
    fourier[fj] = np.dot(sine_wave,data)

# in our example with the complex waveform:
data = complex_wave
N    = len(data)
fourier = np.zeros(data.shape)
time    = np.arange(0,N)/N
# fourier transform
for fj in np.arange(0,N): 
    # create a complex sinewave
    sine_wave = np.exp(-1j*2*np.pi*(fj-1)*time)
    # compute dot product between sine wave and data
    print('result of dot product for {}: {}'.format(fj,np.dot(sine_wave,data)))
    fourier[fj] = np.dot(sine_wave,data)

#%%11.4+5 visualizing the results of fourier transform
plt.bar(np.linspace(0,N/2,N),abs(fourier))
