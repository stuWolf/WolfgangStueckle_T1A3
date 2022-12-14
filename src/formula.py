


def calculate_capital(P, m,  r, Compound_frequ, t ):
    
    # P = 0 # start balance
    # m = 100 # monthly contribution
    # r = 18 # interest rate in %
    # Compound_frequ = 'monthly'
    # t = 10  # number of years
    n = 0 # compound frequency
    A = 0 # future value of capital
    # B_overflow = False
    match Compound_frequ:
        case 'Monthly':
            n = 12
        case 'Quarterly':
            n = 4
        case 'Annualy':
            n = 1
        case _:                                         # Default value
            n = 12


    for i in range ((n*t-1),-1, -1): # t = number of years, n = compound frequ
            try:
                # A += m*pow((1+r/(100*n)),(i))     # calculate monthly contribution and compound interest
                A += m*(1+r/(100*n))**(i)
                
            except OverflowError:
                print('ammount too high, you must be a Trillionaire!!')
                # B_overflow = True
                return 'overflow' 
        
        # correction factor for capital based on compound rate
    A = A*12/n
    # print(A)
    try: 
        A += P*(1+r/(100*n))**(n*t)  # calculate start capital and interest, add to ccompounded monthly contribution
    except OverflowError:
        return 'overflow'
    else:
        # Standart case, return result
        return round(A)

# print(round(A,2))
 


# test data
# print(calculate_capital(1000,100,10,'monthly' ,10))
# def calculate_capital(P, m,  r, Compound_frequ, t ):
#   # P = 0 # start balance
    # m = 100 # monthly contribution
    # r = 18 # interest rate in %
    # Compound_frequ = 'monthly'
    # t = 10  # number of years
#     A = 0 # future value of capital