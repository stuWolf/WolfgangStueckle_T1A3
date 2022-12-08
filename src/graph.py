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
	# start_balance = input_initial.get(1.0, "end-1c")
	# monthly_cont = input_monthly.get(1.0, "end-1c")
	# interest = input_interest.get(1.0, "end-1c")
	# compound_freq = compound.get()
	
    A = 0
    i = 0
    capital = []
    year_contribution = []

    t = np.arange(0, num_years+1, 1)  # t goes from 0 to val, 1 increment
    
    
    # calculate capital for each year (array element) based on compound interest and contribution
    # write each year into list
   
    for i in range(0,num_years+1, 1):
        A = formula.calculate_capital(P, m,  r, Compound_frequ,int( t[i]))
        y = m*12*i
        year_contribution.append(y)
        capital.append(A)
        
    
    # configure and plot graph
    plt.title('Total Savings')
    plt.plot(t, year_contribution, 'r--', t, capital, 'g')
    plt.xlabel('Years')
    plt.ylabel('Value in AUD')
    # plt.title('Histogram of IQ')
    plt.suptitle('Total Capital')
    blue_line = mlines.Line2D([], [], color='red', marker='',markersize=15, label='Total Contribution')
    green_line = mlines.Line2D([], [], color='green', marker='',markersize=15, label= (f'Future value at {r}% interest '))
    plt.legend(handles=[green_line, blue_line])
    plt.show()


# plot_graph(0,100,18,'monthly',10)