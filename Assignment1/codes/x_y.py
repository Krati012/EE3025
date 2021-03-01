#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 21:14:03 2021

@author: krati
"""

import numpy as np
import soundfile as sf
from scipy import signal
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex
#end if

x,fs = sf.read('Sound_Noise.wav')
n = len(x)
y = np.zeros(n)
sampl_freq = fs
order = 4
cutoff_freq = 4000.0
Wn = 2*cutoff_freq/sampl_freq

b,a = signal.butter(order, Wn, 'low')

y[0] = (b[0]/a[0])*x[0]
y[1] = (1/a[0])*(b[0]*x[1]+b[1]*x[0] - a[1]*y[0])
y[2] = (1/a[0])*(b[0]*x[2]+b[1]*x[1]+b[2]*x[0]- 
		a[1]*y[1]-a[2]*y[0])
y[3] = (1/a[0])*(b[0]*x[3]+b[1]*x[2]+b[2]*x[1]+
		b[3]*x[0] - a[1]*y[2]-a[2]*y[1]-a[3]*y[0])
y[4] = (1/a[0])*(b[0]*x[4]+b[1]*x[3]+b[2]*x[2]+
		b[3]*x[1]+b[4]*x[0] - a[1]*y[3]-a[2]*y[2]-
		a[3]*y[1]-a[4]*y[0])

for i in range(5,n):
	y[i] = (1/a[0])*(b[0]*x[i]+b[1]*x[i-1]+b[2]*x[i-2]+
		b[3]*x[i-3]+b[4]*x[i-4] - a[1]*y[i-1]-a[2]*y[i-2]-
		a[3]*y[i-3]-a[4]*y[i-4])

#sf.write('Sound_diffEq.wav',y,fs)
print("x", np.max(x), np.min(x))
print("y", np.max(y), np.min(y))

#subplots
plt.subplot(2, 1, 1)
plt.plot(x)
plt.title('Digital Filter Input-Output')
plt.ylabel('$x(n)$')
plt.grid() #minor

plt.subplot(2, 1, 2)
plt.plot(y)
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid() #minor

#If using termux
plt.savefig('..figs/x_y.pdf')
plt.savefig('..figs/x_y.eps')
subprocess.run(shlex.split("termux-open ../figs/x_y.pdf"))

#else
#plt.show()
