# -*- coding: utf-8 -*-
"""
Created on Fri May 15 10:29:51 2020

simple exercise PCA with simply two electrodes

@author: Katri
"""
#import functions
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os
import mne
import pandas as pd
import re
import seaborn as sns
#%% pick up two electrodes (for simplicity)
sample_data_folder = mne.datasets.sample.data_path()
sample_data_raw_file = os.path.join(sample_data_folder, 'MEG', 'sample','sample_audvis_filt-0-40_raw.fif')
raw = mne.io.read_raw_fif(sample_data_raw_file)
orig_raw = raw.copy()
channels = orig_raw.info['ch_names']
# pick a channel:
electrode1 = channels [-8]
electrode2 = channels [-2]
samples    = 50 ## number of time points we will have a look at (for simplicity)

# visualization of both channels time course:
plt.figure(3)
plt.subplot(121)
plt.plot(orig_raw[electrode1][1][0:samples],orig_raw[electrode1][0][0][0:samples],linewidth=0.8,color='r')
plt.ylabel('Voltage')
plt.xlabel('time in ms')
plt.title('example of a (raw) EEG signal '+electrode1)
plt.subplot(122)
plt.plot(orig_raw[electrode2][1][0:samples],orig_raw[electrode2][0][0][0:samples],linewidth=0.8)
plt.ylabel('Voltage')
plt.xlabel('time in ms')
plt.title('example of a (raw) EEG signal '+electrode2)
#%% we can then place these two electrodes on a third dimensional space:
fig = plt.figure(2)
ax = fig.add_subplot(111, projection='3d')
ax.scatter(orig_raw[electrode1][0][0][0:samples], orig_raw[electrode2][0][0][0:samples], np.arange(0,samples), c='b', marker='o')
ax.set_xlabel('EEG data for electrode {}'.format(electrode1))
ax.set_ylabel('EEG data for electrode {}'.format(electrode2))
ax.set_zlabel('timepoint')
plt.show()
#%%
# or placing both electrodes one against the other:
plt.figure(4)
plt.plot(orig_raw[electrode1][0][0],orig_raw[electrode2][0][0],'+')
plt.xlabel(electrode1)
plt.ylabel(electrode2)
#%% How do we compute PCA? 
#Step 1: compute a covariance matrix
## eg. with only two electrodes:
samples = len(orig_raw[electrode1][0][0])
data_electrodes = np.column_stack((orig_raw[electrode1][0][0][0:samples], orig_raw[electrode2][0][0][0:samples]));pd.DataFrame(data_electrodes,columns=[electrode1,electrode2])
mean_values     = data_electrodes.mean(axis=0);mean_values
covariance      = np.dot(1/(samples-1),np.dot((data_electrodes-mean_values).T,(data_electrodes-mean_values)));pd.DataFrame(covariance,columns=[electrode1,electrode2])
## you can do this for all electrodes at all timepoints:
EEG  = [x for x in channels if re.search('EEG', x)];EEG
data_electrodes = pd.DataFrame(orig_raw[EEG][0][:,0:samples]);data_electrodes
mean_values     = np.tile((data_electrodes.mean(axis=1)),(samples,1)).T;pd.DataFrame(mean_values)
covariance      = np.dot(1/(samples-1),np.dot((data_electrodes-mean_values),(data_electrodes-mean_values).T));pd.DataFrame(covariance)

#%% we can plot this on a heatmap
heatmap = sns.heatmap(covariance)

#%% Step 2: eigendecomposition
E = np.linalg.eig(covariance)
print('Eigenvectors:\n{}'.format(E[0]))
print('Eigenvalues :\n{}'.format(pd.DataFrame(E[1])))
#%% in percentage we get for each component:
PCA      = pd.DataFrame(E[1])
PCA_perc = PCA/PCA.sum(axis=1)*100;PCA_perc
