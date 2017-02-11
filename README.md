##### Understanding Volumetric Convolutions with Python Code

The code in intended to demystify volumentric convolutions, 
a core operation in today's convolutional neural nets (CNNs), 
where we have a 3D volume for the input (a spatial 2D plane times the feature map count) and 
a 3D volume for the output (similarly, a spatial 2D plane times the feature map count). The kernels (aka, weights) are also 3D.

Note, the size of the feature maps in the input and the output can be different 
depending upon your network architecture. 
These feature map sizes also affect the number of parameters 
in the weights (with which you are convolving) and the baises. 

The ideas are lucidly explained by [Andrej Karpathy](http://cs.stanford.edu/people/karpathy/) [here](http://cs231n.github.io/convolutional-networks/#conv); 
this project simply implements volumetric convolutions such that they can be grasped by beginners (or by someone looking for a introductory refresher).

To be sure, several performance optimizations are possible, but they get in the way of comprehension.

The implementation can be verified against the two screen captures below.

##### Test case from Screenshot 1

Frozen from animation using randon inputs & weights [here](http://cs231n.github.io/convolutional-networks/#conv)

![alt text](/screen-shots/Screenshot\ from\ 2017-02-09\ 16\:15\:26.png "screen cap 1")

##### Test case from Screenshot 2

Frozen from animation using randon inputs & weights [here](http://cs231n.github.io/convolutional-networks/#conv)

![alt text](/screen-shots/Screenshot\ from\ 2017-02-09\ 22\:31\:21.png "screen cap 2")



