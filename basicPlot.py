'''
Created on Jun 15, 2013

@author: joe
'''


from pylab import *


def plotData(consumption, generation):
    
    
    day = {"consumption":consumption, "generation":generation}
    
    days = []
    days.append(day)
    
    figure()
    
        
    #subplots for each recorded metric
    for i, day in enumerate(days):
        print i, day
        subplot(len(days), 1, i)
        
        
        for valueLabel in day.iterkeys():
            plot(day[valueLabel], label=valueLabel)
        
        legend(loc='upper center')
        
    savefig("report.png")    
    

def main():
    pass


if __name__ == '__main__':
    main()  
    
    
