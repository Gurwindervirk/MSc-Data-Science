#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import sympy
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


print(np.__version__)


# In[1]:


def hellop(x):
    print(x)
    


# In[2]:


y="hello gurwinder"
hellop(y)
#np? we can ? to see documentation of any module like the code following # sign


# In[54]:


# creating an array in Numpy
arr= np.array([1,2,3,4,5,6])
print(arr.shape)
print(arr)
arr2=np.random.rand(20).reshape(5,4) # to generate an array of random numbers
arr_int= np.random.randint(20, size=(5,4))
print(arr2)


# In[57]:


np.random.seed(20) # seed is used to set and random variable so array genertaed will be same every time
arr4= np.random.rand(20)
print(arr4)
print(arr_int.shape)


# In[59]:


#spliting and merging or joining two arrays
arr5= np.array([[10,20,30,85],[10,52,45,65]])
display(arr5)


# In[72]:


arr6=np.hstack([arr5,arr5])#np.concatenate([arr5,arr5], axis=0) # axis 1 means horizontal or x axis 0 means y or vertical
#similar can be achived using np.vstack for vertical and np.hstack for horizontal stack
arr6
x1=np.array([1,2,3,4,5,6,7,8,9])
x2= np.split(x1, [2,5,7,9])
#np.split?
print(x2)
#np.split?


# In[88]:


#mat= np.random.randint(9, size=(3,3))
mat=np.arange(9).reshape(3,3) #matrix with 0 determinant
print(np.linalg.det(mat))
print(mat)
#print(np.linalg.inv(mat))
np.max(mat)


# In[85]:


x= sympy.Symbol('x')
fx= 2*x**3+5*x+ 15
print(np.min(fx).doit())

