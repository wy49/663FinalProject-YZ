
from __future__ import division
import numpy as np
import numpy.linalg
import math
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import inv

np.random.seed(123)

#weights matrix
A=np.array([[0,1,0,0,0,0,1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,1,1,1,0,0,0,1,0,1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,1,1,1,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,1,0,0,0,0,0,1,0]])

#data simulation
num_objects=100
object_dim=36
 
sigma_x_orig=0.5

I=sigma_x_orig*np.eye(object_dim)
Z_orig=np.zeros((num_objects,4))

X=np.zeros((num_objects,object_dim))

for i in range(num_objects):
    Z_orig[i,:]=(np.random.uniform(0,1,4)>0.5)
    while sum(Z_orig[i,:])==0:
        Z_orig[i,:]=(np.random.uniform(0,1,4)>0.5)
    X[i,:]=np.dot(np.random.normal(0,1,object_dim),I)+np.dot(Z_orig[i,:],A)