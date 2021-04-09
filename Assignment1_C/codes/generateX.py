#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 18:27:13 2021

@author: krati
"""

import numpy as np
import soundfile as sf

#If using termux
import subprocess
import shlex

#read .wav file
input_signal, fs = sf.read('Sound_Noise.wav')
sampl_freq = fs
order = 4
cutoff_freq = 4000

n = int(len(input_signal))
n = int(2 ** np.floor(np.log2(n)))

#writing data into a dat file
f = open("x.dat", "w") 
for i in range(n):
    f.write(str(input_signal[i]) + "\n")
f.close()