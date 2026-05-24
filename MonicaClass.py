
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
from glob import glob

global data
global brs


class viz:
    
    
    data = pd.read_csv('output2.csv')

    def __init__(self, columnx, columny, column2x, column2y):
        self.day = 0
        self.columnx = columnx
        self.column2x = column2x
        self.columny = columny
        self.column2y = column2y

#split every unique bioreactor into it's own sub-file
    def getSubFiles(self,x):
        size = x
        section = 1


        for chunk in pd.read_csv('output2.csv', chunksize = size):
            chunk.to_csv("Bioreactor" + str(section) + '.csv', index=False)
            section +=1

        print('\n')
        print('The', section-1 , 'Bioreactors have been split into their own sub files.')



    def getPlot(self, reactor, columnx, columny):

#read in the individual files
        r = range(1,601)
        c = 1
        name = glob('Bioreactor*.csv')
        br_col = [pd.read_csv(f) for f in name]

        print('\n')
        print('The Bioreactor subfiles have been read in.')

        x = list(br_col[reactor][str(columnx)])
        print(x)
        y = list(br_col[reactor][str(columny)])
        print(y)


        plt.figure()
        plt.plot(x, y, color = 'g', label = columny)

        response = input('Plot title:')
        plt.title(response, fontdict={'fontsize': 14})

        plt.xlabel(columnx)
        plt.ylabel(columny)

        plt.legend()

        plt.show()




    def getSeveralPlot(self, reactor, columnx, column1y, column2y):

        #read in the individual files
        r = range(1,601)
        c = 1
        name = glob('Bioreactor*.csv')
        br_col = [pd.read_csv(f) for f in name]

        print('\n')
        print('The Bioreactor subfiles have been read in.')

        x = list(br_col[reactor][str(columnx)])
        print(x)
        y1 = list(br_col[reactor][str(column1y)])
        print(y1)
        y2 = list(br_col[reactor][str(column2y)])
        print(y2)

        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        ax1.plot(x, y1, color = 'b', label=column1y)
        
        ax1.legend(loc=3)        

        print('Determine the y-axis scale for the first line graph')

        ymin1 = int(input('Set the y-axis minimum:'))
        ymax1 = int(input('Set the y-axis maximum:'))
        
        plt.ylim([ymin1, ymax1])

        
        ax2 = ax1.twinx()
        ax2.plot(x, y2, color = 'r', label=column2y)

        print('Determine the y-axis scale for the second line graph')

        ymin2 = int(input('Set the y-axis minimum:'))
        ymax2 = int(input('Set the y-axis maximum:'))
        
        plt.ylim([ymin2, ymax2])

        ax2.legend(loc=1)

        response = input('Plot title:')
        plt.title(response, fontdict={'fontsize': 14})

        plt.show()





class scatter(viz):

    def __init__(self, reactor, columnx, column2x, columny, column2y):
        viz.__init__(self, columnx, column2x, columny, column2y)
        self.reactor = reactor
        self.columnx = columnx
        self.column2x = column2x
        self.columny = columny
        self.column2y = column2y

    def getScatter(self, reactor, columnx, columny):
        
        #read in the individual files
        r = range(1,601)
        c = 1
        name = glob('Bioreactor*.csv')
        br_col = [pd.read_csv(f) for f in name]

        print('\n')
        print('The Bioreactor subfiles have been read in.')

        x = list(br_col[reactor][str(columnx)])
        print(x)
        y = list(br_col[reactor][str(columny)])
        print(y)

        plt.scatter(x, y, color = 'g', label=columny)

        print('Determine the y-axis scale for the scatter plot')

        ymin2 = int(input('Set the y-axis minimum:'))
        ymax2 = int(input('Set the y-axis maximum:'))
        plt.ylim([ymin2, ymax2])

        reply = input('Plot title:')
        plt.title(reply, fontdict={'fontsize': 14})

        plt.xlabel(columnx)
        plt.ylabel(columny)
        
        plt.legend(loc=1)

        plt.show()


    
    

