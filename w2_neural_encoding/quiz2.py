"""
Created on Wed Apr 22 15:15:16 2015

@author: rkp

Quiz 2 code.
"""

from __future__ import division

import pickle

import matplotlib.pyplot as plt
import numpy as np

from compute_sta import compute_sta

FILENAME = 'c1p8.pickle'

with open(FILENAME, 'rb') as f:
    data = pickle.load(f)

stim = data['stim']
rho = data['rho']

# Fill in these values
sampling_period = 2  # in ms
num_timesteps = 150

sta = compute_sta(stim, rho, num_timesteps)

time = (np.arange(-num_timesteps, 0) + 1) * sampling_period

plt.subplot(2, 1, 1)
plt.plot(time, sta)
plt.xlabel('Time (ms)')
plt.ylabel('Stimulus')
plt.title('Spike-Triggered Average')

plt.subplot(2, 1, 2)
N_samples_represent = 2000
stim_selection = stim[:N_samples_represent]
stim_selection_norm = stim_selection / stim_selection.max()
rho_selection = rho[:N_samples_represent]
time_selection = np.arange(0, N_samples_represent) * (sampling_period / 1000.0)
plt.plot(time_selection, stim_selection_norm)
plt.scatter(time_selection, rho_selection, color='red')
plt.xlabel('Time (s)')
plt.title('Normalized stimulus and spike time-series for the first {} samples'.format(N_samples_represent))
plt.show()
