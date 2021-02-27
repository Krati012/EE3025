#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 21:14:03 2021

@author: krati
"""

import soundfile as sf
from scipy import signal

#read .wav file
input_signal,fs = sf.read('Sound_Noise.wav')

#sampling frequency of input signal
sampl_freq = fs

#order of the filter
order = 4

#cutoff frequency 4kHz
cutoff_freq = 4000.0

#digital frequency
Wn = 2*cutoff_freq/sampl_freq

#b and a are numerator and denominator polynomials respectively
b, a = signal.butter(order, Wn, 'low')

#filter the input signal with butterowrth filtler
output_signal = signal.filtfilt(b, a, input_signal)
#output_signal = signal.lfilter(b, a, input_signal)

#write the output into .wav file
sf.write('Sound_With_ReducedNoise.wav', output_signal, fs)