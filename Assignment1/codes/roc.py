#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 19:57:48 2021

@author: krati
"""

import numpy as np
import soundfile as sf
from scipy import signal
import matplotlib.pyplot as plt
from matplotlib import patches
#If using termux
import subprocess
import shlex
#end if

poles = [0.694+1j*0.41,0.694-1j*0.41,
		0.566+1j*0.134,0.566-1j*0.134]
pole_r = []
pole_i = []
for i in poles:
    pole_r += [i.real]
    pole_i += [i.imag]

zeros = [-4.9+1j*6.153,-4.9-1j*6.153,
		0.18318,5.62274677]
zero_r = []
zero_i = []
for j in zeros:
    zero_r += [j.real]
    zero_i += [j.imag]
    
x = np.linspace(-2,2,100)
ax = plt.subplot(111)
#Add unit circle and zero axes    
unit_circle = patches.Circle((0,0), radius=1, fill=False,color='black', ls='dashed')
ax.add_patch(unit_circle)

y1 = np.sqrt(16-x**2)
y2 = -np.sqrt(16-x**2)
plt.fill_between(x, y1, y2, color='#539ecd')

#Add circle passing through max abs(poles) and zero axes    
req_circle = patches.Circle((0,0), radius=np.max(np.abs(poles))
			, fill=True,color='white',ls='solid')
ax.add_patch(req_circle)
boundary = patches.Circle((0,0), radius=np.max(np.abs(poles))
			, fill=False,color='black',ls='solid')
ax.add_patch(boundary)
#Plot poles and zeros
plt.plot(pole_r,pole_i,'x',color='red',markersize=6)
plt.plot(zero_r,zero_i,'o',color='None',markeredgecolor='red',markersize=6)
plt.text(-0.15,0.05,"z=0")
plt.text(0.4,0.75,"|z|>0.806")
plt.text(0,1.1,"|z|=1")
plt.title('H(z) in z-plane')
plt.xlabel('real')
plt.ylabel('Imaginary')
plt.grid()# minor
plt.axis('scaled')
plt.axis([-1.5,1.5,-1.5,1.5])

#If using termux
plt.savefig('../figs/roc.pdf')
plt.savefig('../figs/roc.eps')
subprocess.run(shlex.split("termux-open ../figs/roc.pdf"))
#else
#plt.show()
