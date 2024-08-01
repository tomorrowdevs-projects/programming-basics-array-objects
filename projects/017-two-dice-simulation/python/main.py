from random import choice
from tabulate import tabulate

def TwoDiceSimulator():
    result=choice(range(1,7))+choice(range(1,7))
    return result

def main():
    #--Asking for the number of executions--#
    simulation_nr=int(input('Please, enter the number of simulation you want to perform (remember that for the Central Limit Theorem a larger execution number brings to a better approximation of the theoretical calculation):'))
    
    #--Setting the dictionary and calculating the theoretical frequency
    data={}
    for i in range(2,13):
        if i<7:
            data[i]=[round((i-1)/36*100,2),0]
        elif i>7:
            data[i]=[round((13-i)/36*100,2),0]
        else:
            data[i]=[round(1/6*100,2),0]
    
    #--Running simulation--#
    for i in range(simulation_nr):
        result=TwoDiceSimulator()
        data[result][1]+=1/simulation_nr*100
    for i in data:
        data[i][1]=round(data[i][1],2) #Rounding the simulation results (rounding the result before, would cause 0 for large numbers of executions)
    
    print('The following table shows the simulation results for {} executions.\n'.format(simulation_nr))
    print(tabulate(data, headers="keys", tablefmt="grid"))
    print('\nLEGENDA\nFirst row --> Dice Result\nSecond row --> Theoretical frequency\nThird row --> Simulation result')

if __name__=='__main__':
    main()