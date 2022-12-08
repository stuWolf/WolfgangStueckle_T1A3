# import math
from math import pow




def calculate_capital(P, m,  r, Compound_frequ, t ):
    
    # P = 0 # start balance
    # m = 100 # monthly contribution
    # r = 18 # interest rate in %
    # Compound_frequ = 'monthly'
    # t = 10  # number of years
    n = 0 # compound frequency
    A = 0 # future value of capital

    match Compound_frequ:
        case 'monthly':
            n = 12
        case 'quarterly':
            n = 4
        case 'annualy':
            n = 1
        case _:                                         # Default value
            n = 12

# P = int(input('enter start balance  '))

# t = int(input('enter number of years  '))
    if (m > 0):
        for i in range ((n*t-1),-1, -1): # t = number of years, n = compound frequ
            try:
                A += m*pow((1+r/(100*n)),(i))     # calculate monthly contribution and compound interest
            except OverflowError:
                print('ammount too high, you must be a Trillionaire!!')
        # print(A)
        # 1000print(i)
    A += P*pow((1+r/(100*n)),(n*t))  # calculate start capital and interest
    return A
# print(round(A,2))
 

# print(int(calculate_capital('monthly',18, 100, 0,10)))

# def calculate_capital(Compound_frequ, r, m, P, t ):
#     r = 18 # interest rate in %
#     m = 100 # monthly contribution
#     Compound_frequ = 'monthly'
#     P = 0 # start balance
#     t = 1  # number of years
#     n = 0 # compound frequency
#     A = 0 # future value of capital