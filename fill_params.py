import numpy as np

def fill_input_from_file(inp, pad):
    with open('data/input.txt', 'r') as f:
        line = f.readline()
        count = int(line.split(' ')[0])
        dim = int(line.split(' ')[1])


        for i in range(count):
            for j in range(dim):
                line = f.readline()
                row = line.strip('\n')
                row = [int(item) for item in row.split(' ')]
                inp[i, j + pad, 0+pad:dim+pad] = np.copy(row)
        return inp


def fill_weights_from_file(weights):
    with open('data/weights.txt', 'r') as f:
        params = f.readline()
        inp_feature_map, output_feature_map, k_size = [int(p) for p in params.split(' ')]

        for i in range(inp_feature_map):
            for o in range(output_feature_map):
                for s in range(k_size):
                    line = f.readline()
                    print line
                    row = line.strip('\n')
                    row = [int(item) for item in row.split(' ')]
                    print row
                    weights[i, o, s, :] = np.copy(row)
        return weights


def fill_input(inp):

    inp[0,1,1] = 1
    inp[0,1,2] = 1
    inp[0,1,3] = 2
    inp[0,1,4] = 2
    inp[0,1,5] = 0

    inp[0,2,1] = 0
    inp[0,2,2] = 2
    inp[0,2,3] = 0
    inp[0,2,4] = 1
    inp[0,2,5] = 1


    inp[0,3,1] = 1
    inp[0,3,2] = 2
    inp[0,3,3] = 2
    inp[0,3,4] = 1
    inp[0,3,5] = 2


    inp[0,4,1] = 2
    inp[0,4,2] = 0
    inp[0,4,3] = 0
    inp[0,4,4] = 1
    inp[0,4,5] = 0

    inp[0,5,1] = 1
    inp[0,5,2] = 1
    inp[0,5,3] = 0
    inp[0,5,4] = 1
    inp[0,5,5] = 0


# ---------------------

    inp[1,1,1] = 0
    inp[1,1,2] = 2
    inp[1,1,3] = 0
    inp[1,1,4] = 0
    inp[1,1,5] = 1

    inp[1,2,1] = 1
    inp[1,2,2] = 2
    inp[1,2,3] = 2
    inp[1,2,4] = 2
    inp[1,2,5] = 0


    inp[1,3,1] = 0
    inp[1,3,2] = 0
    inp[1,3,3] = 1
    inp[1,3,4] = 1
    inp[1,3,5] = 2


    inp[1,4,1] = 1
    inp[1,4,2] = 0
    inp[1,4,3] = 0
    inp[1,4,4] = 1
    inp[1,4,5] = 0

    inp[1,5,1] = 0
    inp[1,5,2] = 2
    inp[1,5,3] = 0
    inp[1,5,4] = 0
    inp[1,5,5] = 1

# ---------------------

    inp[2,1,1] = 0
    inp[2,1,2] = 2
    inp[2,1,3] = 2
    inp[2,1,4] = 2
    inp[2,1,5] = 1

    inp[2,2,1] = 1
    inp[2,2,2] = 0
    inp[2,2,3] = 1
    inp[2,2,4] = 2
    inp[2,2,5] = 0


    inp[2,3,1] = 1
    inp[2,3,2] = 2
    inp[2,3,3] = 1
    inp[2,3,4] = 2
    inp[2,3,5] = 2


    inp[2,4,1] = 1
    inp[2,4,2] = 0
    inp[2,4,3] = 1
    inp[2,4,4] = 0
    inp[2,4,5] = 0

    inp[2,5,1] = 1
    inp[2,5,2] = 2
    inp[2,5,3] = 2
    inp[2,5,4] = 2
    inp[2,5,5] = 0


def fill_weights(F):
    F[0, 0, 0, 0] = -1 
    F[0, 0, 0, 1] = -1
    F[0, 0, 0, 2] =  0
    F[0, 0, 1, 0] = -1
    F[0, 0, 1, 1] =  0
    F[0, 0, 1, 2] =  0
    F[0, 0, 2, 0] =  1
    F[0, 0, 2, 1] =  1
    F[0, 0, 2, 2] =  1

    F[0, 1, 0, 0] =  1 
    F[0, 1, 0, 1] = -1
    F[0, 1, 0, 2] = -1
    F[0, 1, 1, 0] =  0
    F[0, 1, 1, 1] =  0
    F[0, 1, 1, 2] =  1
    F[0, 1, 2, 0] =  0
    F[0, 1, 2, 1] = -1
    F[0, 1, 2, 2] = -1

    F[0, 2, 0, 0] =  0 
    F[0, 2, 0, 1] =  0
    F[0, 2, 0, 2] =  1
    F[0, 2, 1, 0] = -1
    F[0, 2, 1, 1] = -1
    F[0, 2, 1, 2] =  1
    F[0, 2, 2, 0] = -1
    F[0, 2, 2, 1] =  0
    F[0, 2, 2, 2] = -1

# -------------------------

    F[1, 0, 0, 0] = -1 
    F[1, 0, 0, 1] =  0
    F[1, 0, 0, 2] =  0
    F[1, 0, 1, 0] = -1
    F[1, 0, 1, 1] = -1
    F[1, 0, 1, 2] =  1
    F[1, 0, 2, 0] = -1
    F[1, 0, 2, 1] =  0
    F[1, 0, 2, 2] = -1

    F[1, 1, 0, 0] = -1 
    F[1, 1, 0, 1] =  0
    F[1, 1, 0, 2] = -1
    F[1, 1, 1, 0] =  0
    F[1, 1, 1, 1] =  1
    F[1, 1, 1, 2] =  0
    F[1, 1, 2, 0] = -1
    F[1, 1, 2, 1] =  0
    F[1, 1, 2, 2] =  1

    F[1, 2, 0, 0] =  1 
    F[1, 2, 0, 1] =  0
    F[1, 2, 0, 2] =  0
    F[1, 2, 1, 0] =  0
    F[1, 2, 1, 1] = -1
    F[1, 2, 1, 2] = -1
    F[1, 2, 2, 0] =  0
    F[1, 2, 2, 1] = -1
    F[1, 2, 2, 2] =  0

def fill_bias(b):
    b[0] = 1
    b[1] = 0

