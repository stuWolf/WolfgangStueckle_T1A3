import matplotlib.pyplot as plt
import numpy as np

import matplotlib.lines as mlines
import formula
import file




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
    # build up an array for the t axis values
    t = np.arange(0, num_years+1, 1)  # t goes from 0 to val, 1 increment
    
    
    # calculate capital for each year (array element) based on compound interest and contribution
    # write each year into list
   
    for i in range(0,num_years+1, 1):
        # calculate compounded value
        A = formula.calculate_capital(P, m,  r, Compound_frequ,int( t[i])) # calculate compounded value
        #  write ammount of each year in list
        capital.append(A)  
        # calculate personal contribution, write ammount of each year in list
        y = round(m*12*i + P )   
        year_contribution.append(y) 
    

    # configure and plot graph
    # plt.title('Total Savings') no need, does it in plt.suptitle
    # show grid
    plt.grid(color='black', linestyle='-', linewidth=1)
    # plot the actual function with the lists for t axis, contributions and capital
    plt.plot(t, year_contribution, 'r--', t, capital, 'g')
    # show labels
    plt.xlabel('Years')
    plt.ylabel('Value in AUD')
    plt.suptitle('Total Capital')
    # define and show legend
    blue_line = mlines.Line2D([], [], color='red', marker='',markersize=15, label= (f'Total Contribution of {year_contribution[num_years]} AUD'))
    green_line = mlines.Line2D([], [], color='green', marker='',markersize=15, label= (f'Future value at {r}% interest '))
    plt.legend(handles=[green_line, blue_line])
    plt.show()
    


def plot_csv_data(file_name):
    plt.close()
    # P = 0 # start balance
    # m = 100 # monthly contribution
    # r = 18 # interest rate in %
    # Compound_frequ = 'monthly'
    # t = 10  # number of years

    A = 0
    i = 0
    capital = []
    year_contribution = []


    
    
    
    # read outcapital for each year (array element) based on compound interest and contribution
    # write values for each year into lists capital and year_contriburion
   


    capital, year_contribution = file.file_read(file_name)


    # build up an array for the t axis values
    t = np.arange(1, len(capital)+1, 1)  # t goes from 0 to val, 1 increment

    # configure and plot graph
    # plt.title('Total Savings') no need, does it in plt.suptitle
    # show grid
    plt.grid(color='black', linestyle='-', linewidth=1)
    # plot the actual function with the lists for t axis, contributions and capital
    plt.plot(t, year_contribution, 'r--', t, capital, 'g')
    # show labels
    plt.xlabel('Years')
    plt.ylabel('Value in AUD')
    plt.suptitle(f'Total Capital based on {file_name}')
    # define and show legend
    blue_line = mlines.Line2D([], [], color='red', marker='',markersize=15, label= (f'Total Contribution: {year_contribution[-1]} AUD'))
    green_line = mlines.Line2D([], [], color='green', marker='',markersize=15, label= (f'Future value of capital: {capital[-1]} AUD '))
    plt.legend(handles=[green_line, blue_line])
    plt.show()


# file_name = './investment_data.csv'
# plot_csv_data(file_name)
# plot_graph(0,100,18,'monthly',10)