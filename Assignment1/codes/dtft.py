#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 01:19:50 2021

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

#DTFT
def H(z,num,den):
    numr = np.polyval(num,pow(z,-1))
    denr = np.polyval(den,pow(z,-1))
    return numr/denr

x,fs = sf.read('Sound_Noise.wav')
samp_freq = fs
order = 4
cutoff_freq = 4000.0
Wn = 2*cutoff_freq/samp_freq

b, a = signal.butter(order,Wn,'low')

#input and output
omega = np.linspace(-np.pi,np.pi,len(x),endpoint=True)

#subplots
plt.plot(omega,abs(H(np.exp(1j*omega),b,a)))
plt.title('Impulse Frequency Response')
plt.xlabel('$w$')
plt.ylabel('$H(jw)$')
plt.grid()# minor

#If using termux
plt.savefig('../figs/dtft.pdf')
plt.savefig('../figs/dtft.eps')
subprocess.run(shlex.split("termux-open ../figs/dtft.pdf"))
#else
#plt.show()
