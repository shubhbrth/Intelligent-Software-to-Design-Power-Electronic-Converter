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

L=0.0001
Irms=1
data_file=pd.read_csv('Inductor_Specification'+'.csv')
data=np.array(data_file)
size=data.shape
selected=[]

for i in range(0,size[0]):
    temp_inductance=data[i][3]
    temp_irms=data[i][4]
    temp_inductance=temp_inductance.replace(" ","")
    temp_irms=temp_irms.replace(" ","")
    if temp_irms!=' -' and temp_inductance!=' -':
        if temp_inductance[-3:]=="ÂµH":
            temp_inductance=float(temp_inductance[:-3])
            temp_inductance=temp_inductance/1000000
        elif temp_inductance[-2:]=="µH":
            temp_inductance=float(temp_inductance[:-2])
            temp_inductance=temp_inductance/1000000
        elif temp_inductance[-2:]=="mH":
            temp_inductance=float(temp_inductance[:-2])
            temp_inductance=temp_inductance/1000
        elif temp_inductance[-2:]=="nH":
            temp_inductance=float(temp_inductance[:-2])
            temp_inductance=temp_inductance/1000000000
        elif temp_inductance[-2:]=="pH":
            temp_inductance=float(temp_inductance[:-2])
            temp_inductance=temp_inductance/1000000000000
        if temp_irms[-2:]=="mA":
            temp_irms=float(temp_irms[:-2])
            temp_irms=temp_irms/1000
        else:
            temp_irms=float(temp_irms[:-1])
        if temp_inductance>=int(L) and temp_irms>=int(Irms):
            selected.append(i)
            break
print("Selected inductor is"+str(data[selected[0]][1]))
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