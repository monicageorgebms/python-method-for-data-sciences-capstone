#
#
#

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
from glob import glob

global data
global brs


def MergeFile(df1,df2,df3):
        values1 = df1[['Bioreactor','Day', 'pH', 'DO', 'CO2', 'Cell_Density', 'Cell_Viability', 'Product_Titer']]
        values2 = df2[['Bioreactor', 'Day', 'pH', 'CO2', 'Cell_Density', 'Cell_Viability', 'Product_Titer']]
        values3 = df3[['Bioreactor', 'Day', 'pH', 'CO2', 'O2_MFC', 'Cell_Density', 'Cell_Viability', 'Product_Titer']]

        dataframes = [values1, values2, values3]

        combine = pd.concat(dataframes)

        df = combine.to_csv('output.csv', index = False)

        response = input('Do you want to view the output file (Yes/No)? ')
        if (response == 'Yes' or response == 'yes'):
            print(combine)

        else:
            print('The csv files have been merged into one output file.')

        

def ReadOutput():
    global data
    data = pd.read_csv('output.csv')

    
def RenameBioreactors(numreactor, days):
    
    global data
    global brs
    
    l = list(range(1, numreactor))
    r = list(range(0, days))
    brs = []

    for i in l:
        for j in r:
            brs.append(i)

    data['Bioreactor'] = brs
    data.to_csv('output2.csv', index=False)

    print('\n')
    print('The Bioreactors have been renamed with a unique identifier.')


def CheckNumberofReactors(x):
    global brs

    print(brs.pop())
    brs.append(x)





#######

