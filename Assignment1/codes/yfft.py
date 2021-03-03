#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 03:09:33 2021

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

def H(z,num,den):
    numr = np.polyval(num,pow(z,-1))
    denr = np.polyval(den,pow(z,-1))
    return numr/denr

x,fs = sf.read('Sound_Noise.wav')
samp_freq = fs
order = 4
cutoff_freq = 4000.0
Wn = 2*cutoff_freq/samp_freq

b,a = signal.butter(order,Wn,'low')

n = len(x)
y = np.zeros(n)

omega = np.linspace(-np.pi,np.pi,n,endpoint=True)
z = np.exp(1j * omega)
H = H(z,b,a)
X = np.fft.fftshift(np.fft.fft(x))
Y = np.multiply(X,H)
y = np.fft.ifft(np.fft.ifftshift(Y))
sf.write('Sound_fft.wav',np.real(y),fs)

plt.plot(np.real(y))
plt.title('Filter output signal through IFFT')
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()# minor

#If using termux
plt.savefig('../figs/yfft.pdf')
plt.savefig('../figs/yfft.eps')
subprocess.run(shlex.split("termux-open ../figs/yfft.pdf"))
#else
#plt.show()
