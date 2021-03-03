#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 00:29:00 2021

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
samp_freq = fs
order = 4
cutoff_freq = 4000.0
Wn = 2*cutoff_freq/samp_freq
b,a = signal.butter(order,Wn,'low')

h = np.zeros(n)
h[0] = (b[0]/a[0])
h[1] = (1/a[0])*(b[1]-a[1]*h[0])
h[2] = (1/a[0])*(b[2]-a[1]*h[1]-a[2]*h[0])
h[3] = (1/a[0])*(b[3]-a[1]*h[2]-a[2]*h[1]-a[3]*h[0])
h[4] = (1/a[0])*(b[4]-a[1]*h[3]-a[2]*h[2]-a[3]*h[1]
		-a[4]*h[0])
for i in range(5,n):
	h[i] = (1/a[0])*(-a[1]*h[i-1]-a[2]*h[i-2]-a[3]*h[i-3]-
			a[4]*h[i-4])
			
X = np.fft.fftshift(np.fft.fft(x))
H = np.fft.fftshift(np.fft.fft(h))
#subplots
plt.figure(figsize=(9,15))

plt.subplot(4,1,1)
plt.plot(np.abs(X))
plt.title(r'$|X(k)|$')
plt.grid() #minor

plt.subplot(4,1,2)
plt.plot(np.angle(X))
plt.title(r'$\angle{X(k)}$')
plt.grid() #minor

plt.subplot(4,1,3)
plt.plot(np.abs(H))
plt.title(r'$|H(k)|$')
plt.grid() #minor

plt.subplot(4,1,4)
plt.plot(np.angle(H))
plt.title(r'$\angle{H(k)}$')
plt.grid() #minor

#If using termux
plt.savefig('../figs/xhfft.pdf')
plt.savefig('../figs/xhfft.eps')
subprocess.run(shlex.split("termux-open ../figs/xhfft.pdf"))
#else
#plt.show()

