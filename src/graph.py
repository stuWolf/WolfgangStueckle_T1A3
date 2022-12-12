import matplotlib.pyplot as plt
import numpy as np

import matplotlib.lines as mlines
import formula

def plot_graph(P, m,  r, Compound_frequ, num_years ):
    
    # P = 0 # start balance
    # m = 100 # monthly contribution
    # r = 18 # interest rate in %
    # Compound_frequ = 'monthly'
    # t = 10  # number of years

    A = 0
    i = 0
    capital = []
    year_contribution = []

    t = np.arange(0, num_years+1, 1)  # t goes from 0 to val, 1 increment
    
    
    # calculate capital for each year (array element) based on compound interest and contribution
    # write each year into list
   
    for i in range(0,num_years+1, 1):
        A = formula.calculate_capital(P, m,  r, Compound_frequ,int( t[i])) # calculate compounded value
        capital.append(A)  #  write ammount of each year in list
        y = int(m*12*i + P )       # calculate personal contribution, write ammount of each year in list
        year_contribution.append(y) 
        
        
    
    # configure and plot graph
    # plt.title('Total Savings')
    plt.grid(color='black', linestyle='-', linewidth=1)
    plt.plot(t, year_contribution, 'r--', t, capital, 'g')
    plt.xlabel('Years')
    plt.ylabel('Value in AUD')

    plt.suptitle('Total Capital')
    blue_line = mlines.Line2D([], [], color='red', marker='',markersize=15, label= (f'Total Contribution of {year_contribution[num_years]} AUD'))
    green_line = mlines.Line2D([], [], color='green', marker='',markersize=15, label= (f'Future value at {r}% interest '))
    plt.legend(handles=[green_line, blue_line])
    plt.show()


# plot_graph(0,100,18,'monthly',50)