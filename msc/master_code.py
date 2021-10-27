#!/usr/bin/env python
# coding: utf-8

# ## Master code for exams

# In[1]:


from sympy import *


# In[2]:


def df(fx,h):
    fx = Derivative(fx, h).doit()
    return fx

def min_max(fx,x):
    ls=[]
    dv= Derivative(fx,x).doit()
    x_critical_points= solve(dv)
    dv2= Derivative(fx,x,2)

    for ind, i in enumerate(x_critical_points):
    
        cr=dv2.subs({x:x_critical_points[ind]}).evalf()
        ls.append(cr)
    for i, m in enumerate(ls):
        if m>0:
            print(x_critical_points[i]," is local minimum at:",m)
        elif m<0:
            print(x_critical_points[i],"is local maximum at",m)
        else:
            print(x_critical_points[i],"is saddle point at", m)
    return dv, dv2, x_critical_points