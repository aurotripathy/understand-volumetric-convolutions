# attempts to demistify volumentric convolutions
# where we have a 3D volume for the input and a 
# 3D vfolume for the output


import numpy as np
from pudb import set_trace

from fill_params import fill_weights, fill_bias, fill_input

N = 3 # number of feature maps in the input
I_R = 5 # number of rows (R) in the input (I)
I_C = 5 # number of cols (C) in the input (I)
pad = 1 # pad


M = 2 # number of feature maps in the output 
k_R = 3 # kernel size, Row
k_C = 3 # kernel sise, Col

S = 2 # stride

O_R = (I_R + 2 * pad) / 2 # size  of Row Output
O_C = (I_C + 2 * pad) / 2 # size  of Cow Output


# memory allocation...
inp = np.zeros((N, I_R + 2 * pad, I_C + 2 * pad))
out = np.zeros((M, O_R, O_C))
weights = np.zeros((M, N, k_R, k_C))
bias = np.zeros((M))
# ...and initialization
fill_input(inp)
fill_weights(weights)
fill_bias(bias)

# set_trace()

# The convolution 
for m in range(M):
        for ir in range(0, I_R + pad, S):
            for ic in range(0, I_C + pad, S):
                sum = 0
                for n in range(N):
                    interim_sum = 0
                    for kr in range(k_R):
                        for kc in range(k_C):
                            interim_sum += weights[m, n, kr, kc] * inp[n, ir + kr, ic + kc]
                    print 'intermediate sum {}'.format(interim_sum)
                    sum += interim_sum
                sum += bias[m]
                print '{}, {}, sum = {}'.format(ir, ic, sum)
                out[m, ir / S, ic /S] = sum

print out




