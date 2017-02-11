''' 
Simple im2col experiment
'''
import numpy as np
from scipy import signal
from scipy import misc

inp = np.array([[1,2,1,2,3],
               [1,1,1,1,2],
               [2,2,2,2,1],
               [1,3,1,1,1],
               [2,4,2,2,2]])

ker  = np.array([[1,2,1],
                 [1,2,1],
                 [1,2,1]])

def gen_im2col(inp):
    all_patches = np.zeros((9,9))

    patch = np.zeros((9))
    total_patches = 0
    for i in range(3):
        for j in range(3):
            k = 0
            for kr in range(3):
                for kc in range(3):
                    patch[k] = inp[i + kr, j+ kc]
                    k += 1
            # print patch
            all_patches[total_patches] = patch
            total_patches += 1
    return all_patches

def conv_with_im2col(im2col, ker):
    ker = np.reshape(ker, (9))
    return np.reshape(np.dot(im2col, ker), (3,3))


print conv_with_im2col(gen_im2col(inp), ker)

# verify against a library implementation
conv = signal.convolve2d(inp, ker, mode='valid')
print conv


