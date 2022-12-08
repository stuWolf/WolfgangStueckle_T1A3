
def fetch_data():
    start_balance = 0
    monthly_cont = 100
    interest = 18
    compound_freq = 'quarterly'
    num_years = 10
    # A = [start_balance,monthly_cont,interest,compound_freq,num_years]

    
    return start_balance,monthly_cont,interest,compound_freq,num_years



def calculate_capital(P, m,  r, Compound_frequ, t ):
    
    # P = 0 # start balance
    # m = 100 # monthly contribution
    # r = 18 # interest rate in %
    # Compound_frequ = 'monthly'
    # t = 10  # number of years
    n = 0 # compound frequency
    A = 0 # future value of capital

    match Compound_frequ:
        case 'Monthly':
            n = 12
        case 'Quarterly':
            n = 4
        case 'Annualy':
            n = 1
        case _:                                         # Default value
            n = 12
    print(f'n = {n}')
# P = int(input('enter start balance  '))

# t = int(input('enter number of years  '))
    if (m > 0):
        for i in range ((n*t-1),-1, -1): # t = number of years, n = compound frequ
            try:
                # A += m*pow((1+r/(100*n)),(i))     # calculate monthly contribution and compound interest
                A += m*(1+r/(100*n))**(i)
            except OverflowError:
                print('ammount too high, you must be a Trillionaire!!')
        # print(A)
        # 1000print(i)
        A = A*12/n
    A += P*(1+r/(100*n))**(n*t)  # calculate start capital and interest
    return A
# print(round(A,2))
 
# `A = fetch_data()
# print(fetch_data())
# print(int(calculate_capital(A[0],A[1],A[2],A[3],A[4])))`

# def calculate_capital(P, m,  r, Compound_frequ, t ):
#     # P = 0 # start balance
    # m = 100 # monthly contribution
    # r = 18 # interest rate in %
    # Compound_frequ = 'monthly'
    # t = 10  # number of years
#     A = 0 # future value of capital