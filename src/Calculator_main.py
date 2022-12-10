import tkinter as tk
# from tkinter import *
from  tkinter import ttk
# import time
# import matplotlib.pyplot as plt
# import numpy as np

# import matplotlib.lines as mlines
import formula
import Table
import graph

# from ttk import *
# from Table import table

# val = 10

 

# Top level window and display it
root = tk.Tk()
root.title("Investment calculator")
# frame.geometry('400x200')
# Function for getting Input
# from textbox and printing it
# at label widget
main_frame = tk.Canvas(root, width = 600, height = 1000, bg = '#AC99F2' ) # Sice of base window
main_frame.pack()



# get data from input form, handle exceptions and make sure that program gets clean data

def fetch_data():
	
	B_start = B_monthly = B_interest = B_years = False

	compound_freq = compound_var.get()

		

	try:
		start_balance = int (input_initial.get(1.0, "end-1c"))
		# print('start balance')
	except ValueError:
		bal_error_label = tk.Label(main_frame, text = '* numerical value for start balance required' , font= ("Arial", 14,'bold') , fg= 'red',width = 45,  anchor = 'w')
		main_frame.create_window(250, 80, window=bal_error_label)
		print('* numerical start balance required')
	except Exception as e: # parent class off all exception, alternative ZeroDivisionErrpor, ValueError                 
		print(f'this causes a {e} error')
		

	else:
		B_start = True
	finally:
		pass

	try:
		monthly_cont = int(input_monthly.get(1.0, "end-1c"))
	except ValueError:
			cont_error_label = tk.Label(main_frame, text = '* numerical value for monthly saving required' , font= ("Arial", 14,'bold') , fg= 'red',width = 45,anchor = 'w')
			main_frame.create_window(250, 200, window=cont_error_label)
			print('* monthly saving required, must be numerical')
	except Exception as e: # parent class off all exception, alternative ZeroDivisionErrpor, ValueError                 
			print(f'this causes a {e} error')
    # print('devided by zero') # bad practice
	else:
		B_monthly = True
	finally:
		pass

	try:
			interest = int(input_interest.get(1.0, "end-1c"))
	except ValueError:
			int_error_label = tk.Label(main_frame, text = '* numerical value for interest rate required' , font= ("Arial", 14,'bold') , fg= 'red',width = 45, anchor = 'w')
			main_frame.create_window(250, 320, window=int_error_label)
			print('* interest rate required')
	except Exception as e: # parent class off all exception, alternative ZeroDivisionErrpor, ValueError                 
			print(f'this causes a {e} error')
    # print('devided by zero') # bad practice
	else:
		B_interest = True
	finally:
		pass

	try:
		num_years = int(years.get(1.0, "end-1c"))
	except ValueError:
		year_error_label = tk.Label(main_frame, text = '* numerical value for investment period required' , font= ("Arial", 14,'bold') , fg= 'red',width = 45, anchor = 'w')
		main_frame.create_window(250, 560, window=year_error_label)
		print('* investment period required')
	except Exception as e: # parent class off all exception, alternative ZeroDivisionErrpor, ValueError                 
		print(f'this causes a {e} error')
    # print('devided by zero') # bad practice
	
	else:
		B_years = True
	finally:
		pass


	# A = [start_balance,monthly_cont,interest,compound_freq,num_years]

	# print(A)
# if all data good, hand over values, if not return flag for repeat of function
	if B_start and B_monthly and B_interest and B_years:
		return start_balance,monthly_cont,interest,compound_freq,num_years
	else:		
		return False
			
			# time.sleep(0.5)
		




def table():
	data = fetch_data()
	Table.show_table(data[0],data[1],data[2],data[3],data[4])

def plot():
	data = fetch_data()

	
	graph.plot_graph(data[0],data[1],data[2],data[3],data[4])


def reset():
	exit()

def calculate():
	# calculate capital returns tuple with 
	# [0]P = 0 # start balance
    # [1]m = 100 # monthly contribution
    # [2]r = 18 # interest rate in %
    # [3]Compound_frequ = 'monthly'
    # [4]t = 10  # number of years

	# fetch data set and check for plausibility
	result = 0
	data = fetch_data()
	# main_frame.create_window(300, 690, window=top_label) 

	
	if not data == False:
		# calculate investment
		result = formula.calculate_capital(data[0],data[1],data[2],data[3],data[4])
		if (result == 'overflow'):
			top_label = tk.Label(main_frame, text = 'The result exeeds the limit\n please check your data' , font= ("Arial", 18),relief= 'raised', bg = 'red')
			# display result window
			# main_frame.select_clear(window = top_label)
			main_frame.create_window(300, 690, window=top_label)  
		else:
			result = int(result)
	# Label creation for output
			top_label = tk.Label(main_frame, text = f'The result is in:\n After {data[4]} years you will have {"{:,}".format(result)} AUD' , font= ("Arial", 18),relief= 'raised')
			# display result window
			# main_frame.delete( 'top_label'	)
			main_frame.create_window(300, 690, window=top_label)  
			# display button to display table
			main_frame.create_window(200, 780, window=table_button)
		# plot chart
			plot()
		
		
		
		

	
	


    
# TextBox Creation for input Initial Investment
Step1_txt = tk.LabelFrame(main_frame,
				text= 'Step1: Initial Investment', 
				fg='white', bg = 'blue', font= 'bold',
				height = 40,
				width = 400)
input_initial = tk.Text(main_frame,
				height = 1,font= 'bold',
				width = 10)

# TextBox Creation for input Monthly Contribution
Step2_txt = tk.LabelFrame(main_frame,
				text= 'Step2: Monthly Contribution', 
				fg='white', bg = 'blue', font= 'bold',
				height = 40,
				width = 400)
input_monthly = tk.Text(main_frame,
				height = 1,font= 'bold',
				width = 10)

# TextBox Creation for input Monthly Contribution
Step3_txt = tk.LabelFrame(main_frame,
				text= 'Step3: Annual interest rate in %', 
				fg='white', bg = 'blue', font= 'bold',
				height = 40,
				width = 400)
input_interest = tk.Text(main_frame,font= 'bold',
				height = 1,
				width = 10)




Step4_txt = tk.LabelFrame(main_frame,
				text= 'Step4: Choose compound frequency',
				fg='white', bg = 'blue', font= 'bold',
				height = 40,
				width = 400)

# display compound rate choice box
# choices = ['Annually', 'Monthly', 'Quarterly']
# compound = ttk.Combobox(main_frame, values = choices, height = 6, width = 10)
# compound.set('Monthly')

# variable = tk.StringVar()
compound_var = tk.StringVar()
options = ['Annually', 'Monthly', 'Quarterly']
compound_var.set('Quarterly') 
compound = tk.OptionMenu(main_frame, compound_var, *options)



years_txt = tk.LabelFrame(main_frame,
				text= 'Number of years of investment', 
				fg='white', bg = 'blue', font= 'bold',
				height = 40,
				width = 400)
years = tk.Text(main_frame,font= 'bold',
				height = 1,
				width = 10)



calculate_button = tk.Button(main_frame,
						text = "Calculate",
						command = calculate, font= 'bold',fg="white", bg='blue')

table_button = tk.Button(main_frame,
						text = 'Show Table',
						command = table,font= 'bold', fg="white", bg='blue')


reset_button = tk.Button(main_frame,
						text = "Quit",
						command = reset,font= 'bold', fg="white", bg='blue')


# Label Creation for output


main_frame.create_window(200, 30, window=Step1_txt)  # click me
main_frame.create_window(500, 30, window=input_initial)  # click me
main_frame.create_window(200, 150, window=Step2_txt)  # click me
main_frame.create_window(500, 150, window=input_monthly)  # click me
main_frame.create_window(200, 270, window=Step3_txt)  # click me
main_frame.create_window(500, 270, window=input_interest)  # click me
main_frame.create_window(200, 390, window=Step4_txt)  # click me
main_frame.create_window(500, 390, window=compound)  # click me
# main_frame.create_window(500, 210, window=variable)  # click me
main_frame.create_window(200, 510, window=years_txt)  # click me
main_frame.create_window(500, 510, window=years ) # click me
main_frame.create_window(150, 630, window=calculate_button)  # calculate capital, show graph
main_frame.create_window(300, 630, window=reset_button)  # click me
# main_frame.create_window(200, 150, window=square_root_button)  # quit x,y




# plot(10)
main_frame.mainloop()
# print(inputtxt.get(1.0, "end-1c"))
