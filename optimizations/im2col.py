''' 
Simple im2col experiment
Two dimensional for now
Square inputs for now
Stride is 1 for now
Kernel dimensions are always square
TODO Extend to three dimensional
Most of the ideas are takes from http://cs231n.github.io/convolutional-networks/#conv
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

ker_size = ker.shape[0]
input_dim = inp.shape[0]
stride = 1
patch_size = ker_size * ker_size 
steps_in_one_dim = (input_dim - ker_size)/stride + 1

def gen_im2col(inp, ker_size):
    total_patches = steps_in_one_dim * steps_in_one_dim
    print 'total_patches {}'.format(total_patches)
    all_patches = np.zeros((total_patches, patch_size))

    patch = np.zeros((patch_size))
    patch_num = 0
    for i in range(ker_size):
        for j in range(ker_size):
            k = 0
            for kr in range(ker_size):
                for kc in range(ker_size):
                    patch[k] = inp[i + kr, j+ kc]
                    k += 1
            # print patch
            all_patches[patch_num] = patch
            patch_num += 1
    return all_patches

def conv_with_im2col(im2col, ker):
    ker = np.reshape(ker, (patch_size))
    return np.reshape(np.dot(im2col, ker), (steps_in_one_dim,steps_in_one_dim))

print 'Computed:\n{}'.format(conv_with_im2col(gen_im2col(inp, ker_size), ker))

# verify against a library implementation
print 'Expected:\n{}'.format(signal.convolve2d(inp, ker, mode='valid'))



