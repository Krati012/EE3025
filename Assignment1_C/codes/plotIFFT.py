#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 20:24:11 2021

@author: krati
"""

import numpy as np
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex

yn = np.loadtxt('ifft_Y.dat')

plt.plot(yn)
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()
plt.title('Filter output signal through IFFT')
plt.tight_layout()

#if using termux
plt.savefig('../figs/ifft.eps')
plt.savefig('../figs/ifft.pdf')
subprocess.run(shlex.splilt("termux-open ../figs/ifft.pdf"))

#else
#plt.show()