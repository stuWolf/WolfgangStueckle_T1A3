from os import system 
from default import default_values
import formula
import sh_table
import graph
import file
import sys
from items_operations import print_list_of_parameters, update_parameter_value




#gets the list of products from the seed method, imported from seed.py
list_of_parameters = default_values()
# 
# Prints a menu with several options and returns the selected option
def print_options():
    print("1. Show list of parameters")
    print("2. Edit parameters")
    print("3. Calculate future savings")
    print("4. Read.csv")
    print("5. Exit")
    opt = input("Select your option (1-5): ")
    return opt




def edit_parameter():
    # edit patameter in dictionary
    data = fetch_data(list_of_parameters)
    print_list_of_parameters (data[0],data[1],data[2],data[3],data[4])

    name = input("What parameter you want to update? (choose option 1 to 5)")

    update_parameter_value(list_of_parameters,name)
   



def fetch_data(list_of_parameters):
    # list list_of_parameters is a list of 5 data sets, 1 for each parameter
    # the function extracts the actual data from each of them
    start_balance = list_of_parameters[0]
    monthly_cont = list_of_parameters[1]
    interest = list_of_parameters[2]
    compound_freq = list_of_parameters[3]
    num_years = list_of_parameters[4]

    start_balance = start_balance['value']
    monthly_cont = monthly_cont ['value']
    interest = interest ['value']
    compound_freq = compound_freq ['value']
    num_years = abs(num_years ['value'])
    # print(f'Data used:\n Start Balance: {start_balance}\n Monthly Deposit: {monthly_cont}\n Yearly interest: {interest}\n Compound rate:  {compound_freq}\n Time in Years: {num_years}\n')
    return start_balance,monthly_cont,interest,compound_freq,num_years

def calculate():
    # calculate balance and display result. also display sub aptions and execute the 
    # functions that make sence after the result is displayed
    data = fetch_data(list_of_parameters)
    print_list_of_parameters (data[0],data[1],data[2],data[3],data[4])
    result = formula.calculate_capital(data[0],data[1],data[2],data[3],data[4])
    if (result == 'overflow'):
        print( 'The result exeeds the limit\n please check your data' )
			# display result 
			
    else:
        result =  round(result)
	# Label creation for output

        if(result >=0):
            print(f'The result is in:\n After {data[4]} years you will have {"{:,}".format(result)} AUD') 
        else:
            print(f'The result is in:\n After {data[4]} years your balance will be {"{:,}".format(result)} AUD')
    # print(f'calculating with {start_balance,monthly_cont,interest,compound_freq,num_years}')
    print('\n Three more options:\n')
    

    print("1. Show Table, close to continue")
    print("2. Show Graph, close to continue")
    print("3. Print.CSV")
    option = input("Select your option (1-3): ")
    if option == "1":
        
        sh_table.show_table(data[0],data[1],data[2],data[3],data[4])
        # print_list_of_parameters(list_of_parameters)
    elif option == "2":
        # show graph
                graph.plot_graph(data[0],data[1],data[2],data[3],data[4])
    elif option == "3":
        # print("Creating.CSV")
        
        file.store_csv(data[0],data[1],data[2],data[3],data[4])

    else:
        print("Invalid option")
    # input("press Enter to continue...")
    # system('clear')

def get_file_name():
    # gets the file name from user and check for plausibility

    # print('get file name called')
    file_name = input("Input file name ")
    file_error = '* valid .csv file name needed'
    # input("press Enter to continue...")
    if (file_name == ''):
        
        print( file_error)
        return False
    else:
        try:
            f = open(file_name , mode ='r')
        except FileNotFoundError:

		# show error label
            print(f'* No such file: {file_name}' )
            return False
		# print('* investment period required')
        # except Exception as e: # parent class off all exception, alternative ZeroDivisionErrpor, ValueError                 
        #     print(f'this causes a {e} error')
		# # show error label
        #     print(f'* No such file: {file_name}' )
            
            # return False
        else:
            f.close
		# close file, return result
		# cover error label
			
            return file_name
        finally:
            pass
        
    


def read_csv():
    # print('read file called')
    # read out file and return lists of annual contribution and future capital for processing in plot function 
    # only allow 4 attempts to get the fikle name right
    for i in range(3): 
        file_name = get_file_name()

        if not (file_name == False):
		
            print(f'file used: {file_name}')
		# read out file and return list of annual contribution and future capital
            capital, year_contribution = file.file_read(file_name)
		# plot graph with file data
            graph.plot_csv_data(file_name,capital, year_contribution)
		# file.file_read(file_name)

option = ""

# Menu feature: The while loop prints the menu option and the user select the option.
# Each valid option invokes the selected function
# The loop only stops when the input is 6 (exit option)
while option != "5":
    system('clear')
    # invoke print options and return the selected option
    option = print_options()
    system('clear')
    if option == "1":
        # print("shows parameter list .")
        data = fetch_data(list_of_parameters)
        print_list_of_parameters (data[0],data[1],data[2],data[3],data[4])
    elif option == "2":
        # print("asks for name of parameter and updates value")
        edit_parameter()
    elif option == "3":
        print("calculate future savings")
        calculate()
    elif option == "4":
        print("read .CSV")
        read_csv()
    #manages the exit option and the invalid options
    elif option == "5":
        continue
    else:
        print("Invalid option")
    #adds a break in the control flow until the user presses Enter    
    input("press Enter to continue...")
    system('clear')
    

print("Goodbye!") 
sys.exit()

# print('hello')
# print(list_of_parameters)
