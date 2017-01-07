from __future__ import print_function, division
import numpy as np
import pickle
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Load pickle
    with open('tuning.pickle', 'rb') as f:
        data = pickle.load(f)

    T = 10
    stim = data['stim']
    delta_t = T / stim.shape[0]

    # Plot tuning curve for each neuron
    neurons = ('neuron1', 'neuron2', 'neuron3', 'neuron4')
    colors = ('red', 'blue', 'magenta', 'green')
    plt.figure(dpi=200, facecolor='white')
    for neuron_name, color in zip(neurons, colors):
        rate = data[neuron_name]
        mean_response = np.mean(rate, axis=0)
        variance_response = np.var(rate, axis=0)
        plt.plot(stim, mean_response, label=neuron_name, color=color)
        plt.plot(stim, variance_response, linestyle='--', color=color, label='{} variance'.format(neuron_name))
    plt.xlabel('Stimulus')
    plt.ylabel('Mean response')
    plt.title('Tuning curve')
    plt.legend()
    plt.show()
    print('Done')
