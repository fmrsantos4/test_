# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 11:44:16 2023

@author: fmrsa
"""

import wntr
import numpy as np
import matplotlib.pyplot as plt
import pickle
import pandas as pd

#Sensor 1: 2
#Sensor 2: 261236
#Sensor 3: 288705
#Sensor 4: 6911A
#Sensor 5: 358588A
#Sensor 6: 43429
#Sensor 7: 18339
#Sensor 8: 18284
#Sensor 9: 43735


inp_file="C:/Users/fmrsa/Desktop/Tese/1Loop/BairrodaCelbi_py.inp"
wn=wntr.network.WaterNetworkModel(inp_file)
wn.options.hydraulic.demand_model = 'PDA'


# Detalhes de Simulação
wn.options.time.duration = 120*3600
wn.options.time.hydraulic_timestep = 3600
wn.options.time.report_timestep = 3600
wn.options.hydraulic.required_pressure = 15
wn.options.hydraulic.minimum_pressure = 10
wn.options.hydraulic.pressure_exponent=3 #Relação pressão-demand
wn.options.hydraulic.emitter_exponent=0.5 #Exponente pressão-leakage
wn.options.hydraulic.headloss= "H-W"  #Hazen-Williams
#wn.options.hydraulic.headloss= "D-W"  #Darcy-Weisbach


# Simulate hydraulics
sim = wntr.sim.EpanetSimulator(wn)
results = sim.run_sim(version=2.2)


