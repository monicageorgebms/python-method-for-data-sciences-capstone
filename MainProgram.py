#
#
# PMDS Final Project - Main Program
# Author: Monica George
#
#
#


import pandas as pd
import matplotlib.pyplot as plt


import MonicaLibrary as lib


#PART 1: Merging and Cleaning the Bioreactor Data Files

#Reading in our data

df1 = pd.read_csv('Dataset 1.csv')
df2 = pd.read_csv('Dataset 2.csv')
df3 = pd.read_csv('Dataset 3.csv')



#Cleaning the data:
#Rename first file column from "Reactor" to "Bioreactor"

df1.head()
        
header_names1 = ['Bioreactor','Day', 'pH', 'DO', 'CO2', 'Cell_Density', 'Cell_Viability', 'Product_Titer']
df1 = pd.read_csv('Dataset 1.csv', header = None, skiprows = 1, names = header_names1)

print(df1)


#Merge csv files into one
lib.MergeFile(df1, df2, df3)


#Read in the combined file 'output'
lib.ReadOutput()

#Clean the data:
#Rename each reactor with a unique identifier (number)

lib.RenameBioreactors(601,51)

#Check that you have separated out the correct number of reactors.
#We should have 600 unique reactors



lib.CheckNumberofReactors(600)




#PART 2: Creating Desired Visualizations

from MonicaClass import viz


#Creating a simple formatted line graph

plot1 = viz('Day','pH',0,0)


plot1.getSubFiles(51)



plot1.getPlot(30, 'Day', 'pH')

plt.show()



#Creating a graph with two data lines
plot2 = viz('Day', 'pH', 'Day', 'CO2')

plot2.getSeveralPlot(220, 'Day', 'pH', 'CO2')

plt.show()




#Creating a scatter plot

from MonicaClass import viz
from MonicaClass import scatter

plot3 = scatter(421, 'Day', 0, 'Product_Titer', 0)


plot3.getScatter(421, 'Day', 'Product_Titer')


