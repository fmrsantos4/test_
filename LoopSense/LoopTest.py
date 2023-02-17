# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 09:47:32 2023

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
#Sensor 8: 6932A
#Sensor 9: 6944A

inp_file="C:/Users/fmrsa/Desktop/Tese/1Loop/BairrodaCelbi_py.inp"
wn=wntr.network.WaterNetworkModel(inp_file)
wn.options.hydraulic.demand_model = 'PDD'



node_names = wn.node_name_list #Lista de nomes de todos os nodos
num_nodes = wn.num_nodes #Numero de nodos
print(wn.describe(level=0))

# Graph the network
#wntr.graphics.plot_network(wn, title=wn.name)

# Detalhes de Simulação
wn.options.time.duration = 24*3600
wn.options.time.hydraulic_timestep = 300
wn.options.time.report_timestep = 300
wn.options.hydraulic.required_pressure = 15
wn.options.hydraulic.minimum_pressure = 10
wn.options.hydraulic.pressure_exponent=1.5
#wn.options.hydraulic.headloss= "H-W"  #Hazen-Williams
wn.options.hydraulic.headloss= "D-W"  #Darcy-Weisbach


# Simulate hydraulics
sim = wntr.sim.EpanetSimulator(wn)
results = sim.run_sim(version=2.2)

# Plot results on the network
pressure_at_5hr = results.node['pressure'].loc[5*3600, :]

ax = wntr.graphics.plot_network(wn, node_attribute=pressure_at_5hr,node_range=[5,30], node_colorbar_label='Pressure (m)')



node_keys = results.node.keys() #Quais os atributos dos nodos no simulador EPANET
#print(node_keys) 
#com o wntr ainda há o leak demand

link_keys = results.link.keys() #Quais os atributos dos nodos no simulador EPANET
#print(link_keys) 


#SIM RESULTS
pressure = results.node['pressure']

#Pressão a tempos (:,x) no nodo x
node1 = pressure.loc[:,'2']   
node2 = pressure.loc[:,'261236']   
node3 = pressure.loc[:,'288705']   
node4 = pressure.loc[:,'6911A']   
node5 = pressure.loc[:,'358588A']   
node6 = pressure.loc[:,'43429']   
node7 = pressure.loc[:,'18339']   
node8 = pressure.loc[:,'6932A']   
node9 = pressure.loc[:,'6944A']   

#Fazer plots:
plt.figure()
ax = node1.plot(label='Sensor 1')
ax = node2.plot(label='Sensor 2')
ax = node3.plot(label='Sensor 3')
ax = node4.plot(label='Sensor 4')
ax = node5.plot(label='Sensor 5')
ax = node6.plot(label='Sensor 6')
ax = node7.plot(label='Sensor 7')
ax = node8.plot(label='Sensor 8')
ax = node9.plot(label='Sensor 9')
leg=ax.legend()
text = ax.set_xlabel("Time (s)")
text = ax.set_ylabel("Pressure (m)")


node1.to_excel('node1.xlsx')
node2.to_excel('node2.xlsx')
node3.to_excel('node3.xlsx')
node4.to_excel('node4.xlsx')
node5.to_excel('node5.xlsx')
node6.to_excel('node6.xlsx')
node7.to_excel('node7.xlsx')
node8.to_excel('node8.xlsx')
node9.to_excel('node9.xlsx')




