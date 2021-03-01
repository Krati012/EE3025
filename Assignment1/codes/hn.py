#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 01:58:35 2021

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

hn = np.zeros(n)
hn[0] = (b[0]/a[0])
hn[1] = (1/a[0])*(b[1]-a[1]*hn[0])
hn[2] = (1/a[0])*(b[2]-a[1]*hn[1]-a[2]*hn[0])
hn[3] = (1/a[0])*(b[3]-a[1]*hn[2]-a[2]*hn[1]-a[3]*hn[0])
hn[4] = (1/a[0])*(b[4]-a[1]*hn[3]-a[2]*hn[2]-a[3]*hn[1]
		-a[4]*hn[0])

for i in range(5,n):
	hn[i] = (1/a[0])*(-a[1]*hn[i-1]-a[2]*hn[i-2]-a[3]*hn[i-3]-
			a[4]*hn[i-4])

#plotting the graph
plt.plot(hn[0:99])
plt.title('Filter Impulse Response')
plt.xlabel('$n$')
plt.ylabel('$h(n)$')
plt.grid() #minor

#If using termux
plt.savefig('../figs/hn.pdf')
plt.savefig('../figs/hn.eps')
subprocess.run(shlex.split("termux-open ../figs/hn.pdf"))
#else
#plt.show()

