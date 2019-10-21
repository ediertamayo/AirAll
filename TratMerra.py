# -*- coding: utf-8 -*-
"""
Autores: LEAPYS
Descripción: Script para tratar los datos correspondientes al NASA Space Apps Challenge
Fecha de creación: 19/10/2019
"""

import numpy as np
import pandas as pd

inpfiles=np.loadtxt('files.txt')

for x in range(len(inpfiles)):
    if x==0:
        A=np.loadtxt(inpfiles[x],delimiter=',',dtype='str')
        header=A[0,:]
        data=A[1:,:]
        
        Df=pd.DataFrame(data,columns=header)
        Df['BCSMASS']=Df['BCSMASS'].astype(float)
        Df['SO2SMASS']=Df['SO2SMASS'].astype(float)
        Df['TOTEXTTAU']=Df['TOTEXTTAU'].astype(float)
        
        Cdirsem=Df.groupby(['Lat','Lon'],
                            as_index=False)['BCSMASS','SO2SMASS','TOTEXTTAU'].mean()
        
        Cdirsem.to_csv('MERRATratPy.csv')
    if x==1:
        dat1=pd.read_csv(inpfiles[x],sep=';')
        
        A=np.array(dat1.loc[:,'value'])        
        for i in range(len(A)):
            if A[i]<0:
                A[i]==np.nan
            elif A[i]>150:
                A[i]==np.nan
             
        dat1['values']=A
        
        
        Cdirsem=dat1.groupby(['Latitude','Longitude','parameter','date'],
                            as_index=False)['values'].mean()
        Cdirsem.to_csv('LosAngelesTratPy.csv')
    if x==2:
        dat1=pd.read_csv(inpfiles[x],sep=',')
        
        A=np.array(dat1.loc[:,'Sample Measurement'])        
        for i in range(len(A)):
            if A[i]<0:
                A[i]==np.nan
            elif A[i]>150:
                A[i]==np.nan
             
        dat1['Sample Measurement']=A
        Cdirsem=dat1.groupby(['Latitude','Longitude','Parameter Name','Date GMT'],
                            as_index=False)['Sample Measurement'].mean()
        Cdirsem.to_csv('AQtratPy.csv')
        



