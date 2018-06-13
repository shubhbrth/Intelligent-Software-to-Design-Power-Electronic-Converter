#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 15:19:02 2018

@author: shubham
"""
#Library to read csv file
import pandas as pd
#Numpy Array
import numpy as np

Drain_source_Voltage=10
Continuous_drain_current=100
data_file=pd.read_csv('MOSFET_Specification'+'.csv')
data=np.array(data_file)
size=data.shape
selected=[]

for i in range(0,size[0]):
    temp_id=data[i][4]
    temp_id=temp_id.replace(" ","")
    temp_vds=data[i][5]
    temp_vds=temp_vds.replace(" ","")
    if temp_id!=' -' and temp_vds!=' -':
        if temp_id[-2:]=='mA':
            temp_id=float(temp_id[:-2])
            temp_id=temp_id/1000
        elif temp_id[-1:]=='A':
            temp_id=float(temp_id[:-1])
        if temp_vds[-2:]=='mV':
            temp_vds=float(temp_id[:-2])
            temp_vds=temp_vds/1000
        elif temp_vds[-1:]=='V':
            temp_vds=float(temp_vds[:-1])
        if temp_id>=Continuous_drain_current and temp_vds>=Drain_source_Voltage:
            selected.append(i)
            break
print("Selected MOSFET is "+str(data[selected[0]][1]))
    
#%%
for i in range(0,size[0]):
    temp_c=data[i][3]
    temp_c=temp_c.replace(" ","")
    temp_v=data[i][4]
    temp_v=temp_v.replace(" ","")
    if temp_c!=' -' and temp_v!=' -':
        if temp_c[-3:]=='ÂµF':
            temp_c=float(temp_c[:-3])
            temp_c=temp_c/1000000
        elif temp_c[-2]=='µF':
            temp_c=float(temp_c[:-2])
            temp_c=temp_c/1000000
        if temp_v[-1:]=='V':
            temp_v=float(temp_v[:-1])
        elif temp_v[-2]=='mV':
            temp_v=float(temp_v[:-2])
            temp_v=temp_v/1000
        if temp_c>=C and temp_v>=Capacitor_voltage:
            selected.append(i)
            break
print("Selected Conductor is "+str(data[selected[0]][1]))
        
    

        
#%%
data_file=pd.read_csv('Diode_Specification'+'.csv')
data=np.array(data_file)
size=data.shape
selected=[]
for i in range(0,size[0]):
    temp_value=data[i][3]
    temp_value.replace(" ","")
    if temp_value!=' -':
        if temp_value[-2:]=='mA':
            value=float(temp_value[:-2])
            value=value/1000
        else:
            value=float(temp_value[:-1])
        if Forward_current<=value:
            selected.append(i) 

temp=data[selected[0]][4]
temp.replace(" ","")
if temp[-2:]=='mV':
    temp=float(temp[:-2])
    temp=temp/1000
else :
    temp=float(temp[:-1])
select_comp_index=selected[0]
for i in range(1,len(selected)):    
    temp_selected=data[selected[i-1]][4]
    temp_selected.replace(" ","")
    if temp_selected!=' -':
        if temp_selected[-2:]=='mV':
            print(temp_selected+"mv")
            temp_selected=float(temp_selected[:-2])
            temp_selected=temp_selected/1000
        else:
            print(temp_selected+"V")
            temp_selected=float(temp_selected[:-1])
        if temp>temp_selected:
            temp=temp_selected
            select_comp_index=selected[i-1]
print('Selected Diode is '+str(data[select_comp_index][1]))