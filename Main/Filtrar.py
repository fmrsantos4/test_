# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 15:39:08 2023

@author: fmrsa
"""

import numpy as np
from scipy.signal import butter, lfilter,filtfilt
import matplotlib.pyplot as plt
import pandas as pd




data=pd.read_csv('Sensor1_fev23.csv',delimiter=';',decimal=',')
data=data.filter(items=['Pressao(bar)'])
data.plot()
plt.title('Inicial Data')
plt.figure()



data['SMA2']=data.rolling(10,min_periods=1).mean()
data['SMA2'].plot()
plt.title('Moving average data')
plt.figure()


data['SMA2'][0:234].plot()
plt.title('Moving avg 1 day')
data[0:234].plot()
plt.title('1-day data')





# data=pd.read_csv('Sensor1.csv',delimiter=';',decimal=',')
# data=data.filter(items=['Pressao(bar)'])

# def butter_lowpass(cutOff, fs, order=5):
#     nyq = 0.5 * fs
#     normalCutoff = cutOff / nyq
#     b, a = butter(order, normalCutoff, btype='high', analog = True)
#     return b, a

# def butter_lowpass_filter(data, cutOff, fs, order=4):
#     b, a = butter_lowpass(cutOff, fs, order=order)
#     y = lfilter(b, a, data)
#     return y

# cutOff = 100 #cutoff frequency in rad/s
# fs = 1000.495559 #sampling frequency in rad/s
# order = 20 #order of filter

# #print sticker_data.ps1_dxdt2
# plt.figure()
# y = butter_lowpass_filter(data, cutOff, fs, order)
# plt.plot(y)