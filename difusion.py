# -*- coding: utf-8 -*-

from typing import Iterable
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def diffusion(frame: int, *fargs) -> Iterable:
   t, dt = 0, 1 # time related variables

   l, k = fargs[0], fargs[1] # tuple unpacking
   f = np.zeros(shape=l) # empty matrix

   f[0] = 1 # defautl initial conditions (CC)
   f[l-1] = 0

   try:
      f = fargs[2] # try get CC
   except:
      pass

   g = f.copy() # creates aux. g

   while t < frame: # start the loop
      for i in range(1, l-1): # update f and g for len(f) (=l)
         g[i] = f[i] + k*(f[i-1]-2*f[i]+f[i+1])
      
      f = g.copy() # update f
      t += dt # update t with step dt

   plt.cla() # clear "cached" plot

   ## plot axis limits ##
   plt.ylim(0,max(f))
   plt.xlim(0,l-1)

   plt.plot(f) # plot f vs. len(f) (=l)
   
   return(Iterable)

## usage ##
l, k = 25, 0.25
f = np.zeros(shape=l)

f[0] = 10 # initial conditions
f[20] = 25

animate = FuncAnimation(plt.gcf(), diffusion, interval=10, fargs=tuple([l,k,f])) # call function
#plt.tight_layout() # prevent text overlaps
plt.show()
