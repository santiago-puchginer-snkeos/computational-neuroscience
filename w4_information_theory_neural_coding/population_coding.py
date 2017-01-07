from __future__ import print_function, division
import numpy as np
import pickle

if __name__ == '__main__':
    # Load pickle
    with open('pop_coding.pickle', 'rb') as f:
        data = pickle.load(f)

    # Basis vectors (c)
    c1 = data['c1']
    c2 = data['c2']
    c3 = data['c3']
    c4 = data['c4']

    # Responses
    r1 = data['r1']
    r2 = data['r2']
    r3 = data['r3']
    r4 = data['r4']

    r1_coef = np.mean(r1) / r1.max() if r1.max() > 0 else 0
    r2_coef = np.mean(r2) / r2.max() if r2.max() > 0 else 0
    r3_coef = np.mean(r3) / r3.max() if r3.max() > 0 else 0
    r4_coef = np.mean(r4) / r4.max() if r4.max() > 0 else 0

    # Stimulus direction
    v = r1_coef * c1 + r2_coef * c2 + r3_coef * c3 + r4_coef * c4
    v_dir = (np.arctan(v[1] / v[0]) / (2 * np.pi)) * 360
    print('Stimulus vector: {}, {}'.format(v[0], v[1]))
    print('Stimulus angle: {}'.format(v_dir))

    print('Done')

