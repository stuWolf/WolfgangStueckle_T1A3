import tkinter as tk
# from tkinter import *
from  tkinter import ttk

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.lines as mlines
import formula
import Table
import graph
# from ttk import *
# from Table import table

val = 10

 

# Top level window and display it
root = tk.Tk()
root.title("Investment calculator")
# frame.geometry('400x200')
# Function for getting Input
# from textbox and printing it
# at label widget
main_frame = tk.Canvas(root, width = 600, height = 1000, bg = '#AC99F2' ) # Sice of base window
main_frame.pack()



def table():
	start_balance = input_initial.get(1.0, "end-1c")
	monthly_cont = input_monthly.get(1.0, "end-1c")
	interest = input_interest.get(1.0, "end-1c")
	compound_freq = compound.get()
	num_years = years.get(1.0, "end-1c")
	Table.show_table(int(start_balance),int(monthly_cont),int(interest),compound_freq,int(num_years))

def plot():
	start_balance = input_initial.get(1.0, "end-1c")
	monthly_cont = input_monthly.get(1.0, "end-1c")
	interest = input_interest.get(1.0, "end-1c")
	compound_freq = compound.get()
	num_years = years.get(1.0, "end-1c")

	
	graph.plot_graph(int(start_balance),int(monthly_cont),int(interest),compound_freq,int(num_years))


def reset():
	exit()
	# inp = int(input_txt.get(1.0, "end-1c"))
	# res = inp*inp
	# lbl.config(text = "Provided Input: "+ string(inp))
	# top_label.config(text= 'The result is in: ')
	# output_label.config(text =(f'{inp} squared is {res}'))
# Calculate end capital and display on form
def calculate():
	
	start_balance = input_initial.get(1.0, "end-1c")
	monthly_cont = input_monthly.get(1.0, "end-1c")
	interest = input_interest.get(1.0, "end-1c")
	compound_freq = compound.get()
	num_years = years.get(1.0, "end-1c")

	res = formula.calculate_capital(int(start_balance),int(monthly_cont),int(interest),compound_freq,int(num_years))
	# Label creation for output
	top_label = tk.Label(main_frame, text = '' )
	output_label  = tk.Label(main_frame, text = '')
	main_frame.create_window(200, 400, window=top_label)  # Steady text
	main_frame.create_window(200, 440, window=output_label)  # output text
	top_label.config(text= 'The result is in: ', font= 'bold')
	output_label.config(text =(f'After {num_years} years you will have {round(res,1)} AUD'), font= 'bold')
	
	
	# display button to display table
	main_frame.create_window(200, 600, window=table_button)
	# plot chart
	plot()

# plot(10)	
    
# TextBox Creation for input Initial Investment
Step1_txt = tk.LabelFrame(main_frame,
				text= 'Step1: Initial Investment', 
				fg='white', bg = 'blue', font= 'bold',
				height = 40,
				width = 300)
input_initial = tk.Text(main_frame,
				height = 1,font= 'bold',
				width = 10)

# TextBox Creation for input Monthly Contribution
Step2_txt = tk.LabelFrame(main_frame,
				text= 'Step2: Monthly Contribution', 
				fg='white', bg = 'blue', font= 'bold',
				height = 40,
				width = 300)
input_monthly = tk.Text(main_frame,
				height = 1,font= 'bold',
				width = 10)

# TextBox Creation for input Monthly Contribution
Step3_txt = tk.LabelFrame(main_frame,
				text= 'Step3: Annual interest rate in %', 
				fg='white', bg = 'blue', font= 'bold',
				height = 40,
				width = 300)
input_interest = tk.Text(main_frame,font= 'bold',
				height = 1,
				width = 10)


# get compound rate from choice box

Step4_txt = tk.LabelFrame(main_frame,
				text= 'Step4: Choose compound frequency',
				fg='white', bg = 'blue', font= 'bold',
				height = 40,
				width = 300)

choices = ['Annually', 'Monthly', 'Quarterly']
variable = tk.StringVar(main_frame)

compound = ttk.Combobox(main_frame, values = choices, height = 6,
				width = 10)
compound.set('Monthly')
# variable = tk.StringVar()

years_txt = tk.LabelFrame(main_frame,
				text= 'Number of years of investment', 
				fg='white', bg = 'blue', font= 'bold',
				height = 40,
				width = 300)
years = tk.Text(main_frame,font= 'bold',
				height = 1,
				width = 10)
# years = 10
# compound = ttk.Combobox(main_frame, textvariable= variable, height = 6,
# 				width = 10)
# compound['values'] = ['Annually', 'Monthly', 'Quarterly']
# compound['state'] = 'readonly'
# compound.pack(fill=tk.X, padx = 5, pady = 5)
# # Button Creation
# square_button = tk.Button(main_frame,
# 						text = "X^2",
# 						command = square, fg="white", bg='blue')

# Button Creation
calculate_button = tk.Button(main_frame,
						text = "Calculate",
						command = calculate, font= 'bold',fg="white", bg='blue')

table_button = tk.Button(main_frame,
						text = 'Show Table',
						command = table,font= 'bold', fg="white", bg='blue')


reset_button = tk.Button(main_frame,
						text = "Reset",
						command = reset,font= 'bold', fg="white", bg='blue')


# Label Creation for output


main_frame.create_window(150, 30, window=Step1_txt)  # click me
main_frame.create_window(500, 30, window=input_initial)  # click me
main_frame.create_window(150, 90, window=Step2_txt)  # click me
main_frame.create_window(500, 90, window=input_monthly)  # click me
main_frame.create_window(150, 150, window=Step3_txt)  # click me
main_frame.create_window(500, 150, window=input_interest)  # click me
main_frame.create_window(150, 210, window=Step4_txt)  # click me
main_frame.create_window(500, 210, window=compound)  # click me
main_frame.create_window(150, 270, window=years_txt)  # click me
main_frame.create_window(500, 270, window=years ) # click me
main_frame.create_window(150, 350, window=calculate_button)  # calculate capital, show graph
main_frame.create_window(300, 350, window=reset_button)  # click me
# main_frame.create_window(200, 150, window=square_root_button)  # quit x,y




# plot(10)
main_frame.mainloop()
# print(inputtxt.get(1.0, "end-1c"))
