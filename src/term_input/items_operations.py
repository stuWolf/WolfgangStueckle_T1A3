
def print_list_of_parameters(P, m,  r, Compound_frequ, t ):
    # prints a list of the used data
    # P = 0 # start balance
    # m = 100 # monthly contribution
    # r = 18 # interest rate in %
    # Compound_frequ = 'monthly'
    # t = 10  # number of years
    
    
    print(f'Data used:\n1: Start Balance: {"{:,}".format(P)} AUD\n2: Monthly Deposit: {"{:,}".format(m)} AUD\n3: Yearly interest: {r} %\n4: Compound rate:  {Compound_frequ}\n5: Time of investment: {"{:,}".format(t)} Years\n')
    



def update_parameter_value(parameters, data_set_nr):
    # iterate through the list looking for the parameter
    # name = str
    # parameter_name = str
    # parameters = list of dictionary

   
    name = 'nothing'

    match data_set_nr:    
            case "1":
                name = 'Start Balance'
            case '2':
                name = 'Monthly Deposit'
            case '3':
                name = 'Annual interest'
            case '4':
                name = 'Compound rate'
            case '5':
                name = 'Time in Years'
            case _ :
                try:
                    print(f'{name} invalid parameter ')
                except ValueError: 
                    print('invalid input type, must be numerical')
                except Exception as e: # parent class off all exception, alternative ZeroDivisionErrpor, ValueError                 
                    print(f'this causes a {e} error')
                return

    for parameter in parameters:
        
        # check if the parameter's name of this iteration is equal to the name we receive.
        parameter_name = parameter["name"]
       

        if parameter_name == name:
            # ask for the new value
            if name == 'Time in Years':
                value = int(input(f"What is the new value for {name}? "))

                
            elif name == 'Compound rate':
                print("1. Monthly")
                print("2. Quarterly")
                print("3. Yearly")
                option = input("Select your option (1-3): ")
                match option:    
                    case "1":
                        # print("show table")
                        value = 'Monthly'
                     # print_list_of_parameters(list_of_parameters)
                    case "2":
                        value = 'Quarterly'
                        # print("Printing CSV")
                    case "3":
                        value = 'Annualy'
                        # edit_parameter()
                    case _ :
                        print("Invalid option")
                
            else:
                
                value = float(input(f"What is the new value for {name}? "))
                # return
             #update the parameter's value
            parameter["value"] = value
            print(f"{name} was uptaded to {value}")
            return
            # when name found exit function
    print(f'Input can not be {name} ')
