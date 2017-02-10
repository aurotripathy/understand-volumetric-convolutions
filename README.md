##### Understanding Volumetric Convolutions with Python Code

The code in intended to demystify volumentric convolutions, 
a core operation in today's convolutional neural nets (CNNs), 
where we have a 3D volume for the input (a spatial 2D plane times the feature map count) and 
a 3D volume for the output (similarly, a spatial 2D plane times the feature map count). The kernels (aka, weights) are also 3D.

Note, the size of the feature maps in the input and the output can be different 
depending upon your network architecture. 
These feature map sizes also affect the number of paramters in the weights and baises 
with which you are concolving. 

The ideas are lucidly explained [here](http://cs231n.github.io/convolutional-networks/#conv); 
this project implements volumetric convolutions such that they can be grasped by beginners.

To be sure, several performance optimizations are possible, but they get in the way of comprehension.

The implementation can be verified against the two screen captures below.

##### Screenhot 1

Frozen from animation using randon inputs & weights [here](http://cs231n.github.io/convolutional-networks/#conv)

![alt text](/screen-shots/Screenshot\ from\ 2017-02-09\ 16\:15\:26.png "screen cap 1")

##### Screenhot 2

Frozen from animation using randon inputs & weights [here](http://cs231n.github.io/convolutional-networks/#conv)

![alt text](/screen-shots/Screenshot\ from\ 2017-02-09\ 22\:31\:21.png "screen cap 2")



